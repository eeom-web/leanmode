# E-Book: 30 Günlük Kilo Verme Planı

Kostenloses LEAN MODE PRO E-Book (Türkisch), A4-PDF mit 53 Seiten, rund 0,5 MB.
Fertige Datei: [`dist/lean-mode-pro-30-gunluk-kilo-verme-plani.pdf`](dist/lean-mode-pro-30-gunluk-kilo-verme-plani.pdf)

## Aufbau

| Seiten | Inhalt |
| ------ | ------ |
| 1–4 | Cover, Inhaltsverzeichnis, Anleitung und Hinweis, Einleitung |
| 5–13 | Grundlagen, Tellermodell und Handportionen, Einkaufsliste, Aufwärmen und Mobilität, Übungen, Fortschritts- und Gewohnheitstabelle |
| 14–52 | 4 Phasen (je eine Einstiegsseite), 30 Tagesseiten, 3 Wochen-Checks, Tag 30 mit Rückblick, Plan für die Zeit danach |
| 53 | Abschluss |

Jeder Tag hat genau eine Seite mit derselben Struktur: Bugünün odağı, Beslenme,
Hareket, Antrenman, Bugünün ipucu, Günün görevi, Notlarım, Gün sonu kontrolü.

## Texte ändern und neu erzeugen

- Texte: `content/basics.py` (Einleitung, Grundlagen, Übungen …) und `content/plan.py` (Phasen, Workouts, 30 Tage)
- Layout: `build.py` und `style.css`

```bash
python3 ebook/build.py      # erzeugt dist/ebook.html
node ebook/render.mjs       # erzeugt das PDF, prüft jede Seite auf Überlauf und verkleinert es
```

`render.mjs` braucht Playwright mit Chromium und für den letzten Schritt Python mit `pikepdf`
(`pip install pikepdf`). Seitenverweise („s. 12“) und die
türkischen Endungen danach („s. 10'da“) werden automatisch berechnet.

Für ein flüssiges PDF gilt:
- Die Schriften liegen in `fonts/` als statische Schnitte, eine Datei pro Schnitt mit allen türkischen Zeichen.
- Chromium läuft ohne Font-Hinting.
- Im CSS keine Muster-Verläufe, Schatten oder transparenten Verläufe. Chromium macht daraus Bilder, und das PDF würde wieder langsam.

Zum Schluss verkleinert `optimize_pdf.py` die Datei auf etwa die Hälfte, ohne Aussehen oder Text zu ändern:
Chromium setzt jeden Buchstaben einzeln und zeichnet jede abgerundete Ecke mit bis zu 8 Kurvenstücken.
Das Skript fasst Buchstaben einer Zeile zu einem Befehl zusammen (größere Abstände, starke Unterschneidung
und geschützte Leerzeichen bleiben einzeln, damit Kopieren und Suchen in Chrome und Firefox gleich bleiben),
zeichnet Ecken mit einer Kurve, kürzt Koordinaten und speichert das PDF linearisiert (Fast Web View).
Geprüft mit Pixelvergleich aller Seiten und Textvergleich in PDFium (Chrome) und pdf.js (Firefox).
