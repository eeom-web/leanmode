// Renders the photo pins: node render.mjs <jobs.json>
// jobs.json = [{ "out": "/abs/file.jpg", "job": { ...see pin.html } }]
// Needs Playwright (PW_PATH = path of the playwright package, e.g. /opt/node22/lib/node_modules/playwright).
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PW_PATH || 'playwright');
const pinUrl = new URL('pin.html', import.meta.url).href;
const jobs = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1000, height: 1500 } });
let problems = 0;
for (const { out, job } of jobs) {
  await page.goto(`${pinUrl}#${encodeURIComponent(JSON.stringify(job))}`);
  await page.reload();
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => document.getElementById('img').decode());
  const size = await page.evaluate(() => window.fit());
  // The photo must keep a usable height in layouts A and B.
  const ph = await page.evaluate(() => document.querySelector('.ph').getBoundingClientRect().height);
  if (ph < 560) { problems++; console.log('SMALL PHOTO', Math.round(ph), out); }
  if (size <= 58) { problems++; console.log('LONG HEADLINE', out); }
  await page.screenshot({ path: out, type: 'jpeg', quality: 88 });
}
await browser.close();
console.log(`rendered ${jobs.length} pins, ${problems} with problems`);
