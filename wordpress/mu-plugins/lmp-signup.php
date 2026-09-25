<?php
/**
 * Plugin Name: Lean Mode Pro – Anmeldung (Brevo)
 * Description: REST-Endpunkt POST /wp-json/lmp/v1/subscribe für das Anmeldeformular. Startet bei Brevo
 *              das Double-Opt-in; der Bestätigungslink führt auf die Dankeseite. Zugangsdaten stehen in der
 *              Option „lmp_brevo“ (api_key, list_id, template_id, redirect_url), nicht im Code.
 * Version:     1.0
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action(
	'rest_api_init',
	static function () {
		register_rest_route(
			'lmp/v1',
			'/subscribe',
			array(
				'methods'             => 'POST',
				'permission_callback' => '__return_true',
				'callback'            => 'lmp_signup_handle',
			)
		);
	}
);

/**
 * @param WP_REST_Request $request Payload: { email, source, website (honeypot) }.
 */
function lmp_signup_handle( WP_REST_Request $request ) {
	$cfg = get_option( 'lmp_brevo', array() );
	if ( empty( $cfg['api_key'] ) || empty( $cfg['list_id'] ) || empty( $cfg['template_id'] ) ) {
		return lmp_signup_reply( 503, 'not_configured' );
	}

	// Bots fill the hidden field; they get a normal answer and nothing is sent.
	if ( '' !== trim( (string) $request->get_param( 'website' ) ) ) {
		return lmp_signup_reply( 200 );
	}

	$email = strtolower( trim( (string) $request->get_param( 'email' ) ) );
	if ( strlen( $email ) > 254 || ! is_email( $email ) ) {
		return lmp_signup_reply( 400, 'invalid_email' );
	}

	// Abuse protection: at most 5 requests per IP in 10 minutes. Only a keyed hash of the IP is kept, for 10 minutes.
	$ip_key = 'lmp_rl_' . substr( hash_hmac( 'sha256', (string) ( $_SERVER['REMOTE_ADDR'] ?? '' ), wp_salt( 'nonce' ) ), 0, 24 );
	$count  = (int) get_transient( $ip_key );
	if ( $count >= 5 ) {
		return lmp_signup_reply( 429, 'rate_limited' );
	}
	set_transient( $ip_key, $count + 1, 10 * MINUTE_IN_SECONDS );

	$response = wp_remote_post(
		'https://api.brevo.com/v3/contacts/doubleOptinConfirmation',
		array(
			'timeout' => 12,
			'headers' => array(
				'api-key'      => $cfg['api_key'],
				'Content-Type' => 'application/json',
				'Accept'       => 'application/json',
			),
			'body'    => wp_json_encode(
				array(
					'email'          => $email,
					'includeListIds' => array( (int) $cfg['list_id'] ),
					'templateId'     => (int) $cfg['template_id'],
					'redirectionUrl' => $cfg['redirect_url'] ?? home_url( '/kayit-onaylandi/' ),
				)
			),
		)
	);

	if ( is_wp_error( $response ) ) {
		error_log( '[lmp-signup] ' . $response->get_error_message() );
		return lmp_signup_reply( 502, 'upstream' );
	}

	$code = (int) wp_remote_retrieve_response_code( $response );
	if ( $code >= 200 && $code < 300 ) {
		return lmp_signup_reply( 200 );
	}

	$error = json_decode( wp_remote_retrieve_body( $response ), true );
	// Already on the list: answer like a new signup, so the form does not reveal who is subscribed.
	if ( 400 === $code && 'duplicate_parameter' === ( $error['code'] ?? '' ) ) {
		return lmp_signup_reply( 200 );
	}

	error_log( sprintf( '[lmp-signup] Brevo %d %s %s', $code, $error['code'] ?? '', $error['message'] ?? '' ) );
	return lmp_signup_reply( 502, 'upstream' );
}

function lmp_signup_reply( $status, $error = null ) {
	$response = new WP_REST_Response( $error ? array( 'ok' => false, 'error' => $error ) : array( 'ok' => true ), $status );
	$response->header( 'Cache-Control', 'no-store' );
	return $response;
}
