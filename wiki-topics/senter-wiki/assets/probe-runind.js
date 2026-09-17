// WEAVER (v14.77): RUNNING-BOT INDICATOR probe — live bridge. Run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-runind.js [--shot]
// Asserts: #runInd renders one .rpet per bot with a live turn/tool in the last 90s of REAL bridge events; the sprite's
// background-position changes between two samples 400ms apart (CSS steps() animation); hidden when state is reset;
// a synthetic turn/start via runInd.feed renders + a turn/end removes; x-count label only when n>1. Writes assets/proof-runind.png.
const { chromium } = require(process.env.PW);
const path = require('path'), fs = require('fs');
const file = 'file://' + path.resolve(__dirname, '..', 'vault-live.html');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1456, height: 914 } });
  const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto(file); await p.waitForTimeout(2500);
  const state = await p.evaluate(() => ({ live: window.__bridgeLive, st: window.runInd.state(), on: document.getElementById('runInd').classList.contains('on'),
    pets: [...document.querySelectorAll('#runInd .rpet')].map(e => ({ bot: e.dataset.bot, slug: e.dataset.slug, n: e.dataset.n, cnt: e.querySelector('.cnt').textContent, cap: e.querySelector('.cap').textContent, bg: getComputedStyle(e.querySelector('.sprite')).backgroundImage.slice(0, 80), box: e.getBoundingClientRect().toJSON() })) }));
  const s1 = await p.evaluate(() => [...document.querySelectorAll('#runInd .sprite')].map(e => getComputedStyle(e).backgroundPosition));
  await p.waitForTimeout(400);
  const s2 = await p.evaluate(() => [...document.querySelectorAll('#runInd .sprite')].map(e => getComputedStyle(e).backgroundPosition));
  const imgOk = await p.evaluate(async () => { const r = await Promise.all([...document.querySelectorAll('#runInd .sprite')].map(e => new Promise(res => { const m = /url\("?([^")]+)"?\)/.exec(getComputedStyle(e).backgroundImage); if (!m) return res(false); const i = new Image(); i.onload = () => res(i.naturalWidth === 1536 && i.naturalHeight === 1872); i.onerror = () => res(false); i.src = m[1]; }))); return r; });
  const box = await p.evaluate(() => document.getElementById('runInd').getBoundingClientRect().toJSON());
  const z = await p.evaluate(() => ({ run: getComputedStyle(document.getElementById('runInd')).zIndex, chat: getComputedStyle(document.getElementById('chat')).zIndex, strip: getComputedStyle(document.getElementById('topstrip')).zIndex }));
  if (process.argv.includes('--shot')) { await p.screenshot({ path: path.join(__dirname, 'proof-runind.png'), clip: { x: 0, y: 914 - 160, width: 520, height: 160 } }); await p.screenshot({ path: path.join(__dirname, 'proof-runind-full.png') }); }
  // synthetic path + hidden-when-idle
  const syn = await p.evaluate(async () => {
    runInd.reset(); const hidden = !document.getElementById('runInd').classList.contains('on');
    runInd.feed({ ts: Date.now() / 1000, bot: 'teknium', kind: 'turn', phase: 'start', pid: 111 }); const one = document.querySelector('#runInd .rpet[data-bot="teknium"]');
    const x1 = one && one.querySelector('.cnt').textContent;
    runInd.feed({ ts: Date.now() / 1000, bot: 'teknium', kind: 'tool', phase: 'start', pid: 222 }); const x2 = one.querySelector('.cnt').textContent;
    runInd.feed({ ts: Date.now() / 1000, bot: 'teknium', kind: 'turn', phase: 'end', pid: 222 }); const back1 = one.querySelector('.cnt').textContent;
    runInd.feed({ ts: Date.now() / 1000 - 200, bot: 'anser', kind: 'turn', phase: 'start' }); const stale = !!document.querySelector('#runInd .rpet[data-bot="anser"]');
    runInd.feed({ ts: Date.now() / 1000, bot: 'teknium', kind: 'turn', phase: 'end', pid: 111 }); await new Promise(r => setTimeout(r, 250));
    return { hidden, x1, x2, back1, stale, offAfter: !document.getElementById('runInd').classList.contains('on'), left: document.querySelectorAll('#runInd .rpet').length, on: document.getElementById('runInd').classList.contains('on') };
  });
  const out = { errs, box, z, state, s1, s2, imgOk, syn };
  console.log(JSON.stringify(out, null, 1));
  const weaver = state.pets.find(x => x.bot === 'weaver');
  const fails = [];
  if (!state.live) fails.push('bridge not live');
  if (!state.on || !state.pets.length) fails.push('overlay not on with live events');
  if (!weaver) fails.push('weaver not shown'); else if (!(+weaver.n >= 2) || weaver.cnt !== 'x' + weaver.n) fails.push('weaver count/label wrong ' + JSON.stringify(weaver));
  if (!s1.length || s1.some((v, i) => v === s2[i])) fails.push('sprite frame did not change in 400ms');
  if (imgOk.some(v => !v)) fails.push('a spritesheet failed to load at 1536x1872');
  if (!(box.x >= 18 && box.x <= 22 && Math.abs(914 - box.bottom - 20) <= 1)) fails.push('overlay not ~20px from left/bottom');
  if (!(+z.run > 40 && +z.run < +z.chat && +z.chat < +z.strip)) fails.push('z-order wrong');
  if (!(syn.hidden && syn.x1 === '' && syn.x2 === 'x2' && syn.back1 === '' && !syn.stale && syn.offAfter && syn.left === 0)) fails.push('synthetic path wrong');
  if (errs.length) fails.push('page errors');
  console.log(fails.length ? 'FAIL ' + fails.join(' | ') : 'probe-runind OK');
  await b.close(); process.exit(fails.length ? 1 : 0);
})();
