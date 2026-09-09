// probe-T.js — model ▾ / + menu anchoring (item T). Usage: PW=... node assets/probe-T.js [WxH] [shotdir]
const path=require('path'); const { chromium } = require(process.env.PW || '/Users/sovthpaw/.hermes/hermes-agent/node_modules/playwright');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number); const shotdir=process.argv[3]||'';
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
(async()=>{
  const br=await chromium.launch(); const pg=await br.newPage({viewport:{width:W,height:H}});
  const errs=[]; pg.on('pageerror',e=>errs.push('PAGE '+e.message)); pg.on('console',m=>{ if(m.type()==='error') errs.push('CON '+m.text()); });
  await pg.goto(FILE); await pg.waitForTimeout(3600);
  await pg.mouse.move(600,4); await pg.mouse.move(600,30); await pg.waitForTimeout(400);
  const measure = async (k) => pg.evaluate((k)=>{
    const R=e=>{ if(!e) return null; const b=e.getBoundingClientRect(); return {l:Math.round(b.left),t:Math.round(b.top),r:Math.round(b.right),b:Math.round(b.bottom),w:Math.round(b.width),h:Math.round(b.height)}; };
    const btn=document.querySelector('#composerRow .csq[data-k="'+k+'"]'); const pop=document.getElementById('popup-'+k);
    const strip=document.getElementById('topstrip');
    const items=[...pop.querySelectorAll('button')].map(b=>{ const r=b.getBoundingClientRect(); const cx=r.left+r.width/2, cy=r.top+r.height/2; const el=document.elementFromPoint(cx,cy); return {txt:b.textContent.trim().slice(0,18), hit: !!el && (el===b||b.contains(el))}; });
    const cs=getComputedStyle(strip);
    return {btn:R(btn), pop:R(pop), on:pop.classList.contains('on'), up:pop.classList.contains('up'), items, strip:{h:strip.getBoundingClientRect().height, overflow:cs.overflow, clip:cs.clipPath, scrollH:strip.scrollHeight}, vw:innerWidth, vh:innerHeight};
  }, k);
  const out={vp:W+'x'+H, errs};
  for(const k of ['model','context']){
    await pg.evaluate(k=>document.querySelector('#composerRow .csq[data-k="'+k+'"]').click(), k); await pg.waitForTimeout(250);
    const m=await measure(k);
    const dl=m.pop.l-m.btn.l, dt=m.pop.t-(m.btn.b+6);
    m.checks={ left_eq_pill: Math.abs(dl)<=2, top_eq_pill_bottom_plus6: Math.abs(dt)<=2, in_viewport: m.pop.b<=m.vh-8 && m.pop.r<=m.vw-8, all_hittable: m.items.length>0 && m.items.every(i=>i.hit), dl, dt };
    out[k]=m;
    if(shotdir) await pg.screenshot({path:path.join(shotdir,`T-${k}-${W}x${H}.png`)});
    await pg.evaluate(()=>document.body.click()); await pg.waitForTimeout(150);
  }
  // flip test: the row sits at y=22 so nothing can ever fit ABOVE it at real geometry — synthesize the overflow case by moving the composer row near the viewport bottom, then re-place
  await pg.evaluate(()=>{ const s=document.getElementById('topstrip'), r=document.getElementById('composerRow'); s.style.height=innerHeight+'px'; s.style.clipPath='inset(0)'; r.style.top=(innerHeight-90)+'px'; document.querySelector('#composerRow .csq[data-k="model"]').click(); }); await pg.waitForTimeout(250);
  const f=await measure('model'); f.checks={ up:f.up, bottom_eq_pill_top_minus6: Math.abs((f.btn.t-6)-f.pop.b)<=2, fits: f.pop.b<=f.vh-8 && f.pop.t>=0, all_hittable:f.items.every(i=>i.hit) }; out.flip=f;
  if(shotdir) await pg.screenshot({path:path.join(shotdir,`T-model-flip-${W}x${H}.png`)});
  console.log(JSON.stringify(out,null,1)); await br.close();
})();
