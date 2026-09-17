// quick check: canvas cap-height center for a .navtab vs pixel scan (108 @ all widths)
const {chromium}=require(process.env.PW||'playwright'); const path=require('path');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1456,height:914}});
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500); await p.mouse.move(300,30); await p.waitForTimeout(400);
 console.log(JSON.stringify(await p.evaluate(()=>{ const tab=document.querySelector('#topnav .navtab[data-view="feed"]'); const cs=getComputedStyle(tab); const rg=document.createRange(); rg.selectNodeContents(tab); const r=rg.getBoundingClientRect();
   const c=document.createElement('canvas').getContext('2d'); c.font=`${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`; const m=c.measureText('FEED'); const mH=c.measureText('H');
   const baseline=r.top+m.fontBoundingBoxAscent; const capTop=baseline-mH.actualBoundingBoxAscent; const capBottom=baseline+mH.actualBoundingBoxDescent;
   return {font:c.font, rTop:r.top, rBottom:r.bottom, rH:r.height, fbA:m.fontBoundingBoxAscent, fbD:m.fontBoundingBoxDescent, capAsc:mH.actualBoundingBoxAscent, capDesc:mH.actualBoundingBoxDescent, baseline, capTop, capBottom, capCenter:(capTop+capBottom)/2, lineHeight:cs.lineHeight}; })));
 await b.close(); })();
