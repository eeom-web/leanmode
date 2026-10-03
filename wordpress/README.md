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

## Anmeldeformular (Brevo, Double-Opt-in)

Das Formular der Website sendet direkt an ein Brevo-Anmeldeformular (Stand 03.10.2026). Im gemeinsamen
Assets-Widget steht in `CONFIG.brevoFormUrl` die öffentliche Formular-Adresse aus dem Brevo-Einbettungscode
(`action`, `…sibforms.com/serve/…`). Das ist kein Geheimnis: Es wird **kein API-Schlüssel** verwendet, auf
dem Server ist keiner gespeichert.

Ablauf: Eintragen → das Skript schickt `EMAIL`, das leere Spam-Schutzfeld `email_address_check` und `locale`
per POST an `<brevoFormUrl>?isAjax=1` (wie Brevos eigenes Einbettungsskript, ohne Cookies) → bei
`success: true` Weiterleitung auf `/tesekkurler/` → Brevo schickt die Bestätigungs-Mail → nach dem Klick
leitet Brevo auf die im Formular eingestellte Seite weiter (`/kayit-onaylandi/`, Download).

Liste, Bestätigungs-Mail, Weiterleitung nach der Bestätigung und Captcha (aus) werden in Brevo im Formular
eingestellt, nicht hier. Brevo-Skripte, -Styles oder -Schriften werden nicht geladen; Brevo wird erst beim
Absenden kontaktiert. Leeres `brevoFormUrl` = Demo-Modus.

`brevo/doi-tr.html` ist ein Entwurf für die Bestätigungs-Mail; die Platzhalter `{{lmp:name}}` usw. müssen vor
der Verwendung durch die Angaben aus dem Impressum ersetzt werden, `{{ doubleoptin }}` ist Brevos Platzhalter
für den Bestätigungslink.
