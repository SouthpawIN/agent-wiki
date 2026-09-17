// AF probe: media widget x vs last nav title; ⚙ flush right; voice cluster anchors; AB gap; AE centers. Optional shot with THREE guides (tab cap centerline, #mPrev.left, ⚙ ink right).
// Usage: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-AF.js [WxH] [shot.png]
const {chromium}=require(process.env.PW||'playwright'); const path=require('path');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number); const shot=process.argv[3];
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500);
 await p.mouse.move(900,6); await p.waitForTimeout(400);
 const g=await p.evaluate(()=>{ const R=v=>Math.round(v*10)/10; const rc=el=>{ const rg=document.createRange(); rg.selectNodeContents(el); return rg.getBoundingClientRect(); };
   const tabs=[...document.querySelectorAll('#topnav .navtab[data-view]')]; const last=tabs[tabs.length-1]; const lastInk=rc(last); const lastBox=last.getBoundingClientRect();
   const plus=document.getElementById('navPlus'); const plusR=plus&&plus.offsetParent?plus.getBoundingClientRect().right:0;
   const navRight=Math.max(lastInk.right, plusR); // last title ink right (or the + if it trails the last tab)
   const m=document.getElementById('media').getBoundingClientRect(); const gear=document.getElementById('navSettings'); const gb=gear.getBoundingClientRect(); const gg=rc(gear);
   const prev=document.getElementById('mPrev').getBoundingClientRect(); const cl=document.getElementById('composerRight').getBoundingClientRect();
   const gl=[...document.querySelectorAll('#composerRight .csq:not(#composerStop) .lucide svg')].map(e=>e.getBoundingClientRect());
   const steps=gl.slice(1).map((r,i)=>R(r.left-gl[i].left)); const ol=document.getElementById('senterOverline').getBoundingClientRect();
   const tab=document.querySelector('#topnav .navtab[data-view="feed"]'); const cs=getComputedStyle(tab); const tr=rc(tab); const c=document.createElement('canvas').getContext('2d'); c.font=`${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`; const mm=c.measureText(tab.textContent.trim()); const h=c.measureText('H'); const cap=tr.top+mm.fontBoundingBoxAscent-h.actualBoundingBoxAscent/2;
   const play=document.getElementById('mPlay').getBoundingClientRect(); const rgT=rc(document.getElementById('mTitle'));
   return {vw:innerWidth, lastTab:last.textContent.trim(), lastInkRight:R(lastInk.right), lastBoxRight:R(lastBox.right), plusRight:R(plusR), navRight:R(navRight),
     mediaLeft:R(m.left), mediaRight:R(m.right), clear:R(m.left-navRight), gearBoxRight:R(gb.right), gearInkRight:R(gg.right), gearFlush:R(innerWidth-gb.right),
     prevLeft:R(prev.left), clusterLeft:R(cl.left), clusterRight:R(cl.right), dL:R(cl.left-prev.left), dR:R(cl.right-gg.right), steps, glyphW:R(gl[0].width), glyphBottom:R(Math.max(...gl.map(r=>r.bottom))), overlineTop:R(ol.top),
     cap:R(cap), dPlay:R((play.top+play.bottom)/2-cap), dPrev:R((rc(document.getElementById('mPrev')).top+rc(document.getElementById('mPrev')).bottom)/2-cap), dGear:R((gg.top+gg.bottom)/2-cap), artistGap:R(rgT.top-play.bottom),
     caps:[...document.querySelectorAll('#composerRight .csq:not(#composerStop) .cap')].map(e=>e.textContent)}; });
 console.log(JSON.stringify(g,null,1)); console.log('errors:',errs.length, errs.slice(0,3));
 if(shot){ await p.evaluate((cap)=>{ const prev=document.getElementById('mPrev').getBoundingClientRect(); const ge=document.getElementById('navSettings'); const rg=document.createRange(); rg.selectNodeContents(ge); const gg=rg.getBoundingClientRect();
   const mk=css=>{ const d=document.createElement('div'); d.style.cssText='position:fixed;background:#FFE45A;z-index:999;pointer-events:none;'+css; document.body.appendChild(d); };
   mk(`top:${cap-0.5}px;height:1px;left:0;width:${innerWidth}px`); mk(`top:0;height:300px;left:${prev.left-0.5}px;width:1px`); mk(`top:0;height:300px;left:${gg.right-0.5}px;width:1px`); }, g.cap);
   await p.screenshot({path:shot}); console.log('shot',shot); }
 await b.close();
})().catch(e=>{ console.error(e); process.exit(2); });
