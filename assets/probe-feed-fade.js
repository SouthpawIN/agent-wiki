// AJ: FEED bottom fade ramp probe — measures #fade height on FEED vs WIKI and shoots FEED (overflowing) + WIKI w/ stream open.
// Run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-feed-fade.js <tag>
const { chromium } = require(process.env.PW);
const path = require('path');
(async () => {
  const tag = process.argv[2] || 'x';
  const file = 'file://' + path.resolve(__dirname, '..', 'vault-live.html');
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1456, height: 914 } });
  const errs = []; pg.on('pageerror', e => errs.push(String(e)));
  await pg.goto(file); await pg.waitForTimeout(900);
  // WIKI: fade height + stream mask
  const wiki = await pg.evaluate(() => ({ fadeH: getComputedStyle(document.getElementById('fade')).height, fadeBg: getComputedStyle(document.getElementById('fade')).backgroundImage, chatMask: getComputedStyle(document.getElementById('chat')).webkitMaskImage || getComputedStyle(document.getElementById('chat')).maskImage }));
  await pg.mouse.move(1300, 850); await pg.waitForTimeout(500);
  await pg.screenshot({ path: path.join(__dirname, 'look', `AJ-wiki-stream-${tag}-1456x914.png`) });
  // FEED: switch, pad posts so it overflows, scroll to middle
  await pg.evaluate(() => { showView('feed'); });
  await pg.waitForTimeout(400);
  const feed = await pg.evaluate(() => {
    const f = document.getElementById('feed'); const posts = [...f.querySelectorAll('.post')];
    let n = posts.length;
    while (f.querySelectorAll('.post').length < 40 && posts.length) { posts.forEach(p => { if (f.querySelectorAll('.post').length < 40) f.appendChild(p.cloneNode(true)); }); }
    const v = document.getElementById('view-feed'); v.scrollTop = 300;
    const fd = document.getElementById('fade'); const cs = getComputedStyle(fd);
    return { postsBefore: n, postsNow: f.querySelectorAll('.post').length, scrollH: v.scrollHeight, fadeH: cs.height, fadeBg: cs.backgroundImage, fadeBottom: fd.getBoundingClientRect().bottom, fadeTop: fd.getBoundingClientRect().top, chatHidden: document.getElementById('chat').classList.contains('hide') };
  });
  await pg.mouse.move(600, 500); await pg.waitForTimeout(300);
  await pg.screenshot({ path: path.join(__dirname, 'look', `AJ-feed-${tag}-1456x914.png`) });
  console.log(JSON.stringify({ wiki, feed, errs }, null, 1));
  await b.close();
})();
