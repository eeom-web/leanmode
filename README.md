# Lean Mode Pro: Landingpage

Landingpage für **leanmodepro.com**. Die WordPress/Elementor-Version liegt in
[`wordpress/elementor/`](wordpress/elementor/README.md). Sie stellt das kostenlose E-Book
**„30 Günlük Kilo Verme Planı"** vor und sammelt E-Mail-Adressen. Die Seite ist komplett auf Türkisch.

> Das E-Book selbst ist **nicht** Teil dieses Projekts. Die Seite zeigt nur das Konzept
> (Cover-Mockup, Aufbau eines Tages, 30-Tage-Ablauf), aber keine echten Inhalte.

## Stack

- [Astro 7](https://astro.build): statisches Build, **kein Framework-JavaScript im Browser**
- Reines CSS mit Design-Tokens (`src/styles/global.css`), Styles je Komponente scoped
- Schrift *Instrument Sans* wird lokal ausgeliefert (Astro Fonts API mit Preload und
  metrik-angepasstem Fallback). Keine Anfragen an Google Fonts, gut für die DSGVO.
- Laufzeitabhängigkeiten: nur `astro` und das Font-Paket

## Befehle

| Befehl            | Zweck                                         |
| ----------------- | --------------------------------------------- |
| `npm install`     | Abhängigkeiten installieren (Node ≥ 22.12)    |
| `npm run dev`     | Entwicklungsserver auf `http://localhost:4321` |
| `npm run build`   | Produktions-Build nach `dist/`                |
| `npm run preview` | Build lokal ansehen                           |

## Struktur

```
src/
├── config/
│   ├── site.ts            Marke, SEO, Footer-Links
│   └── signup.ts          Formular-Konfiguration und alle Formulartexte
├── components/
│   ├── sections/          Eine Datei pro Sektion (Hero, Signup, Contents, …)
│   ├── SignupForm.astro   E-Mail-Formular inkl. Validierung und Zuständen
│   ├── EbookMockup.astro  E-Book-Cover, nur in CSS (kein Bild)
│   ├── Header / Footer / Logo / Icon
├── layouts/               BaseLayout (SEO/OG), LegalLayout (Platzhalter)
├── lib/                   E-Mail-Validierung, Client-Versand
├── server/                Vorbereitetes Backend (siehe unten)
└── pages/                 index, Rechtsseiten (Platzhalter), 404, sitemap.xml
```

Die Reihenfolge der Sektionen steht in `src/pages/index.astro`.

## E-Mail-Formular

Das Formular schickt `POST { email, source }` als JSON an `PUBLIC_SIGNUP_ENDPOINT`.
`source` ist `hero` oder `final-cta`, je nachdem, welches Formular benutzt wurde.

**Aktueller Stand: Demo-Modus.** Solange `PUBLIC_SIGNUP_ENDPOINT` leer ist, prüft das
Formular die Eingabe und zeigt die Erfolgsmeldung an, **sendet aber nichts**. In der
Browser-Konsole erscheint dazu ein Hinweis.

Als E-Mail-Dienst ist **Brevo** vorgesehen. Die Anbindung folgt in einem eigenen Schritt.
`src/server/subscribe.ts` ist ein framework-unabhängiger Handler (Web-Standard
`Request` → `Response`) mit Validierung, Honeypot und CORS. Dort wird später der
Brevo-Provider statt `consoleProvider` eingesetzt.

## Offene Punkte vor dem Livegang

- [ ] Brevo anbinden (siehe oben)
- [ ] Rechtstexte einfügen: `src/pages/gizlilik-politikasi.astro`,
      `cerez-politikasi.astro`, `yasal-bilgiler.astro`. Sie stehen aktuell als Platzhalter
      auf `noindex` und sind nicht in der Sitemap.
- [ ] Nach dem Einfügen `noindex` entfernen und die Seiten in `src/pages/sitemap.xml.ts`
      aufnehmen
- [ ] E-Book erstellen (separater Schritt)

## Deployment

`npm run build` erzeugt eine rein statische Seite in `dist/`. Sie kann auf jedem
Static-Hosting liegen (z. B. Hostinger, Netlify, Vercel, Cloudflare Pages).
`public/og-image.jpg` ist das Vorschaubild für Social Media (1200 × 630).
