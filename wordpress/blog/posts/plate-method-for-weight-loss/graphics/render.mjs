import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PW_PATH);
const dir = new URL('.', import.meta.url).pathname; // fonts/ = @fontsource/instrument-sans 5.3.0 (latin 400-700 woff2)
const jobs = [['featured', 1200, 1500], ['diagram', 1600, 1000], ['pin1', 1000, 1500], ['pin2', 1000, 1500]];
const browser = await chromium.launch();
for (const [v, w, h] of jobs) {
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  await page.goto(`file://${dir}/graphics.html?v=${v}`);
  await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(200);
  const over = await page.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.scrollHeight, [...document.fonts].filter(f => f.status === 'loaded').length]);
  console.log(v, over);
  await page.screenshot({ path: `${dir}/${v}.png` });
  await page.close();
}
await browser.close();
