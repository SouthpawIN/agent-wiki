// AB probe: media controls row vs artist lettering — gap between the (▸) circle's ink bottom and the #mTitle ink top, plus every neighbour that must NOT move (skips, #mCtl, #mNow, #media box, gear, tabs, cluster vs #mPrev — the R2 anchor).
// Usage: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-AB.js [WxH] [shot.png]
// Shot = full-frame capture with two gold guide lines: play.bottom and #mTitle ink top (the ≥8px band Chris asked for), plus a 3× crop of the widget.
const {chromium}=require(process.env.PW||'playwright'); const path=require('path');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number); const shot=process.argv[3];
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500);
 await p.mouse.move(300,30); await p.waitForTimeout(400);
 const g=await p.evaluate(()=>{ const q=s=>document.querySelector(s).getBoundingClientRect(); const R=v=>Math.round(v*10)/10;
   const play=q('#media .mbtn.play'), prev=q('#mPrev'), ctl=q('#mCtl'), now=q('#mNow'), media=q('#media'), title=q('#mTitle'), sub=q('#mSub'), gear=q('#navSettings'), tab=q('.navtab[data-view]'), cl=q('#composerRight');
   const rg=document.createRange(); rg.selectNodeContents(document.getElementById('mTitle')); const ink=rg.getBoundingClientRect();
   const ge=document.getElementById('navSettings'); const rg2=document.createRange(); rg2.selectNodeContents(ge); const gg=rg2.getBoundingClientRect();
   const cs=getComputedStyle(document.querySelector('#media .mbtn.play')), csCtl=getComputedStyle(document.getElementById('mCtl')), csT=getComputedStyle(document.getElementById('mTitle')), csNow=getComputedStyle(document.getElementById('mNow'));
   return {vw:innerWidth, gapPlayToInk:R(ink.top-play.bottom), play:[R(play.top),R(play.bottom)], prev:[R(prev.top),R(prev.bottom),R(prev.left)], ctl:[R(ctl.top),R(ctl.bottom)], now:[R(now.top),R(now.bottom)], titleBox:[R(title.top),R(title.bottom)], titleInk:[R(ink.top),R(ink.bottom)], sub:[R(sub.top),R(sub.bottom)], media:[R(media.top),R(media.bottom),R(media.left),R(media.right)], gear:[R(gear.top),R(gear.bottom)], tab:[R(tab.top),R(tab.bottom)],
     clusterLeft:R(cl.left), dLeft_R2:R(cl.left-prev.left), dRight_R2:R(cl.right-gg.right),
     css:{playTransform:cs.transform, ctlMarginBottom:csCtl.marginBottom, ctlPaddingBottom:csCtl.paddingBottom, titleLineHeight:csT.lineHeight, titleFontSize:csT.fontSize, titleMarginTop:csT.marginTop, nowMarginTop:csNow.marginTop, nowPaddingTop:csNow.paddingTop, mediaGap:getComputedStyle(document.getElementById('media')).gap} }; });
 console.log(JSON.stringify(g,null,1)); console.log('errors:',errs.length, errs.slice(0,3));
 if(shot){ await p.evaluate(()=>{ const play=document.querySelector('#media .mbtn.play').getBoundingClientRect(); const rg=document.createRange(); rg.selectNodeContents(document.getElementById('mTitle')); const ink=rg.getBoundingClientRect(); const m=document.getElementById('media').getBoundingClientRect();
   for(const y of [play.bottom,ink.top]){ const d=document.createElement('div'); d.style.cssText=`position:fixed;left:${Math.round(m.left)-40}px;width:${Math.round(m.width)+80}px;top:${y-0.5}px;height:1px;background:#FFE45A;z-index:999;pointer-events:none`; document.body.appendChild(d);} });
   await p.screenshot({path:shot}); const m=g.media; await p.screenshot({path:shot.replace('.png','-crop3x.png'), clip:{x:m[2]-40,y:Math.max(0,m[0]-20),width:(m[3]-m[2])+80,height:(m[1]-m[0])+40}}); console.log('shot',shot); }
 await b.close();
})().catch(e=>{ console.error(e); process.exit(2); });
