<?php
/**
 * Plugin Name: Lean Mode Pro – Statistik-Schnittstelle
 * Description: Stellt die Besucherzahlen von Independent Analytics als WordPress-Ability `lmp/site-stats` bereit
 *              (nur lesen, nur für Administratoren). Die Statistik-App in Claude ruft sie über die
 *              Novamira-Verbindung ab. Liefert nur zusammengefasste Zahlen, keine Daten einzelner Besucher.
 * Version:     1.0
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action(
	'wp_abilities_api_init',
	static function () {
		if ( ! function_exists( 'wp_register_ability' ) ) {
			return;
		}
		wp_register_ability(
			'lmp/site-stats',
			array(
				'label'               => 'Lean Mode Pro: website statistics',
				'description'         => 'Read-only summary of the website statistics from Independent Analytics for a period: views, '
					. 'visitors, sessions, signups (thank-you page) and confirmations (welcome page), per day or hour, top pages, '
					. 'sources, countries and devices, compared with the previous period. Aggregated numbers only.',
				'category'            => 'site',
				'input_schema'        => array(
					'type'                 => 'object',
					'properties'           => array(
						'days'      => array(
							'type'        => 'integer',
							'enum'        => array( 1, 7, 30, 90, 365 ),
							'default'     => 30,
							'description' => '1 = today (by hour), otherwise the last N days including today.',
						),
						'tz_offset' => array(
							'type'        => 'integer',
							'default'     => 0,
							'minimum'     => -720,
							'maximum'     => 840,
							'description' => 'Viewer time zone in minutes east of UTC (e.g. 120 for CEST).',
						),
					),
					'additionalProperties' => false,
				),
				'output_schema'       => array( 'type' => 'object' ),
				'execute_callback'    => 'lmp_site_stats',
				'permission_callback' => static fn() => current_user_can( 'manage_options' ),
				'meta'                => array(
					'annotations'  => array(
						'readonly'    => true,
						'destructive' => false,
						'idempotent'  => true,
					),
					'show_in_rest' => true,
					'mcp'          => array(
						'public' => true,
						'type'   => 'tool',
					),
				),
			)
		);
	}
);

/**
 * @param array $input { days, tz_offset }
 */
