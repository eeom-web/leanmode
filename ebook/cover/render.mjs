// Renders the e-book cover: node render.mjs <out-dir>
// writes cover-720x1080.png (website mockup) and cover-1120x1584.png (PDF cover page).
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PW_PATH || 'playwright');
const out = process.argv[2] || '.';
const page = new URL('cover.html', import.meta.url).href;
const browser = await chromium.launch();
for (const [w, h] of [[720, 1080], [1120, 1584]]) {
  const p = await browser.newPage({ viewport: { width: w, height: h } });
  await p.goto(`${page}?w=${w}&h=${h}`);
  await p.evaluate(() => document.fonts.ready);
  const over = await p.evaluate(() => { const c = document.getElementById('cover'); return [c.scrollHeight - c.clientHeight, c.scrollWidth - c.clientWidth]; });
  console.log(`${w}x${h}`, over[0] > 1 || over[1] > 1 ? `OVERFLOW ${over}` : 'ok');
  await p.screenshot({ path: `${out}/cover-${w}x${h}.png` });
  await p.close();
}
await browser.close();
