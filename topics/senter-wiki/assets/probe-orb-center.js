// WEAVER v14.79: ORB CENTRE + TWO-STAGE HOVER probe — the WIKI dot+logo group must sit centred in the empty band between the longest
// title's right edge and the wallpaper girl's VISIBLE left edge, which is SAMPLED from the rendered asset by sampleFigureEdge()
// (window.__figFrac, fraction of the drawn contain width; fallback 0.62). Then: row hover → all four orbs ~22px with black numbers, gap 18;
// hovering one orb → 38px, centre delta 0 vs the 22px state, caption + card; leave → 4px.
// run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-orb-center.js [--shot dir]
const path=require('path'); const fs=require('fs'); const { chromium } = require(process.env.PW||'playwright');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const VPS=[[1456,914],[1040,880]]; const shotIdx=process.argv.indexOf('--shot'); const shotDir=shotIdx>0?process.argv[shotIdx+1]:null;
(async()=>{
  const br=await chromium.launch(); let fail=0; const out={};
  for(const [W,H] of VPS){
    const pg=await br.newPage({viewport:{width:W,height:H,deviceScaleFactor:2}}); const errs=[]; pg.on('pageerror',e=>errs.push(String(e)));
    await pg.goto(FILE); await pg.waitForTimeout(900);
    await pg.evaluate(async()=>{ await window.sampleFigureEdge(); window.orbColumn(); }); await pg.waitForTimeout(200);
    await pg.mouse.move(W-60,H-40); await pg.waitForTimeout(150); await pg.mouse.move(W/2,4); await pg.waitForTimeout(400); await pg.mouse.move(5,H/2); await pg.waitForTimeout(300);
    await pg.evaluate(()=>window.orbColumn()); await pg.waitForTimeout(250);
    const m=await pg.evaluate(()=>{
      const v=document.getElementById('view-wiki'); const rows=[...v.querySelectorAll('.topic .thead')].filter(t=>t.querySelector('.orb'));
      v.classList.add('orbMeasure'); let tr=0; rows.forEach(t=>{ tr=Math.max(tr,t.querySelector('.tname').getBoundingClientRect().right); }); v.classList.remove('orbMeasure');
      const W=innerWidth,H=innerHeight, R=1.54, dw=Math.min(W,H*R), il=(W-dw)/2, frac=window.__figFrac, fig=il+dw*(frac||0.62), face=il+dw*0.67;
      const xs=rows.map(t=>t.querySelector('.orb').getBoundingClientRect().left);
      const g=rows[0].querySelector('.orbs').getBoundingClientRect(); let logoR=0; rows.forEach(t=>{ const d=t.querySelector('.idots'); if(d) logoR=Math.max(logoR,d.getBoundingClientRect().right); });
      const gc=(g.left+Math.max(g.right,logoR))/2; const restW=rows[0].querySelector('.orb').getBoundingClientRect().width;
      return { orbcol:v.style.getPropertyValue('--orbcol'), figFrac:frac, figSample:window.__figSample, figLeftDataset:v.dataset.figLeft, figSrc:v.dataset.figSrc, titleRight:tr, figLeft:fig, faceLeft:face, target:(tr+fig)/2, groupCentre:gc, groupLeft:g.left, groupRight:Math.max(g.right,logoR),
               firstOrbX:xs[0], spread:Math.max(...xs)-Math.min(...xs), rows:rows.length, logosRight:logoR, restOrbW:restW };
    });
    if(shotDir) await pg.screenshot({path:path.join(shotDir,`orb-rest-${W}.png`)});
    // STAGE 1: hover the third row's title → all four orbs ~22px with numbers, gap widened
    const rowSel='#view-wiki .topic:nth-of-type(3) .thead';
    const tb=await (await pg.$(rowSel+' .tname')).boundingBox(); await pg.mouse.move(tb.x+20,tb.y+tb.height/2); await pg.waitForTimeout(400);
    const s1=await pg.evaluate(s=>{ const t=document.querySelector(s); const os=[...t.querySelectorAll('.orb')]; const rs=os.map(o=>o.getBoundingClientRect());
      const gaps=rs.slice(1).map((r,i)=>r.left-rs[i].right); const nums=os.map(o=>{ const v=o.querySelector('.v'); const cs=getComputedStyle(v); return {txt:v.textContent, fs:cs.fontSize, color:cs.color, w:v.getBoundingClientRect().width}; });
      const other=document.querySelector('#view-wiki .topic:nth-of-type(5) .thead .orb').getBoundingClientRect().width; const under=getComputedStyle(t,'::after').width;
      return { widths:rs.map(r=>r.width), gaps, nums, otherRowOrbW:other, underlineW:under, centres:[...t.querySelectorAll('.orb,.idot')].map(e=>{const r=e.getBoundingClientRect(); return (r.left+r.right)/2;}) }; },rowSel);
    if(shotDir) await pg.screenshot({path:path.join(shotDir,`orb-rowhover-${W}.png`)});
    // STAGE 2: hover the second orb → 38px, centre unchanged vs stage 1, caption + card
    const ob=await pg.$(rowSel+' .orb:nth-child(2)'); const bb=await ob.boundingBox(); await pg.mouse.move(bb.x+bb.width/2,bb.y+bb.height/2); await pg.waitForTimeout(450);
    const s2=await pg.evaluate(s=>{ const t=document.querySelector(s); const os=[...t.querySelectorAll('.orb')]; const r=os[1].getBoundingClientRect(); const card=document.querySelector('.hcard.show'); const cap=getComputedStyle(os[1],'::before').opacity;
      return { hovW:r.width, hovCentre:(r.left+r.right)/2, centres:[...t.querySelectorAll('.orb,.idot')].map(e=>{const q=e.getBoundingClientRect(); return (q.left+q.right)/2;}), cardShown:!!card, cardIn:!!(card&&card.classList.contains('in')), capOpacity:cap, widths:os.map(o=>o.getBoundingClientRect().width) }; },rowSel);
    if(shotDir) await pg.screenshot({path:path.join(shotDir,`orb-orbhover-${W}.png`)});
    await pg.mouse.move(5,H/2); await pg.waitForTimeout(400);
    const s3=await pg.evaluate(s=>[...document.querySelector(s).querySelectorAll('.orb')].map(o=>o.getBoundingClientRect().width),rowSel);
    const hoverDelta=Math.abs(s2.hovCentre-s1.centres[1]); const sibMax=Math.max(...s1.centres.map((c,i)=>i===1?0:Math.abs(s2.centres[i]-c)));
    const bandLeft=m.titleRight, bandRight=m.figLeft; const inBand=m.firstOrbX>bandLeft+28 && m.groupRight<bandRight; const centreDev=Math.abs(m.groupCentre-m.target);
    const ok = errs.length===0 && m.figSrc==='sampled' && inBand && centreDev<=1 && m.spread<=1 && m.restOrbW<=4.5 && s1.widths.every(w=>Math.abs(w-22)<=1) && s1.gaps.every(g=>g>=17) && s1.nums.every(n=>n.txt.trim().length>0 && n.w>0 && n.color==='rgb(0, 0, 0)') && s1.otherRowOrbW<=4.5 && Math.abs(s2.hovW-38)<=1 && hoverDelta<=1 && sibMax<=1 && s2.cardShown && s2.capOpacity==='1' && s3.every(w=>w<=4.5) && m.logosRight<m.faceLeft;
    if(!ok) fail++;
    out[`${W}x${H}`]={ ok, errs, rest:m, rowHover:s1, orbHover:{...s2, hoverDelta, sibMax}, afterLeave:s3, band:{left:bandLeft,right:bandRight,inBand,centreDev} };
    await pg.close();
  }
  await br.close(); console.log(JSON.stringify(out,null,1)); console.log(fail?'PROBE FAIL':'PROBE OK'); process.exit(fail?1:0);
})();
