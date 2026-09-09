// U probe: input-row hover captions (.cap under +, auto, dictate, voice, read, wake) vs the orb caption (.orb::before) on wiki rows.
// Usage: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-U.js [WxH] [shot.png]
// Prints rendered font-size (px) of both caption kinds, cap top vs overline, and — with a shot path — a full-frame capture with ALL SIX labels forced visible.
const {chromium}=require(process.env.PW||'playwright'); const path=require('path');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number); const shot=process.argv[3];
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500);
 // 1) orb caption: hover the first wiki row + its first orb so .thead:hover .orb:hover::before is live
 const orb=await p.evaluate(()=>{ const o=document.querySelector('#view-wiki .topic .thead .orb'); const r=o.getBoundingClientRect(); return {x:r.left+r.width/2, y:r.top+r.height/2}; });
 await p.mouse.move(orb.x, orb.y); await p.waitForTimeout(450);
 const orbCap=await p.evaluate(()=>{ const o=document.querySelector('#view-wiki .topic .thead:hover .orb:hover')||document.querySelector('#view-wiki .topic .thead .orb'); const cs=getComputedStyle(o,'::before'); return {fontPx:parseFloat(cs.fontSize), letter:cs.letterSpacing, opacity:cs.opacity, family:cs.fontFamily, orbFontPx:parseFloat(getComputedStyle(o).fontSize)}; });
 // 2) input-row captions: open the strip, force all six visible, measure
 await p.mouse.move(300,400); await p.waitForTimeout(300); await p.mouse.move(300,30); await p.waitForTimeout(400);
 const caps=await p.evaluate(()=>{ const ol=document.getElementById('senterOverline').getBoundingClientRect(); const R=Math.round;
   return {olTop:R(ol.top), olBottom:R(ol.bottom), caps:[...document.querySelectorAll('#composerRow .csq:not(#composerStop)')].map(bt=>{ const c=bt.querySelector('.cap'); c.style.opacity='1'; const r=c.getBoundingClientRect(); const cs=getComputedStyle(c); c.style.opacity=''; return {k:bt.dataset.k||bt.className, text:c.textContent, fontPx:+parseFloat(cs.fontSize).toFixed(2), top:R(r.top), h:R(r.height), l:R(r.left), r:R(r.right), w:R(r.width), btnBottom:R(bt.getBoundingClientRect().bottom)}; })}; });
 const minPx=Math.min(...caps.caps.map(c=>c.fontPx));
 const out={vw:innerWidthSafe(W), orbCaption:orbCap, inputCaptions:caps,
   checks:{ capsGE13: minPx>=13, capsMatchOrb: Math.abs(minPx-orbCap.fontPx)<=0.6, capsBelowLine5: caps.caps.every(c=>c.top>=caps.olBottom+2), oneRow: new Set(caps.caps.map(c=>c.top)).size===1, noOverlap: noOverlap(caps.caps) }};
 console.log(JSON.stringify(out,null,1)); console.log('errors:',errs.length, errs.slice(0,3));
 if(shot){ await p.evaluate(()=>{ document.querySelectorAll('#composerRow .csq:not(#composerStop) .cap').forEach(c=>{ c.style.opacity='1'; c.style.color='#fff'; }); });
   await p.waitForTimeout(150); await p.screenshot({path:shot}); console.log('shot',shot); }
 await b.close();
 function innerWidthSafe(w){ return w; }
 function noOverlap(cs){ const s=[...cs].sort((a,b)=>a.l-b.l); for(let i=1;i<s.length;i++){ if(s[i].l < s[i-1].r+4) return false; } return true; }
})().catch(e=>{ console.error(e); process.exit(2); });
