# WordPress (leanmodepro.com)

| Ordner | Inhalt |
| ------ | ------ |
| `elementor/` | Seitenaufbau für Elementor, Rechtstexte, gemeinsames CSS/JS (siehe dortige README) |
| `mu-plugins/lmp-privacy.php` | Schaltet das WordPress-Emoji-Skript ab (kein Browser-Speicher, keine Anfragen an s.w.org) |
| `mu-plugins/lmp-site-icon.php` | Vollflächiges Apple-Touch-Icon statt des abgerundeten Website-Icons |
| `mu-plugins/lmp-closed.php` | Wartungsseite (HTTP 503), war vom 14.10.2026 bis zur englischen Neueröffnung aktiv. Liegt nicht mehr auf dem Server; zum Schließen der Seite wieder nach `wp-content/mu-plugins/` kopieren |
| `mu-plugins/lmp-blog.php`, `mu-plugins/lmp-blog/template.php` | Blog im Lean-Mode-Pro-Design: Beiträge, `/blog/` und Archive mit eigenem Template statt Block-Theme; jeder Beitrag bekommt oben einen Affiliate-Hinweis, unten Gesundheitshinweis und Anmeldebox; Open-Graph-Tags für Pinterest Rich Pins; Kommentare aus; Danke- und Willkommensseite nicht in der Sitemap; 301-Weiterleitungen der alten türkischen Adressen. CSS/JS, Formular und Cover kommen aus der Option `lmp_blog` (`elementor/dist/blog.json`) |
| `brand/site-icon-512.png` | Website-Icon (Tab-Symbol), aus `public/favicon.svg` erzeugt |
| `brand/apple-touch-icon-180.png` | Icon für den iPhone-Homescreen (vollflächig) |
| `brand/favicon.ico` | Klassisches `/favicon.ico` im Web-Stammverzeichnis (16, 32, 48 px) |
| `brand/ebook-cover-en-{360,540,720}.webp` | E-Book-Cover für die Website: Fotos aus der Canva-Vorlage des Betreibers, englisches Titelband, 2:3; Mediathek „Lean Mode Pro – E-Book Cover“ |
| `brevo/doi-en.html` | Entwurf der Bestätigungs-Mail (Double-Opt-in, Englisch) zum Einfügen in Brevo |

Die Must-use-Plugins liegen auf dem Server in `wp-content/mu-plugins/`.

## Anmeldeformular (Brevo, Double-Opt-in)

Das Formular der Website sendet direkt an ein Brevo-Anmeldeformular (Stand 03.10.2026). Im gemeinsamen
Assets-Widget steht in `CONFIG.brevoFormUrl` die öffentliche Formular-Adresse aus dem Brevo-Einbettungscode
(`action`, `…sibforms.com/serve/…`). Das ist kein Geheimnis: Es wird **kein API-Schlüssel** verwendet, auf
dem Server ist keiner gespeichert.

Ablauf: Eintragen → das Skript schickt `EMAIL`, das leere Spam-Schutzfeld `email_address_check` und `locale`
per POST an `<brevoFormUrl>?isAjax=1` (wie Brevos eigenes Einbettungsskript, ohne Cookies) → bei
`success: true` Weiterleitung auf `/thank-you/` → Brevo schickt die Bestätigungs-Mail → nach dem Klick
leitet Brevo auf die im Formular eingestellte Seite weiter (`/welcome/`, Download; die alte Adresse
`/kayit-onaylandi/` leitet per 301 dorthin weiter).

Liste, Bestätigungs-Mail, Weiterleitung nach der Bestätigung und Captcha (aus) werden in Brevo im Formular
eingestellt, nicht hier. Brevo-Skripte, -Styles oder -Schriften werden nicht geladen; Brevo wird erst beim
Absenden kontaktiert. Leeres `brevoFormUrl` = Demo-Modus.

`brevo/doi-en.html` ist ein Entwurf für die Bestätigungs-Mail; die Platzhalter `{{lmp:name}}` usw. müssen vor
der Verwendung durch die Angaben aus dem Impressum ersetzt werden, `{{ doubleoptin }}` ist Brevos Platzhalter
für den Bestätigungslink.
