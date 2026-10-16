<?php
/**
 * Plugin Name: Lean Mode Pro – Contact form
 * Description: Backend of the contact form on /contact/ (second contact channel for the Legal Notice). The form posts
 *              to /wp-json/lmp/v1/contact. Every message is saved as a private "Message" in WordPress (Dashboard →
 *              Messages) and sent to the email address in the option `lmp_operator` with wp_mail (whatever mailer
 *              the site uses, currently WP Mail SMTP). Spam protection without external services: honeypot field,
 *              limit of 5 messages per hour per IP (only a hash of the IP is kept, for one hour), link limit.
 *              Messages are deleted automatically after 12 months.
 * Version:     1.0
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const LMP_CONTACT_MAX_PER_HOUR = 5;

add_action(
	'init',
	static function () {
		register_post_type(
			'lmp_message',
			array(
				'labels'          => array(
					'name'          => 'Messages',
					'singular_name' => 'Message',
					'menu_name'     => 'Messages',
					'all_items'     => 'All messages',
					'edit_item'     => 'Message',
					'search_items'  => 'Search messages',
					'not_found'     => 'No messages yet.',
				),
				'public'          => false,
				'show_ui'         => true,
				'show_in_menu'    => true,
				'show_in_rest'    => false,
				'menu_icon'       => 'dashicons-email-alt',
				'menu_position'   => 26,
				'supports'        => array( 'title', 'editor' ),
				'capability_type' => 'post',
				'capabilities'    => array( 'create_posts' => 'do_not_allow' ),
				'map_meta_cap'    => true,
			)
		);
	}
);

add_action(
	'rest_api_init',
	static function () {
		register_rest_route(
			'lmp/v1',
			'/contact',
			array(
				'methods'             => 'POST',
				'callback'            => 'lmp_contact_submit',
				'permission_callback' => '__return_true',
			)
		);
	}
);

/**
 * Answer for the script on the page (JSON) or, without JavaScript, a small HTML page.
 */
function lmp_contact_reply( $ok, $ajax, $error = '' ) {
	$texts = array(
		'invalid' => 'Please enter a valid email address and a message.',
		'links'   => 'Please remove the links from your message.',
		'rate'    => 'You have sent several messages in a short time. Please try again later or email us directly.',
		'failed'  => 'Your message could not be sent. Please email us directly.',
	);
	if ( $ajax ) {
		return new WP_REST_Response( array( 'ok' => $ok, 'message' => $ok ? '' : ( $texts[ $error ] ?? $texts['failed'] ) ), $ok ? 200 : 400 );
	}
	$title = $ok ? 'Thanks, your message has been sent.' : ( $texts[ $error ] ?? $texts['failed'] );
	status_header( $ok ? 200 : 400 );
	header( 'Content-Type: text/html; charset=utf-8' );
	header( 'X-Robots-Tag: noindex' );
	echo '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Contact – Lean Mode Pro</title>'
		. '<style>body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px;box-sizing:border-box;background:#F6F5F1;color:#414B46;font:17px/1.6 system-ui,sans-serif;text-align:center}h1{color:#101614;font-size:24px}a{color:#1D5A48}</style></head>'
		. '<body><div><h1>' . esc_html( $title ) . '</h1><p><a href="' . esc_url( home_url( '/contact/' ) ) . '">Back to the contact page</a></p></div></body></html>';
	exit;
}

