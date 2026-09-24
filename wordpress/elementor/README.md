# Elementor-Build für leanmodepro.com

Hier wird die Landingpage für WordPress/Elementor erzeugt, und zwar mit dem klassischen Editor
(Container und Standard-Widgets, kein Atomic Editor, kein Elementor Pro).

| Datei        | Inhalt                                                                   |
| ------------ | ------------------------------------------------------------------------ |
| `tokens.py`  | Farben und Schriftstile, die auch als globale Elementor-Werte angelegt sind |
| `kit.py`     | Globale Elementor-Einstellungen (Farben, Schriften, Containerbreite)     |
| `assets.py`  | Inhalt der HTML-Widgets: Seiten-CSS, Formular-Skript, E-Book-Cover, Formular |
| `gen.py`     | Seitenaufbau (Landingpage und drei Rechtsseiten als Platzhalter)          |
| `dist/*.json`| Erzeugte Elementor-Daten (`python3 gen.py`)                              |

## Wichtig

- Nach dem Import wird die Seite **direkt in Elementor** gepflegt. `gen.py` dient nur für den
  ersten Aufbau und als Backup. Ein erneuter Import überschreibt Änderungen, die im Editor
  gemacht wurden.
- Das E-Mail-Formular steckt in HTML-Widgets, weil Elementor Free kein Formular-Widget hat.
  Bis Brevo angebunden ist, läuft es im **Demo-Modus** und sendet nichts. Die Einstellung
  steht im Widget „home-assets“ (erstes Element im Header), Variable `CONFIG.endpoint`.
- Globale Farben und Schriften: Elementor → Website-Einstellungen → Globale Farben / Globale Schriftarten.
