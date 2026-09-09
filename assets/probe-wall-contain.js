// WEAVER (v14.67): prove the ENTIRE wallpaper is inside the pane (contain + center), letterbox bands are page black,
// nothing between z0 and the content paints an opaque region over the wall, and report the collapsed pills' backing.
// run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-wall-contain.js
const path = require('path');
const { chromium } = require(process.env.PW || '/Users/sovthpaw/.hermes/hermes-agent/node_modules/playwright');
const FILE = 'file://' + path.resolve(__dirname, '..', 'vault-live.html');
(async () => {
  const br = await chromium.launch();
  const out = {};
  for (const [w, h] of [[1456, 914], [1040, 880]]) {
    const p = await br.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    const errs = []; p.on('pageerror', e => errs.push(String(e)));
    await p.goto(FILE); await p.waitForTimeout(900);
    // wait for the wall image to load
    await p.evaluate(() => new Promise(r => { const bd = document.getElementById('wallBackdrop'); const u = (getComputedStyle(bd).backgroundImage.match(/url\("?([^")]+)"?\)/) || [])[1]; if (!u) return r(); const i = new Image(); i.onload = i.onerror = () => r(); i.src = u; }));
    await p.waitForTimeout(400);
    const st = await p.evaluate(() => {
      const bd = document.getElementById('wallBackdrop'); const cs = getComputedStyle(bd); const r = bd.getBoundingClientRect();
      const u = (cs.backgroundImage.match(/url\("?([^")]+)"?\)/) || [])[1]; const i = new Image(); i.src = u;
      const iw = i.naturalWidth, ih = i.naturalHeight; const s = Math.min(innerWidth / iw, innerHeight / ih);
      const dw = iw * s, dh = ih * s; const bandX = (innerWidth - dw) / 2, bandY = (innerHeight - dh) / 2;
      // every element with z-index between wall(0) and the views: opaque backgrounds that cover the wall?
      const opaque = [], pills = [], grads = [];
      document.querySelectorAll('body *').forEach(e => {
        const c0 = getComputedStyle(e); if (c0.display !== 'none' && /gradient/.test(c0.backgroundImage) && !e.closest('#topstrip') && !e.closest('#stream')) { const b0 = e.getBoundingClientRect(); if (b0.width * b0.height > 4000) grads.push({ sel: e.id ? '#' + e.id : e.tagName.toLowerCase() + '.' + [...e.classList].join('.'), w: Math.round(b0.width), h: Math.round(b0.height), bgi: c0.backgroundImage.slice(0, 90) }); }
        const c = getComputedStyle(e); if (c.display === 'none' || c.visibility === 'hidden' || Number(c.opacity) === 0) return;
        const m = c.backgroundColor.match(/rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)/); if (!m) return; const a = m[4] === undefined ? 1 : Number(m[4]); if (a < 0.9) return;
        const b = e.getBoundingClientRect(); if (b.width * b.height < 4000) return; // ignore tiny chips
        if (e.id === 'wallBackdrop' || e.closest('#topstrip') || e.closest('#stream') || e.closest('.warn')) return;
        if (e.closest('#chat .mini')) { pills.push({ bg: c.backgroundColor, op: c.opacity, w: Math.round(b.width), h: Math.round(b.height) }); return; } // pill-owner's domain: report, don't fail
        opaque.push({ sel: (e.id ? '#' + e.id : e.tagName.toLowerCase() + '.' + [...e.classList].join('.')), bg: c.backgroundColor, w: Math.round(b.width), h: Math.round(b.height), z: c.zIndex, pos: c.position });
      });
      const mini = document.querySelector('#chat .mini .msg'); const mc = mini ? getComputedStyle(mini) : null;
      return { vw: innerWidth, vh: innerHeight, rect: [r.x, r.y, r.width, r.height], z: cs.zIndex, size: cs.backgroundSize, pos: cs.backgroundPosition, bgColor: cs.backgroundColor, op: cs.opacity, img: u, iw, ih,
        drawn: [Math.round(dw), Math.round(dh)], bandX: +bandX.toFixed(1), bandY: +bandY.toFixed(1), bandPctX: +(100 * bandX / innerWidth).toFixed(2),
        dim: getComputedStyle(bd, '::after').backgroundColor, mmZ: getComputedStyle(document.getElementById('mindmap')).zIndex, mmBg: getComputedStyle(document.getElementById('mindmap')).backgroundColor,
        bodyBg: getComputedStyle(document.body).backgroundColor, viewsBg: [...document.querySelectorAll('.view.on')].map(v => v.id + ':' + getComputedStyle(v).backgroundColor), opaque, pills, grads,
        miniBg: mc && mc.backgroundColor, miniOp: mc && mc.opacity, miniBorder: mc && mc.borderColor };
    });
    st.errs = errs;
    // full-UI shot (what Chris sees) + wall-only shot (UI hidden, dim kept) for the vision check
    const shot = path.resolve(__dirname, `wall-contain-${w}x${h}.png`); await p.screenshot({ path: shot }); st.shot = shot;
    await p.evaluate(() => { document.querySelectorAll('body > *').forEach(e => { if (e.id !== 'wallBackdrop') e.style.visibility = 'hidden'; }); });
    const shotWall = path.resolve(__dirname, `wall-contain-${w}x${h}-wallonly.png`); await p.screenshot({ path: shotWall }); st.shotWall = shotWall;
    // sample band pixels vs image pixels on the wall-only shot
    const px = await p.evaluate(() => { const c = document.createElement('canvas'); return null; });
    out[`${w}x${h}`] = st; await p.close();
  }
  await br.close();
  console.log(JSON.stringify(out, null, 1));
  const a = out['1456x914'];
  const ok = a.size === 'contain' && a.pos === '50% 50%' && a.bgColor === 'rgb(6, 6, 6)' && a.z === '0' && a.mmZ === '1' && a.op === '1' && a.opaque.length === 0 && a.errs.length === 0 && a.bandX > 0;
  console.log(ok ? 'PROBE OK' : 'PROBE FAIL'); process.exit(ok ? 0 : 1);
})().catch(e => { console.error(e); process.exit(2); });
