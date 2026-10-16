# Pinterest-Pins mit echten Fotos

30 Pins (1000 × 1500 px) in `pins/`, gebaut mit echten Fotos von [Pexels](https://www.pexels.com/): keine KI-Bilder,
keine Personen. Die Nummer im Dateinamen ist die Reihenfolge zum Posten.

| Datei | Inhalt |
|---|---|
| `pins.json` | Pro Pin: Nummer, Tag, Layout, Artikel (`slug`, `link`), Pexels-Foto-ID, Bildausschnitt (`pos`), Lage der Textkarte (`card`), Bildtexte (`kicker`, `headline`, `hl` = hervorgehobener Teil, `sub`) und die Texte für Pinterest (`board`, `title`, `desc`, `alt`) |
| `pin.html` | Vorlage mit drei Layouts: **A** Foto oben, grüner Textblock; **B** heller Hintergrund, abgerundetes Foto; **C** Foto über die ganze Fläche mit Textkarte |
| `render.mjs` | Macht aus der Vorlage JPG-Dateien (Playwright) |
| `build.py` | Lädt die Fotos und baut alle Pins |
| `pins/` | Die fertigen Pins |

```
python3 build.py --fetch                          # Fotos von Pexels nach photos/ laden
PW_PATH=/pfad/zu/playwright python3 build.py      # alle Pins bauen
PW_PATH=/pfad/zu/playwright python3 build.py 4 8  # nur Pin 4 und 8
```

**Lizenz der Fotos:** Pexels-Lizenz, kostenlos, auch kommerziell, ohne Namensnennung. Nicht erlaubt ist, die
Originalfotos unverändert weiterzugeben oder zu verkaufen. Darum liegen nur die fertigen Pins im Repository; der
Ordner `photos/` wird von git ignoriert. Die Foto-Seite zu jeder ID: `https://www.pexels.com/photo/<id>/`.

**Posten:** Der Tag steht in `pins.json` (Feld `day`) und im gemeinsamen Plan `../pin-plan.csv`: pro Tag 2 Pins
mit Link (Foto- und Grafik-Pins gemischt) und 1 Tipp-Pin ohne Link aus `../tip-pins/`. Derselbe Artikel kommt
frühestens nach 4 Tagen wieder dran. Pins 2, 10 und 27 verlinken auf die Startseite (kostenloser Plan), alle
anderen auf ihren Artikel.

Schrift: Instrument Sans (OFL) aus `../graphics/fonts/`.
