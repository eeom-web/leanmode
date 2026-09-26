# WordPress (leanmodepro.com)

| Ordner | Inhalt |
| ------ | ------ |
| `elementor/` | Seitenaufbau für Elementor, Rechtstexte, gemeinsames CSS/JS (siehe dortige README) |
| `mu-plugins/lmp-privacy.php` | Schaltet das WordPress-Emoji-Skript ab (kein Browser-Speicher, keine Anfragen an s.w.org) |
| `mu-plugins/lmp-signup.php` | Anmelde-Endpunkt `POST /wp-json/lmp/v1/subscribe` für das Formular |
| `mu-plugins/lmp-site-icon.php` | Vollflächiges Apple-Touch-Icon statt des abgerundeten Website-Icons |
| `brand/site-icon-512.png` | Website-Icon (Tab-Symbol), aus `public/favicon.svg` erzeugt |
| `brand/apple-touch-icon-180.png` | Icon für den iPhone-Homescreen (vollflächig) |
| `brevo/doi-tr.html` | Bestätigungs-Mail (Double-Opt-in, Türkisch) als Brevo-Vorlage |

Die Must-use-Plugins liegen auf dem Server in `wp-content/mu-plugins/`.

## Anmeldung mit Brevo (Double-Opt-in)

1. Das Formular schickt `{ email, source }` an `/wp-json/lmp/v1/subscribe`.
2. Der Endpunkt ruft Brevo `POST /v3/contacts/doubleOptinConfirmation` auf (Liste, DOI-Vorlage,
   Weiterleitung nach der Bestätigung auf `/kayit-onaylandi/`).
3. Der Besucher landet auf `/tesekkurler/`, bestätigt per Mail und kommt auf die Download-Seite.

Zugangsdaten stehen nur in der WordPress-Option `lmp_brevo` (`api_key`, `list_id`, `template_id`,
`redirect_url`), nie im Repository. In Brevo: Absender `info@leanmodepro.com`, Liste
„LEAN MODE PRO – 30 Günlük Plan“, Vorlage „LEAN MODE PRO – Double Opt-in (TR)“ mit Tag `optin`.
Ohne vollständige Option antwortet der Endpunkt mit 503; bereits eingetragene Adressen bekommen
dieselbe Antwort wie neue, damit das Formular nicht verrät, wer auf der Liste steht. Pro IP sind
5 Anfragen in 10 Minuten erlaubt.

Die Vorlage enthält Platzhalter (`{{lmp:name}}` …), die beim Anlegen aus der Option `lmp_operator`
gefüllt werden, und den Brevo-Platzhalter `{{ doubleoptin }}` für den Bestätigungslink. Die Mail
enthält bewusst keine Werbung.
