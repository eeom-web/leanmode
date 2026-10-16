# Elementor-Build für leanmodepro.com

Hier wird die Landingpage für WordPress/Elementor erzeugt, und zwar mit dem klassischen Editor
(Container und Standard-Widgets, kein Atomic Editor, kein Elementor Pro).

| Datei        | Inhalt                                                                   |
| ------------ | ------------------------------------------------------------------------ |
| `tokens.py`  | Farben und Schriftstile, die auch als globale Elementor-Werte angelegt sind |
| `kit.py`     | Globale Elementor-Einstellungen (Farben, Schriften, Containerbreite)     |
| `assets.py`  | Inhalt der HTML-Widgets: Seiten-CSS, Formular-Skript, E-Book-Cover, Formular |
| `gen.py`     | Seitenaufbau aller Seiten (siehe unten)                                  |
| `legal.py`   | Texte der Rechtsseiten (Türkisch)                                        |
| `dist/*.json`| Erzeugte Elementor-Daten (`python3 gen.py`)                              |

## Seiten

Die Website ist seit 14.10.2026 englisch (vorher türkisch, siehe Git-Historie).

| Seite | Adresse | Zweck |
| ----- | ------- | ----- |
| Landingpage | `/` | Startseite mit Anmeldeformular (`#signup`) |
| Bestätigungsseite | `/thank-you/` | Nach dem Absenden des Formulars: „E-Mail prüfen und bestätigen“ |
| Dankeseite | `/welcome/` | Nach dem Klick auf den Bestätigungslink: E-Book zum Download |
| Rechtsseiten | `/legal-notice/` (Impressum), `/privacy-policy/` (Datenschutz), `/disclaimer/` (Gesundheitshinweis und Affiliate-Offenlegung) | Texte in `legal.py` |
| Blog | `/blog/` und Beiträge | Eigenes Template im Must-use-Plugin `lmp-blog` (siehe `../README.md`) |

Bestätigungs- und Dankeseite passen am PC ohne Scrollen auf einen Bildschirm und sind auf
„noindex“ gestellt. Das E-Book-PDF liegt in der Mediathek unter
`/wp-content/uploads/2026/10/lean-mode-pro-30-day-weight-loss-plan-v2.pdf` (bei jeder Änderung ein neuer
Dateiname, damit kein Cache Teile der alten Datei ausliefert; die alte Adresse ohne `-v2` liefert dieselbe
Datei, damit ältere Links funktionieren). In Brevo gehört
`https://leanmodepro.com/welcome/` als Weiterleitung nach der Double-Opt-in-Bestätigung eingetragen
(die alte Adresse `/kayit-onaylandi/` leitet per 301 weiter).

## Rechtstexte

- Name, Anschrift, E-Mail, Telefon und USt-IdNr. stehen **nicht** im Repository. Die Texte enthalten
  Platzhalter wie `{{lmp:name}}`; beim Import auf WordPress werden sie aus der Option `lmp_operator`
  ersetzt. Leere optionale Felder (USt-IdNr., Telefon, zuständige Aufsichtsbehörde, `amazon`) fallen samt
  ihrem Block weg, z. B. alles zwischen `<!--lmp:vat-->` und `<!--/lmp:vat-->`.
- Stand 14.10.2026: keine Cookies, kein Browser-Speicher, kein Pixel, keine Analyse, keine externen
  Verbindungen für Besucher (deshalb auch kein Cookie-Banner und keine Cookie-Seite). „Hostinger Reach“ ist
  deaktiviert und `wordpress/mu-plugins/lmp-privacy.php` schaltet das Emoji-Skript ab. Wer Pixel, Analyse,
  Einbettungen oder neue Plugins einbaut, braucht wieder Banner und angepasste Texte (der frühere Meta-Pixel-
  Banner steht in der Git-Historie, Commit 3582b2f).
- Die Privacy Policy folgt im Aufbau der e-recht24-Vorlage (übersetzt und angepasst, Quellenhinweis am Ende):
  1. Überblick, 2. Hosting (Hostinger International Ltd. laut AVV, Registrar HOSTINGER operations, UAB),
  3. Pflichtinformationen und Rechte, 4. Datenerfassung (keine Cookies, Server-Logs, E-Mail-Kontakt, Schrift,
  Download, Affiliate-Links), 5. Social Media (keine Plugins; Profile auf Pinterest, Instagram, TikTok, YouTube),
  6. Newsletter mit Double-Opt-in über Brevo, 7. Änderungen.
- Der Disclaimer enthält Gesundheitshinweis (18+, keine Ergebnisgarantie) und Affiliate-Offenlegung. Sobald der
  Betreiber im Amazon-Partnerprogramm ist, `amazon` in `lmp_operator` setzen und die Rechtsseiten neu
  befüllen: Dann erscheinen der Pflichtsatz „As an Amazon Associate I earn from qualifying purchases“ und der
  Amazon-Abschnitt (der Blog-Hinweis über jedem Beitrag liest die Option direkt).
- Brevo läuft mit Double-Opt-in; die Privacy Policy beschreibt die Messung von Öffnungen und Klicks
  (Brevo-Standard). Der Einwilligungstext am Formular erwähnt sie nicht (Entscheidung des Betreibers);
  alternativ das Tracking in Brevo abschalten.

## Wichtig

- Nach dem Import wird die Seite **direkt in Elementor** gepflegt. `gen.py` dient nur für den
  ersten Aufbau und als Backup. Ein erneuter Import überschreibt Änderungen, die im Editor
  gemacht wurden.
- Das E-Mail-Formular steckt in HTML-Widgets, weil Elementor Free kein Formular-Widget hat.
  Es sendet an ein Brevo-Anmeldeformular (Double-Opt-in), siehe `../README.md`. Die Einstellung steht
  im Assets-Widget (erstes Element im Header jeder Seite), Variable `CONFIG.brevoFormUrl`.
- Globale Farben und Schriften: Elementor → Website-Einstellungen → Globale Farben / Globale Schriftarten.
