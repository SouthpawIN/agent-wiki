// Records a screen tour of the Senter Wiki UI using Playwright's built-in video capture.
// Output: assets/senter-wiki-tour.webm (converted to mp4 by the caller).
const path = require('path');
const fs = require('fs');
const { chromium } = require(process.env.PW || 'playwright');

const FILE = 'file:///Users/sovthpaw/Documents/Projects/Projects/vault-live.html';
const OUT = '/Users/sovthpaw/Documents/Projects/Projects/assets/tour-raw';
const W = 1440, H = 900;

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

async function glide(page, x, y, steps = 18) {
  await page.mouse.move(x, y, { steps });
}

(async () => {
  fs.rmSync(OUT, { recursive: true, force: true });
  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    viewport: { width: W, height: H },
    recordVideo: { dir: OUT, size: { width: W, height: H } },
  });
  const page = await ctx.newPage();
  await page.goto(FILE);
  await page.waitForTimeout(1600);

  // --- 1. Wiki: hover down the list, hero rotates ---
  const heads = await page.$$('#view-wiki .topic .thead');
  for (let i = 0; i < Math.min(5, heads.length); i++) {
    const b = await heads[i].boundingBox();
    if (!b) continue;
    await glide(page, b.x + 120, b.y + b.height / 2, 14);
    await sleep(650);
  }
  await sleep(400);

  // --- 2. Twinkle: fire a few bot pulses so the stars twinkle on camera ---
  await page.evaluate(() => {
    const seq = [['turbosovth', 'turbofit'], ['teknium', 'hermes-agent'], ['senter', 'senter'], ['klerik', 'anser']];
    seq.forEach(([b, t], i) => setTimeout(() => { try { botActivity(b); } catch (e) {} }, i * 350));
  });
  await sleep(1800);

  // --- 2b. Orbs: hover TurboFit, dwell so the metric values + slow orbit show, then click the SKILLS orb ---
  {
    const b0 = await heads[0].boundingBox();
    await glide(page, b0.x + 120, b0.y + b0.height / 2, 12); await sleep(1400);
    const orb = await page.$('#view-wiki .topic .orb[data-k="skills"]');
    if (orb) { const ob = await orb.boundingBox(); await glide(page, ob.x + ob.width / 2, ob.y + ob.height / 2, 10); await sleep(700); }
    // integration card straight from the list row
    const li = await page.$('#view-wiki .topic .idots .iwrap .idot');
    if (li) { const lb = await li.boundingBox(); await glide(page, lb.x + lb.width / 2, lb.y + lb.height / 2, 10); await sleep(1100); await glide(page, lb.x + lb.width / 2 + 160, lb.y + lb.height / 2, 8); await sleep(400); }
    if (orb) { await orb.click(); await sleep(2200); await page.keyboard.press('Escape'); await sleep(1200); }
  }
  // --- 3. Open TurboFit editor: camera zooms to its star, pet enters ---
  await heads[0].click();
  await sleep(1800);
  // integration icon hover -> card
  const icon = await page.$('#edIcons .iwrap .idot');
  if (icon) {
    const b = await icon.boundingBox();
    await glide(page, b.x + b.width / 2, b.y + b.height / 2, 16);
    await sleep(900);
    const link = await page.$('#edIcons .ilink');
    if (link) { const lb = await link.boundingBox(); await glide(page, lb.x + 30, lb.y + lb.height / 2, 10); await sleep(1100); }
    await glide(page, b.x + b.width / 2 + 220, b.y + b.height / 2, 12); // sweep off horizontally -> card gone
    await sleep(500);
  }
  // scroll the editor body
  await page.mouse.wheel(0, 500); await sleep(700);
  await page.mouse.wheel(0, 700); await sleep(700);
  await page.mouse.wheel(0, -1200); await sleep(600);
  // back with the backslash
  const back = await page.$('#edBack');
  if (back) { const b = await back.boundingBox(); if (b) { await glide(page, b.x + 6, b.y + b.height / 2, 14); await sleep(500); await back.click(); } else { await page.keyboard.press('Escape'); } }
  await sleep(1500);

  // --- 4. Second topic: navigate star to star ---
  await heads[2].click(); await sleep(1600);
  await page.keyboard.press('Escape'); await sleep(1300);

  // --- 5. Fleet stream: hover -> fills the side, scroll it, leave ---
  const mini = await page.$('#mini');
  if (mini) {
    const b = await mini.boundingBox();
    await glide(page, b.x + b.width / 2, b.y + b.height / 2, 16);
    await sleep(1200);
    await page.mouse.wheel(0, -900); await sleep(900);
    await page.mouse.wheel(0, 900); await sleep(700);
    await glide(page, 300, 500, 16); await sleep(900);
  }

  // --- 6. Top nav: summon at the top edge, walk the tabs ---
  await glide(page, 500, 6, 10); await sleep(700);
  async function tab(view, dwell) {
    await glide(page, 500, 6, 6); await sleep(250);
    const t = await page.$(`.navtab[data-view="${view}"]`);
    const b = await t.boundingBox();
    await glide(page, b.x + b.width / 2, b.y + b.height / 2, 10);
    await sleep(200); await t.click(); await sleep(dwell);
  }
  await tab('feed', 1800);
  await page.mouse.wheel(0, 400); await sleep(600);

  await tab('skills', 1400);
  await page.mouse.wheel(0, 500); await sleep(600);
  const sk = await page.$$('#skills-list .topic .thead');
  if (sk.length) { const b = await sk[3].boundingBox(); if (b) { await glide(page, b.x + 100, b.y + b.height / 2, 12); await sleep(700); await sk[3].click(); await sleep(1500); await page.keyboard.press('Escape'); await sleep(900); } }

  await tab('bots', 1400);
  const bt = await page.$$('#bots-list .topic .thead');
  for (let i = 0; i < Math.min(3, bt.length); i++) { const b = await bt[i].boundingBox(); if (b) { await glide(page, b.x + 100, b.y + b.height / 2, 10); await sleep(450); } }
  if (bt.length) { await bt[0].click(); await sleep(1500); await page.keyboard.press('Escape'); await sleep(900); }

  // --- 7. SENTER SPACE: the constellation ---
  await tab('senter', 800);
  await page.evaluate(() => { ['turbofit', 'senter', 'hermes-agent', 'anser', 'pocket-shop'].forEach((t, i) => setTimeout(() => { try { mmPulse(t, ['#9ece6a', '#e0af68', '#f7768e', '#7dcfff', '#bb9af7'][i]); } catch (e) {} }, i * 400)); });
  await sleep(3200);

  // --- 8. Home ---
  await tab('wiki', 1500);
  await glide(page, 700, 450, 20); await sleep(1200);

  await ctx.close();
  await browser.close();
  const files = fs.readdirSync(OUT).filter(f => f.endsWith('.webm'));
  console.log('VIDEO', path.join(OUT, files[0]));
})().catch(e => { console.error(e); process.exit(1); });
