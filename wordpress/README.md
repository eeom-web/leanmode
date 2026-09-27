# WordPress (leanmodepro.com)

| Ordner | Inhalt |
| ------ | ------ |
| `elementor/` | Seitenaufbau für Elementor, Rechtstexte, gemeinsames CSS/JS (siehe dortige README) |
| `mu-plugins/lmp-privacy.php` | Schaltet das WordPress-Emoji-Skript ab (kein Browser-Speicher, keine Anfragen an s.w.org) |
| `mu-plugins/lmp-site-icon.php` | Vollflächiges Apple-Touch-Icon statt des abgerundeten Website-Icons |
| `brand/site-icon-512.png` | Website-Icon (Tab-Symbol), aus `public/favicon.svg` erzeugt |
| `brand/apple-touch-icon-180.png` | Icon für den iPhone-Homescreen (vollflächig) |
| `brand/favicon.ico` | Klassisches `/favicon.ico` im Web-Stammverzeichnis (16, 32, 48 px) |
| `brevo/doi-tr.html` | Entwurf einer Bestätigungs-Mail (Double-Opt-in, Türkisch), nicht verbunden |

Die Must-use-Plugins liegen auf dem Server in `wp-content/mu-plugins/`.

## Anmeldeformular

Die Website ist mit keinem E-Mail-Dienst verbunden (Stand 27.09.2026). Das Formular läuft im
Demo-Modus: `CONFIG.endpoint` im gemeinsamen Assets-Widget ist leer, es wird nichts gesendet oder
gespeichert, Besucher werden nur auf `/tesekkurler/` weitergeleitet. Die frühere Brevo-Anbindung
(Must-use-Plugin `lmp-signup.php`, Option `lmp_brevo`) ist vom Server und aus dem Repository entfernt.

Für eine spätere Anbindung: Nach der Double-Opt-in-Bestätigung sollte auf `/kayit-onaylandi/`
(Download-Seite) weitergeleitet werden. `brevo/doi-tr.html` ist ein Entwurf für die Bestätigungs-Mail;
die Platzhalter `{{lmp:name}}` usw. müssen vor der Verwendung durch die Angaben aus dem Impressum
ersetzt werden, `{{ doubleoptin }}` ist Brevos Platzhalter für den Bestätigungslink.
