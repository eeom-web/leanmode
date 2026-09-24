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
  ersetzt. Ohne USt-IdNr. fällt der Block zwischen `<!--lmp:vat-->` und `<!--/lmp:vat-->` weg.
- Die Datenschutzerklärung beschreibt den Stand vom 24.09.2026: keine Cookies, kein Browser-Speicher,
  keine externen Verbindungen für Besucher. Dafür ist „Hostinger Reach“ deaktiviert und das
  Must-use-Plugin `wordpress/mu-plugins/lmp-privacy.php` schaltet das WordPress-Emoji-Skript ab.
  Wer neue Plugins, Einbettungen, Statistik-Tools oder Ähnliches einbaut, muss die Texte anpassen.
- Brevo muss mit Double-Opt-in und **ohne** Öffnungs- und Klick-Tracking eingerichtet werden, so steht es
  in der Datenschutzerklärung.

## Wichtig

- Nach dem Import wird die Seite **direkt in Elementor** gepflegt. `gen.py` dient nur für den
  ersten Aufbau und als Backup. Ein erneuter Import überschreibt Änderungen, die im Editor
  gemacht wurden.
- Das E-Mail-Formular steckt in HTML-Widgets, weil Elementor Free kein Formular-Widget hat.
  Bis Brevo angebunden ist, läuft es im **Demo-Modus** und sendet nichts. Die Einstellung
  steht im Widget „home-assets“ (erstes Element im Header), Variable `CONFIG.endpoint`.
- Globale Farben und Schriften: Elementor → Website-Einstellungen → Globale Farben / Globale Schriftarten.
