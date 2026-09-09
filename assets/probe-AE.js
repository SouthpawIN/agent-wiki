// AE/AB probe: media controls row (‹‹ ▸ ››) + ⚙ vertical centers vs the nav tab titles' cap-height center; AB artist gap; R2 re-assert.
// Usage: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-AE.js [WxH] [shot.png]
// Prints DOM bboxes (JSON) — the true cap-height center is then pixel-scanned from the shot by assets/scan-AE.py (ink rows of a non-active tab).
// Shot = full-frame capture with a horizontal gold guide through the tab-title cap center (+ R2's two vertical guides).
const {chromium}=require(process.env.PW||'playwright'); const path=require('path'); const fs=require('fs');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number); const shot=process.argv[3]; const guideY=process.argv[4]?Number(process.argv[4]):null;
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500);
 await p.mouse.move(300,30); await p.waitForTimeout(400);
 const g=await p.evaluate(()=>{ const R=v=>Math.round(v*10)/10; const rr=el=>{const r=el.getBoundingClientRect(); return {l:R(r.left),t:R(r.top),r:R(r.right),b:R(r.bottom),cy:R((r.top+r.bottom)/2),cx:R((r.left+r.right)/2)};};
   const ink=el=>{ const rg=document.createRange(); rg.selectNodeContents(el); const r=rg.getBoundingClientRect(); return {l:R(r.left),t:R(r.top),r:R(r.right),b:R(r.bottom),cy:R((r.top+r.bottom)/2)}; };
   const tabs=[...document.querySelectorAll('#topnav .navtab[data-view]')].map(t=>({v:t.dataset.view,on:t.classList.contains('on'),box:rr(t),ink:ink(t),fs:getComputedStyle(t).fontSize}));
   const ctl=document.getElementById('mCtl'), play=document.getElementById('mPlay'), prev=document.getElementById('mPrev'), next=document.querySelector('#mCtl .mbtn[data-m=next]');
   const gear=document.getElementById('navSettings'); const title=document.getElementById('mTitle'); const media=document.getElementById('media'); const cl=document.getElementById('composerRight');
   const gl=[...document.querySelectorAll('#composerRight .csq:not(#composerStop) .lucide svg')].map(e=>e.getBoundingClientRect());
   const gearInk=ink(gear);
   return { vw:innerWidth, vh:innerHeight, strip:rr(document.getElementById('topstrip')), stripOn:document.getElementById('topstrip').classList.contains('on'), nav:rr(document.getElementById('topnav')),
     tabs, ctl:rr(ctl), play:rr(play), prev:rr(prev), prevInk:ink(prev), next:rr(next), gearBox:rr(gear), gearInk, gearTransform:getComputedStyle(gear).transform, playTransform:getComputedStyle(play).transform,
     media:rr(media), mTitle:rr(title), mTitleInk:ink(title), artistGap:R(title.getBoundingClientRect().top - play.getBoundingClientRect().bottom),
     cluster:rr(cl), inkLeft:R(Math.min(...gl.map(r=>r.left))), inkRight:R(Math.max(...gl.map(r=>r.right))), overlineY:R(document.getElementById('senterOverline').getBoundingClientRect().top),
     r2:{ dLeft:R(cl.getBoundingClientRect().left-prev.getBoundingClientRect().left), dRight:R(cl.getBoundingClientRect().right-gearInk.r) } }; });
 console.log(JSON.stringify(g,null,1)); console.log('errors:',errs.length, errs.slice(0,3));
 if(shot){ await p.evaluate((gy)=>{ const prev=document.getElementById('mPrev').getBoundingClientRect(); const ge=document.getElementById('navSettings'); const rg=document.createRange(); rg.selectNodeContents(ge); const gg=rg.getBoundingClientRect(); const ol=document.getElementById('senterOverline').getBoundingClientRect();
   if(gy!=null){ for(const x of [prev.left,gg.right]){ const d=document.createElement('div'); d.style.cssText=`position:fixed;top:0;height:${Math.round(ol.top)+110}px;left:${x-0.5}px;width:1px;background:#FFE45A;z-index:999;pointer-events:none;opacity:.55`; document.body.appendChild(d);} 
     const h=document.createElement('div'); h.style.cssText=`position:fixed;left:0;right:0;top:${gy-0.5}px;height:1px;background:#FFE45A;z-index:999;pointer-events:none`; document.body.appendChild(h); } }, guideY);
   await p.screenshot({path:shot}); console.log('shot',shot); }
 await b.close();
})().catch(e=>{ console.error(e); process.exit(2); });
