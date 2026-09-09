// WEAVER v14.80: ORB COLUMN AT CHRIS'S REAL PANE WIDTH. He views the wiki inside the Hermes desktop PREVIEW PANE (~736 CSS px wide,
// x 720–1456 of his 1456-wide window), not at 1456. PRIMARY viewport = 736x850 @2x; 1040x880 and 1456x914 are secondary.
// Reports: longest title text right, first orb x, last logo right, sampled figure left, band centre vs group centre, then the two-stage hover.
// run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-orb-736.js [--shot dir]
const path=require('path'); const fs=require('fs'); const { chromium } = require(process.env.PW||'playwright');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const VPS=[[1151,834],[736,850],[1040,880],[1456,914]]; /* v14.81: 1151x834 = Chris's preview webview (AX tree) — PRIMARY; the rest are secondary sanity */ const shotIdx=process.argv.indexOf('--shot'); const shotDir=shotIdx>0?process.argv[shotIdx+1]:null;
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
      // longest title's TEXT right edge (rest size, unclamped) — measured with a Range so ellipsis/flex-basis do not inflate it
      v.classList.add('orbMeasure'); let tr=0, trName=''; rows.forEach(t=>{ const n=t.querySelector('.tname'); const rg=document.createRange(); rg.selectNodeContents(n); const r=rg.getBoundingClientRect(); if(r.bottom<=0||r.top>=innerHeight) return; /* v14.81: the band Chris sees ends at the longest title ON SCREEN */ if(r.right>tr){ tr=r.right; trName=n.textContent.trim(); } }); v.classList.remove('orbMeasure');
      const W=innerWidth,H=innerHeight, R=1.54, dw=Math.min(W,H*R), il=(W-dw)/2, frac=window.__figFrac, fig=il+dw*(frac||0.62), face=il+dw*0.67;
      const xs=rows.map(t=>t.querySelector('.orb').getBoundingClientRect().left);
      // VISIBLE title end = the ellipsized cell's right edge when the column clamps the longest title (736 pane), else the text's own right edge
      let cellR=0; rows.forEach(t=>{ cellR=Math.max(cellR,t.querySelector('.tname').getBoundingClientRect().right); }); const visR=Math.min(tr,cellR); const ellipsized=cellR<tr-1;
      const g=rows[0].querySelector('.orbs').getBoundingClientRect(); let logoR=0; rows.forEach(t=>{ const d=t.querySelector('.idots'); if(d) logoR=Math.max(logoR,d.getBoundingClientRect().right); });
      const gc=(g.left+Math.max(g.right,logoR))/2; const restW=rows[0].querySelector('.orb').getBoundingClientRect().width;
      const wrapped=rows.filter(t=>t.getBoundingClientRect().height>60).length;
      return { orbcol:v.style.getPropertyValue('--orbcol'), figFrac:frac, figSample:window.__figSample, figSrc:v.dataset.figSrc, titleTextRight:tr, titleVisibleRight:visR, ellipsized, longestTitle:trName, figLeft:fig, faceLeft:face, drawnLeft:il, drawnW:dw, bandCentre:(visR+fig)/2, groupCentre:gc, groupLeft:g.left, groupRight:Math.max(g.right,logoR),
               firstOrbX:xs[0], firstOrbPct:+(xs[0]/W*100).toFixed(1), spread:Math.max(...xs)-Math.min(...xs), rows:rows.length, lastLogoRight:logoR, restOrbW:restW, wrappedRows:wrapped };
    });
    if(shotDir) await pg.screenshot({path:path.join(shotDir,`orb736-rest-${W}.png`)});
    const rowSel='#view-wiki .topic:nth-of-type(3) .thead';
    const tb=await (await pg.$(rowSel+' .tname')).boundingBox(); await pg.mouse.move(tb.x+20,tb.y+tb.height/2); await pg.waitForTimeout(400);
    const s1=await pg.evaluate(s=>{ const t=document.querySelector(s); const os=[...t.querySelectorAll('.orb')]; const rs=os.map(o=>o.getBoundingClientRect());
      const gaps=rs.slice(1).map((r,i)=>r.left-rs[i].right); const nums=os.map(o=>{ const v=o.querySelector('.v'); const cs=getComputedStyle(v); return {txt:v.textContent, color:cs.color, w:v.getBoundingClientRect().width}; });
      const other=document.querySelector('#view-wiki .topic:nth-of-type(5) .thead .orb').getBoundingClientRect().width; let logoR=0; t.querySelectorAll('.idot').forEach(d=>logoR=Math.max(logoR,d.getBoundingClientRect().right));
      return { widths:rs.map(r=>r.width), gaps, nums, otherRowOrbW:other, rowH:t.getBoundingClientRect().height, hoverLogosRight:logoR, centres:[...t.querySelectorAll('.orb,.idot')].map(e=>{const r=e.getBoundingClientRect(); return (r.left+r.right)/2;}) }; },rowSel);
    if(shotDir) await pg.screenshot({path:path.join(shotDir,`orb736-rowhover-${W}.png`)});
    const ob=await pg.$(rowSel+' .orb:nth-child(2)'); const bb=await ob.boundingBox(); await pg.mouse.move(bb.x+bb.width/2,bb.y+bb.height/2); await pg.waitForTimeout(450);
    const s2=await pg.evaluate(s=>{ const t=document.querySelector(s); const os=[...t.querySelectorAll('.orb')]; const r=os[1].getBoundingClientRect(); const card=document.querySelector('.hcard.show'); const cap=getComputedStyle(os[1],'::before').opacity;
      return { hovW:r.width, hovCentre:(r.left+r.right)/2, centres:[...t.querySelectorAll('.orb,.idot')].map(e=>{const q=e.getBoundingClientRect(); return (q.left+q.right)/2;}), cardShown:!!card, capOpacity:cap, widths:os.map(o=>o.getBoundingClientRect().width) }; },rowSel);
    if(shotDir) await pg.screenshot({path:path.join(shotDir,`orb736-orbhover-${W}.png`)});
    await pg.mouse.move(5,H/2); await pg.waitForTimeout(400);
    const s3=await pg.evaluate(s=>[...document.querySelector(s).querySelectorAll('.orb')].map(o=>o.getBoundingClientRect().width),rowSel);
    const hoverDelta=Math.abs(s2.hovCentre-s1.centres[1]); const sibMax=Math.max(...s1.centres.map((c,i)=>i===1?0:Math.abs(s2.centres[i]-c)));
    const inBand=m.firstOrbX>m.titleVisibleRight+8 && m.groupRight<m.figLeft; const centreDev=Math.abs(m.groupCentre-m.bandCentre);
    // hover geometry (22px orbs + 30px logos) is transient and sits on the row's solid #000 hover bg; it must stay inside the pane, and rest must not touch her
    const hoverInBand=s1.hoverLogosRight<W-10;
    const ok = errs.length===0 && m.figSrc==='sampled' && inBand && centreDev<=1 && m.spread<=1 && m.restOrbW<=4.5 && m.wrappedRows===0 && s1.widths.every(w=>Math.abs(w-22)<=1) && s1.gaps.every(g=>g>=17) && s1.nums.every(n=>n.txt.trim().length>0 && n.w>0 && n.color==='rgb(0, 0, 0)') && s1.otherRowOrbW<=4.5 && Math.abs(s2.hovW-38)<=1 && hoverDelta<=1 && sibMax<=1 && s2.cardShown && s2.capOpacity==='1' && s3.every(w=>w<=4.5) && hoverInBand;
    if(!ok) fail++;
    out[`${W}x${H}`]={ ok, errs, rest:m, rowHover:s1, orbHover:{...s2, hoverDelta, sibMax}, afterLeave:s3, band:{left:m.titleTextRight,right:m.figLeft,inBand,hoverInBand,centreDev} };
    await pg.close();
  }
  await br.close(); console.log(JSON.stringify(out,null,1)); console.log(fail?'PROBE FAIL':'PROBE OK'); process.exit(fail?1:0);
})();
