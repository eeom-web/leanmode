# Pins ohne Link

105 Pins (1000 × 1500 px) in `pins/`, auf denen der ganze Inhalt steht. Sie werden **ohne Link** gepostet (Feld „Link“
leer lassen). Sie sollen gespeichert werden und Vertrauen aufbauen; die Pins mit Link bringen die Besucher auf die
Website. Fotos: echte Fotos von [Pexels](https://www.pexels.com/), keine KI-Bilder, keine Personen, keine Markenlogos.

| Art (`type`) | Anzahl | Layout | Inhalt |
|---|---|---|---|
| `tip` | 40 | T1, T2, T3 | Ein Tipp mit Foto (hell, grün, Foto über die ganze Fläche mit Textkarte) |
| `list` | 24 | L1, L2 | Kurze Liste mit Foto; Punkte als `Vorher\|Nachher` werden als Tausch mit Pfeil gezeigt |
| `quote` | 12 | Q1, Q2 | Motivations-Zitat auf einem Landschaftsfoto (Q1) oder ohne Foto in Grün, Gelb oder Creme (Q2) |
| `myth` | 8 | M | Mythos oder Fakt, ohne Foto (hell oder grün) |
| `swap` | 8 | S | „Statt … lieber …“ mit zwei Fotos und ungefähren Kalorien |
| `number` | 6 | N | Eine große Zahl mit Foto (z. B. 8,000 Schritte am Tag) |
| `challenge` | 7 | C | 7-Tage-Challenge zum Abhaken, ohne Foto |

| Datei | Inhalt |
|---|---|
| `pins.json` | Pro Pin: Nummer, Tag im Plan, Art, Layout, Pexels-Foto-ID(s), Bildausschnitt (`pos`), die Bildtexte je nach Art und die Texte für Pinterest (`board`, `title`, `desc`, `alt`) |
| `pin.html` | Vorlage für alle Layouts; die Felder je Layout stehen oben in der Datei |
| `render.mjs`, `build.py` | Bauen die Pins wie bei `../photo-pins/`; `render.mjs` meldet Pins, deren Text nicht passt |

```
python3 build.py --fetch                          # Fotos von Pexels nach photos/ laden (nicht in git)
PW_PATH=/pfad/zu/playwright python3 build.py      # alle Pins bauen
PW_PATH=/pfad/zu/playwright python3 build.py 4 8  # nur Pin 4 und 8
```

**Posten:** 5 Pins am Tag, davon 1 mit Link (an jedem zweiten Tag 2) und 3–4 ohne Link aus diesem Ordner. Der Plan für
30 Tage steht in `../pin-plan.csv`; der Tag jedes Pins auch im Feld `day`. Die Arten sind gleichmäßig über die Tage
verteilt, so dass an einem Tag nie zwei Zitate, Mythen, Tausch-Pins, Zahlen oder Challenges kommen.

**Pinnwand:** Die Zitat-Pins gehören auf die Pinnwand „Weight Loss Motivation“; alle anderen Pinnwände gibt es schon.

**Kalorien auf den Tausch-Pins:** gerundete Durchschnittswerte für die angegebene Menge (Packungsangaben schwanken).

**Lizenz der Fotos:** Pexels-Lizenz, kostenlos, auch kommerziell, ohne Namensnennung. Nur die fertigen Pins liegen im
Repository, nicht die Originalfotos.
