// Probe: top input bar key behavior + voice-cluster geometry at 1456x914.
// Run: PW=~/.hermes/hermes-agent/node_modules/playwright node scripts/probe-keys.js [shot.png]
const { chromium } = require(process.env.PW);
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1456, height: 914 } });
  const errs = [];
  pg.on('pageerror', e => errs.push('pageerror: ' + e.message));
  pg.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
  await pg.goto('file://' + path.resolve(__dirname, '..', 'vault-live.html'));
  await pg.waitForTimeout(700);
  // stub send + count submits
  await pg.evaluate(() => {
    window.__submits = 0;
    const orig = window.fetch;
    window.fetch = (u, o) => { if (String(u).includes('/ask')) { window.__submits++; return Promise.resolve({ ok: true, json: async () => ({}) }); } return orig(u, o); };
  });
  // summon strip and focus hidden input
  await pg.mouse.move(600, 4); await pg.waitForTimeout(250);
  await pg.evaluate(() => { document.getElementById('topstrip').classList.add('on'); document.getElementById('senterHiddenInput').focus(); });
  const hid = '#senterHiddenInput';
  await pg.keyboard.type('ab'); await pg.waitForTimeout(60);
  const v0 = await pg.$eval(hid, e => e.value);
  // simulate focus stolen by a glyph/pill click (the real-world path): blur, then Backspace must still reach the field
  await pg.evaluate(() => document.getElementById('senterHiddenInput').blur());
  await pg.keyboard.press('Backspace'); await pg.waitForTimeout(60);
  const v1 = await pg.$eval(hid, e => e.value);
  await pg.keyboard.press('Shift+Enter'); await pg.waitForTimeout(120);
  const v2 = await pg.$eval(hid, e => e.value);
  const s2 = await pg.evaluate(() => window.__submits);
  await pg.keyboard.type('cd'); await pg.waitForTimeout(60);
  await pg.keyboard.press('Shift+Enter'); await pg.keyboard.type('ef'); await pg.keyboard.press('Shift+Enter'); await pg.keyboard.type('gh'); await pg.keyboard.press('Shift+Enter'); await pg.keyboard.type('ij'); await pg.waitForTimeout(120);
  const geo = await pg.evaluate(() => {
    const r = document.getElementById('senterText').getBoundingClientRect();
    const ov = document.getElementById('senterOverline').getBoundingClientRect();
    const h = document.getElementById('senterHiddenInput');
    return { textH: Math.round(r.height), textTop: Math.round(r.top), overlineY: Math.round(ov.top), lines: h.value.split('\n').length, scrollH: document.getElementById('senterText').scrollHeight, inH: getComputedStyle(document.getElementById('topstrip')).getPropertyValue('--inH').trim(), navTabTop: Math.round(document.querySelector('#topnav .navtab').getBoundingClientRect().top), text: document.getElementById('senterText').textContent };
  });
  // cluster geometry
  const cl = await pg.evaluate(() => {
    const g = [...document.querySelectorAll('#composerRight .csq .lucide svg')].map(s => s.getBoundingClientRect());
    const c = g.map(r => Math.round((r.left + r.right) / 2));
    const prev = document.getElementById('mPrev').getBoundingClientRect();
    return { centers: c, span: c[3] - c[0], step: Math.round((c[3] - c[0]) / 3), mid: Math.round((c[0] + c[3]) / 2), prevLeft: Math.round(prev.left), sizes: g.map(r => Math.round(r.width)), tops: g.map(r => Math.round(r.top)) };
  });
  const shot = process.argv[2];
  if (shot) await pg.screenshot({ path: shot });
  await pg.keyboard.press('Enter'); await pg.waitForTimeout(200);
  const s3 = await pg.evaluate(() => window.__submits);
  const v3 = await pg.$eval(hid, e => e.value);
  console.log(JSON.stringify({ afterType: v0, afterBackspace: v1, afterShiftEnter: JSON.stringify(v2), submitsAfterShiftEnter: s2, geo, submitsAfterEnter: s3, valueAfterEnter: v3, cluster: cl, errs }, null, 1));
  await b.close();
})();
