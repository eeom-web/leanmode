// @ts-check
import { defineConfig, fontProviders } from 'astro/config';

/** @param {'latin' | 'latin-ext'} subset */
const fontFile = (subset) =>
  `@fontsource-variable/instrument-sans/files/instrument-sans-${subset}-wght-normal.woff2`;

// https://docs.astro.build/en/reference/configuration-reference/
export default defineConfig({
  site: 'https://leanmodepro.com',
  compressHTML: true,
  build: {
    // Single landing page: inline the (small) CSS to avoid a render-blocking request.
    inlineStylesheets: 'always',
  },
  // Self-hosted font (no requests to third-party font servers).
  fonts: [
    {
      provider: fontProviders.local(),
      name: 'Instrument Sans',
      cssVariable: '--font-sans',
      fallbacks: ['ui-sans-serif', 'system-ui', 'sans-serif'],
      options: {
        variants: [
          {
            src: [fontFile('latin')],
            weight: '400 700',
            style: 'normal',
            display: 'swap',
            unicodeRange: [
              'U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD',
            ],
          },
          {
            // Turkish characters such as ğ, ş, İ live in the latin-ext subset.
            src: [fontFile('latin-ext')],
            weight: '400 700',
            style: 'normal',
            display: 'swap',
            unicodeRange: [
              'U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF',
            ],
          },
        ],
      },
    },
  ],
});
