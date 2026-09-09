// AH probe — wall backdrop is an explicit ⚙ setting (default ON), not gated on isFS().
// Run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-ah.js [--vp 1456x914] [--shot assets/look]
const path = require('path');
const { chromium } = require(process.env.PW || '/Users/sovthpaw/.hermes/hermes-agent/node_modules/playwright');
const arg = process.argv.indexOf('--vp'); const [W, H] = (arg > 0 ? process.argv[arg + 1] : '1456x914').split('x').map(Number);
const sa = process.argv.indexOf('--shot'); const SHOT = sa > 0 ? process.argv[sa + 1] : null;
const URL = 'file://' + path.resolve(__dirname, '..', 'vault-live.html');
let pass = 0, fail = 0;
const ok = (name, cond, extra) => { if (cond) pass++; else fail++; console.log((cond ? 'ok   ' : 'FAIL ') + name + (extra ? '  ' + extra : '')); };
const lum = ([r, g, b]) => { const f = c => { c /= 255; return c <= .03928 ? c / 12.92 : Math.pow((c + .055) / 1.055, 2.4); }; return .2126 * f(r) + .7152 * f(g) + .0722 * f(b); };
const contrast = (a, b) => { const la = lum(a) + .05, lb = lum(b) + .05; return la > lb ? la / lb : lb / la; };

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W, height: H } });
  const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto(URL); await p.waitForTimeout(3600);

  const state = () => p.evaluate(() => { const bd = document.getElementById('wallBackdrop'); const cs = getComputedStyle(bd); const af = getComputedStyle(bd, '::after');
    return { op: cs.opacity, z: cs.zIndex, img: cs.backgroundImage, dim: af.backgroundColor, ls: localStorage.getItem('sw.wall'), cur: window._wallCur && window._wallCur(), fs: window._isFS(), on: bd.classList.contains('on'),
      mmZ: getComputedStyle(document.getElementById('mindmap')).zIndex, mmOp: getComputedStyle(document.getElementById('mindmap')).opacity,
      viewBg: (document.querySelector('.view.on') ? getComputedStyle(document.querySelector('.view.on')).backgroundColor : 'no-view-on'), bodyBg: getComputedStyle(document.body).backgroundColor }; });

  // 1. default state (fresh profile, no localStorage) = ON, galactic, opacity 1, even though isFS() is false
  let s = await state();
  ok('AH default: sw.wall unset → hermes-galactic ON (opacity 1) while isFS() is false', s.op === '1' && s.on && /hermes-galactic\.jpg/.test(s.img) && s.fs === false && s.ls === null, JSON.stringify(s));
  ok('AH layering: backdrop z0 < mindmap z1; active view transparent; semi-transparent dim on ::after (α .3–.7 — value owned by AI)', s.z === '0' && s.mmZ === '1' && s.viewBg === 'rgba(0, 0, 0, 0)' && /rgba\(\d+, \d+, \d+, 0\.[3-6]\d*\)/.test(s.dim), JSON.stringify({ z: s.z, mmZ: s.mmZ, viewBg: s.viewBg, dim: s.dim }));
  ok('AH mind map above the wall at .17 on WIKI', s.mmOp === '0.17', s.mmOp);
  // no setInterval left in the backdrop IIFE
  ok('AH backdrop IIFE has no timer', await p.evaluate(() => !/setInterval/.test([...document.scripts].map(x => x.textContent).join('').split('/* BACKDROP')[1].split('})();')[0])));

  // 2. the wall is really painted: pixel in an empty region (not black) — take a pixel sample via canvas of the screenshot
  const shotBuf = await p.screenshot({ type: 'png' });
  const stats = await p.evaluate(async (b64) => { return await new Promise(res => { const im = new Image(); im.onload = () => { const c = document.createElement('canvas'); c.width = im.width; c.height = im.height; const x = c.getContext('2d'); x.drawImage(im, 0, 0); const px = (X, Y) => [...x.getImageData(X, Y, 1, 1).data].slice(0, 3);
      // sample a grid over the lower-middle area (below the list, away from text)
      const samples = []; for (let X = 60; X < im.width - 500; X += 90) for (let Y = Math.round(im.height * .55); Y < im.height - 210; Y += 60) samples.push(px(X, Y));
      const nonBlack = samples.filter(v => Math.max(...v) > 14).length; const maxV = Math.max(...samples.map(v => Math.max(...v)));
      // hero title ink vs its local background: sample title bbox
      const t = document.querySelector('.view.on .heroTitle'); const r = document.createRange(); r.selectNodeContents(t); const bb = r.getBoundingClientRect();
      let darkest = [255, 255, 255]; for (let X = Math.round(bb.left); X < Math.min(bb.right, bb.left + 400); X += 6) for (let Y = Math.round(bb.top); Y < bb.bottom; Y += 4) { const v = px(X, Y); if (v[0] + v[1] + v[2] < darkest[0] + darkest[1] + darkest[2]) darkest = v; }
      // busiest region of the wall itself: brightest pixel over the whole lower half (the wall bleeding through)
      let brightest = [0, 0, 0]; for (let X = 0; X < im.width; X += 8) for (let Y = 0; Y < im.height; Y += 8) { const v = px(X, Y); const e = document.elementFromPoint(X, Y); if (e && (e.closest('.hero') || e.closest('#chat') || e.closest('.thead'))) continue; if (v[0] + v[1] + v[2] > brightest[0] + brightest[1] + brightest[2]) brightest = v; }
      res({ total: samples.length, nonBlack, maxV, titleBg: darkest, wallBright: brightest }); }; im.src = 'data:image/png;base64,' + b64; }); }, shotBuf.toString('base64'));
  ok('AH wall pixels visible on WIKI (a bright wall feature reaches the page; the galactic wall is itself mostly black — median L=1)', stats.maxV > 60, JSON.stringify(stats));
  // differential proof: how many screen pixels change when the wall is switched to none (same view, same frame)
  const diff = await p.evaluate(async (b64on) => { window._setWall('none'); await new Promise(r => setTimeout(r, 500)); return b64on; }, shotBuf.toString('base64'));
  const shotOff = await p.screenshot({ type: 'png' }); await p.evaluate(() => window._setWall('hermes-galactic')); await p.waitForTimeout(500);
  const changed = await p.evaluate(async ([a, b]) => { const load = s => new Promise(res => { const im = new Image(); im.onload = () => res(im); im.src = 'data:image/png;base64,' + s; }); const [ia, ib] = await Promise.all([load(a), load(b)]); const c = document.createElement('canvas'); c.width = ia.width; c.height = ia.height; const x = c.getContext('2d'); x.drawImage(ia, 0, 0); const da = x.getImageData(0, 0, c.width, c.height).data; x.drawImage(ib, 0, 0); const db = x.getImageData(0, 0, c.width, c.height).data; let n = 0; for (let i = 0; i < da.length; i += 4) { if (Math.abs(da[i] - db[i]) + Math.abs(da[i + 1] - db[i + 1]) + Math.abs(da[i + 2] - db[i + 2]) > 12) n++; } return { changed: n, total: da.length / 4, pct: +(100 * n / (da.length / 4)).toFixed(1) }; }, [diff, shotOff.toString('base64')]);
  ok('AH differential: switching wall → none changes ≥ 5% of the frame (the wall is really painted under the page; galactic is ~88% black itself, measured 12–13%)', changed.pct >= 5, JSON.stringify(changed));
  const cr = contrast([255, 255, 255], stats.wallBright);
  ok('AH hero title (#fff) contrast over the BRIGHTEST wall pixel ≥ 4.5:1', cr >= 4.5, 'brightest wall px ' + JSON.stringify(stats.wallBright) + ' → ' + cr.toFixed(2) + ':1');
  if (SHOT) await p.screenshot({ path: path.join(SHOT, `AH-wiki-${W}x${H}.png`) });

  // 3. SPACE: map at 1, wall still on
  await p.evaluate(() => showView('senter')); await p.waitForTimeout(700);
  s = await state();
  ok('AH SPACE: wall on, mind map opacity 1 above it', s.on && s.op === '1' && s.mmOp === '1', JSON.stringify({ op: s.op, mmOp: s.mmOp }));
  if (SHOT) await p.screenshot({ path: path.join(SHOT, `AH-space-${W}x${H}.png`) });
  await p.evaluate(() => showView('wiki')); await p.waitForTimeout(300);

  // 4. picker switches live
  await p.evaluate(() => document.getElementById('navSettings').click()); await p.waitForTimeout(300);
  const pick = await p.evaluate(() => { const sel = document.getElementById('setWall'); return sel ? { opts: [...sel.options].map(o => o.value), val: sel.value, label: sel.previousElementSibling.textContent } : null; });
  ok('AH ⚙ picker: 9 options (none + 8 walls), default selected = hermes-galactic, label no longer says fullscreen', pick && pick.opts.length === 9 && pick.opts[0] === 'none' && pick.val === 'hermes-galactic' && !/fullscreen/i.test(pick.label), JSON.stringify(pick));
  await p.evaluate(() => { const sel = document.getElementById('setWall'); sel.value = 'hermes-ember'; sel.dispatchEvent(new Event('change', { bubbles: true })); }); await p.waitForTimeout(450);
  s = await state();
  ok('AH pick hermes-ember → image swaps live, persisted', /hermes-ember\.jpg/.test(s.img) && s.op === '1' && s.ls === 'hermes-ember', JSON.stringify({ img: s.img, ls: s.ls }));
  if (SHOT) await p.screenshot({ path: path.join(SHOT, `AH-picker-ember-${W}x${H}.png`) });
  await p.evaluate(() => { const sel = document.getElementById('setWall'); sel.value = 'none'; sel.dispatchEvent(new Event('change', { bubbles: true })); }); await p.waitForTimeout(450);
  s = await state();
  ok('AH pick none → opacity 0, no image, persisted (OFF = today\'s body, unchanged)', s.op === '0' && !s.on && s.img === 'none' && s.ls === 'none' && s.bodyBg === 'rgb(6, 6, 6)', JSON.stringify({ op: s.op, img: s.img, ls: s.ls, bodyBg: s.bodyBg }));
  // 5. persists across reload
  await p.reload(); await p.waitForTimeout(1500);
  s = await state();
  ok('AH none persists across reload', s.op === '0' && s.ls === 'none', JSON.stringify({ op: s.op, ls: s.ls }));
  await p.evaluate(() => window._setWall('hermes-galactic')); await p.waitForTimeout(450);
  s = await state();
  ok('AH _setWall(galactic) → back on', s.op === '1' && /hermes-galactic/.test(s.img));
  // 6. isFS hint only bumps the dim
  const dimFs = await p.evaluate(() => { const bd = document.getElementById('wallBackdrop'); bd.classList.add('fs'); const d = getComputedStyle(bd, '::after').backgroundColor; bd.classList.remove('fs'); return d; });
  ok('AH .fs (fullscreen hint) deepens the dim (value > default)', parseFloat((dimFs.match(/0\.\d+/) || ['0'])[0]) > parseFloat((s.dim.match(/0\.\d+/) || ['1'])[0]), dimFs + ' vs ' + s.dim);
  ok('AH no page/console errors', errs.filter(e => !/chris\.png|avatars\//.test(e)).length === 0, errs.join(' | ').slice(0, 300));
  await b.close();
  console.log(`\nAH ${pass}/${pass + fail} @${W}x${H}`); process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
