// Probe: gear font-size + ink bbox, cluster right anchor, caret bottom vs overline top.
// Run: PW=~/.hermes/hermes-agent/node_modules/playwright node scripts/probe-gear-caret.js [--shot out.png]
const pw = require(process.env.PW);
const path = require('path');
const file = 'file://' + path.resolve(__dirname, '..', 'vault-live.html');
const shot = process.argv.includes('--shot') ? process.argv[process.argv.indexOf('--shot') + 1] : null;

async function measure(page) {
  return page.evaluate(() => {
    const r = (el) => { const b = el.getBoundingClientRect(); return { l: +b.left.toFixed(1), r: +b.right.toFixed(1), t: +b.top.toFixed(1), b: +b.bottom.toFixed(1), w: +b.width.toFixed(1), h: +b.height.toFixed(1) }; };
    const gear = document.getElementById('navSettings');
    const rg = document.createRange(); rg.selectNodeContents(gear); const ink = rg.getBoundingClientRect();
    const media = document.getElementById('media');
    const nav = document.getElementById('topnav');
    const row = document.getElementById('composerRow');
    const right = document.getElementById('composerRight');
    const caret = document.getElementById('senterCaret');
    const line = document.getElementById('senterOverline');
    const cs = getComputedStyle(gear);
    return {
      vw: innerWidth, vh: innerHeight,
      gearFont: cs.fontSize, gearTransform: cs.transform, gearBox: r(gear),
      gearInk: { l: +ink.left.toFixed(1), r: +ink.right.toFixed(1), t: +ink.top.toFixed(1), b: +ink.bottom.toFixed(1), w: +ink.width.toFixed(1), h: +ink.height.toFixed(1) },
      mediaRight: +media.getBoundingClientRect().right.toFixed(1),
      navPaddingRight: getComputedStyle(nav).paddingRight,
      navContentRight: +(nav.getBoundingClientRect().right - parseFloat(getComputedStyle(nav).paddingRight)).toFixed(1),
      rowPaddingRight: row.style.paddingRight,
      clusterRight: right ? r(right).r : null,
      clusterBox: right ? r(right) : null,
      caretBox: r(caret), caretDisplay: getComputedStyle(caret).display, caretTransform: getComputedStyle(caret).transform,
      overlineTop: +line.getBoundingClientRect().top.toFixed(1),
      caretGap: +(line.getBoundingClientRect().top - caret.getBoundingClientRect().bottom).toFixed(1),
      textBox: r(document.getElementById('senterText')),
    };
  });
}

(async () => {
  const browser = await pw.chromium.launch();
  const out = {};
  for (const [w, h] of [[1456, 914], [1040, 880]]) {
    const page = await browser.newPage({ viewport: { width: w, height: h } });
    const errs = [];
    page.on('pageerror', e => errs.push(String(e)));
    await page.goto(file);
    await page.waitForTimeout(600);
    await page.evaluate(() => { document.getElementById('topstrip').classList.add('on'); if (window._alignCluster) window._alignCluster(); });
    await page.waitForTimeout(350);
    const m = await measure(page);
    m.pageErrors = errs;
    out[`${w}x${h}`] = m;
    if (shot && w === 1456) {
      await page.evaluate((m) => {
        const mk = (css) => { const d = document.createElement('div'); d.style.cssText = 'position:fixed;z-index:99999;pointer-events:none;' + css; document.body.appendChild(d); return d; };
        // guide 1: vertical at gear ink right edge (aligned target)
        mk(`left:${m.gearInk.r}px;top:0;width:1px;height:220px;background:#FFE45A;opacity:.9`);
        // guide 2: horizontal at overline top (caret must sit above it)
        mk(`left:0;right:0;top:${m.overlineTop}px;height:1px;background:#ff4444;opacity:.9`);
        // marker: caret bottom
        mk(`left:${m.caretBox.l - 6}px;top:${m.caretBox.b}px;width:14px;height:1px;background:#4af;opacity:.9`);
        // label
        mk(`left:${m.gearInk.r - 330}px;top:150px;color:#FFE45A;font:12px monospace;background:#000;padding:2px 4px`).textContent = `gear ${m.gearFont} ink right ${m.gearInk.r} · cluster right ${m.clusterRight} · caret gap ${m.caretGap}px`;
      }, m);
      await page.screenshot({ path: shot, clip: { x: 0, y: 0, width: 1456, height: 914 } });
    }
    await page.close();
  }
  await browser.close();
  console.log(JSON.stringify(out, null, 1));
})().catch(e => { console.error(e); process.exit(1); });
