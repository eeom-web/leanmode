<?php
/**
 * Plugin Name: Lean Mode Pro – Datenschutz
 * Description: Schaltet die WordPress-Emoji-Skripte im Frontend ab. Sie schreiben in den Browser-Speicher
 *              (sessionStorage) und laden bei älteren Browsern Bilder von s.w.org. Die Seite nutzt keine Emojis.
 * Version:     1.0
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action(
	'init',
	static function () {
		remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
		remove_action( 'wp_enqueue_scripts', 'wp_enqueue_emoji_styles' );
		remove_action( 'wp_print_styles', 'print_emoji_styles' );
		remove_filter( 'the_content_feed', 'wp_staticize_emoji' );
		remove_filter( 'comment_text_rss', 'wp_staticize_emoji' );
		remove_filter( 'wp_mail', 'wp_staticize_emoji_for_email' );
		add_filter( 'emoji_svg_url', '__return_false' );
	}
);
