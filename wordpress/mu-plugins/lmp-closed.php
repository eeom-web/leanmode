<?php
/**
 * Plugin Name: Lean Mode Pro – Seite geschlossen
 * Description: Schließt die Website für Besucher (HTTP 503, kein Formular, kein Pixel). Erreichbar bleiben die
 *              Rechtsseiten (Impressum-Pflicht für Facebook/Instagram, Links in den E-Mails) und die Download-Seite
 *              für bereits angemeldete Leser. Eingeloggte Administratoren sehen die Seite normal.
 *              Zum Wiedereröffnen diese Datei aus wp-content/mu-plugins/ löschen.
 * Version:     1.0
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action(
	'template_redirect',
	static function () {
		if ( current_user_can( 'manage_options' ) ) {
			return;
		}
		$open = array( 'yasal-bilgiler', 'gizlilik-politikasi', 'kvkk-aydinlatma-metni', 'cerez-politikasi', 'kayit-onaylandi' );
		if ( is_page( $open ) ) {
			return;
		}

		status_header( 503 );
		header( 'Retry-After: 86400' );
		header( 'Cache-Control: no-store' );
		header( 'X-Robots-Tag: noindex' );
		header( 'Content-Type: text/html; charset=utf-8' );
		?>
<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>LEAN MODE PRO</title>
<style>
body{margin:0;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px 16px;box-sizing:border-box;background:#F6F5F1;color:#414B46;font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;text-align:center}
.logo{margin:0 0 28px;color:#101614;font-size:14px;font-weight:700;letter-spacing:.14em}
.logo span{color:#1D5A48}
h1{margin:0 0 12px;color:#101614;font-size:26px;line-height:1.2;font-weight:600}
p{margin:0 auto 12px;max-width:34rem}
nav{margin-top:32px;font-size:14px}
nav a{color:#5D6762;margin:0 8px;text-decoration:underline;text-underline-offset:2px}
</style>
</head>
<body>
<p class="logo">LEAN MODE <span>PRO</span></p>
<h1>Site şu anda kapalı</h1>
<p>Şu anda yeni kayıt almıyoruz.</p>
<p>Daha önce kayıt olduysan, planına onay e-postandaki bağlantıdan ulaşabilirsin.</p>
<nav>
<a href="/yasal-bilgiler/">Yasal Bilgiler</a>
<a href="/gizlilik-politikasi/">Gizlilik Politikası</a>
<a href="/kvkk-aydinlatma-metni/">KVKK Aydınlatma Metni</a>
<a href="/cerez-politikasi/">Çerez Politikası</a>
</nav>
</body>
</html>
		<?php
		exit;
	},
	0
);
