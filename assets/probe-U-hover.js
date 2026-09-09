// U real-hover shot: hover ONE voice glyph (dictate) so exactly its caption shows — the actual UX (captions are one-at-a-time).
const {chromium}=require(process.env.PW||'playwright'); const path=require('path');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const shot=process.argv[2]||'assets/look/U-hover-dictate-1456x914.png';
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1456,height:914}});
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500);
 await p.mouse.move(300,30); await p.waitForTimeout(400);
 const c=await p.evaluate(()=>{ const r=document.querySelector('#composerRight .csq[data-k=dictate]').getBoundingClientRect(); return {x:r.left+r.width/2,y:r.top+r.height/2}; });
 await p.mouse.move(c.x,c.y); await p.waitForTimeout(300);
 const vis=await p.evaluate(()=>[...document.querySelectorAll('#composerRow .csq:not(#composerStop) .cap')].map(e=>({t:e.textContent,op:getComputedStyle(e).opacity})));
 console.log(JSON.stringify(vis));
 await p.screenshot({path:shot}); console.log('shot',shot); await b.close();
})().catch(e=>{ console.error(e); process.exit(2); });
