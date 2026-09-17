// Ledger diagnostics: run verify-wiki.js with a recording must(), then for each FAILING
// assertion list the individual regex literals on its source line and whether each hits.
// Usage: node assets/diag-ledger.js
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'vault-live.html'), 'utf8');
let src = fs.readFileSync(path.join(__dirname, 'verify-wiki.js'), 'utf8');
const rec = [];
src = src.replace(/const must = [^\n]*\n/, 'const must = (cond, msg) => { rec.push([!!cond, msg]); };\n')
         .replace(/^if \(fails\.length\)[\s\S]*$/m, '')
         .replace(/^console\.log\('verify-wiki OK[^\n]*\n/m, '');
new Function('require', '__dirname', 'rec', src)(require, __dirname, rec);
const lines = fs.readFileSync(path.join(__dirname, 'verify-wiki.js'), 'utf8').split('\n');
function regexes(line) {
  const out = []; let cls = false;
  for (let a = 0; a < line.length; a++) {
    if (line[a] === '/' && /[\(\s!&|,]/.test(line[a - 1] || '(') && line[a + 1] !== '/' && line[a + 1] !== '*') {
      let b = a + 1; cls = false;
      for (; b < line.length; b++) {
        if (line[b] === '\\') { b++; continue; }
        if (line[b] === '[') cls = true; else if (line[b] === ']') cls = false;
        else if (line[b] === '/' && !cls) break;
      }
      let flags = ''; let c = b + 1; while (/[gimsuy]/.test(line[c] || '')) flags += line[c++];
      out.push([line.slice(a + 1, b), flags]); a = c - 1;
    }
  }
  return out;
}
let pass = 0, fail = 0;
for (const [ok, msg] of rec) {
  if (ok) { pass++; continue; }
  fail++;
  console.log('\nFAIL: ' + msg);
  let li = lines.findIndex(l => l.includes(msg.slice(0, 40)));
  let start = li; while (start > 0 && !lines[start].startsWith('must(')) start--;
  const line = li < 0 ? '' : lines.slice(start, li + 1).join(' ');
  for (const [p, f] of regexes(line)) {
    let hit; try { hit = new RegExp(p, f.replace('g', '')).test(html); } catch (e) { hit = 'ERR'; }
    if (hit !== true) console.log('   MISS  /' + p.slice(0, 120) + '/' + f);
  }
}
console.log('\nmust() total ' + rec.length + ' — pass ' + pass + ' / fail ' + fail);
