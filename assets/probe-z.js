// Z: dead space above the hero at rest — measure #hero / #heroTitle geometry per view + hit-zone behavior.
// run: PW=~/.hermes/hermes-agent/node_modules/playwright ~/.hermes/node/bin/node assets/probe-z.js [WxH] [shot-prefix]
const path=require('path'); const fs=require('fs');
const pw=require(process.env.PW||path.join(process.env.HOME,'.hermes/hermes-agent/node_modules/playwright'));
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number); const shot=process.argv[3]||'';
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
(async()=>{
  const b=await pw.chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
  const errs=[]; p.on('pageerror',e=>errs.push('pageerror '+e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push('console '+m.text()); });
  await p.goto(FILE); await p.waitForTimeout(3600); await p.mouse.move(700,600); await p.waitForTimeout(300);
  const on=()=>p.evaluate(()=>document.getElementById('topstrip').classList.contains('on'));
  const geo=await p.evaluate(()=>{
    const out={}; const views=['wiki','feed','skills','bots','player'];
    for(const v of views){ const el=document.getElementById('view-'+v); if(!el) continue; const h=el.querySelector('.hero'); const t=h&&h.querySelector('.heroTitle'); if(!h) continue;
      const was=el.classList.contains('on'); const disp=getComputedStyle(el).display;
      if(disp==='none'){ el.style.display='block'; }
      const hr=h.getBoundingClientRect(); const tr=t.getBoundingClientRect(); const rg=document.createRange(); rg.selectNodeContents(t); const ink=rg.getBoundingClientRect();
      out[v]={heroTop:Math.round(hr.top), titleTop:Math.round(tr.top), inkTop:Math.round(ink.top), heroPadTop:getComputedStyle(h).paddingTop, viewPadTop:getComputedStyle(el).paddingTop, lineY:Math.round(h.querySelector('.heroLine').getBoundingClientRect().top)};
      if(disp==='none') el.style.display='';
    }
    const ed=document.getElementById('edHero'); if(ed){ const ev=document.getElementById('view-editor'); const d=getComputedStyle(ev).display; if(d==='none') ev.style.display='block'; out.editor={heroTop:Math.round(ed.getBoundingClientRect().top), heroPadTop:getComputedStyle(ed).paddingTop}; if(d==='none') ev.style.display=''; }
    const s=document.getElementById('topstrip'); const cs=getComputedStyle(s);
    out.strip={position:cs.position, height:cs.height, clip:cs.clipPath, on:s.classList.contains('on')};
    out.bodyPad=getComputedStyle(document.body).paddingTop; out.bodyMargin=getComputedStyle(document.body).marginTop;
    // anything in normal flow above the wiki view?
    const vw=document.getElementById('view-wiki'); out.viewWikiTop=Math.round(vw.getBoundingClientRect().top);
    return out;
  });
  console.log('GEO', JSON.stringify(geo,null,1));
  // hit zone: y=10..60 at x=900 (clear of title text) and over the title text
  const rest=async()=>{ await p.mouse.move(700,600); await p.waitForTimeout(300); };
  const res={};
  for(const y of [10,30,50,60]){ await rest(); await p.mouse.move(900,y); await p.waitForTimeout(250); res['x900y'+y]=await on(); }
  await rest(); const tb=await p.evaluate(()=>{ const rg=document.createRange(); rg.selectNodeContents(document.getElementById('heroTitle')); const r=rg.getBoundingClientRect(); return {x:Math.round(r.left+20), y:Math.round(r.top+r.height/2)}; });
  await p.mouse.move(tb.x,tb.y); await p.waitForTimeout(250); res.overTitleText={...tb, on:await on()};
  await rest(); res.y600=await on();
  await rest(); const heroAtRest=await p.evaluate(()=>Math.round(document.getElementById('hero').getBoundingClientRect().top));
  res.heroTopAtRest=heroAtRest;
  console.log('HIT', JSON.stringify(res));
  if(shot){ await rest(); await p.screenshot({path:shot+'-rest.png'}); await p.mouse.move(900,40); await p.waitForTimeout(300); await p.screenshot({path:shot+'-open.png'}); }
  console.log('ERRORS', errs.length, errs.slice(0,5));
  await b.close();
})().catch(e=>{ console.error(e); process.exit(1); });
