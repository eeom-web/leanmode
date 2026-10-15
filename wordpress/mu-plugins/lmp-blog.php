<?php
/**
 * Plugin Name: Lean Mode Pro – Blog
 * Description: Renders blog posts, the blog index (/blog/) and post archives in the Lean Mode Pro design
 *              (lmp-blog/template.php) instead of the block theme. Every post automatically gets an affiliate
 *              disclosure at the top, a health note and the signup box at the end, plus Open Graph tags for
 *              Pinterest Rich Pins. The brand CSS/JS and the signup form come from the option `lmp_blog`
 *              (written on deploy from wordpress/elementor/dist/blog.json). Old Turkish URLs redirect to the
 *              English pages. Comments are switched off.
 * Version:     1.0
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Old Turkish addresses (until 13.10.2026) -> English pages. */
function lmp_old_paths() {
	return array(
		'ucretsiz-30-gunluk-plan' => '/',
		'tesekkurler'             => '/thank-you/',
		'kayit-onaylandi'         => '/welcome/',
		'gizlilik-politikasi'     => '/privacy-policy/',
		'cerez-politikasi'        => '/privacy-policy/',
		'kvkk-aydinlatma-metni'   => '/privacy-policy/',
		'yasal-bilgiler'          => '/legal-notice/',
	);
}

add_action(
	'template_redirect',
	static function () {
		$path = trim( (string) wp_parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH ), '/' );
		$map  = lmp_old_paths();
		if ( isset( $map[ $path ] ) ) {
			wp_safe_redirect( home_url( $map[ $path ] ), 301 );
			exit;
		}
	},
	0
);

function lmp_is_blog_view() {
	return is_singular( 'post' ) || is_home() || is_category() || is_tag() || is_author() || is_date();
}

add_filter(
	'template_include',
	static function ( $template ) {
		return lmp_is_blog_view() ? __DIR__ . '/lmp-blog/template.php' : $template;
	},
	99
);

add_action(
	'wp_enqueue_scripts',
	static function () {
		if ( lmp_is_blog_view() ) {
			// Instrument Sans as hosted locally by Elementor (no request to Google).
			wp_enqueue_style( 'lmp-font', content_url( '/uploads/elementor/google-fonts/css/instrumentsans.css' ), array(), null );
		}
	}
);

/** Open Graph tags for posts (Pinterest Rich Pins read og:* and article:*). */
add_action(
	'wp_head',
	static function () {
		if ( ! is_singular( 'post' ) ) {
			return;
		}
		$post = get_queried_object();
		$desc = has_excerpt( $post ) ? get_the_excerpt( $post ) : wp_trim_words( wp_strip_all_tags( strip_shortcodes( $post->post_content ) ), 30, '…' );
		$tags = array(
			'og:type'                => 'article',
			'og:site_name'           => get_bloginfo( 'name' ),
			'og:title'               => get_the_title( $post ),
			'og:description'         => $desc,
			'og:url'                 => get_permalink( $post ),
			'article:published_time' => get_the_date( 'c', $post ),
			'article:modified_time'  => get_the_modified_date( 'c', $post ),
		);
		if ( has_post_thumbnail( $post ) ) {
			$tags['og:image'] = get_the_post_thumbnail_url( $post, 'large' );
		}
		foreach ( $tags as $property => $content ) {
			printf( '<meta property="%s" content="%s">' . "\n", esc_attr( $property ), esc_attr( $content ) );
		}
		printf( '<meta name="description" content="%s">' . "\n", esc_attr( $desc ) );
	},
	1
);

/** Keep the noindex pages (thank-you, welcome) out of the WordPress sitemap. */
add_filter(
	'wp_sitemaps_posts_query_args',
	static function ( $args, $post_type ) {
		if ( 'page' === $post_type ) {
			$ids = array_filter( array_map( static fn( $slug ) => get_page_by_path( $slug )?->ID, array( 'thank-you', 'welcome' ) ) );
			$args['post__not_in'] = array_merge( $args['post__not_in'] ?? array(), $ids );
		}
		return $args;
	},
	10,
	2
);

/** No comments anywhere (nothing to moderate, no comment data in the privacy policy). */
add_filter( 'comments_open', '__return_false', 20 );
add_filter( 'pings_open', '__return_false', 20 );
add_filter( 'comments_array', '__return_empty_array', 10 );

/**
 * Affiliate links in posts are marked automatically: rel="sponsored nofollow noopener" and a visible
 * "(affiliate link)" label right after the link (FTC guides, German UWG: the advertising must be recognizable at
 * the link itself). Detected by the link's host (Amazon and common networks) or by rel="sponsored" set by hand.
 */
function lmp_affiliate_hosts() {
	return apply_filters(
		'lmp_affiliate_hosts',
		array( 'amzn.to', 'amzn.eu', 'amzn.com', 'a.co', 'awin1.com', 'shareasale.com', 'hop.clickbank.net', 'digistore24.com', 'go.skimresources.com' )
	);
}

function lmp_is_affiliate_url( $url ) {
	$host = preg_replace( '/^www\./', '', strtolower( (string) wp_parse_url( $url, PHP_URL_HOST ) ) );
	if ( '' === $host ) {
		return false;
	}
	if ( preg_match( '/^amazon\.[a-z.]+$/', $host ) ) {
		return true;
	}
	foreach ( lmp_affiliate_hosts() as $aff ) {
		if ( $host === $aff || str_ends_with( $host, '.' . $aff ) ) {
			return true;
		}
	}
	return false;
}

add_filter(
	'the_content',
	static function ( $html ) {
		if ( 'post' !== get_post_type() || false === stripos( $html, '<a ' ) ) {
			return $html;
		}
		return preg_replace_callback(
			'#(<a\s[^>]*>)(.*?)</a>#is',
			static function ( $m ) {
				$tag = new WP_HTML_Tag_Processor( $m[1] );
				if ( ! $tag->next_tag( 'a' ) ) {
					return $m[0];
				}
				$rel  = preg_split( '/\s+/', strtolower( trim( (string) $tag->get_attribute( 'rel' ) ) ) );
				$href = html_entity_decode( (string) $tag->get_attribute( 'href' ) );
				if ( ! in_array( 'sponsored', $rel, true ) && ! lmp_is_affiliate_url( $href ) ) {
					return $m[0];
				}
				$tag->set_attribute( 'rel', implode( ' ', array_unique( array_filter( array_merge( $rel, array( 'sponsored', 'nofollow', 'noopener' ) ) ) ) ) );
				return $tag->get_updated_html() . $m[2] . '</a><span class="lmp-aff"> (affiliate link)</span>';
			},
			$html
		);
	},
	20
);

/** Text blocks the template adds around every post. */
function lmp_affiliate_note() {
	$op     = get_option( 'lmp_operator', array() );
	$amazon = trim( (string) ( $op['amazon'] ?? '' ) ) !== '' ? ' As an Amazon Associate I earn from qualifying purchases.' : '';
	return '<p class="lmp-post__disclosure">This post may contain affiliate links. If you buy through them, we may earn a commission at no extra cost to you.' . $amazon . ' <a href="/disclaimer/">Learn more</a></p>';
}

function lmp_health_note() {
	return '<p class="lmp-post__health">This article is for general information only and isn\'t medical advice. Talk to your doctor before changing how you eat or exercise. <a href="/disclaimer/">Disclaimer</a></p>';
}
