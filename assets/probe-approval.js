// Prove #18 (gold dissipation plays on real animatable props) + #18b (approved card stays white across re-render) + (B) zero console errors + live loader.
// Run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-approval.js
const { chromium } = require(process.env.PW || 'playwright');
const fs = require('fs'), path = require('path'), os = require('os');
const VAULT = path.join(os.homedir(), 'Documents/Projects/Projects');
const TOKEN = fs.readFileSync(path.join(os.homedir(), '.hermes/senter-bridge/token'), 'utf8').trim();
const BASE = 'http://127.0.0.1:8643';
const OUT = path.join(VAULT, 'assets/proof-18'); fs.mkdirSync(OUT, { recursive: true });

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  const errors = [], logs = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console.error: ' + m.text()); else logs.push(m.type() + ': ' + m.text()); });
  await page.goto('file://' + VAULT + '/vault-live.html?view=feed', { waitUntil: 'load' });
  await page.waitForTimeout(1500);

  // (B) live loader through GET /file
  const railRows = await page.evaluate(() => [...document.querySelectorAll('#intStream .msg')].map(e => e.querySelector('.who')?.textContent + '|' + e.querySelector('.meta')?.textContent));
  console.log('rail rows', railRows.length, 'first:', railRows.slice(0, 4).join(' ; '));
  const bridgeLive = await page.evaluate(() => window.bridgeLive && window.bridgeLive());
  console.log('bridge live', bridgeLive);

  // real approval through the bridge: POST to pending/ via a fake bot record and emit pending event (same shape __init__.py writes)
  const id = 'probe' + Date.now().toString(16);
  const rec = { id, session_key: 'probe', bot: 'teknium', ts: Date.now() / 1000, command: 'rm -rf /tmp/probe-18', description: 'probe: gold dissipation proof', pattern_key: 'rm' };
  fs.writeFileSync(path.join(os.homedir(), '.hermes/senter-bridge/pending', id + '.json'), JSON.stringify(rec));
  fs.appendFileSync(path.join(os.homedir(), '.hermes/senter-bridge/events.jsonl'), JSON.stringify({ kind: 'approval', phase: 'pending', ...rec }) + '\n');
  await page.waitForSelector('#feed .post.approval[data-aid="' + id + '"]', { timeout: 8000 });
  const cardSel = '#feed .post.approval[data-aid="' + id + '"]';
  const bb = await page.locator(cardSel).first().boundingBox();
  console.log('card at', JSON.stringify(bb));
  const clip = { x: Math.max(0, bb.x - 8), y: Math.max(0, bb.y - 8), width: Math.min(1280 - bb.x + 8, bb.width + 16), height: bb.height + 16 };
  const pre = await page.evaluate(s => { const el = document.querySelector(s); const cs = getComputedStyle(el); return { border: cs.borderTopColor, pos: cs.position, cls: el.className }; }, cardSel);
  console.log('pre-click', JSON.stringify(pre));

  // click ALLOW in the FEED (real click)
  await page.locator(cardSel + ' .allow-main').first().click();
  const t0 = Date.now();
  const frames = [];
  for (const at of [0, 200, 400, 600, 800]) {
    const wait = at - (Date.now() - t0); if (wait > 0) await page.waitForTimeout(wait);
    const st = await page.evaluate(s => { const el = document.querySelector(s); const cs = getComputedStyle(el, '::before'); return { t: performance.now() | 0, cls: el.className.replace('post approval', '').trim(), clip: cs.clipPath, dust: el.querySelectorAll('.gold-dust').length, receipt: !!el.querySelector('.receipt') }; }, cardSel);
    const f = path.join(OUT, 'frame-' + at + '.png'); await page.screenshot({ path: f, clip });
    frames.push({ at, ...st, png: f });
  }
  await page.waitForTimeout(400);
  frames.forEach(f => console.log('frame', f.at + 'ms', f.cls || '(none)', 'clip=' + f.clip, 'dust=' + f.dust, 'receipt=' + f.receipt));
  const distinctClips = new Set(frames.map(f => f.clip)).size;
  console.log('distinct clip-path values across frames:', distinctClips, distinctClips >= 3 ? '(WIPE ANIMATES)' : '(STATIC — BUG)');

  // final state + idempotency: SSE 'decided' echo arrives after the click → markDone twice
  await page.waitForTimeout(1200);
  const post = await page.evaluate(s => [...document.querySelectorAll('[data-aid="' + s + '"]')].map(el => ({ where: el.closest('#feed') ? 'feed' : el.closest('#stream') ? 'stream' : 'mini', cls: el.className, border: getComputedStyle(el).borderTopColor, receipts: el.querySelectorAll('.receipt').length, dust: el.querySelectorAll('.gold-dust').length })), id);
  console.log('post-settle', JSON.stringify(post));

  // #18b: hover / un-hover the stream ×3 (collapse/expand re-render path) — card must stay done/white
  const chat = page.locator('#chat');
  for (let i = 0; i < 3; i++) { await page.mouse.move(1200, 700); await page.waitForTimeout(250); await page.mouse.move(400, 300); await page.waitForTimeout(250); }
  // and a fresh page load: replay must NOT resurrect the card (pending file removed by /approve → replay filter drops it)
  const stillGold = await page.evaluate(s => [...document.querySelectorAll('[data-aid="' + s + '"]')].map(el => getComputedStyle(el).borderTopColor), id);
  console.log('after hover x3 borders', JSON.stringify(stillGold));
  await page.reload({ waitUntil: 'load' }); await page.waitForTimeout(2500);
  const afterReload = await page.evaluate(s => document.querySelectorAll('[data-aid="' + s + '"]').length, id);
  console.log('cards for approved id after reload (replay):', afterReload, afterReload === 0 ? '(OK — not resurrected)' : '(BUG)');

  console.log('console/page errors:', errors.length, errors.slice(0, 5));
  fs.writeFileSync(path.join(OUT, 'result.json'), JSON.stringify({ frames, post, stillGold, afterReload, errors }, null, 2));
  await browser.close();
  process.exit(errors.length || distinctClips < 3 || afterReload !== 0 ? 1 : 0);
})();
