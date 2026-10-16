# Tipp-Pins ohne Link

30 Pins (1000 × 1500 px) in `pins/`, auf denen der ganze Tipp steht: 20 einzelne Tipps und 10 kurze Listen. Sie werden
**ohne Link** gepostet (Feld „Link“ leer lassen). Sie sollen gespeichert werden und Vertrauen aufbauen; die Pins mit
Link bringen die Besucher auf die Website. Fotos: echte Fotos von [Pexels](https://www.pexels.com/), keine KI-Bilder,
keine Personen.

| Datei | Inhalt |
|---|---|
| `pins.json` | Pro Pin: Nummer, Tag, Art (`tip` oder `list`), Layout, Pexels-Foto-ID, Bildausschnitt (`pos`), Bildtexte (`kicker`, `headline`, `hl` = hervorgehobener Teil, `body` oder `items`) und die Texte für Pinterest (`board`, `title`, `desc`, `alt`) |
| `pin.html` | Vorlage: **T1** / **T2** = ein Tipp (hell / grün), **L1** / **L2** = Liste (hell / grün). Listenpunkte als `Vorher\|Nachher` werden als Tausch mit Pfeil gezeigt |
| `render.mjs`, `build.py` | Bauen die Pins wie bei `../photo-pins/` |

```
python3 build.py --fetch                          # Fotos von Pexels nach photos/ laden (nicht in git)
PW_PATH=/pfad/zu/playwright python3 build.py      # alle Pins bauen
PW_PATH=/pfad/zu/playwright python3 build.py 4 8  # nur Pin 4 und 8
```

**Posten:** Ein Tipp-Pin pro Tag (Tag 1–30), zusätzlich zu 2 Pins mit Link. Der gemeinsame Plan für alle Pins steht in
`../pin-plan.csv`.

**Lizenz der Fotos:** Pexels-Lizenz, kostenlos, auch kommerziell, ohne Namensnennung. Nur die fertigen Pins liegen im
Repository, nicht die Originalfotos.
