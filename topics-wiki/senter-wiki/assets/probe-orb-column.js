// WEAVER v14.74 — ORB COLUMN: the first orb of every WIKI row starts at one shared x (measured column, not a hardcoded px);
// integration logos follow the four orbs and keep their brand colours; long titles ellipsize. Also: no animation on any orb at rest, rest 5px.
// run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-orb-column.js [--shot]
const path = require('path');
const { chromium } = require(process.env.PW || '/Users/sovthpaw/.hermes/hermes-agent/node_modules/playwright');
(async () => {
  const b = await chromium.launch(); const out = {};
  for (const vp of [[1456, 914], [1040, 880]]) {
    const page = await b.newPage({ viewport: { width: vp[0], height: vp[1] } });
    const errs = []; page.on('pageerror', e => errs.push(String(e.message)));
    await page.goto('file://' + path.resolve(__dirname, '..', 'vault-live.html'));
    await page.waitForTimeout(1200); await page.mouse.move(vp[0] - 20, vp[1] - 5); await page.waitForTimeout(150);
    const r = await page.evaluate(() => {
      const rows = [...document.querySelectorAll('#view-wiki .topic .thead')].filter(h => h.querySelector('.orb'));
      const data = rows.map(h => { const nm = h.querySelector('.tname'), o = h.querySelector('.orb'), fi = h.querySelector('.idots .idot');
        const nr = nm.getBoundingClientRect(), orr = o.getBoundingClientRect();
        return { title: nm.textContent.trim(), titleW: Math.round(nr.width * 10) / 10, titleScrollW: nm.scrollWidth, ellipsized: nm.scrollWidth > nm.clientWidth + 1, tOverflow: getComputedStyle(nm).textOverflow,
          orbX: Math.round(orr.left * 10) / 10, orbW: Math.round(orr.width * 10) / 10, orbH: Math.round(orr.height * 10) / 10, anim: getComputedStyle(o).animationName,
          firstIdotX: fi ? Math.round(fi.getBoundingClientRect().left * 10) / 10 : null, idotAfterOrbs: fi ? fi.getBoundingClientRect().left > h.querySelectorAll('.orb')[3].getBoundingClientRect().right : null }; });
      const xs = data.map(d => d.orbX); const spread = Math.max(...xs) - Math.min(...xs);
      const widest = (() => { const v = document.getElementById('view-wiki'); v.classList.add('orbMeasure'); let best = { title: '', w: 0 }; rows.forEach(h => { const n = h.querySelector('.tname'); const w = n.getBoundingClientRect().width; if (w > best.w) best = { title: n.textContent.trim(), w: Math.round(w * 10) / 10 }; }); v.classList.remove('orbMeasure'); return best; })();
      const orbAnims = [...document.querySelectorAll('.orb')].map(o => getComputedStyle(o).animationName).filter(a => a !== 'none');
      const orbSizes = [...new Set([...document.querySelectorAll('#view-wiki .orb')].map(o => o.getBoundingClientRect().width.toFixed(1)))];
      let pulseKf = 0; for (const s of document.styleSheets) { try { for (const rr of s.cssRules) if (rr.type === CSSRule.KEYFRAMES_RULE && /orb/i.test(rr.name)) pulseKf++; } catch (e) {} }
      // brand colours: every .idot must carry a non-white fill/colour
      const idots = [...document.querySelectorAll('#view-wiki .idots .idot')];
      const idotColors = idots.map(s => { const cs = getComputedStyle(s); const f = s.getAttribute('fill') || cs.fill || cs.color; return (s.dataset.kind || s.getAttribute('viewBox') || '?') + ':' + f; });
      const whiteIdots = idotColors.filter(c => /:(#fff(fff)?|rgb\(255, 255, 255\)|white)$/i.test(String(c).trim())).length;
      const col = getComputedStyle(document.getElementById('view-wiki')).getPropertyValue('--orbcol').trim();
      return { rows: data.length, columnX: xs[0], spread, allEqual: spread <= 1, widest: { title: widest.title, w: widest.w }, orbcolVar: col, ellipsized: data.filter(d => d.ellipsized).map(d => d.title),
        idotsAfterOrbs: data.every(d => d.idotAfterOrbs !== false), idots: idots.length, whiteIdots, sampleIdotColors: [...new Set(idotColors)].slice(0, 12),
        orbAnimsNotNone: orbAnims.length, orbKeyframes: pulseKf, orbRestSizes: orbSizes, perRow: data.map(d => [d.title, d.orbX, d.titleW]) };
    });
    out[vp.join('x')] = { errs, ...r };
    // HOVER pass (Chris, live): the enlarged dot must grow from its CENTRE — hovered-orb centre x == resting centre x (±1) on every row, and siblings + logos must not move
    const hov = await page.evaluate(() => [...document.querySelectorAll('#view-wiki .topic .thead')].filter(h => h.querySelector('.orb')).map((h, i) => { h.dataset.probeRow = i; const c = r => { const b = r.getBoundingClientRect(); return b.left + b.width / 2; };
      return { i, restC: [...h.querySelectorAll('.orb')].map(c), restIdot: [...h.querySelectorAll('.idot')].map(c), y: h.getBoundingClientRect().top + h.getBoundingClientRect().height / 2 }; }));
    const deltas = [];
    for (const row of hov) { if (row.y < 0 || row.y > vp[1]) continue; const sel = '#view-wiki .thead[data-probe-row="' + row.i + '"] .orb';
      await page.mouse.move(vp[0] - 20, vp[1] - 5); await page.waitForTimeout(120);
      await page.locator('#view-wiki .thead[data-probe-row="' + row.i + '"] .tname').hover({ force: true }); await page.waitForTimeout(300);   // ROW hover baseline (title grown, logos grown) — no orb hovered
      const base = await page.evaluate((s) => { const os = [...document.querySelectorAll(s)]; const h = os[0].closest('.thead'); const c = r => { const b = r.getBoundingClientRect(); return b.left + b.width / 2; }; const n = h.querySelector('.tname');
        return { orbC: os.map(c), idot: [...h.querySelectorAll('.idot')].map(c), titleEllipsized: n.scrollWidth > n.clientWidth + 1, titleFs: getComputedStyle(n).fontSize }; }, sel);
      const loc = page.locator(sel).first(); await loc.hover({ force: true }); await page.waitForTimeout(300);
      const m = await page.evaluate((s) => { const os = [...document.querySelectorAll(s)]; const h = os[0].closest('.thead'); const c = r => { const b = r.getBoundingClientRect(); return b.left + b.width / 2; };
        const b = os[0].getBoundingClientRect(); const cap = getComputedStyle(os[0], '::before'); return { w: b.width, hovC: os.map(c), idot: [...h.querySelectorAll('.idot')].map(c), capOpacity: cap.opacity, capTransform: cap.transform }; }, sel);
      deltas.push({ row: row.i, hovW: m.w, dC: Math.round((m.hovC[0] - row.restC[0]) * 10) / 10, sibMax: Math.round(Math.max(...m.hovC.slice(1).map((x, k) => Math.abs(x - row.restC[k + 1]))) * 10) / 10,
        idotMax: m.idot.length ? Math.round(Math.max(...m.idot.map((x, k) => Math.abs(x - base.idot[k]))) * 10) / 10 : 0, cap: m.capOpacity, hoverTitleEllipsized: base.titleEllipsized, hoverTitleFs: base.titleFs }); }
    await page.mouse.move(vp[0] - 20, vp[1] - 5); await page.waitForTimeout(200);
    out[vp.join('x')].hover = { rowsHovered: deltas.length, hovW: [...new Set(deltas.map(d => d.hovW))], maxCentreDelta: Math.max(...deltas.map(d => Math.abs(d.dC))), maxSiblingShift: Math.max(...deltas.map(d => d.sibMax)), maxIdotShiftVsRowHover: Math.max(...deltas.map(d => d.idotMax)), captionShown: deltas.every(d => Number(d.cap) === 1), hoverTitleEllipsized: deltas.filter(d => d.hoverTitleEllipsized).length, hoverTitleFs: [...new Set(deltas.map(d => d.hoverTitleFs))] };
    out[vp.join('x')].hoverEllipsized = await page.evaluate(async () => { const rows = [...document.querySelectorAll('#view-wiki .topic .thead')]; const out = []; for (const h of rows) { const n = h.querySelector('.tname'); n.style.fontSize = '2.3em'; if (n.scrollWidth > n.clientWidth + 1) out.push(n.textContent.trim()); n.style.fontSize = ''; } return out; });
    if (process.argv.includes('--shot')) { await page.screenshot({ path: path.resolve(__dirname, 'proof-orb-column-' + vp[0] + '.png'), clip: { x: 0, y: 0, width: Math.min(vp[0], 1000), height: vp[1] } });
      await page.locator('#view-wiki .thead[data-probe-row="5"] .orb').first().hover({ force: true }); await page.waitForTimeout(300);
      await page.screenshot({ path: path.resolve(__dirname, 'proof-orb-column-hover-' + vp[0] + '.png'), clip: { x: 0, y: 200, width: Math.min(vp[0], 1000), height: 420 } }); }
    await page.close();
  }
  console.log(JSON.stringify(out, null, 1));
  await b.close();
})();
