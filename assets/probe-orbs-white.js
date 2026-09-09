// probe-orbs-white.js — WEAVER v14.70: every .orb (WIKI + SKILLS + BOTS + INTEGRATIONS) is a plain white dot at rest AND on hover;
// reports rest diameter, hover diameter, satellite (::after) colour, and writes a proof shot. Run:
//   PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-orbs-white.js [out.png]
const path=require('path'); const pw=require(process.env.PW||'playwright');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const OUT=process.argv[2]||path.resolve(__dirname,'proof-orbs-white.png');
const WHITE=new Set(['rgb(255, 255, 255)','rgba(255, 255, 255, 1)']);
(async()=>{
  const b=await pw.chromium.launch(); const pg=await b.newPage({viewport:{width:1456,height:914}});
  const errs=[]; pg.on('pageerror',e=>errs.push(String(e))); pg.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
  await pg.goto(FILE); await pg.waitForTimeout(900);
  const views=['wiki','skills','bots','integrations'];
  const report={views:{},errs};
  for(const v of views){
    await pg.evaluate(v=>{ try{ showView(v); }catch(e){} },v); await pg.waitForTimeout(350);
    const rest=await pg.evaluate(()=>{
      const on=document.querySelector('.view.on')||document.body;
      const orbs=[...on.querySelectorAll('.orb')].filter(o=>o.getBoundingClientRect().width>0);
      const bg=orbs.map(o=>getComputedStyle(o).backgroundColor);
      const sizes=orbs.map(o=>+o.getBoundingClientRect().width.toFixed(2));
      const sat=orbs.map(o=>getComputedStyle(o,'::after').backgroundColor);
      const shadow=orbs.map(o=>getComputedStyle(o).boxShadow);
      return {n:orbs.length, nonWhite:bg.filter(c=>!['rgb(255, 255, 255)'].includes(c)).length, uniqBg:[...new Set(bg)], uniqSat:[...new Set(sat)], uniqShadow:[...new Set(shadow)], rest:[...new Set(sizes)]};
    });
    // hover the first row + first orb
    const hov=await pg.evaluate(async()=>{
      const on=document.querySelector('.view.on')||document.body;
      const th=on.querySelector('.thead'); if(!th) return null;
      const r=th.getBoundingClientRect(); return {x:r.x+40,y:r.y+r.height/2};
    });
    let hover=null;
    if(hov){ await pg.mouse.move(hov.x,hov.y); await pg.waitForTimeout(300);
      const orb=await pg.evaluate(()=>{ const o=document.querySelector('.view.on .thead:hover .orb'); if(!o) return null; const r=o.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2}; });
      if(orb){ await pg.mouse.move(orb.x,orb.y); await pg.waitForTimeout(350); }
      hover=await pg.evaluate(()=>{
        const th=document.querySelector('.view.on .thead:hover'); if(!th) return null;
        const orbs=[...th.querySelectorAll('.orb')];
        return {n:orbs.length, bg:[...new Set(orbs.map(o=>getComputedStyle(o).backgroundColor))], size:[...new Set(orbs.map(o=>+o.getBoundingClientRect().width.toFixed(2)))],
          hovOrb:(()=>{ const o=th.querySelector('.orb:hover'); if(!o) return null; const cs=getComputedStyle(o); return {bg:cs.backgroundColor, transform:cs.transform, caption:getComputedStyle(o,'::before').opacity}; })()};
      });
      if(v==='wiki'){ await pg.screenshot({path:OUT}); }
      await pg.mouse.move(700,880); await pg.waitForTimeout(250);
    }
    report.views[v]={rest,hover};
  }
  // orbit ring: light one orb and read the satellite colour
  await pg.evaluate(()=>{ showView('wiki'); const o=document.querySelector('#view-wiki .orb'); o.classList.add('on'); });
  await pg.waitForTimeout(120);
  report.satelliteOn=await pg.evaluate(()=>{ const o=document.querySelector('#view-wiki .orb.on'); const cs=getComputedStyle(o,'::after'); return {bg:cs.backgroundColor, w:cs.width, anim:cs.animationName}; });
  // rest-state shot without hover (mouse parked bottom)
  await pg.mouse.move(700,900); await pg.waitForTimeout(300);
  await pg.screenshot({path:OUT.replace(/\.png$/,'-rest.png')});
  console.log(JSON.stringify(report,null,1));
  await b.close();
})().catch(e=>{ console.error(e); process.exit(1); });
