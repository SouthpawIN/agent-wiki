// AI — backdrop at native quality + neutral dim. Run:
//   PW=~/.hermes/hermes-agent/node_modules/playwright ~/.hermes/node/bin/node assets/probe-AI.js [WxH] [dpr] [shotDir]
// Prints: asset picked, natural size, dim color, opacity, ledger (assetW >= dpr*innerWidth), then writes WIKI + SPACE shots.
const pw = require(process.env.PW || 'playwright');
const path = require('path'), fs = require('fs');
const [W, H] = (process.argv[2] || '1456x914').split('x').map(Number);
const DPR = Number(process.argv[3] || 2);
const OUT = process.argv[4] || 'assets/look';
const FILE = 'file://' + path.resolve('vault-live.html');
(async () => {
  const b = await pw.chromium.launch();
  const ctx = await b.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: DPR });
  const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.route('**/ask**', r => r.fulfill({ status: 202, body: '{"ok":true}' }));
  // AI one-shot reset: a stale pre-AI pick (badge-galaxy = the gold variant) must come back as galactic; a pick made AFTER the marker must persist.
  await p.goto(FILE + '?view=wiki'); await p.evaluate(() => { localStorage.clear(); localStorage.setItem('sw.wall', 'hermes-badge-galaxy'); });
  await p.goto(FILE + '?view=wiki'); await p.waitForTimeout(600);
  const mig1 = await p.evaluate(() => ({ wall: localStorage.getItem('sw.wall'), marker: localStorage.getItem('sw.wall.ai'), asset: document.getElementById('wallBackdrop').dataset.asset }));
  await p.evaluate(() => { window._setWall('hermes-ember'); });
  await p.goto(FILE + '?view=wiki'); await p.waitForTimeout(600);
  const mig2 = await p.evaluate(() => localStorage.getItem('sw.wall'));
  await p.evaluate(() => { localStorage.removeItem('sw.wall'); });
  await p.goto(FILE + '?view=wiki'); await p.waitForTimeout(3600);
  const info = await p.evaluate(async () => {
    // eslint-disable-next-line no-unused-vars
    const bd = document.getElementById('wallBackdrop');
    const cs = getComputedStyle(bd), af = getComputedStyle(bd, '::after');
    const url = (cs.backgroundImage.match(/url\("?([^")]+)"?\)/) || [])[1] || '';
    const img = new Image(); img.src = url;
    await new Promise(r => { img.onload = r; img.onerror = r; });
    const mm = document.getElementById('mindmap');
    return { dpr: devicePixelRatio, innerWidth, innerHeight, asset: bd.dataset.asset, url, naturalW: img.naturalWidth, naturalH: img.naturalHeight,
      opacity: cs.opacity, on: bd.classList.contains('on'), fs: bd.classList.contains('fs'), size: cs.backgroundSize, pos: cs.backgroundPosition,
      dim: af.backgroundColor, bodyBg: getComputedStyle(document.body).backgroundColor, mmOpacity: mm && getComputedStyle(mm).opacity,
      viewBg: getComputedStyle(document.querySelector('.view.on')).backgroundColor };
  });
  const need = info.dpr * info.innerWidth;
  const checks = [
    ['one-shot reset: stale badge-galaxy pick → galactic (' + mig1.wall + ', marker ' + mig1.marker + ', asset ' + mig1.asset + ')', mig1.wall === 'hermes-galactic' && mig1.marker === '1' && /hermes-galactic@2x/.test(mig1.asset)],
    ['post-marker pick persists (ember stays ember)', mig2 === 'hermes-ember'],
    ['asset is the @2x export when dpr>1', info.dpr > 1 ? /@2x\.jpg$/.test(info.asset) : /[^x]\.jpg$/.test(info.asset)],
    ['ledger: asset width >= dpr x viewport width (' + info.naturalW + ' >= ' + need + ')', info.naturalW >= need],
    ['asset loads (natural size > 0)', info.naturalW > 0 && info.naturalH > 0],
    ['backdrop on, opacity 1', info.on && info.opacity === '1'],
    ['dim is pure neutral black rgba(0,0,0,a) a in [.40,.50]', (() => { const m = info.dim.match(/rgba\((\d+), (\d+), (\d+), ([\d.]+)\)/); return !!m && m[1] === '0' && m[2] === '0' && m[3] === '0' && +m[4] >= .40 && +m[4] <= .50; })()],
    // framing: Chris (v14.66, after AI was specced) asked for the WHOLE artwork → `contain` centered; `cover` 50% 50% was the AI spec. Accept either, report which.
    ['framing is contain|cover, centered (' + info.size + ' ' + info.pos + ')', (info.size === 'contain' || info.size === 'cover') && info.pos === '50% 50%'],
    ['constellation stays .17 on wiki', info.mmOpacity === '0.17'],
    ['no page errors (ignoring pre-existing ERR_FILE_NOT_FOUND from sibling items)', errs.filter(e => !/ERR_FILE_NOT_FOUND/.test(e)).length === 0],
  ];
  let bad = 0; for (const [n, ok] of checks) { console.log((ok ? 'OK  ' : 'FAIL') + ' ' + n); if (!ok) bad++; }
  console.log(JSON.stringify(info));
  if (errs.length) console.log('errors:', errs.slice(0, 5));
  fs.mkdirSync(OUT, { recursive: true });
  await p.mouse.move(W - 40, H - 40);
  const tag = W + 'x' + H + '@' + DPR;
  await p.screenshot({ path: path.join(OUT, 'AI-wiki-' + tag + '.png') });
  await p.evaluate(() => showView('senter')); await p.waitForTimeout(1200);
  await p.screenshot({ path: path.join(OUT, 'AI-space-' + tag + '.png') });
  // pure backdrop frame (no UI, no dim) for pixel compare against the desktop — plus wall+dim and wall+dim+map frames for the cast check
  const hideUI = () => { document.querySelectorAll('body > *').forEach(e => { if (e.id !== 'wallBackdrop' && e.id !== 'mindmap') e.style.visibility = 'hidden'; }); };
  await p.evaluate(() => showView('wiki')); await p.waitForTimeout(400);
  await p.evaluate(hideUI); await p.waitForTimeout(300);
  await p.screenshot({ path: path.join(OUT, 'AI-walldimmap-' + tag + '.png') });
  await p.evaluate(() => { document.getElementById('mindmap').style.visibility = 'hidden'; }); await p.waitForTimeout(200);
  await p.screenshot({ path: path.join(OUT, 'AI-walldim-' + tag + '.png') });
  await p.evaluate(() => { const s = document.createElement('style'); s.textContent = '#wallBackdrop::after{display:none}'; document.head.appendChild(s); });
  await p.waitForTimeout(300);
  await p.screenshot({ path: path.join(OUT, 'AI-wallonly-' + tag + '.png') });
  console.log('shots → ' + OUT + '/AI-{wiki,space,walldimmap,walldim,wallonly}-' + tag + '.png');
  await b.close();
  process.exit(bad ? 1 : 0);
})();
