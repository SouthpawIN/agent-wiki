// probe-row-align.js — measure caret / + / auto / voice glyphs / gear centers + volume rocker hover from both sides.
// run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-row-align.js [w h] [--shot out.png]
const { chromium } = require(process.env.PW || '/Users/sovthpaw/.hermes/hermes-agent/node_modules/playwright');
const path = require('path');
const FILE = 'file://' + path.resolve(__dirname, '..', 'vault-live.html');
const args = process.argv.slice(2);
const W = +args[0] || 1456, H = +args[1] || 914;
const shotIdx = args.indexOf('--shot'); const SHOT = shotIdx >= 0 ? args[shotIdx + 1] : null;

(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: W, height: H } });
  const errs = []; pg.on('pageerror', e => errs.push(String(e)));
  await pg.goto(FILE); await pg.waitForTimeout(3300); // > the page's 3s boot stripArm() so it can't close the strip mid-test
  await pg.evaluate(() => { document.getElementById('topstrip').classList.add('on'); document.getElementById('senterOverlineZone').classList.add('on'); if (window._alignCluster) window._alignCluster(); });
  await pg.waitForTimeout(350);
  const m = await pg.evaluate(() => {
    const r = s => { const e = document.querySelector(s); if (!e) return null; const b = e.getBoundingClientRect(); return { top: +b.top.toFixed(1), bottom: +b.bottom.toFixed(1), left: +b.left.toFixed(1), right: +b.right.toFixed(1), cy: +((b.top + b.bottom) / 2).toFixed(1) }; };
    const ink = s => { const e = document.querySelector(s); if (!e) return null; const rg = document.createRange(); rg.selectNodeContents(e); const b = rg.getBoundingClientRect(); return { top: +b.top.toFixed(1), bottom: +b.bottom.toFixed(1), right: +b.right.toFixed(1), cy: +((b.top + b.bottom) / 2).toFixed(1) }; };
    const gl = [...document.querySelectorAll('#composerRight .csq .lucide svg')].map(e => { const b = e.getBoundingClientRect(); return +((b.top + b.bottom) / 2).toFixed(1); });
    const caps = [...document.querySelectorAll('#composerRow .csq .cap')].map(e => +e.getBoundingClientRect().top.toFixed(1));
    return {
      overline: r('#senterOverline'), plus: r('#composerLeft .csq[data-k="context"] .lucide svg'), auto: r('#composerLeft .model-pill .pillBox'),
      caret: r('#senterCaret'), glyphs: gl, gearBox: r('#navSettings'), gearInk: ink('#navSettings'), caps, media: r('#media'), mVol: r('#mVol'), mVolTrack: r('#mVolTrack'), mNext: r('#mNext'), mPrev: r('#mPrev'),
      volOpenRest: document.getElementById('media').classList.contains('volOpen'), vw: innerWidth,
    };
  });
  console.log(JSON.stringify({ W, H, ...m }, null, 0));
  // hover tests. Rocker region = #mVol box. Approach from the RIGHT (gear) straight to the rocker's x, never crossing #media buttons.
  const vol = m.mVol, med = m.media;
  const yRock = (vol.top + vol.bottom) / 2, xRock = (vol.left + vol.right) / 2;
  const isOpen = () => pg.evaluate(() => { const v = document.getElementById('mVol'); const cs = getComputedStyle(v); return { volOpen: document.getElementById('media').classList.contains('volOpen'), opacity: cs.opacity, pe: cs.pointerEvents }; });
  // keep the strip open for the whole hover test (leaving #topstrip closes it and the widget is clipped away → hero). Neutral point = inside the strip, empty area under the tabs.
  const open = () => pg.evaluate(() => { if (typeof stripShow === 'function') stripShow(); else { document.getElementById('topstrip').classList.add('on'); } });
  const NX = Math.round(W * 0.42), NY = 176;
  await pg.mouse.move(NX, NY); await open(); await pg.waitForTimeout(600);
  const rest = await isOpen();
  // from right: start at gear ink x, at rocker y, glide left to rocker center (first hop goes via the far-right bottom corner so the straight line never crosses #media)
  await pg.mouse.move(W - 30, NY, { steps: 3 }); await pg.waitForTimeout(60);
  await pg.mouse.move(m.gearInk.right - 10, yRock, { steps: 4 }); await pg.waitForTimeout(80);
  const atGear = await isOpen();
  await pg.mouse.move(vol.right - 4, yRock, { steps: 12 }); await pg.waitForTimeout(120);
  await pg.mouse.move(xRock, yRock, { steps: 6 }); await pg.waitForTimeout(220);
  const fromRight = await isOpen();
  // leave downward far away, wait out grace
  await pg.mouse.move(NX, NY, { steps: 6 }); await open(); await pg.waitForTimeout(800);
  const afterLeave = await isOpen();
  // from left: start left of #media at rocker y but BELOW the media buttons? buttons live in #mCtl; approach along a y below #media box then up into rocker from its left edge.
  // Path: start at (media.left-60, media.bottom+30) → move to (vol.left+4, media.bottom+30) → up to (vol.left+4, yRock) → xRock. Never enters #media's button hit boxes.
  const yUnder = Math.min(med.bottom + 14, 186);
  await pg.mouse.move(med.left - 60, yUnder, { steps: 4 }); await pg.waitForTimeout(80);
  await pg.mouse.move(vol.left + 3, yUnder, { steps: 8 }); await pg.waitForTimeout(80);
  await pg.mouse.move(vol.left + 3, yRock, { steps: 8 }); await pg.waitForTimeout(120);
  await pg.mouse.move(xRock, yRock, { steps: 4 }); await pg.waitForTimeout(220);
  const fromLeft = await isOpen();
  console.log(JSON.stringify({ rest, atGear, fromRight, afterLeave, fromLeft, errs }));
  if (SHOT) {
    const cy = m.auto ? m.auto.cy : 0;
    await pg.evaluate(y => { const g = document.createElement('div'); g.id = '__guide'; g.style.cssText = `position:fixed;left:0;right:0;top:${y - 0.5}px;height:1px;background:#FF3B30;z-index:99999;pointer-events:none`; document.body.appendChild(g); }, cy);
    await pg.screenshot({ path: SHOT, clip: { x: 0, y: 0, width: W, height: 140 } });
    console.log('shot ' + SHOT + ' guide y=' + cy);
  }
  await b.close();
})();
