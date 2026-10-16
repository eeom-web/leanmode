# Blogartikel

Jeder Artikel hat einen eigenen Ordner unter `posts/<slug>/`. Neue Artikel schreibt man als `post.md`
(Kopfbereich mit Titel, Beschreibung, Kategorie, Bild- und Pin-Texten, darunter der Text in einfachem Markdown) und
erzeugt den Rest mit:

```
PW_PATH=/pfad/zu/playwright python3 build.py            # alle Artikel
PW_PATH=/pfad/zu/playwright python3 build.py <slug>     # nur einer
python3 build.py --no-images                            # nur Text, keine Bilder
```

| Datei | Inhalt |
|---|---|
| `post.md` | Quelle: Kopfbereich (`title`, `excerpt`, `category`, `tags`, `icon`, `img_title`, `img_sub`, `kicker`, `points`, `headline`, `pin1_*`, `pin2_*`) und Artikeltext |
| `post.html` | Artikeltext im Block-Format von WordPress (Gutenberg), erzeugt |
| `post.json` | Titel, Adresse (Slug), Textauszug (= Beschreibung für Google und Pinterest), Kategorie, Schlagwörter, Bilder und die Texte für die Pins, erzeugt |
| `featured.webp` | Beitragsbild (1200 × 1500 px), erzeugt |
| `pin-1.jpg`, `pin-2.jpg` | Pins für Pinterest (1000 × 1500 px), erzeugt; werden nicht auf die Website hochgeladen |
| `posts/manifest.json` | SHA-256 der Dateien, die beim Einspielen hochgeladen werden |

`graphics/` enthält die Vorlage für Beitragsbilder und Pins (`card.html`, Illustrationen in `icons.js`, Schrift
Instrument Sans unter OFL in `fonts/`). Der Artikel `plate-method-for-weight-loss` ist von Hand gebaut (ohne
`post.md`, eigene Grafiken in seinem Ordner).

Design, Affiliate-Hinweis, Anmeldebox und Gesundheitshinweis kommen automatisch aus `mu-plugins/lmp-blog/template.php`;
im Artikeltext steht nur der Inhalt. Ans Ende jedes Artikels hängt `build.py` einen Hinweis auf den kostenlosen Plan an.

## Fotos in den Artikeln

Jeder Artikel zeigt oben ein echtes Foto (Pexels, keine Personen) im Querformat 3:2, dasselbe Foto steht auf seiner
Karte in der Blog-Übersicht. `hero-photos.json` legt pro Artikel fest: Pexels-Foto-ID, Alt-Text und Bildausschnitt
(`pos`). Beim Einspielen lädt der Server das Foto, legt es in der Mediathek an und speichert die ID im Beitrag
(`_lmp_hero`, Ausschnitt in `_lmp_hero_pos`). Das gezeichnete Beitragsbild (`featured.webp`) bleibt das Bild für
Pinterest und Vorschauen beim Teilen. Ohne Foto zeigt die Vorlage wie bisher das Beitragsbild.

## Pinterest

| Ordner / Datei | Inhalt |
|---|---|
| `posts/<slug>/pin-*.jpg` | 42 Grafik-Pins mit Link (2 pro Artikel) |
| `photo-pins/` | 30 Pins mit echten Fotos und Link |
| `tip-pins/` | 30 Tipp-Pins ohne Link, der Tipp steht ganz auf dem Bild |
| `pin-plan.csv` | Gemeinsamer Plan: pro Tag 2 Pins mit Link und 1 Tipp-Pin ohne Link (Tag 1–36) |
