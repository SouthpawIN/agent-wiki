// Smoke variant: same as probe-smoke.js but Chromium launched with --allow-file-access-from-files
// so CSS mask-image:url(file://…) is not CORS-blocked (mirrors the Electron webview, which allows it).
// Usage: node assets/probe-smoke-mask.js [day]
const pw = require(process.env.PW || '/Users/sovthpaw/.hermes/hermes-agent/node_modules/playwright');
(async () => {
  const b = await pw.chromium.launch({ args: ['--allow-file-access-from-files'] });
  const pg = await b.newPage({ viewport: { width: 1151, height: 834 }, deviceScaleFactor: 2 });
  const errs = [], cons = [];
  pg.on('pageerror', e => errs.push(String(e.message).slice(0, 200)));
  pg.on('console', m => { if (m.type() === 'error') cons.push(m.text().slice(0, 200)); });
  await pg.goto('file:///Users/sovthpaw/Documents/Projects/Projects/vault-live.html');
  await pg.waitForTimeout(3000);
  const r = await pg.evaluate(() => {
    const bd = document.querySelector('#wallBackdrop');
    return {
      rows: document.querySelectorAll('#view-wiki .topic').length,
      wallOn: bd && bd.classList.contains('on'), wallAsset: bd && bd.dataset.asset,
      wallOpacity: bd && getComputedStyle(bd).opacity,
      wallImg: bd && getComputedStyle(bd).getPropertyValue('--wallImg').slice(0, 80),
      figFrac: window.__figFrac, figSample: window.__figSample && window.__figSample.from,
      deadLeft: window.__deadLeft,
    };
  });
  console.log(JSON.stringify({ pageErrors: errs, consoleErrors: cons.slice(0, 8), ...r }, null, 1));
  const day = process.argv[2] || new Date().toISOString().slice(0, 10);
  await pg.screenshot({ path: '/Users/sovthpaw/Documents/Projects/Projects/assets/look/verify-nightly-' + day + '-rest-mask-1151x834.png' });
  await b.close();
})();
