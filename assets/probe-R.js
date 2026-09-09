// R probe: voice cluster geometry vs #media.left / ⚙.right / overline. Usage: PW=... node assets/probe-R.js [WxH] [shot.png]
const {chromium}=require(process.env.PW||'playwright'); const path=require('path');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number); const shot=process.argv[3];
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500);
 await p.mouse.move(300,30); await p.waitForTimeout(300);
 const g=await p.evaluate(()=>{ const q=s=>document.querySelector(s).getBoundingClientRect(); const R=Math.round;
   const cl=q('#composerRight'), m=q('#media'), gear=q('#navSettings'), ol=q('#senterOverline'), row=q('#composerRow');
   const gl=[...document.querySelectorAll('#composerRight .csq:not(#composerStop) .lucide svg')].map(e=>e.getBoundingClientRect());
   const btns=[...document.querySelectorAll('#composerRight .csq:not(#composerStop)')].map(b=>{ const c=b.querySelector('.cap'); c.style.opacity='1'; const t=R(c.getBoundingClientRect().top); c.style.opacity=''; return {k:b.dataset.k, btnBottom:R(b.getBoundingClientRect().bottom), capTop:t}; });
   const plusCap=(()=>{ const c=document.querySelector('.csq[data-k=context] .cap'); c.style.opacity='1'; const t=R(c.getBoundingClientRect().top); c.style.opacity=''; return t; })();
   return {vw:innerWidth, overlineY:R(ol.top), overlineBottom:R(ol.bottom), rowTop:R(row.top), rowH:R(row.height), rowBottom:R(row.bottom),
     inkLeft:R(Math.min(...gl.map(r=>r.left))), inkRight:R(Math.max(...gl.map(r=>r.right))), clusterLeft:R(cl.left), clusterRight:R(cl.right), clusterW:R(cl.width),
     mediaLeft:R(m.left), gearRight:R(gear.right), glyphBottom:R(Math.max(...gl.map(r=>r.bottom))), glyphTop:R(Math.min(...gl.map(r=>r.top))), glyphW:R(gl[0].width),
     steps:gl.slice(1).map((r,i)=>R(r.left-gl[i].left)), btns, plusCap,
     checks:{ leftOK: Math.min(...gl.map(r=>r.left))>=m.left+4, rightOK: Math.max(...gl.map(r=>r.right))<=gear.right-4, liftOK: Math.max(...gl.map(r=>r.bottom))<=ol.top-6 } }; });
 console.log(JSON.stringify(g,null,1)); console.log('errors:',errs.length, errs.slice(0,3));
 if(shot){ await p.evaluate(()=>{ const m=document.getElementById('media').getBoundingClientRect(), g=document.getElementById('navSettings').getBoundingClientRect(), ol=document.getElementById('senterOverline').getBoundingClientRect(); for(const x of [m.left,g.right]){ const d=document.createElement('div'); d.style.cssText=`position:fixed;top:0;height:120px;left:${x-0.5}px;width:1px;background:#FFE45A;z-index:999;pointer-events:none`; document.body.appendChild(d);} const o=document.createElement('div'); o.style.cssText=`position:fixed;left:0;right:0;top:${ol.top}px;height:1px;background:#FFE45A;opacity:.6;z-index:999;pointer-events:none`; document.body.appendChild(o); });
   await p.screenshot({path:shot, clip:{x:Math.max(0,g.mediaLeft-140), y:0, width:Math.min(W-Math.max(0,g.mediaLeft-140), 560), height:150}}); console.log('shot',shot); }
 await b.close();
})().catch(e=>{ console.error(e); process.exit(2); });
