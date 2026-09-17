// Smoke: load vault-live.html headless at 1151x834, collect page errors / console errors, count wiki rows.
const pw = require(process.env.PW || '/Users/sovthpaw/.hermes/hermes-agent/node_modules/playwright');
(async () => {
  const b = await pw.chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1151, height: 834 }, deviceScaleFactor: 2 });
  const errs = [], cons = [];
  pg.on('pageerror', e => errs.push(String(e.message).slice(0, 200)));
  pg.on('console', m => { if (m.type() === 'error') cons.push(m.text().slice(0, 200)); });
  await pg.goto('file:///Users/sovthpaw/Documents/Projects/Projects/vault-live.html');
  await pg.waitForTimeout(2500);
  const r = await pg.evaluate(() => ({
    rows: document.querySelectorAll('#view-wiki .topic').length,
    hero: !!document.querySelector('#hero'),
    orbcol: getComputedStyle(document.querySelector('#view-wiki')).getPropertyValue('--orbcol'),
    rowcap: getComputedStyle(document.querySelector('#view-wiki')).getPropertyValue('--rowcap'),
    deadLeft: window.__deadLeft, figFrac: window.__figFrac,
    runInd: !!document.querySelector('#runInd'), topstrip: !!document.querySelector('#topstrip'),
    navtabs: [...document.querySelectorAll('.navtab')].map(n => n.textContent.trim()),
  }));
  console.log(JSON.stringify({ pageErrors: errs, consoleErrors: cons.slice(0, 8), ...r }, null, 1));
  const day = process.argv[2] || new Date().toISOString().slice(0, 10);
  await pg.screenshot({ path: '/Users/sovthpaw/Documents/Projects/Projects/assets/look/verify-nightly-' + day + '-rest-1151x834.png' });
  await b.close();
})();
