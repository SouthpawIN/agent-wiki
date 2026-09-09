// WEAVER (v14.70): mind-map spread probe — steady-state node bbox (incl. drift ±14/±10 + radius), min distance to each pane edge,
// hub centre px and canvas opacity, on WIKI and SPACE, at 1456×914 and 1040×880. Also SPACE label overhang (text is measured, reported separately).
// run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-mm-spread.js [shot.png]
const { chromium } = require(process.env.PW);
const path = require('path');
const file = 'file://' + path.resolve(__dirname, '..', 'vault-live.html');
const shot = process.argv[2];
(async () => {
  const br = await chromium.launch();
  const out = {};
  for (const vp of [[1456, 914], [1040, 880]]) {
    const pg = await br.newPage({ viewport: { width: vp[0], height: vp[1] } });
    const errs = []; pg.on('pageerror', e => errs.push(String(e)));
    await pg.goto(file); await pg.waitForTimeout(700);
    const measure = async (view) => {
      if (view === 'space') { await pg.evaluate(() => showView('senter')); await pg.waitForTimeout(2500); }
      return pg.evaluate(() => {
        const W = innerWidth, H = innerHeight, s = CAM.ts, tx = CAM.tx, ty = CAM.ty;
        const hub = MNODES[0];
        const sx = v => v * s + tx, sy = v => v * s + ty;
        let minX = 1e9, maxX = -1e9, minY = 1e9, maxY = -1e9, labMaxX = -1e9;
        const c = document.getElementById('mindmap').getContext('2d');
        c.font = (11) + 'px Collapse, ui-monospace, monospace';
        MNODES.forEach(n => { if (n.hub) return;
          const dx = (14 + n.r) * s, dy = (10 + n.r) * s;
          minX = Math.min(minX, sx(n.ox) - dx); maxX = Math.max(maxX, sx(n.ox) + dx);
          minY = Math.min(minY, sy(n.oy) - dy); maxY = Math.max(maxY, sy(n.oy) + dy);
          labMaxX = Math.max(labMaxX, sx(n.ox) + dx + 8 + c.measureText(n.label.toUpperCase()).width);
        });
        const r = v => Math.round(v * 10) / 10;
        return { view: document.body.classList.contains('space') ? 'space' : 'wiki', vw: W, vh: H, scale: s,
          hub: { x: r(sx(hub.ox)), y: r(sy(hub.oy)), worldX: r(hub.ox), worldY: r(hub.oy) },
          bbox: { l: r(minX), r: r(maxX), t: r(minY), b: r(maxY) },
          edge: { left: r(minX), right: r(W - maxX), top: r(minY), bottom: r(H - maxY) },
          minEdge: r(Math.min(minX, W - maxX, minY, H - maxY)),
          labelRightClear: r(W - labMaxX),
          opacity: getComputedStyle(document.getElementById('mindmap')).opacity,
          nodes: MNODES.length - 1, spread: typeof MM_SPREAD !== 'undefined' ? MM_SPREAD : null };
      });
    };
    const wiki = await measure('wiki');
    if (shot && vp[0] === 1456) await pg.screenshot({ path: shot });
    const space = await measure('space');
    out[vp.join('x')] = { wiki, space, errs };
    await pg.close();
  }
  await br.close();
  console.log(JSON.stringify(out, null, 1));
})();
