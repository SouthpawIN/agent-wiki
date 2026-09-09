// AJ: byte-diff two 1456x914 PNGs — used to prove the stream (WIKI) shot is pixel-identical before/after the FEED-only fade change.
// Run: node assets/png-diff.js a.png b.png
const { PNG } = require('/Users/sovthpaw/.hermes/hermes-agent/node_modules/pngjs');
const fs = require('fs');
const [a, b] = process.argv.slice(2).map(p => PNG.sync.read(fs.readFileSync(p)));
let diff = 0, band = { top: 0, bottom: 0 };
for (let y = 0; y < a.height; y++) for (let x = 0; x < a.width; x++) {
  const i = (y * a.width + x) * 4;
  if (a.data[i] !== b.data[i] || a.data[i + 1] !== b.data[i + 1] || a.data[i + 2] !== b.data[i + 2]) { diff++; if (y < a.height / 2) band.top++; else band.bottom++; }
}
console.log(JSON.stringify({ w: a.width, h: a.height, diffPx: diff, ...band }));
