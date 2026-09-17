// WEAVER v14.72 — orbit removed, orbs 6px at rest, black lettering on the enlarged white dot.
// run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-orbs-noorbit.js
const path = require('path');
const { chromium } = require(process.env.PW || '/Users/sovthpaw/.hermes/hermes-agent/node_modules/playwright');
(async () => {
  const b = await chromium.launch(); const page = await b.newPage({ viewport: { width: 1456, height: 914 } });
  const errs = []; page.on('pageerror', e => errs.push(String(e.message)));
  await page.goto('file://' + path.resolve(__dirname, '..', 'vault-live.html')); await page.waitForTimeout(900);
  const orbitProbe = () => page.evaluate(() => {
    const orbs = [...document.querySelectorAll('.orb')];
    const withAfter = orbs.filter(o => getComputedStyle(o, '::after').content !== 'none').length;
    let kf = 0; for (const s of document.styleSheets) { try { for (const r of s.cssRules) if (r.type === CSSRule.KEYFRAMES_RULE && /orbit/i.test(r.name)) kf++; } catch (e) {} }
    const sel = document.querySelectorAll('[class*="orbit"], .orbit, .sat, .satellite').length;
    const src = document.documentElement.outerHTML; const orbitCss = (src.match(/orbit/gi) || []).length;
    return { orbs: orbs.length, withAfter, orbitKeyframes: kf, orbitSelectorMatches: sel, orbitWordInMarkupAndCss: orbitCss };
  });
  const rest = await page.evaluate(() => { const o = document.querySelector('#view-wiki .topic .orb'); const r = o.getBoundingClientRect(); return { w: r.width, h: r.height, bg: getComputedStyle(o).backgroundColor }; });
  const atRest = await orbitProbe();
  // force a running state on the first row, then hover the first orb
  await page.evaluate(() => { const t = document.querySelector('#view-wiki .topic .tname').textContent.trim(); setOrbActive(t, 'agents', true); });
  const o = page.locator('#view-wiki .topic .orb').first(); await o.hover(); await page.waitForTimeout(500);
  const hov = await page.evaluate(() => {
    const o = document.querySelector('#view-wiki .topic .orb'); const r = o.getBoundingClientRect(); const v = o.querySelector('.v'); const on = document.querySelector('#view-wiki .topic .orb.on');
    return { w: r.width, h: r.height, bg: getComputedStyle(o).backgroundColor, vColor: getComputedStyle(v).color, vStroke: getComputedStyle(v).webkitTextStrokeWidth, capColor: getComputedStyle(o, '::before').color, capOpacity: getComputedStyle(o, '::before').opacity,
      transform: getComputedStyle(o).transform, onAnim: on ? getComputedStyle(on).animationName : null, onAfter: on ? getComputedStyle(on, '::after').content : null };
  });
  const onHover = await orbitProbe();
  const shot = path.resolve(__dirname, 'proof-orbs-noorbit.png'); await page.screenshot({ path: shot, clip: { x: 0, y: 0, width: 900, height: 420 } });
  console.log(JSON.stringify({ errs, rest, atRest, hov, onHover, shot }, null, 1));
  await b.close();
})();
