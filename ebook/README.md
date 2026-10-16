# E-Book: The 30-Day Weight Loss Plan

Kostenloses LEAN MODE PRO E-Book (Englisch, US-Schreibweise, metrische Angaben mit US-Einheiten), A4-PDF mit
53 Seiten, rund 0,7 MB. Fertige Datei:
[`dist/lean-mode-pro-30-day-weight-loss-plan.pdf`](dist/lean-mode-pro-30-day-weight-loss-plan.pdf)

Bis 14.10.2026 war das E-Book türkisch („30 Günlük Kilo Verme Planı“); die türkische Fassung liegt in der
Git-Historie.

## Aufbau

| Seiten | Inhalt |
| ------ | ------ |
| 1–4 | Cover, Inhaltsverzeichnis, Anleitung und Hinweis, Einleitung |
| 5–13 | Grundlagen, Tellermodell und Handportionen, Einkaufsliste, Aufwärmen und Mobilität, Übungen, Fortschritts- und Gewohnheitstabelle |
| 14–52 | 4 Phasen (je eine Einstiegsseite), 30 Tagesseiten, 3 Wochen-Checks, Tag 30 mit Rückblick, Plan für die Zeit danach |
| 53 | Abschluss |

Jeder Tag hat genau eine Seite mit derselben Struktur: Today's focus, Nutrition, Movement, Workout,
Tip of the day, Task of the day, My notes, End-of-day check-in.

Das Cover ist ein ganzseitiges Bild: `assets/cover.jpg` (1120 × 1584 px, rund 135 dpi). Es ist eine eigene
Illustration (keine Fotos, keine fremden Bildrechte) passend zum Inhalt: 30-Tage-Kalender, Teller-Methode,
Turnschuh und Hantel für Ernährung, Bewegung, Workouts und Gewohnheiten. Quelle ist `cover/cover.html`;
`node cover/render.mjs <ordner>` erzeugt daraus das A4-Bild fürs PDF (1120 × 1584) und die 2:3-Version für die
Website (720 × 1080, daraus `wordpress/brand/ebook-cover-en-*.webp`). Chromium übernimmt das JPEG unverändert
ins PDF.

## Texte ändern und neu erzeugen

- Texte: `content/basics.py` (Einleitung, Grundlagen, Übungen …) und `content/plan.py` (Phasen, Workouts, 30 Tage)
- Layout: `build.py` und `style.css`

```bash
python3 ebook/build.py      # erzeugt dist/ebook.html
node ebook/render.mjs       # erzeugt das PDF, prüft jede Seite auf Überlauf und verkleinert es
```

`render.mjs` braucht Playwright mit Chromium und für den letzten Schritt Python mit `pikepdf`
(`pip install pikepdf`). Seitenverweise („p. 12“) werden automatisch berechnet.

Für ein flüssiges PDF gilt:
- Die Schriften liegen in `fonts/` als statische Schnitte, eine Datei pro Schnitt mit Latin und Latin Extended.
- Chromium läuft ohne Font-Hinting.
- Im CSS keine Muster-Verläufe, Schatten oder transparenten Verläufe. Chromium macht daraus Bilder, und das PDF würde wieder langsam.

Zum Schluss verkleinert `optimize_pdf.py` die Datei auf etwa die Hälfte, ohne Aussehen oder Text zu ändern:
Chromium setzt jeden Buchstaben einzeln und zeichnet jede abgerundete Ecke mit bis zu 8 Kurvenstücken.
Das Skript fasst Buchstaben einer Zeile zu einem Befehl zusammen (größere Abstände, starke Unterschneidung
und geschützte Leerzeichen bleiben einzeln, damit Kopieren und Suchen in Chrome und Firefox gleich bleiben),
zeichnet Ecken mit einer Kurve, kürzt Koordinaten und speichert das PDF linearisiert (Fast Web View).
Geprüft mit Pixelvergleich aller Seiten und Textvergleich in PDFium (Chrome) und pdf.js (Firefox).
