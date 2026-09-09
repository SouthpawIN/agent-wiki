// Timed screen tour of Senter Wiki — each section paced to its voiceover length (from /tmp/timeline.json).
const fs = require('fs'); const path = require('path');
const { chromium } = require(process.env.PW || 'playwright');
const TL = JSON.parse(fs.readFileSync('/tmp/timeline.json', 'utf8'));
const FILE = 'file:///Users/sovthpaw/Documents/Projects/Projects/vault-live.html';
const OUT = '/Users/sovthpaw/Documents/Projects/Projects/assets/tour-raw2';
const W = 1440, H = 900;
const sleep = ms => new Promise(r => setTimeout(r, ms));
const t0 = () => Date.now();

(async () => {
  fs.rmSync(OUT, { recursive: true, force: true });
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: W, height: H }, recordVideo: { dir: OUT, size: { width: W, height: H } } });
  const page = await ctx.newPage();
  const start = t0();
  const at = s => Math.max(0, TL.starts[s] * 1000 - (t0() - start));   // ms until section s should begin
  const until = s => TL.starts[s] * 1000 + TL.durs[s] * 1000;            // absolute ms when section s VO ends
  const waitUntil = absMs => sleep(Math.max(0, absMs - (t0() - start)));
  const glide = (x, y, steps = 16) => page.mouse.move(x, y, { steps });
  const tab = async (view) => { await glide(500, 6, 8); await sleep(250); const t = await page.$(`.navtab[data-view="${view}"]`); const b = await t.boundingBox(); await glide(b.x + b.width / 2, b.y + b.height / 2, 10); await sleep(150); await t.click(); };
  const heads = async () => page.$$('#view-wiki .topic .thead');

  await page.goto(FILE); await page.waitForTimeout(800);
  await page.evaluate(() => { localStorage.setItem('sw.radio.source', 'lofi'); });
  await glide(700, 500, 4);

  // 0 INTRO — sit on the wiki, gentle drift
  await sleep(at(0)); await glide(760, 520, 30); await waitUntil(until(0) - 1500);

  // 1 TALK — hover down 4 topics (turbofit, hermes-agent, ... pocket-shop) slowly; fire twinkles for each "idea"
  await sleep(at(1));
  const hs = await heads();
  const idx = [0, 1, 4, 2];
  for (let k = 0; k < idx.length; k++) {
    const b = await hs[idx[k]].boundingBox(); if (!b) continue;
    await glide(b.x + 120, b.y + b.height / 2, 18);
    await page.evaluate(i => { try { const n = document.querySelectorAll('#view-wiki .topic .tname')[i].textContent.trim(); mmPulse(n, ['#9ece6a', '#f7768e', '#bb9af7', '#e0af68'][i % 4]); } catch (e) {} }, idx[k]);
    await sleep(2600);
  }
  // land on turbofit, let orbs open
  { const b = await hs[0].boundingBox(); await glide(b.x + 120, b.y + b.height / 2, 14); }
  await waitUntil(until(1) - 800);

  // 2 ORBS — hover each orb (rise + caption), then click skills orb → editor at SKILLS, Esc
  await sleep(at(2));
  for (const k of ['ctx', 'skills', 'agents', 'loops']) {
    const o = await page.$(`#view-wiki .topic .orb[data-k="${k}"]`); const b = await o.boundingBox();
    await glide(b.x + b.width / 2, b.y + b.height / 2, 10); await sleep(1500);
  }
  { const o = await page.$('#view-wiki .topic .orb[data-k="skills"]'); await o.click(); }
  await sleep(2500); await page.keyboard.press('Escape'); await waitUntil(until(2) - 300);

  // 3 EDITOR — open turbofit, scroll body, hover integration icon → card, back with \
  await sleep(at(3));
  { const h = (await heads())[0]; await h.click(); }
  await sleep(1800);
  await page.mouse.wheel(0, 380); await sleep(1500); await page.mouse.wheel(0, 500); await sleep(1500); await page.mouse.wheel(0, -880); await sleep(900);
  { const ic = await page.$('#edIcons .iwrap .idot'); if (ic) { const b = await ic.boundingBox(); await glide(b.x + b.width / 2, b.y + b.height / 2, 14); await sleep(1600); const l = await page.$('#edIcons .ilink'); if (l) { const lb = await l.boundingBox(); await glide(lb.x + 30, lb.y + lb.height / 2, 8); await sleep(1300); } await glide(b.x + 260, b.y + b.height / 2, 10); await sleep(500); } }
  { const back = await page.$('#edBack'); const b = await back.boundingBox(); if (b) { await glide(b.x + 6, b.y + b.height / 2, 12); await sleep(600); await back.click(); } else await page.keyboard.press('Escape'); }
  await waitUntil(until(3) - 200);

  // 4 MAP — twinkles, open a topic (camera glides), Esc, then SPACE
  await sleep(at(4));
  await page.evaluate(() => { ['turbofit', 'senter', 'hermes-agent', 'anser', 'pocket-shop', 'omarchy-usb'].forEach((t, i) => setTimeout(() => { try { mmPulse(t, ['#9ece6a', '#e0af68', '#f7768e', '#7dcfff', '#bb9af7', '#73daca'][i]); } catch (e) {} }, i * 350)); });
  await sleep(2600);
  { const h = (await heads())[2]; await h.click(); } await sleep(2600); await page.keyboard.press('Escape'); await sleep(1200);
  await tab('senter'); await sleep(600);
  await page.evaluate(() => { ['turbofit', 'senter', 'hermes-agent', 'anser'].forEach((t, i) => setTimeout(() => { try { mmPulse(t, ['#9ece6a', '#e0af68', '#f7768e', '#7dcfff'][i]); } catch (e) {} }, i * 500)); });
  await waitUntil(until(4) + 400);

  // 5 FEED — tab, hover posts, plus follows the tab
  await sleep(at(5)); await tab('feed'); await sleep(900);
  const posts = await page.$$('#feed .post');
  for (let i = 0; i < Math.min(5, posts.length); i++) { const b = await posts[i].boundingBox(); if (b) { await glide(b.x + 200, b.y + 24, 12); await sleep(2100); } }
  await glide(500, 6, 8); await sleep(1400);  // show nav with + beside FEED
  { const plus = await page.$('#navPlus'); if (plus) { const b = await plus.boundingBox(); if (b) { await glide(b.x + b.width / 2, b.y + b.height / 2, 10); await sleep(1500); } } }
  await waitUntil(until(5) + 300);

  // 6 SKILLS + BOTS
  await sleep(at(6)); await tab('skills'); await sleep(900);
  await page.mouse.wheel(0, 420); await sleep(1400);
  { const sk = await page.$$('#skills-list .topic .thead'); if (sk.length > 4) { const b = await sk[4].boundingBox(); if (b) { await glide(b.x + 120, b.y + b.height / 2, 12); await sleep(1600); } } }
  await tab('bots'); await sleep(900);
  { const bt = await page.$$('#bots-list .topic .thead'); for (let i = 0; i < Math.min(4, bt.length); i++) { const b = await bt[i].boundingBox(); if (b) { await glide(b.x + 120, b.y + b.height / 2, 10); await sleep(900); } } if (bt.length) { await bt[0].click(); await sleep(2400); await page.keyboard.press('Escape'); } }
  await waitUntil(until(6) + 300);

  // 7 STREAM — back to wiki, hover the stream, scroll it
  await sleep(at(7)); await tab('wiki'); await sleep(700);
  { const mini = await page.$('#mini'); const b = await mini.boundingBox(); await glide(b.x + b.width / 2, b.y + b.height / 2, 16); await sleep(1400); await page.mouse.wheel(0, -700); await sleep(1500); await page.mouse.wheel(0, 700); await sleep(1000); }
  await glide(400, 500, 14); await waitUntil(until(7) + 300);

  // 8 RADIO + BROWSER — nav widget, volume slider, player page with a queued lofi stream, then browser tab
  await sleep(at(8)); await glide(500, 6, 8); await sleep(500);
  { const ctl = await page.$('#mCtl'); const b = await ctl.boundingBox(); await glide(b.x + b.width / 2, b.y + b.height / 2, 12); await sleep(1200);
    const tr = await page.$('#mVolTrack'); const tb = await tr.boundingBox(); await glide(tb.x + tb.width / 2, tb.y + tb.height * .7, 10); await sleep(400);
    await page.mouse.down(); await glide(tb.x + tb.width / 2, tb.y + tb.height * .25, 8); await page.mouse.up(); await sleep(900);
    const now = await page.$('#mNow'); const nb = await now.boundingBox(); await glide(nb.x + nb.width / 2, nb.y + nb.height / 2, 8); await sleep(300); await now.click(); }
  await sleep(900);
  await page.evaluate(() => radio.set({ title: 'Rain on the Vault', artist: 'Evolutionary Lo-fi', album: 'gen #0412', url: '' }));
  await sleep(2600);
  await page.evaluate(() => radio.enqueue('file:///Users/sovthpaw/Documents/Projects/Projects/assets/lofi-sample.wav')); await sleep(1200); await page.evaluate(() => { const t=radio.state.track; t.title='Rain on the Vault'; t.artist='Evolutionary Lo-fi'; t.album='gen #0412'; radio.set(t); }); await sleep(3000);
  await tab('browser'); await sleep(900);
  { const bm = await page.$$('#brMarks .topic .thead'); for (let i = 0; i < Math.min(4, bm.length); i++) { const b = await bm[i].boundingBox(); if (b) { await glide(b.x + 120, b.y + b.height / 2, 10); await sleep(1100); } } }
  await waitUntil(until(8) + 400);

  // 9 OUTRO — home, drift on wiki
  await sleep(at(9)); await tab('wiki'); await sleep(600);
  await page.evaluate(() => { ['turbofit', 'senter', 'hermes-agent', 'anser', 'pocket-shop'].forEach((t, i) => setTimeout(() => { try { mmPulse(t, ['#9ece6a', '#e0af68', '#f7768e', '#7dcfff', '#bb9af7'][i]); } catch (e) {} }, i * 700)); });
  await glide(760, 520, 30);
  await waitUntil(TL.total * 1000);

  await ctx.close(); await browser.close();
  const f = fs.readdirSync(OUT).find(x => x.endsWith('.webm')); console.log('VIDEO', path.join(OUT, f));
})().catch(e => { console.error(e); process.exit(1); });
