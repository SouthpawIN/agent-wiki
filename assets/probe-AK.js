// AK probe: collapsed fleet-stream pills vs the wall figure's face. Measures #chat .mini .msg bboxes + computed opacity at rest,
// shoots rest + hovered (expanded #stream) frames. Usage: PW=… node assets/probe-AK.js [WxH] [prefix]
const {chromium}=require(process.env.PW||'playwright'); const path=require('path');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number); const pre=process.argv[3]||'/tmp/AK';
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500);
 await p.mouse.move(300,500); await p.waitForTimeout(600);
 const g=await p.evaluate(()=>{ const R=v=>Math.round(v*10)/10;
   const pills=[...document.querySelectorAll('#chat .mini .msg')].map(m=>{ const r=m.getBoundingClientRect(); const cs=getComputedStyle(m); return {x:R(r.left),y:R(r.top),w:R(r.width),h:R(r.height),op:cs.opacity,bg:cs.backgroundColor,txt:getComputedStyle(m.querySelector('.txt')).color}; });
   const mini=document.querySelector('#chat .mini').getBoundingClientRect(); const wall=document.getElementById('wallBackdrop');
   return {vw:innerWidth,vh:innerHeight,pills,mini:{x:R(mini.left),y:R(mini.top),w:R(mini.width),h:R(mini.height)},wallOn:wall&&wall.classList.contains('on'),wallOp:wall&&getComputedStyle(wall).opacity}; });
 console.log(JSON.stringify(g,null,1)); console.log('errors:',errs.length,errs.slice(0,3));
 await p.screenshot({path:pre+'-rest.png'});
 // wall only (hide UI) to locate the face
 await p.evaluate(()=>{ document.querySelectorAll('body > *:not(#wallBackdrop)').forEach(e=>e.style.visibility='hidden'); });
 await p.screenshot({path:pre+'-wall.png'});
 await p.evaluate(()=>{ document.querySelectorAll('body > *').forEach(e=>e.style.visibility=''); });
 // hovered → expanded stream
 const pill=g.pills[g.pills.length-1]; await p.mouse.move(pill.x+pill.w/2, pill.y+pill.h/2, {steps:8}); await p.waitForTimeout(900);
 const open=await p.evaluate(()=>{ const c=document.getElementById('chat'); const s=document.getElementById('stream'); const r=s.getBoundingClientRect(); const first=s.querySelector('.msg'); const fr=first?first.getBoundingClientRect():null; return {open:c.classList.contains('open'),stream:{x:r.left,y:r.top,w:r.width,h:r.height},msgs:s.querectorAll?0:s.querySelectorAll('.msg').length,firstOp:first?getComputedStyle(first).opacity:null,firstW:fr&&fr.width}; });
 console.log('OPEN',JSON.stringify(open)); await p.screenshot({path:pre+'-open.png'});
 await b.close();
})();