function lmp_contact_submit( WP_REST_Request $request ) {
	$ajax = '1' === $request->get_header( 'x_lmp_ajax' );

	// Bots fill the hidden field: pretend success, keep nothing.
	if ( '' !== trim( (string) $request->get_param( 'website' ) ) ) {
		return lmp_contact_reply( true, $ajax );
	}

	$name    = sanitize_text_field( mb_substr( (string) $request->get_param( 'name' ), 0, 100 ) );
	$email   = sanitize_email( mb_substr( (string) $request->get_param( 'email' ), 0, 254 ) );
	$message = sanitize_textarea_field( mb_substr( (string) $request->get_param( 'message' ), 0, 5000 ) );
	if ( ! is_email( $email ) || mb_strlen( trim( $message ) ) < 2 ) {
		return lmp_contact_reply( false, $ajax, 'invalid' );
	}
	if ( preg_match_all( '#https?://|www\.#i', $message ) > 3 ) {
		return lmp_contact_reply( false, $ajax, 'links' );
	}

	$ip   = (string) ( $_SERVER['REMOTE_ADDR'] ?? '' );
	$key  = 'lmp_contact_' . substr( hash_hmac( 'sha256', $ip, wp_salt( 'nonce' ) ), 0, 32 );
	$sent = (int) get_transient( $key );
	if ( $sent >= LMP_CONTACT_MAX_PER_HOUR ) {
		return lmp_contact_reply( false, $ajax, 'rate' );
	}
	set_transient( $key, $sent + 1, HOUR_IN_SECONDS );

	$from = '' !== $name ? $name . ' <' . $email . '>' : $email;
	$id   = wp_insert_post(
		array(
			'post_type'    => 'lmp_message',
			'post_status'  => 'private',
			'post_title'   => $from,
			'post_content' => $message,
			'meta_input'   => array(
				'_lmp_email' => $email,
				'_lmp_name'  => $name,
			),
		),
		true
	);
	if ( is_wp_error( $id ) ) {
		return lmp_contact_reply( false, $ajax, 'failed' );
	}

	$op = get_option( 'lmp_operator', array() );
	$to = sanitize_email( (string) ( $op['email'] ?? '' ) );
	if ( $to ) {
		$reply_name = str_replace( array( '"', '<', '>' ), '', $name );
		$headers    = array(
			'Content-Type: text/plain; charset=UTF-8',
			'Reply-To: ' . ( '' !== $reply_name ? '"' . $reply_name . '" <' . $email . '>' : $email ),
		);
		$body       = "New message via the contact form on leanmodepro.com\n\n"
			. 'Name: ' . ( '' !== $name ? $name : '–' ) . "\n"
			. 'Email: ' . $email . "\n\n"
			. $message . "\n\n"
			. "Reply to this email to answer. The message is also saved in WordPress under Messages:\n"
			. admin_url( 'post.php?post=' . $id . '&action=edit' ) . "\n";
		$mailed     = wp_mail( $to, 'Contact form: ' . ( '' !== $name ? $name : $email ), $body, $headers );
		update_post_meta( $id, '_lmp_mailed', $mailed ? 1 : 0 );
	}

	// The message is saved even if the email could not be sent, so the visitor gets a success message.
	return lmp_contact_reply( true, $ajax );
}

/** Dashboard list: sender email and whether the notification email went out. */
add_filter(
	'manage_lmp_message_posts_columns',
	static function ( $cols ) {
		return array(
			'cb'          => $cols['cb'] ?? '',
			'title'       => 'From',
			'lmp_excerpt' => 'Message',
			'lmp_mailed'  => 'Email sent',
			'date'        => 'Date',
		);
	}
);

add_action(
	'manage_lmp_message_posts_custom_column',
	static function ( $col, $post_id ) {
		if ( 'lmp_excerpt' === $col ) {
			echo esc_html( wp_trim_words( get_post_field( 'post_content', $post_id ), 20, '…' ) );
		} elseif ( 'lmp_mailed' === $col ) {
			echo get_post_meta( $post_id, '_lmp_mailed', true ) ? 'yes' : 'no';
		}
	},
	10,
	2
);

/** Messages older than 12 months are deleted (storage limitation, see Privacy Policy). */
add_action(
	'lmp_contact_cleanup',
	static function () {
		$old = get_posts(
			array(
				'post_type'      => 'lmp_message',
				'post_status'    => 'any',
				'date_query'     => array( array( 'before' => '12 months ago' ) ),
				'fields'         => 'ids',
				'posts_per_page' => 200,
			)
		);
		foreach ( $old as $id ) {
			wp_delete_post( $id, true );
		}
	}
);

add_action(
	'init',
	static function () {
		if ( ! wp_next_scheduled( 'lmp_contact_cleanup' ) ) {
			wp_schedule_event( time() + HOUR_IN_SECONDS, 'daily', 'lmp_contact_cleanup' );
		}
	}
);
