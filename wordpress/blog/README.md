# Blogartikel

Jeder Artikel hat einen eigenen Ordner unter `posts/<slug>/`:

| Datei | Inhalt |
|---|---|
| `post.html` | Artikeltext im Block-Format von WordPress (Gutenberg). `{{img:<name>}}` wird beim Import durch die Adresse des hochgeladenen Bildes ersetzt |
| `post.json` | Titel, Adresse (Slug), Textauszug (= Beschreibung für Google und Pinterest), Kategorie, Schlagwörter, Bilder und die Texte für die Pins |
| `featured.webp` | Beitragsbild (1200 × 1500 px) |
| `*.webp` | Bilder im Artikel |
| `pin-*.jpg` | Pins für Pinterest (1000 × 1500 px), werden nicht auf die Website hochgeladen |
| `graphics/` | Quelle der Grafiken (HTML + Playwright-Skript; Schrift Instrument Sans aus `@fontsource/instrument-sans` in `graphics/fonts/` legen) |

Design, Affiliate-Hinweis, Anmeldebox und Gesundheitshinweis kommen automatisch aus `mu-plugins/lmp-blog/template.php`;
im Artikeltext steht nur der Inhalt.
