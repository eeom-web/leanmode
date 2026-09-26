<?php
/**
 * Plugin Name: Lean Mode Pro – Website-Icon
 * Description: Liefert für iPhone/iPad eine vollflächige Variante des Website-Icons aus (iOS füllt durchsichtige
 *              Ecken schwarz). Das Website-Icon selbst steht unter Einstellungen → Allgemein; die Anhang-ID der
 *              Apple-Variante in der Option „lmp_apple_touch_icon“.
 * Version:     1.0
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_filter(
	'site_icon_meta_tags',
	static function ( $tags ) {
		$url = wp_get_attachment_image_url( (int) get_option( 'lmp_apple_touch_icon' ), 'full' );
		if ( ! $url ) {
			return $tags;
		}
		foreach ( $tags as $i => $tag ) {
			if ( str_contains( $tag, 'apple-touch-icon' ) ) {
				$tags[ $i ] = sprintf( '<link rel="apple-touch-icon" href="%s" />', esc_url( $url ) );
			}
		}
		return $tags;
	}
);
