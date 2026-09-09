// R2 probe: voice cluster edges vs Chris's EXACT reference points — #mPrev (‹‹ hitbox) LEFT edge and the ⚙ glyph's VISIBLE right edge (text Range, not the .navtab box).
// Usage: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-R2.js [WxH] [shot.png]
// Shot = full 1456×914 capture with two gold guide lines at prev.left / gearGlyph.right (the proof Chris asked for) — cluster must sit inside them.
const {chromium}=require(process.env.PW||'playwright'); const path=require('path');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number); const shot=process.argv[3];
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500);
 await p.mouse.move(300,30); await p.waitForTimeout(400);
 const g=await p.evaluate(()=>{ const q=s=>document.querySelector(s).getBoundingClientRect(); const R=Math.round;
   const cl=q('#composerRight'), m=q('#media'), prev=q('#mPrev'), gearBox=q('#navSettings'), ol=q('#senterOverline'), row=q('#composerRow');
   const gearEl=document.getElementById('navSettings'); const rg=document.createRange(); rg.selectNodeContents(gearEl); const gg=rg.getBoundingClientRect();
   const gl=[...document.querySelectorAll('#composerRight .csq:not(#composerStop) .lucide svg')].map(e=>e.getBoundingClientRect());
   const inkL=Math.min(...gl.map(r=>r.left)), inkR=Math.max(...gl.map(r=>r.right));
   return {vw:innerWidth, overlineY:R(ol.top), rowTop:R(row.top), rowH:R(row.height),
     clusterLeft:R(cl.left), clusterRight:R(cl.right), inkLeft:R(inkL), inkRight:R(inkR),
     mediaLeft:R(m.left), prevLeft:R(prev.left), prevRight:R(prev.right), gearBoxRight:R(gearBox.right), gearGlyphRight:R(gg.right), gearGlyphLeft:R(gg.left),
     glyphBottom:R(Math.max(...gl.map(r=>r.bottom))), glyphW:R(gl[0].width), steps:gl.slice(1).map((r,i)=>R(r.left-gl[i].left)),
     dLeft:R(cl.left-prev.left), dRight:R(cl.right-gg.right),
     checks:{ leftOK: Math.abs(cl.left-prev.left)<=2, rightOK: Math.abs(cl.right-gg.right)<=2, liftOK: Math.max(...gl.map(r=>r.bottom))<=ol.top-6, sizeOK: R(gl[0].width)===26 } }; });
 console.log(JSON.stringify(g,null,1)); console.log('errors:',errs.length, errs.slice(0,3));
 if(shot){ await p.evaluate(()=>{ const prev=document.getElementById('mPrev').getBoundingClientRect(); const ge=document.getElementById('navSettings'); const rg=document.createRange(); rg.selectNodeContents(ge); const gg=rg.getBoundingClientRect(); const ol=document.getElementById('senterOverline').getBoundingClientRect();
   for(const x of [prev.left,gg.right]){ const d=document.createElement('div'); d.style.cssText=`position:fixed;top:0;height:${Math.round(ol.top)+110}px;left:${x-0.5}px;width:1px;background:#FFE45A;z-index:999;pointer-events:none`; document.body.appendChild(d);} });
   await p.screenshot({path:shot}); console.log('shot',shot); }
 await b.close();
})().catch(e=>{ console.error(e); process.exit(2); });
