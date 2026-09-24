// Renders ebook/dist/ebook.html to PDF with Chromium (Playwright) and checks every page for overflow.
//   node ebook/render.mjs [--png]
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const pwPath = process.env.PLAYWRIGHT_PATH ?? path.join(execSync('npm root -g').toString().trim(), 'playwright');
const { chromium } = require(pwPath);

const here = path.dirname(fileURLToPath(import.meta.url));
const dist = path.join(here, 'dist');
const out = path.join(dist, 'lean-mode-pro-30-gunluk-kilo-verme-plani.pdf');

// Without hinting, glyph positions are not snapped to whole pixels: even letter spacing in the
// PDF, and word spaces that PDF viewers recognise (search and copy work).
const browser = await chromium.launch({ args: ['--font-render-hinting=none'] });
const page = await browser.newPage({ viewport: { width: 794, height: 1123 } });
await page.goto(`file://${path.join(dist, 'ebook.html')}`, { waitUntil: 'load' });
await page.emulateMedia({ media: 'print' });
await page.evaluate(() => document.fonts.ready);

const problems = await page.evaluate(() =>
  [...document.querySelectorAll('.page')].flatMap((el, i) => {
    const over = el.scrollHeight - el.clientHeight;
    // content must also stay clear of the footer (bottom 20mm padding area)
    const limit = el.getBoundingClientRect().bottom - (20 / 25.4) * 96 + 2;
    const kids = [...el.children].filter((c) => !c.classList.contains('foot'));
    const lowest = Math.max(...kids.map((c) => c.getBoundingClientRect().bottom));
    const issues = [];
    if (over > 1) issues.push(`page ${i + 1}: overflows by ${over}px`);
    if (el.querySelector('.foot') && lowest > limit) issues.push(`page ${i + 1}: content reaches footer by ${Math.round(lowest - limit)}px`);
    return issues;
  }),
);
const count = await page.locator('.page').count();

if (process.argv.includes('--png')) {
  const pages = page.locator('.page');
  for (let i = 0; i < count; i++) {
    await pages.nth(i).screenshot({ path: path.join(dist, 'preview', `p${String(i + 1).padStart(2, '0')}.png`) });
  }
}

await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
await browser.close();

console.log(`${count} pages -> ${path.relative(process.cwd(), out)}`);
if (problems.length) {
  console.log('LAYOUT PROBLEMS:\n' + problems.join('\n'));
  process.exitCode = 1;
} else {
  console.log('No overflowing pages.');
}
