// WEAVER 2026-09-02: primary-viewport probe (1151x834 dpr2 = Chris's Hermes preview webview, measured from the AX tree).
// usage: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-1151.js [W H] [outPrefix]
const pw = require(process.env.PW || '/Users/sovthpaw/.hermes/hermes-agent/node_modules/playwright');
const path = require('path');
const W = +(process.argv[2] || 1151), H = +(process.argv[3] || 834), out = process.argv[4] || ('/tmp/wiki-' + W + 'x' + H);
const file = 'file://' + path.resolve(__dirname, '..', 'vault-live.html');
(async () => {
  const br = await pw.chromium.launch();
  const pg = await br.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  const errs = []; pg.on('pageerror', e => errs.push(String(e))); pg.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await pg.goto(file); await pg.waitForTimeout(2600);
  const m = () => pg.evaluate(() => {
    const v = document.getElementById('view-wiki'); const names = [...v.querySelectorAll('.topic .thead .tname')];
    v.classList.add('orbMeasure'); let titleTextRightAll = 0, titleTextRight = 0; names.forEach(n => { const r = n.getBoundingClientRect(); titleTextRightAll = Math.max(titleTextRightAll, r.right); if (r.top < innerHeight && r.bottom > 0) titleTextRight = Math.max(titleTextRight, r.right); }); v.classList.remove('orbMeasure');
    const th = v.querySelector('.topic .thead'); const orbs = [...th.querySelectorAll('.orb')].map(o => o.getBoundingClientRect());
    let gRight = 0, gLeft = Infinity; v.querySelectorAll('.topic .thead').forEach(t => { const os = t.querySelector('.orbs'), id = t.querySelector('.idots'); if (os) { const r = os.getBoundingClientRect(); gLeft = Math.min(gLeft, r.left); gRight = Math.max(gRight, r.right); } if (id && id.children.length) gRight = Math.max(gRight, id.getBoundingClientRect().right); });
    const figLeft = +v.dataset.figLeft, figSrc = v.dataset.figSrc, frac = window.__figFrac, samp = window.__figSample;
    const bandC = (titleTextRight + figLeft) / 2, groupC = (gLeft + gRight) / 2;
    const thr = th.getBoundingClientRect();
    return { W: innerWidth, H: innerHeight, orbcol: v.style.getPropertyValue('--orbcol'), rowcap: v.style.getPropertyValue('--rowcap'), titleTextRight: +titleTextRight.toFixed(1), titleTextRightAll: +titleTextRightAll.toFixed(1), figLeft, figSrc, figFrac: frac, samp, firstOrbX: +orbs[0].left.toFixed(1), orbXs: orbs.map(o => +o.left.toFixed(1)), groupLeft: +gLeft.toFixed(1), groupRight: +gRight.toFixed(1), bandCentre: +bandC.toFixed(1), groupCentre: +groupC.toFixed(1), delta: +(groupC - bandC).toFixed(1), rowBoxRight: +thr.right.toFixed(1), rowBoxWidth: +thr.width.toFixed(1), rows: names.length, deadLeft: window.__deadLeft };
  });
  const rest = await m(); console.log('REST', JSON.stringify(rest));
  await pg.screenshot({ path: out + '-rest.png' });
  // stage 1: row hover
  const th = pg.locator('#view-wiki .topic .thead').first(); const bb = await th.boundingBox();
  await pg.mouse.move(bb.x + 60, bb.y + bb.height / 2); await pg.waitForTimeout(500);
  const hov = await pg.evaluate(() => { const th = document.querySelector('#view-wiki .topic .thead'); const os = [...th.querySelectorAll('.orb')].map(o => { const r = o.getBoundingClientRect(); return { x: +r.left.toFixed(1), w: +r.width.toFixed(1), cx: +(r.left + r.width / 2).toFixed(1), txt: o.textContent.trim(), col: getComputedStyle(o.querySelector('.v') || o).color }; }); const gaps = os.slice(1).map((o, i) => +(o.x - (os[i].x + os[i].w)).toFixed(1)); const tn = th.querySelector('.tname'); return { orbs: os, gaps, tnameFS: getComputedStyle(tn).fontSize, underline: getComputedStyle(th, '::after').width, dead: document.body.classList.contains('deadzone'), idle: document.body.classList.contains('idle') }; });
  console.log('ROWHOVER', JSON.stringify(hov)); await pg.screenshot({ path: out + '-rowhover.png' });
  // stage 2: orb hover
  const o2 = hov.orbs[1]; const ob = await th.locator('.orb').nth(1).boundingBox();
  await pg.mouse.move(ob.x + ob.width / 2, ob.y + ob.height / 2, { steps: 4 }); await pg.waitForTimeout(500);
  const oh = await pg.evaluate(() => { const th = document.querySelector('#view-wiki .topic .thead'); const o = th.querySelectorAll('.orb')[1]; const r = o.getBoundingClientRect(); const others = [...th.querySelectorAll('.orb')].map(x => +(x.getBoundingClientRect().left + x.getBoundingClientRect().width / 2).toFixed(1)); return { w: +r.width.toFixed(1), cx: +(r.left + r.width / 2).toFixed(1), capOpacity: getComputedStyle(o, '::before').opacity, centres: others, card: !!document.querySelector('.hcard, .orbcard') }; });
  console.log('ORBHOVER', JSON.stringify({ ...oh, restCx: o2.cx, centreDelta: +(oh.cx - o2.cx).toFixed(1) })); await pg.screenshot({ path: out + '-orbhover.png' });
  console.log('ERRORS', JSON.stringify(errs.slice(0, 5)));
  await br.close();
})();
