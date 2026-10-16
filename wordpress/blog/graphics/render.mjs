// Renders the blog graphics: node render.mjs <jobs.json>
// jobs.json = [{ "out": "/abs/file.png", "w": 1200, "h": 1500, "job": { ...see card.html } }]
// Needs Playwright (PW_PATH = path of the playwright package, e.g. /opt/node22/lib/node_modules/playwright).
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PW_PATH || 'playwright');
const card = new URL('card.html', import.meta.url).href;
const jobs = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1500 } });
let problems = 0;
for (const { out, w, h, job } of jobs) {
  await page.setViewportSize({ width: w, height: h });
  await page.goto(`${card}#${encodeURIComponent(JSON.stringify(job))}`);
  await page.reload();
  await page.evaluate(() => document.fonts.ready);
  const over = await page.evaluate(() => { const c = document.querySelector('.c'); return c.scrollHeight - c.clientHeight; });
  if (over > 2) { problems++; console.log('OVERFLOW', over, out); }
  await page.screenshot({ path: out });
}
await browser.close();
console.log(`rendered ${jobs.length} images, ${problems} with overflow`);
