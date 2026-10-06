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

| Seite | Adresse | Zweck |
| ----- | ------- | ----- |
| Landingpage | `/` | Startseite mit Anmeldeformular |
| Bestätigungsseite | `/tesekkurler/` | Nach dem Absenden des Formulars: „E-Mail prüfen und bestätigen“ |
| Dankeseite | `/kayit-onaylandi/` | Nach dem Klick auf den Bestätigungslink: E-Book zum Download |
| Rechtsseiten | `/yasal-bilgiler/` (Impressum), `/gizlilik-politikasi/` (Datenschutz), `/cerez-politikasi/` (Cookies) | Texte in `legal.py` |

Bestätigungs- und Dankeseite passen am PC ohne Scrollen auf einen Bildschirm und sind auf
„noindex“ gestellt. Das E-Book-PDF liegt in der Mediathek unter
`/wp-content/uploads/2026/09/lean-mode-pro-30-gunluk-kilo-verme-plani.pdf`. In Brevo gehört
`https://leanmodepro.com/kayit-onaylandi/` als Weiterleitung nach der Double-Opt-in-Bestätigung eingetragen.

## Rechtstexte

- Name, Anschrift, E-Mail, Telefon und USt-IdNr. stehen **nicht** im Repository. Die Texte enthalten
  Platzhalter wie `{{lmp:name}}`; beim Import auf WordPress werden sie aus der Option `lmp_operator`
  ersetzt. Leere optionale Felder (USt-IdNr., Telefon, zuständige Aufsichtsbehörde) fallen samt
  ihrem Block weg, z. B. alles zwischen `<!--lmp:vat-->` und `<!--/lmp:vat-->`.
- Die Datenschutzerklärung beschreibt den Stand vom 24.09.2026: keine Cookies, kein Browser-Speicher,
  keine externen Verbindungen für Besucher. Dafür ist „Hostinger Reach“ deaktiviert und das
  Must-use-Plugin `wordpress/mu-plugins/lmp-privacy.php` schaltet das WordPress-Emoji-Skript ab.
  Wer neue Plugins, Einbettungen, Statistik-Tools oder Ähnliches einbaut, muss die Texte anpassen.
- Brevo läuft mit Double-Opt-in; die Datenschutzerklärung beschreibt die Messung von Öffnungen und
  Klicks (Brevo-Standard). Wird das Tracking in Brevo abgeschaltet, kann der Abschnitt wieder raus.
- **Tracking-Schalter** in `lmp_operator`: `tracking` (Cookie-Banner aktiv) und je Werkzeug `meta`, `ga`,
  `gads`, `google` (= ga oder gads). Nur gesetzte Werkzeuge erscheinen in Datenschutz- und Cookie-Seite.
  Stand 06.10.2026: `tracking` und `meta` gesetzt (Meta Pixel 2362284981222890).
- **Cookie-Banner** im gemeinsamen Assets-Skript: Der Meta Pixel lädt erst nach „Kabul et“, die Wahl steht
  im notwendigen Cookie `lmp_consent` (12 Monate). Footer-Link „Çerez ayarları“ (`#cerez-ayarlari`) öffnet
  den Banner erneut; beim Widerruf werden `_fbp`/`_fbc` gelöscht. Kein `<noscript>`-Pixel (der würde ohne
  Einwilligung senden). Weitere Werkzeuge (Google) müssen ebenfalls über diesen Banner laufen.

## Wichtig

- Nach dem Import wird die Seite **direkt in Elementor** gepflegt. `gen.py` dient nur für den
  ersten Aufbau und als Backup. Ein erneuter Import überschreibt Änderungen, die im Editor
  gemacht wurden.
- Das E-Mail-Formular steckt in HTML-Widgets, weil Elementor Free kein Formular-Widget hat.
  Es sendet an ein Brevo-Anmeldeformular (Double-Opt-in), siehe `../README.md`. Die Einstellung steht
  im Assets-Widget (erstes Element im Header jeder Seite), Variable `CONFIG.brevoFormUrl`.
- Globale Farben und Schriften: Elementor → Website-Einstellungen → Globale Farben / Globale Schriftarten.