function lmp_site_stats( $input = array() ) {
	global $wpdb;
	$t = $wpdb->prefix . 'independent_analytics_';
	if ( $wpdb->get_var( $wpdb->prepare( 'SHOW TABLES LIKE %s', $t . 'views' ) ) !== $t . 'views' ) {
		return new WP_Error( 'lmp_no_analytics', 'Independent Analytics is not installed or has no data tables.' );
	}

	$days = (int) ( $input['days'] ?? 30 );
	$days = in_array( $days, array( 1, 7, 30, 90, 365 ), true ) ? $days : 30;
	$tz   = max( -720, min( 840, (int) ( $input['tz_offset'] ?? 0 ) ) );

	// Period boundaries in UTC (Independent Analytics stores UTC); local midnight of the first day.
	$now        = time();
	$local_now  = $now + $tz * 60;
	$start_loc  = $local_now - ( $local_now % DAY_IN_SECONDS ) - ( $days - 1 ) * DAY_IN_SECONDS;
	$from       = $start_loc - $tz * 60;
	$prev_from  = $from - $days * DAY_IN_SECONDS;
	$fmt        = static fn( $ts ) => gmdate( 'Y-m-d H:i:s', $ts );
	$to_s       = $fmt( $now );
	$from_s     = $fmt( $from );
	$prev_s     = $fmt( $prev_from );
	$prev_end_s = $fmt( $now - $days * DAY_IN_SECONDS );

	$totals = static function ( $a, $b ) use ( $wpdb, $t ) {
		$row = $wpdb->get_row(
			$wpdb->prepare(
				"SELECT COUNT(*) AS views, COUNT(DISTINCT v.session_id) AS sessions, COUNT(DISTINCT s.visitor_id) AS visitors
				 FROM {$t}views v LEFT JOIN {$t}sessions s ON s.session_id = v.session_id
				 WHERE v.viewed_at >= %s AND v.viewed_at <= %s",
				$a,
				$b
			),
			ARRAY_A
		);
		return array_map( 'intval', $row ?: array( 'views' => 0, 'sessions' => 0, 'visitors' => 0 ) );
	};

	// Signups = views of the thank-you page, confirmations = views of the welcome page (download).
	$page_ids = array_filter(
		array(
			'signups'       => get_page_by_path( 'thank-you' )?->ID,
			'confirmations' => get_page_by_path( 'welcome' )?->ID,
		)
	);
	$goals    = static function ( $a, $b ) use ( $wpdb, $t, $page_ids ) {
		$out = array( 'signups' => 0, 'confirmations' => 0 );
		foreach ( $page_ids as $key => $id ) {
			$out[ $key ] = (int) $wpdb->get_var(
				$wpdb->prepare(
					"SELECT COUNT(*) FROM {$t}views v JOIN {$t}resources r ON r.id = v.resource_id
					 WHERE r.singular_id = %d AND v.viewed_at >= %s AND v.viewed_at <= %s",
					$id,
					$a,
					$b
				)
			);
		}
		return $out;
	};

	$pinterest = static function ( $a, $b ) use ( $wpdb, $t ) {
		return (int) $wpdb->get_var(
			$wpdb->prepare(
				"SELECT COUNT(*) FROM {$t}sessions s JOIN {$t}referrers ref ON ref.id = s.referrer_id
				 WHERE s.created_at >= %s AND s.created_at <= %s
				   AND (ref.domain LIKE %s OR ref.domain LIKE %s)",
				$a,
				$b,
				'%pinterest.%',
				'pin.it'
			)
		);
	};

	$current           = $totals( $from_s, $to_s ) + $goals( $from_s, $to_s );
	$current['pinterest_sessions'] = $pinterest( $from_s, $to_s );
	$previous          = $totals( $prev_s, $prev_end_s ) + $goals( $prev_s, $prev_end_s );
	$previous['pinterest_sessions'] = $pinterest( $prev_s, $prev_end_s );

	// Series: by hour for today, otherwise by day (in the viewer's time zone).
	$bucket = 1 === $days ? '%Y-%m-%d %H:00' : '%Y-%m-%d';
	$rows   = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT DATE_FORMAT(DATE_ADD(v.viewed_at, INTERVAL %d MINUTE), %s) AS k,
			        COUNT(*) AS views, COUNT(DISTINCT s.visitor_id) AS visitors
			 FROM {$t}views v LEFT JOIN {$t}sessions s ON s.session_id = v.session_id
			 WHERE v.viewed_at >= %s AND v.viewed_at <= %s GROUP BY k",
			$tz,
			$bucket,
			$from_s,
			$to_s
		),
		ARRAY_A
	);
	$by_key = array();
	foreach ( $rows as $r ) {
		$by_key[ $r['k'] ] = array( (int) $r['views'], (int) $r['visitors'] );
	}
	$series = array();
	$steps  = 1 === $days ? 24 : $days;
	for ( $i = 0; $i < $steps; $i++ ) {
		$ts       = $start_loc + $i * ( 1 === $days ? HOUR_IN_SECONDS : DAY_IN_SECONDS );
		$key      = 1 === $days ? gmdate( 'Y-m-d H:00', $ts ) : gmdate( 'Y-m-d', $ts );
		$series[] = array(
			'label'    => $key,
			'views'    => $by_key[ $key ][0] ?? 0,
			'visitors' => $by_key[ $key ][1] ?? 0,
		);
	}

	$top_pages = array_map(
		static fn( $r ) => array(
			'title'    => wp_strip_all_tags( (string) $r['title'] ),
			'url'      => (string) $r['url'],
			'views'    => (int) $r['views'],
			'visitors' => (int) $r['visitors'],
		),
		$wpdb->get_results(
			$wpdb->prepare(
				"SELECT r.cached_title AS title, r.cached_url AS url, COUNT(*) AS views, COUNT(DISTINCT s.visitor_id) AS visitors
				 FROM {$t}views v JOIN {$t}resources r ON r.id = v.resource_id
				 LEFT JOIN {$t}sessions s ON s.session_id = v.session_id
				 WHERE v.viewed_at >= %s AND v.viewed_at <= %s
				 GROUP BY r.id ORDER BY views DESC LIMIT 10",
				$from_s,
				$to_s
			),
			ARRAY_A
		)
	);

	$group = static function ( $select, $join, $by, $limit ) use ( $wpdb, $t, $from_s, $to_s ) {
		return $wpdb->get_results(
			$wpdb->prepare(
				"SELECT {$select}, COUNT(*) AS sessions FROM {$t}sessions s {$join}
				 WHERE s.created_at >= %s AND s.created_at <= %s GROUP BY {$by} ORDER BY sessions DESC LIMIT %d",
				$from_s,
				$to_s,
				$limit
			),
			ARRAY_A
		);
	};
	$cast  = static function ( $rows ) {
		return array_map(
			static function ( $r ) {
				$r['sessions'] = (int) $r['sessions'];
				return $r;
			},
			$rows
		);
	};

	$sources   = $cast(
		$group(
			"COALESCE(NULLIF(ref.domain, ''), rt.referrer_type, 'Direct') AS name, COALESCE(rt.referrer_type, 'Direct') AS type",
			"LEFT JOIN {$t}referrers ref ON ref.id = s.referrer_id LEFT JOIN {$t}referrer_types rt ON rt.id = ref.referrer_type_id",
			'name, type',
			10
		)
	);
	$channels  = $cast(
		$group(
			"COALESCE(rt.referrer_type, 'Direct') AS name",
			"LEFT JOIN {$t}referrers ref ON ref.id = s.referrer_id LEFT JOIN {$t}referrer_types rt ON rt.id = ref.referrer_type_id",
			'name',
			10
		)
	);
	$countries = $cast(
		$group(
			"COALESCE(c.country, 'Unknown') AS name, COALESCE(c.country_code, '') AS code",
			"LEFT JOIN {$t}countries c ON c.country_id = s.country_id",
			'name, code',
			10
		)
	);
	$devices   = $cast(
		$group(
			"COALESCE(d.device_type, 'Unknown') AS name",
			"LEFT JOIN {$t}device_types d ON d.device_type_id = s.device_type_id",
			'name',
			5
		)
	);

	$live = (int) $wpdb->get_var(
		$wpdb->prepare(
			"SELECT COUNT(DISTINCT s.visitor_id) FROM {$t}views v JOIN {$t}sessions s ON s.session_id = v.session_id
			 WHERE v.viewed_at >= %s",
			$fmt( $now - 30 * MINUTE_IN_SECONDS )
		)
	);

	return array(
		'generated_at'   => gmdate( 'c', $now ),
		'tracking_since' => (string) get_option( 'iawp_beginning_of_time', '' ),
		'days'           => $days,
		'tz_offset'      => $tz,
		'period'         => array(
			'from' => gmdate( 'Y-m-d', $start_loc ),
			'to'   => gmdate( 'Y-m-d', $local_now ),
		),
		'totals'         => $current,
		'previous'       => $previous,
		'live_visitors'  => $live,
		'series'         => $series,
		'top_pages'      => $top_pages,
		'sources'        => $sources,
		'channels'       => $channels,
		'countries'      => $countries,
		'devices'        => $devices,
	);
}
