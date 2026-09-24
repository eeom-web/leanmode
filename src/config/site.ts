export const site = {
  name: 'Lean Mode Pro',
  wordmark: { main: 'LEAN MODE', accent: 'PRO' },
  url: 'https://leanmodepro.com',
  locale: 'tr_TR',
  lang: 'tr',
  themeColor: '#f6f5f1',
  seo: {
    title: 'Lean Mode Pro | Ücretsiz 30 Günlük Kilo Verme Planı',
    description:
      'Beslenme, antrenman, günlük hareket ve pratik kilo verme stratejilerini içeren ücretsiz 30 günlük adım adım planı keşfet.',
    ogImage: {
      src: '/og-image.jpg',
      width: 1200,
      height: 630,
      alt: 'Lean Mode Pro — 30 Günlük Kilo Verme Planı e-kitap kapağı',
    },
  },
  /** Anchor of the main signup form — every CTA on the page points here. */
  signupAnchor: '#kayit',
  legalLinks: [
    { label: 'Gizlilik Politikası', href: '/gizlilik-politikasi/' },
    { label: 'Çerez Politikası', href: '/cerez-politikasi/' },
    { label: 'Yasal Bilgiler', href: '/yasal-bilgiler/' },
  ],
} as const;
