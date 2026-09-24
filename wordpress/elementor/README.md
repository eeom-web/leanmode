# Elementor-Build für leanmodepro.com

Hier wird die Landingpage für WordPress/Elementor erzeugt, und zwar mit dem klassischen Editor
(Container und Standard-Widgets, kein Atomic Editor, kein Elementor Pro).

| Datei        | Inhalt                                                                   |
| ------------ | ------------------------------------------------------------------------ |
| `tokens.py`  | Farben und Schriftstile, die auch als globale Elementor-Werte angelegt sind |
| `kit.py`     | Globale Elementor-Einstellungen (Farben, Schriften, Containerbreite)     |
| `assets.py`  | Inhalt der HTML-Widgets: Seiten-CSS, Formular-Skript, E-Book-Cover, Formular |
| `gen.py`     | Seitenaufbau aller Seiten (siehe unten)                                  |
| `dist/*.json`| Erzeugte Elementor-Daten (`python3 gen.py`)                              |

## Seiten

| Seite | Adresse | Zweck |
| ----- | ------- | ----- |
| Landingpage | `/` | Startseite mit Anmeldeformular |
| Bestätigungsseite | `/tesekkurler/` | Nach dem Absenden des Formulars: „E-Mail prüfen und bestätigen“ |
| Dankeseite | `/kayit-onaylandi/` | Nach dem Klick auf den Bestätigungslink: E-Book zum Download |
| Rechtsseiten | `/gizlilik-politikasi/`, `/cerez-politikasi/`, `/yasal-bilgiler/` | Platzhalter |

Bestätigungs- und Dankeseite passen am PC ohne Scrollen auf einen Bildschirm und sind auf
„noindex“ gestellt. Das E-Book-PDF liegt in der Mediathek unter
`/wp-content/uploads/2026/09/lean-mode-pro-30-gunluk-kilo-verme-plani.pdf`. In Brevo gehört
`https://leanmodepro.com/kayit-onaylandi/` als Weiterleitung nach der Double-Opt-in-Bestätigung eingetragen.

## Wichtig

- Nach dem Import wird die Seite **direkt in Elementor** gepflegt. `gen.py` dient nur für den
  ersten Aufbau und als Backup. Ein erneuter Import überschreibt Änderungen, die im Editor
  gemacht wurden.
- Das E-Mail-Formular steckt in HTML-Widgets, weil Elementor Free kein Formular-Widget hat.
  Bis Brevo angebunden ist, läuft es im **Demo-Modus** und sendet nichts. Die Einstellung
  steht im Widget „home-assets“ (erstes Element im Header), Variable `CONFIG.endpoint`.
- Globale Farben und Schriften: Elementor → Website-Einstellungen → Globale Farben / Globale Schriftarten.
