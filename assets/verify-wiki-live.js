// Senter Wiki LIVE regression ledger (Playwright, pointer-driven) — one permanent assertion per fix. Never remove; a red line is a regression.
// Companion to assets/verify-wiki.js (static checks, teknium). Run both before every report:
//   PATH=$HOME/.hermes/node/bin:$PATH PW=~/.hermes/hermes-agent/node_modules/playwright node assets/verify-wiki-live.js [--vp 1040x880]
const {chromium}=require(process.env.PW||'playwright');
const path=require('path');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const arg=process.argv.indexOf('--vp'); const [W,H]=(arg>0?process.argv[arg+1]:'1040x880').split('x').map(Number);
const results=[]; function ok(name,cond,detail){ results.push({name,ok:!!cond,detail}); }

(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); }); p.on('response',r=>{ if(r.status()>=400) errs.push('HTTP '+r.status()+' '+r.url().replace(/token=[^&]+/,'token=…').slice(0,120)); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(900);
 const on=()=>p.evaluate(()=>document.getElementById('topstrip').classList.contains('on'));
 const rest=async()=>{ await p.mouse.move(300,400); await p.waitForTimeout(350); };

 // ---- A #17: closed strip zero-flow but hit zone ≥48px (title top −10) ----
 // Z (v14.50) re-point: the hero title now sits at y=26 (baseline), so the old probe column x=300 lands ON the title ink (rest() hovers a row → POCKET-SHOP, ink right 313) — and the title ink is the ONE spot that must never open the strip (#17 gap rule). Probe the zone at a title-free column HX = ink.right+60 instead; the assertions themselves are unchanged.
 const HX=await p.evaluate(()=>Math.round(innerWidth*0.6)); /* rest() hovers a row and rotates the hero title, so a title-relative column is stale by probe time — use 60% of the viewport width (always clear of any title ink, no nav element sits there at rest) */
 const geo=await p.evaluate(()=>{ const h=document.querySelector('.hero'); const ht=document.getElementById('heroTitle'); return {heroTop:Math.round(h.getBoundingClientRect().top), titleTop:Math.round(ht.getBoundingClientRect().top)}; });
 ok('#17 hero zero-flow at rest (hero.top 0)', geo.heroTop===0, JSON.stringify(geo));
 const opened=[]; for(const y of [30,50,Math.max(48,geo.titleTop-10)-1]){ await rest(); await p.mouse.move(HX,y); await p.waitForTimeout(250); opened.push([y,await on()]); }
 ok('#17 strip opens at y=30/50/(titleTop-11)', opened.every(o=>o[1]), JSON.stringify(opened));
 await rest(); const tb=await p.evaluate(()=>{ const r=document.getElementById('heroTitle').getBoundingClientRect(); return {x:Math.round(r.left+30),y:Math.round(r.top+r.height/2)}; });
 await p.mouse.move(tb.x,tb.y); await p.waitForTimeout(250); ok('#17 hero title does NOT open strip', !(await on()));
 await rest(); ok('#17 y=400 closed', !(await on()));
 await p.mouse.move(HX,30); await p.waitForTimeout(250); await p.mouse.move(HX,150); await p.waitForTimeout(200); ok('#17 stays open inside 190px', await on());

 // ---- A #19: open strip opaque, hero hidden, ≤200ms ----
 await rest(); const t0=Date.now(); await p.mouse.move(HX,30); let ms=null;
 for(let i=0;i<40;i++){ const cp=await p.evaluate(()=>getComputedStyle(document.getElementById('topstrip')).clipPath); if(/inset\(0(px)?\)/.test(cp)){ ms=Date.now()-t0; break; } await p.waitForTimeout(10); }
 ok('#19 fully open ≤200ms', ms!==null && ms<=200, ms+'ms');
 await p.waitForTimeout(150);
 const pix=await p.evaluate(()=>{ const h=document.querySelector('.hero'); const y=Math.round(h.getBoundingClientRect().top)+10; const el=document.elementFromPoint(500,y); return {y,inStrip:!!(el&&el.closest('#topstrip')),bg:getComputedStyle(document.getElementById('topstrip')).backgroundColor,heroVis:getComputedStyle(h).visibility}; });
 ok('#19 elementFromPoint(500,hero.top+10) inside #topstrip', pix.inStrip, JSON.stringify(pix));
 ok('#19 open strip bg opaque black', pix.bg==='rgb(0, 0, 0)', pix.bg);
 ok('#19 hero hidden while open', pix.heroVis==='hidden', pix.heroVis);
 const one=await p.screenshot({clip:{x:500,y:pix.y,width:1,height:1}}); const zlib=require('zlib'); let off=8,idat=[]; while(off<one.length){ const len=one.readUInt32BE(off); const type=one.toString('ascii',off+4,off+8); if(type==='IDAT') idat.push(one.slice(off+8,off+8+len)); off+=12+len; } const raw=zlib.inflateSync(Buffer.concat(idat));
 ok('#19 pixel (500,hero.top+10) is #000', raw[1]===0&&raw[2]===0&&raw[3]===0, `rgb ${raw[1]},${raw[2]},${raw[3]}`);
 const cycles=await p.evaluate(()=>new Promise(r=>{ let n=0; const mo=new MutationObserver(()=>n++); mo.observe(document.getElementById('topstrip'),{attributes:true,attributeFilter:['class']}); setTimeout(()=>{mo.disconnect(); r(n);},300); }));
 ok('#17 no alignCluster class thrash (0 class flips in 300ms while open)', cycles===0, cycles+' flips');
 const tab=await p.evaluate(()=>{ const t=[...document.querySelectorAll('#topnav .navtab')].find(x=>x.textContent.trim()==='FEED'); const r=t.getBoundingClientRect(); return {x:Math.round(r.left+r.width/2),y:Math.round(r.top+r.height/2)}; });
 await p.mouse.move(tab.x,tab.y); await p.waitForTimeout(80);
 ok('#17 tab center hit-tests the tab', await p.evaluate(({x,y})=>{ const e=document.elementFromPoint(x,y); return !!(e&&e.closest('.navtab')); },tab));

 // ---- B #16 → I (v14.37) → superseded by N (v14.38): I's "cluster.right == #media.right" is intentionally no longer true (Chris: span media.left → ⚙.right); the live N assertions below replace it. Kept as a record, not asserted. ----
 /* I (retired): cluster.right == #media.right ±2 at open/closed/resize */

 // ---- C #0 overflow: 700-char message grows the card (width 400, height auto, no clip) in mini tail, #stream and #feed; the card below stays fully on screen ----
 { const LONG=('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ').repeat(6).slice(0,700);
   await p.evaluate((t)=>{ notify('teknium',t); notify('anser','short one after the long card'); const f=document.getElementById('feed'); f.insertAdjacentHTML('afterbegin','<div class="post" data-who="anser" data-when="now">'+av('anser')+'<span class="who">anser</span><span class="when">now</span><div class="txt">short</div></div>'); f.insertAdjacentHTML('afterbegin','<div class="post" data-who="teknium" data-when="now">'+av('teknium')+'<span class="who">teknium</span><span class="when">now</span><div class="txt">'+t+'</div></div>'); }, LONG);
   await p.waitForTimeout(400);
   const m=await p.evaluate(()=>{ const box=e=>{const r=e.getBoundingClientRect(); return {w:Math.round(r.width),h:Math.round(r.height),b:Math.round(r.bottom),clip:e.scrollHeight>e.clientHeight+1};}; const pick=list=>{ const i=list.findIndex(x=>x.querySelector('.txt').textContent.length>600); return i<0?null:{long:box(list[i]),txt:box(list[i].querySelector('.txt')),next:list[i+1]?box(list[i+1]):null}; }; return {vh:innerHeight, mini:pick([...document.querySelectorAll('#chat .mini .tail .msg')]), feed:pick([...document.querySelectorAll('#feed .post')])}; });
   ok('#0 mini: long card w400 grows (h>250) no clip', m.mini && m.mini.long.w===400 && m.mini.long.h>250 && !m.mini.long.clip && !m.mini.txt.clip, JSON.stringify(m.mini&&m.mini.long));
   ok('#0 mini: card below the long one fully on screen', m.mini && m.mini.next && m.mini.next.b<=m.vh-14 && !m.mini.next.clip, JSON.stringify(m.mini&&m.mini.next));
   await p.mouse.move(W-40,H-40); await p.waitForTimeout(450);
   const s=await p.evaluate(()=>{ const box=e=>{const r=e.getBoundingClientRect(); return {w:Math.round(r.width),h:Math.round(r.height),clip:e.scrollHeight>e.clientHeight+1};}; const l=[...document.querySelectorAll('#stream .msg')].find(x=>x.querySelector('.txt').textContent.length>600); return l?box(l):null; });
   ok('#0 stream (open): long card w400 h>250 no clip', s && s.w===400 && s.h>250 && !s.clip, JSON.stringify(s));
   await p.evaluate(()=>showView('feed')); await p.waitForTimeout(400);
   const fd=await p.evaluate(()=>{ const box=e=>{const r=e.getBoundingClientRect(); return {w:Math.round(r.width),h:Math.round(r.height),clip:e.scrollHeight>e.clientHeight+1};}; const list=[...document.querySelectorAll('#feed .post')]; const i=list.findIndex(x=>x.querySelector('.txt').textContent.length>600); return i<0?null:{long:box(list[i]),next:list[i+1]?box(list[i+1]):null}; });
   ok('#0 feed: long post w400 grows no clip, next post intact', fd && fd.long.w===400 && fd.long.h>250 && !fd.long.clip && fd.next && !fd.next.clip, JSON.stringify(fd&&fd.long));
   await p.evaluate(()=>showView('wiki')); await p.waitForTimeout(300); await rest(); }

 // ---- D #8: no bridge chip bottom-right; health text lives in the ⚙ panel ----
 ok('#8 no #bridgeChip element', await p.evaluate(()=>!document.getElementById('bridgeChip')));
 ok('#8 nothing fixed-positioned in the bottom-right corner except the fleet stream', await p.evaluate(()=>{ const els=[...document.querySelectorAll('body *')].filter(e=>{ const cs=getComputedStyle(e); if(cs.position!=='fixed'||cs.display==='none') return false; const r=e.getBoundingClientRect(); return r.width>0 && r.bottom>innerHeight-40 && r.right>innerWidth-40 && !e.closest('#chat') && e.id!=='chat' && !e.closest('#intRail') && e.id!=='fade' && e.id!=='wallBackdrop' && e.id!=='mindmap'; }); return els.length===0 || els.map(e=>e.id||e.className).join(','); })===true);
 await p.evaluate(()=>document.getElementById('navSettings').click()); await p.waitForTimeout(250);
 ok('#8 ⚙ panel shows bridge health line', await p.evaluate(()=>{ const bh=document.getElementById('bridgeHealth'); return !!bh && /bridge · .+ · \d+ pending/.test(bh.textContent); }), await p.evaluate(()=>document.getElementById('bridgeHealth')?.textContent));
 await p.keyboard.press('Escape'); await p.evaluate(()=>{ const m=document.getElementById('warnMask'); if(m) m.remove(); }); await p.waitForTimeout(150);

 // ---- E #9 → AB (v14.51): play circle ink clears the artist ink by ≥8px (E's ≥12 superseded — Chris wanted the controls row DOWN ~4px, so 13 → 9); #mNow/title/media box untouched; controls row moved as a unit ----
 await p.mouse.move(300,30); await p.waitForTimeout(250);
 const e9=await p.evaluate(()=>{ const play=document.querySelector('#media .mbtn.play').getBoundingClientRect(); const rg=document.createRange(); rg.selectNodeContents(document.getElementById('mTitle')); const ink=rg.getBoundingClientRect(); const skip=document.querySelector('#mCtl .mbtn:first-child').getBoundingClientRect(); const media=document.getElementById('media').getBoundingClientRect(); const ctl=document.getElementById('mCtl').getBoundingClientRect(); const now=document.getElementById('mNow').getBoundingClientRect(); return {gap:Math.round(ink.top-play.bottom), playTop:Math.round(play.top), skipTop:Math.round(skip.top), ctlTop:Math.round(ctl.top), nowTop:Math.round(now.top), titleTop:Math.round(ink.top), mediaTop:Math.round(media.top), mediaH:Math.round(media.height), playInCtl:Math.round(play.top-ctl.top), skipInCtl:Math.round(skip.top-ctl.top)}; });
 ok('AB play circle ≥8px (and ≤10) above artist ink (E had 13; controls row scooted down 4)', e9.gap>=8 && e9.gap<=10, JSON.stringify(e9));
 ok('AB relative geometry: #mNow sits 38px under #media.top (controls row + margins unchanged in height), #media h 67, play ring 4px above #mCtl.top (E lift kept) — absolute y is AE\'s (whole-widget translate), not asserted here', (e9.nowTop-e9.mediaTop)===38 && e9.mediaH===67 && e9.playInCtl===-4, JSON.stringify(e9));
 ok('#9→AB skips travel WITH the controls row: skip.top − play.top constant (1 before AE / −3 after AE\'s shared lift, |Δ|≤3) and title ink == #mNow.top', Math.abs(e9.skipTop-e9.playTop)<=3 && e9.titleTop===e9.nowTop, JSON.stringify(e9));
 await rest();

 // ---- K: caret + text LEFT-aligned right of the model pill (~14px), grow rightward; bottom on the overline ----
 await p.mouse.move(300,30); await p.waitForTimeout(250);
 const k0=await p.evaluate(()=>{ const pill=document.querySelector('.model-pill').getBoundingClientRect(); const c=document.getElementById('senterCaret').getBoundingClientRect(); const ol=document.getElementById('senterOverline').getBoundingClientRect(); return {gap:Math.round(c.left-pill.right), caretB:Math.round(c.bottom), olY:Math.round(ol.top), vwHalf:Math.round(innerWidth/2), caretL:Math.round(c.left)}; });
 ok('K caret starts 12–16px right of the model pill, not centered', k0.gap>=12 && k0.gap<=16 && Math.abs(k0.caretL-k0.vwHalf)>100, JSON.stringify(k0));
 ok('K caret bottom sits on the overline (±1)', Math.abs(k0.caretB-k0.olY)<=1, JSON.stringify(k0));
 await p.keyboard.type('HELLO CHRIS'); await p.waitForTimeout(120);
 const k1=await p.evaluate(()=>{ const pill=document.querySelector('.model-pill').getBoundingClientRect(); const t=document.getElementById('senterText').getBoundingClientRect(); const c=document.getElementById('senterCaret').getBoundingClientRect(); return {textL:Math.round(t.left-pill.right), textW:Math.round(t.width), caretAfterText:Math.round(c.left-t.right), textB:Math.round(t.bottom), olY:Math.round(document.getElementById('senterOverline').getBoundingClientRect().top)}; });
 ok('K typed text starts at the same left edge and grows rightward; caret trails it', k1.textL>=12 && k1.textL<=16 && k1.textW>60 && k1.caretAfterText>=0 && k1.caretAfterText<=4 && Math.abs(k1.textB-k1.olY)<=1, JSON.stringify(k1));
 await p.keyboard.press('Escape'); await p.waitForTimeout(150); await rest();

 // ---- J: + and model pill raised 4–6px; nothing else moved; + never closes the strip ----
 await p.mouse.move(300,30); await p.waitForTimeout(250);
 const j0=await p.evaluate(()=>{ const q=s=>document.querySelector(s).getBoundingClientRect(); const row=q('#composerRow'); /* O (v14.39): the lift lives on the inner glyph / pill box, not the 32px button — measure those */ const plus=q('.csq[data-k=context] .lucide'); const pill=q('.model-pill .pillBox'); const cl=q('#composerRight'); const cy=r=>r.top+r.height/2; return {plusLift:Math.round(cy(row)-cy(plus)), pillLift:Math.round(cy(row)-cy(pill)), clusterLift:Math.round(cy(row)-cy(cl)), rowT:Math.round(row.top), rowH:Math.round(row.height)}; });
 ok('J + and model pill lifted 4–6px; cluster/row unchanged', j0.plusLift>=4 && j0.plusLift<=6 && j0.pillLift>=4 && j0.pillLift<=6 && j0.clusterLift===0 && j0.rowT===22 && j0.rowH===32, JSON.stringify(j0));
 const np=await p.evaluate(()=>{ const r=document.getElementById('navPlus').getBoundingClientRect(); return {x:r.left+r.width/2,y:r.top+r.height/2}; });
 await p.mouse.move(np.x,np.y); await p.waitForTimeout(120); await p.mouse.click(np.x,np.y); await p.waitForTimeout(400);
 const j1=await p.evaluate(()=>({on:document.getElementById('topstrip').classList.contains('on'), ask:!!document.getElementById('askVal'), focused:document.activeElement&&document.activeElement.id==='askVal'}));
 ok('J clicking the travelling + opens the house ASK box and the strip stays open', j1.on && j1.ask && j1.focused, JSON.stringify(j1));
 await p.mouse.move(300,600); await p.waitForTimeout(300);
 ok('J strip holds open while the ASK box is up (pointer at y=600)', await on());
 await p.keyboard.press('Escape'); await p.waitForTimeout(150);
 ok('J Escape closes the ASK box; strip still open', (await p.evaluate(()=>!document.getElementById('askVal'))) && await on());
 await rest();

 // ---- L: media song · album marquee scrolls continuously and seamlessly ----
 const l0=await p.evaluate(()=>({scroll:document.getElementById('media').classList.contains('scroll'), anim:getComputedStyle(document.getElementById('mSub')).animationName, tx:getComputedStyle(document.getElementById('mSub')).transform, copies:document.querySelectorAll('#mSub .mq').length}));
 await p.waitForTimeout(1000);
 const l1=await p.evaluate(()=>getComputedStyle(document.getElementById('mSub')).transform);
 ok('L marquee running (two frames 1s apart differ, 2 text copies for a seamless loop)', l0.scroll && l0.anim==='mMarquee' && l0.copies===2 && l0.tx!==l1, JSON.stringify({...l0, tx1:l1}));

 // ---- M: hovering a nav tab / the + fades the input row out; back on the row fades it in; strip stays open ----
 await p.mouse.move(300,30); await p.waitForTimeout(250);
 const wiki=await p.evaluate(()=>{ const r=[...document.querySelectorAll('.navtab[data-view]')][0].getBoundingClientRect(); return {x:r.left+r.width/2,y:r.top+r.height/2}; });
 await p.mouse.move(wiki.x,wiki.y); await p.waitForTimeout(220);
 const m0=await p.evaluate(()=>{ const cs=getComputedStyle(document.getElementById('composerRow')); return {op:cs.opacity, pe:cs.pointerEvents, on:document.getElementById('topstrip').classList.contains('on')}; });
 ok('M hover WIKI → input row opacity 0 + pointer-events none, strip open', m0.op==='0' && m0.pe==='none' && m0.on, JSON.stringify(m0));
 await p.mouse.move(np.x,np.y); await p.waitForTimeout(220);
 ok('M hover the travelling + → row still faded', await p.evaluate(()=>getComputedStyle(document.getElementById('composerRow')).opacity==='0'));
 await p.mouse.move(300,38); await p.waitForTimeout(220);
 const m1=await p.evaluate(()=>{ const cs=getComputedStyle(document.getElementById('composerRow')); return {op:cs.opacity, pe:cs.pointerEvents, on:document.getElementById('topstrip').classList.contains('on')}; });
 ok('M back on the input row → opacity 1, clickable, strip open', m1.op==='1' && m1.pe==='auto' && m1.on, JSON.stringify(m1));
 await rest();

 // ---- I → N → R → R2 (v14.42): cluster spans #mPrev.left (‹‹ hitbox) → ⚙ glyph ink right (text Range, not the .navtab box) ±2, four glyphs evenly spread, 26px glyphs, row height 32, at rest/open/resize ----
 for(const state of ['open','closed']){ if(state==='closed') await rest(); else { await p.mouse.move(300,30); await p.waitForTimeout(250); }
   const c=await p.evaluate(()=>{ const cl=document.getElementById('composerRight').getBoundingClientRect(); const pv=document.getElementById('mPrev').getBoundingClientRect(); const ge=document.getElementById('navSettings'); const rg=document.createRange(); rg.selectNodeContents(ge); const gg=rg.getBoundingClientRect(); const ls=[...document.querySelectorAll('#composerRight .csq:not(#composerStop) .lucide')].map(e=>Math.round(e.getBoundingClientRect().left)); const steps=ls.slice(1).map((x,i)=>x-ls[i]); const gw=Math.round(document.querySelector('#composerRight .csq .lucide svg').getBoundingClientRect().width); return {dL:Math.round(cl.left-pv.left), dR:Math.round(cl.right-gg.right), rowH:Math.round(cl.height), steps, gw}; });
   ok(`R2 cluster.left == #mPrev.left ±2 && cluster.right == ⚙ glyph.right ±2 (supersedes R's ±6 inset off #media/⚙ box), even spread, 26px glyphs, rowH 32 (${state})`, Math.abs(c.dL)<=2 && Math.abs(c.dR)<=2 && c.rowH===32 && c.steps.length===3 && Math.max(...c.steps)-Math.min(...c.steps)<=1 && c.gw===26, JSON.stringify(c)); }
 await p.setViewportSize({width:W-100,height:H}); await p.waitForTimeout(400);
 ok('R2 realigns on resize (prev.left / ⚙ glyph.right ±2; −100px — below ~900px the nav itself overflows the viewport, pre-existing)', await p.evaluate(()=>{ const cl=document.getElementById('composerRight').getBoundingClientRect(); const ge=document.getElementById('navSettings'); const rg=document.createRange(); rg.selectNodeContents(ge); return Math.abs(cl.left-document.getElementById('mPrev').getBoundingClientRect().left)<=2 && Math.abs(cl.right-rg.getBoundingClientRect().right)<=2; }), await p.evaluate(()=>{ const ge=document.getElementById('navSettings'); const rg=document.createRange(); rg.selectNodeContents(ge); return JSON.stringify({vw:innerWidth, gearInkR:Math.round(rg.getBoundingClientRect().right), clL:Math.round(document.getElementById('composerRight').getBoundingClientRect().left), clR:Math.round(document.getElementById('composerRight').getBoundingClientRect().right), prevL:Math.round(document.getElementById('mPrev').getBoundingClientRect().left)}); }));
 await p.setViewportSize({width:W,height:H}); await p.waitForTimeout(300);

 // ---- O: every hover label (.cap) sits ≥2px BELOW the overline and at the same y as the voice cluster's labels; labels anchor to the line, not the glyph ----
 await p.mouse.move(300,30); await p.waitForTimeout(250);
 const o0=await p.evaluate(()=>{ const ol=document.getElementById('senterOverline').getBoundingClientRect(); const caps=[...document.querySelectorAll('#composerRow .csq:not(#composerStop)')].map(b=>{ const c=b.querySelector('.cap'); c.style.opacity='1'; const t=Math.round(c.getBoundingClientRect().top); c.style.opacity=''; return {k:b.dataset.k, top:t, btnH:Math.round(b.getBoundingClientRect().height)}; }); return {olBottom:Math.round(ol.bottom), caps}; });
 ok('O + / auto labels ≥2px below the overline, same top as the voice labels, all buttons 32px', o0.caps.every(c=>c.top>=o0.olBottom+2 && c.btnH===32) && new Set(o0.caps.map(c=>c.top)).size===1, JSON.stringify(o0));
 const o1=await p.evaluate(()=>{ const lift=b=>{ const r=b.getBoundingClientRect(); const g=b.querySelector('.lucide, .pillBox').getBoundingClientRect(); return Math.round((r.top+r.height/2)-(g.top+g.height/2)); }; return {plus:lift(document.querySelector('.csq[data-k=context]')), pill:lift(document.querySelector('.model-pill'))}; });
 ok('O + / auto glyphs still lifted 4–6px inside their fixed-height buttons (J kept)', o1.plus>=4 && o1.plus<=6 && o1.pill>=4 && o1.pill<=6, JSON.stringify(o1));
 await rest();

 // ---- P: the overline fades with the input row on nav-tab hover (same class, .12s), restores with it ----
 await p.mouse.move(300,30); await p.waitForTimeout(250);
 await p.mouse.move(wiki.x,wiki.y); await p.waitForTimeout(220);
 const p0=await p.evaluate(()=>{ const ol=getComputedStyle(document.getElementById('senterOverline')); const row=getComputedStyle(document.getElementById('composerRow')); return {olOp:ol.opacity, olT:ol.transitionDuration, rowOp:row.opacity, on:document.getElementById('topstrip').classList.contains('on')}; });
 ok('P hover WIKI → overline opacity 0 with the row (.12s), strip open', p0.olOp==='0' && p0.rowOp==='0' && /0\.12s/.test(p0.olT) && p0.on, JSON.stringify(p0));
 await p.mouse.move(300,38); await p.waitForTimeout(220);
 const p1=await p.evaluate(()=>{ const ol=document.getElementById('senterOverline'); return {olOp:getComputedStyle(ol).opacity, w:Math.round(ol.getBoundingClientRect().width), rowOp:getComputedStyle(document.getElementById('composerRow')).opacity}; });
 ok('P back on the row → overline opacity 1, full width, row 1', p1.olOp==='1' && p1.w===W && p1.rowOp==='1', JSON.stringify(p1));
 await rest();

 // ---- Q (v14.41): ALLOW ▾ on the LAST stream card flips UP (.up) so menu.bottom ≤ innerHeight−8 and ≤ #stream's clip edge; every option elementFromPoint-hittable; close restores state ----
 const q0=await p.evaluate(()=>{
   const s=document.getElementById('stream'); const id='q-ledger';
   s.insertAdjacentHTML('beforeend','<div class="msg approval" data-aid="'+id+'" data-who="klerik" data-when="12:00"><img class="avatar sm" src="assets/avatars/klerik.png"><span class="who">klerik</span><div class="txt">wants approval · protected write<div class="cmd">write SOUL.md</div></div><div class="aacts"><span class="allow-group"><button class="allow-main" data-choice="once">ALLOW</button><button class="allow-caret" data-toggle>▾</button><span class="allow-menu"><button data-choice="once">Allow</button><button data-choice="session">Allow this session</button><button data-choice="always">Always allow</button></span></span><button data-a="deny">DENY</button></div></div>');
   document.getElementById('chat').classList.add('open'); s.scrollTop=s.scrollHeight;
   const card=s.querySelector('[data-aid="q-ledger"]'); card.querySelector('.allow-caret').click();
   const menu=card.querySelector('.allow-menu'); const m=menu.getBoundingClientRect(); const sr=s.getBoundingClientRect();
   const hits=[...menu.querySelectorAll('button')].map(o=>{ const r=o.getBoundingClientRect(); return document.elementFromPoint(r.left+r.width/2, r.top+r.height/2)===o; });
   const open=card.querySelector('.allow-group').classList.contains('open'), up=menu.classList.contains('up');
   document.body.click(); const after={open:document.querySelectorAll('.allow-group.open').length, up:document.querySelectorAll('.allow-menu.up').length, pads:document.querySelectorAll('[data-menu-pad]').length};
   card.remove(); document.getElementById('chat').classList.remove('open');
   return {open, up, mTop:Math.round(m.top), mBottom:Math.round(m.bottom), streamBottom:Math.round(sr.bottom), ih:innerHeight, hits, after};
 });
 ok('Q last-card ALLOW ▾ menu flips up: bottom ≤ innerHeight−8 and ≤ #stream edge, top ≥ 0', q0.open && q0.up && q0.mBottom<=q0.ih-8 && q0.mBottom<=q0.streamBottom && q0.mTop>=0, JSON.stringify(q0));
 ok('Q all three menu options hittable (elementFromPoint) + close leaves no .open/.up/padding', q0.hits.length===3 && q0.hits.every(Boolean) && q0.after.open===0 && q0.after.up===0 && q0.after.pads===0, JSON.stringify({hits:q0.hits, after:q0.after}));

 // ---- R (v14.41) lift kept; R2 (v14.42) edges: glyph ink ≥6px above the overline (lift on .lucide, buttons/labels still anchored to the line), cluster box edges ON #mPrev.left / ⚙ glyph ink right (±2), ink stays inside both, even spread kept ----
 await p.mouse.move(300,30); await p.waitForTimeout(250);
 const r0=await p.evaluate(()=>{ const q=s=>document.querySelector(s).getBoundingClientRect(); const ol=q('#senterOverline'), pv=q('#mPrev'), cl=q('#composerRight'); const ge=document.getElementById('navSettings'); const rg=document.createRange(); rg.selectNodeContents(ge); const gg=rg.getBoundingClientRect(); const gl=[...document.querySelectorAll('#composerRight .csq:not(#composerStop) .lucide svg')].map(e=>e.getBoundingClientRect()); const steps=gl.slice(1).map((r,i)=>Math.round(r.left-gl[i].left)); const caps=[...document.querySelectorAll('#composerRight .csq:not(#composerStop)')].map(b=>{ const c=b.querySelector('.cap'); c.style.opacity='1'; const t=Math.round(c.getBoundingClientRect().top); c.style.opacity=''; return {btnBottom:Math.round(b.getBoundingClientRect().bottom), capTop:t}; }); return {olY:Math.round(ol.top), glyphBottom:Math.round(Math.max(...gl.map(r=>r.bottom))), dL:Math.round(cl.left-pv.left), dR:Math.round(cl.right-gg.right), inkL:Math.round(Math.min(...gl.map(r=>r.left))-pv.left), inkR:Math.round(gg.right-Math.max(...gl.map(r=>r.right))), steps, caps}; });
 ok('R glyph.bottom ≤ overline.y−6 (lifted off the line)', r0.glyphBottom<=r0.olY-6, JSON.stringify({olY:r0.olY, glyphBottom:r0.glyphBottom}));
 ok('R2 cluster.left == #mPrev.left ±2 && cluster.right == ⚙ glyph.right ±2; ink inside both anchors; even spread (replaces R ±6 inset)', Math.abs(r0.dL)<=2 && Math.abs(r0.dR)<=2 && r0.inkL>=0 && r0.inkR>=0 && Math.max(...r0.steps)-Math.min(...r0.steps)<=1, JSON.stringify({dL:r0.dL, dR:r0.dR, inkL:r0.inkL, inkR:r0.inkR, steps:r0.steps}));
 ok('R buttons still bottom on the line, labels still at line+5 (O rule kept under the lift)', r0.caps.every(c=>c.btnBottom===r0.olY && c.capTop===r0.olY+6), JSON.stringify(r0.caps));
 await rest();

 // ---- T (v14.44): model ▾ + `+` popups anchor under THEIR OWN button (left == btn.left ±2, top == btn.bottom+6 ±2), inside the viewport, every option hittable; flip UP (.up, bottom == btn.top−6) only when the menu would cross innerHeight−8; close clears .on/.up/inline pos/.popupOpen ----
 await p.mouse.move(600,4); await p.mouse.move(600,30); await p.waitForTimeout(300);
 const tT=await p.evaluate(()=>{
   const R=e=>{ const b=e.getBoundingClientRect(); return {l:Math.round(b.left),t:Math.round(b.top),r:Math.round(b.right),b:Math.round(b.bottom),h:Math.round(b.height)}; };
   const one=k=>{ const btn=document.querySelector('#composerRow .csq[data-k="'+k+'"]'), pop=document.getElementById('popup-'+k); btn.click(); const bb=R(btn), pb=R(pop); const hits=[...pop.querySelectorAll('button')].map(o=>{ const r=o.getBoundingClientRect(); const el=document.elementFromPoint(r.left+r.width/2, r.top+r.height/2); return el===o||o.contains(el); }); const out={dl:pb.l-bb.l, dt:pb.t-(bb.b+6), inVp:pb.b<=innerHeight-8&&pb.r<=innerWidth-8, up:pop.classList.contains('up'), hits, popupOpen:document.getElementById('topstrip').classList.contains('popupOpen')}; document.body.click(); return out; };
   const model=one('model'), context=one('context');
   // synthetic overflow: park the row near the bottom so pill.bottom+6+menu.h > innerHeight, then place
   const s=document.getElementById('topstrip'), row=document.getElementById('composerRow'); const keep={h:s.style.height, cp:s.style.clipPath, top:row.style.top};
   s.style.height=innerHeight+'px'; s.style.clipPath='inset(0)'; row.style.top=(innerHeight-90)+'px';
   const btn=document.querySelector('#composerRow .csq[data-k="model"]'), pop=document.getElementById('popup-model'); btn.click(); const bb=R(btn), pb=R(pop);
   const flip={up:pop.classList.contains('up'), dBottom:pb.b-(bb.t-6), fits:pb.b<=innerHeight-8&&pb.t>=0, hits:[...pop.querySelectorAll('button')].map(o=>{ const r=o.getBoundingClientRect(); const el=document.elementFromPoint(r.left+r.width/2, r.top+r.height/2); return el===o||o.contains(el); })};
   document.body.click(); s.style.height=keep.h; s.style.clipPath=keep.cp; row.style.top=keep.top;
   const after={on:document.querySelectorAll('.csqPopup.on').length, up:document.querySelectorAll('.csqPopup.up').length, pos:[...document.querySelectorAll('.csqPopup')].filter(e=>e.style.left||e.style.top).length, popupOpen:s.classList.contains('popupOpen')};
   return {model, context, flip, after};
 });
 ok('T model ▾ menu anchored under the pill: left == pill.left ±2, top == pill.bottom+6 ±2, in viewport, all options hittable, strip un-clipped while open', Math.abs(tT.model.dl)<=2 && Math.abs(tT.model.dt)<=2 && tT.model.inVp && !tT.model.up && tT.model.hits.length>0 && tT.model.hits.every(Boolean) && tT.model.popupOpen, JSON.stringify(tT.model));
 ok('T + menu anchored under +: left == +.left ±2, top == +.bottom+6 ±2, in viewport, all options hittable', Math.abs(tT.context.dl)<=2 && Math.abs(tT.context.dt)<=2 && tT.context.inVp && tT.context.hits.length===4 && tT.context.hits.every(Boolean), JSON.stringify(tT.context));
 ok('T flip: when the menu would cross innerHeight−8 it opens UP (.up, bottom == pill.top−6 ±2), fits, hittable; close clears .on/.up/inline pos/.popupOpen', tT.flip.up && Math.abs(tT.flip.dBottom)<=2 && tT.flip.fits && tT.flip.hits.every(Boolean) && tT.after.on===0 && tT.after.up===0 && tT.after.pos===0 && !tT.after.popupOpen, JSON.stringify({flip:tT.flip, after:tT.after}));
 await rest();

 // ---- U: input-row hover captions readable — absolute 13px (≥ the wiki-row orb caption, ≥13 floor), still one row at line+5 (O), every string non-empty ----
 await p.mouse.move(300,30); await p.waitForTimeout(250);
 const u0=await p.evaluate(()=>{ const ol=document.getElementById('senterOverline').getBoundingClientRect(); const orb=document.querySelector('#view-wiki .topic .thead .orb'); const orbPx=orb?parseFloat(getComputedStyle(orb,'::before').fontSize):0; const caps=[...document.querySelectorAll('#composerRow .csq:not(#composerStop)')].map(b=>{ const c=b.querySelector('.cap'); c.style.opacity='1'; const r=c.getBoundingClientRect(); const px=parseFloat(getComputedStyle(c).fontSize); c.style.opacity=''; return {k:b.dataset.k, px:+px.toFixed(2), top:Math.round(r.top), text:c.textContent.trim()}; }); return {olY:Math.round(ol.top), orbPx:+orbPx.toFixed(2), caps}; });
 ok('U six captions ≥13px rendered AND ≥ orb caption px (was 6.9 / 5.2 under the pill)', u0.caps.length===6 && u0.caps.every(c=>c.px>=13 && c.px>=u0.orbPx && c.text.length>0), JSON.stringify({orbPx:u0.orbPx, px:u0.caps.map(c=>c.px)}));
 ok('U captions still one row at overline+6 (O anchor kept under the size bump)', u0.caps.every(c=>c.top===u0.olY+6), JSON.stringify(u0.caps.map(c=>[c.k,c.top])));
 await rest();

 // ---- Z (v14.50): NO dead space above the hero at rest. Baseline = v14.11 (assets/senter-wiki-default-layout.png, pane top y=92 → title ink at y=122 → ink 30px below the top; .hero padding-top 26 + 4px ink offset). Closed strip must add ZERO layout height (fixed overlay); #17 hit zone y=10–60 still opens at x=900; the title ink itself never opens. ----
 await p.evaluate(()=>{ if(typeof showView==='function') showView('wiki'); }); await p.waitForTimeout(400); await rest();
 const z0=await p.evaluate(()=>{ const h=document.getElementById('hero'); const ht=document.getElementById('heroTitle'); const rg=document.createRange(); rg.selectNodeContents(ht); const ink=rg.getBoundingClientRect(); const s=document.getElementById('topstrip'); const cs=getComputedStyle(s); const pads=['view-wiki','view-feed','view-skills','view-bots','view-player'].map(id=>{ const v=document.getElementById(id); const hh=v&&v.querySelector('.hero'); return hh?parseFloat(getComputedStyle(hh).paddingTop):null; }); return {heroTop:Math.round(h.getBoundingClientRect().top), titleTop:Math.round(ht.getBoundingClientRect().top), inkTop:Math.round(ink.top), inkH:Math.round(ink.height), stripPos:cs.position, pads, edPad:parseFloat(getComputedStyle(document.getElementById('edHero')).paddingTop)}; });
 ok('Z hero.top == 0, title block top == 26, title ink top == 30 (v14.11 baseline; was 74/78)', z0.heroTop===0 && z0.titleTop===26 && z0.inkTop===30 && z0.inkH>0, JSON.stringify(z0));
 ok('Z every view hero padding-top == 26 == #edHero (one baseline, strip position:fixed)', z0.pads.every(v=>v===26) && z0.edPad===26 && z0.stripPos==='fixed', JSON.stringify({pads:z0.pads, edPad:z0.edPad, stripPos:z0.stripPos}));
 const zh=[]; for(const y of [10,30,50,60]){ await rest(); await p.mouse.move(900,y); await p.waitForTimeout(250); zh.push([y,await on()]); }
 ok('Z #17 hit zone survives: x=900 y=10/30/50/60 all open', zh.every(o=>o[1]), JSON.stringify(zh));
 await rest();

 // ---- S (v14.47): unified hover cards on wiki rows — orbs + integration logos: 12px rise + caption, one hairline .hcard centred on the icon (±2), fits viewport, 220px body with inner fade, wheel scrolls the card not the page, 250ms grace icon→card, dead zone suppresses, click-through unchanged, no dummy data (empty → "— none yet —") ----
 { await p.evaluate(()=>{ try{ closeEditor(false); }catch(e){} showView('wiki'); }); await rest();   /* S owns its own starting state: wiki view on, strip closed — earlier blocks may leave the page viewless */
   const trow=await p.evaluate(()=>{ const t=[...document.querySelectorAll('#view-wiki .topic')].find(x=>x.querySelector('.tname').textContent.trim().toLowerCase()==='turbofit'); const r=t.querySelector('.thead').getBoundingClientRect(); return {x:Math.round(r.left+60), y:Math.round(r.top+r.height/2)}; });
   await p.mouse.move(trow.x,trow.y); await p.waitForTimeout(350);
   const sIcons=await p.evaluate(()=>{ const t=[...document.querySelectorAll('#view-wiki .topic')].find(x=>x.querySelector('.tname').textContent.trim().toLowerCase()==='turbofit'); return t._hcard.icons.map(ic=>{ const r=ic.getBoundingClientRect(); return {id:ic.dataset.k||ic.dataset.kind, x:Math.round(r.left+r.width/2), y:Math.round(r.top+r.height/2)}; }); });
   const per=[]; const DEAD=W-478;
   for(const ic of sIcons){ if(ic.x>DEAD) continue;   /* logos inside the dead lane at narrow viewports must NOT card — covered by the dead-zone check below */
     const rest=await p.evaluate(({x,y})=>{ const el=document.elementFromPoint(x,y); const ico=el&&el.closest('.orb,.iwrap'); if(!ico) return null; const g=ico.classList.contains('iwrap')?ico.querySelector('.idot'):ico; const r=g.getBoundingClientRect(); const m=new DOMMatrixReadOnly(getComputedStyle(g).transform); return r.top-(m.m42||0); },ic);
     await p.mouse.move(ic.x,ic.y); await p.waitForTimeout(420);
     per.push(await p.evaluate(({id,rest})=>{ const t=[...document.querySelectorAll('#view-wiki .topic')].find(x=>x.querySelector('.tname').textContent.trim().toLowerCase()==='turbofit'); const card=t.querySelector('.hcard'), box=card.querySelector('.hbox'), body=card.querySelector('.hbody');
       const ico=t.querySelector('.orb.hov,.iwrap.hov'); const g=ico&&(ico.classList.contains('iwrap')?ico.querySelector('.idot'):ico); const ir=ico?ico.getBoundingClientRect():null; const br=box.getBoundingClientRect();
       const cap=ico? (ico.classList.contains('orb')? getComputedStyle(ico,'::before').opacity : getComputedStyle(ico.querySelector('.icap')).opacity) : '0';
       const laneL=innerWidth-478;   /* the fleet-stream lane (#chat, fixed z 50) owns the right 478px by design (v13 dead zone) — a card edge that reaches under it is not occluded wrongly */
       const onTop=[0.25,0.5,0.75].every(fx=>[0.3,0.6,0.9].every(fy=>{ const x=br.left+br.width*fx; if(x>=laneL) return true; const e=document.elementFromPoint(x, br.top+br.height*fy); return !!(e&&e.closest('.hcard')); }));
       const rows=body.querySelectorAll('.hrow,.hp,.ilink').length, none=body.querySelectorAll('.hrow.none').length;
       return {id, shown:card.classList.contains('show')&&card.classList.contains('in'), rise:g&&rest!=null?Math.round(rest-g.getBoundingClientRect().top):null, cap:+cap, dx:ir?Math.round((br.left+br.width/2)-(ir.left+ir.width/2)):null, inVP:br.left>=0&&br.top>=0&&br.right<=innerWidth&&br.bottom<=innerHeight, onTop, hairline:getComputedStyle(box).borderTopWidth==='1px'&&getComputedStyle(box).backgroundColor==='rgb(0, 0, 0)', maxH:getComputedStyle(body).maxHeight, rows, none}; },{id:ic.id,rest})); }
   ok('S every orb + logo on TURBOFIT: rise 12 + caption + card shown, hairline black, centred ±2, in viewport, on top', per.length>=6 && per.every(c=>c.shown&&c.rise===12&&c.cap===1&&Math.abs(c.dx)<=2&&c.inVP&&c.onTop&&c.hairline&&c.maxH==='220px'), JSON.stringify(per.map(c=>[c.id,c.rise,c.dx,c.onTop,c.shown,c.cap,c.inVP,c.hairline,c.maxH])));
   ok('S content is vault data or one "— none yet —" row (no dummy): ctx≥1 line, skills 2 (turbofit/skills/*), bots+loops empty → none row', per.find(c=>c.id==='ctx').rows>=1 && per.find(c=>c.id==='skills').rows===2 && per.find(c=>c.id==='agents').none===1 && per.find(c=>c.id==='loops').none===1, JSON.stringify(per.map(c=>[c.id,c.rows,c.none])));
   const sk=sIcons.find(i=>i.id==='skills'); await p.mouse.move(trow.x,trow.y); await p.waitForTimeout(300);
   const sc=await p.evaluate(async()=>{ const t=[...document.querySelectorAll('#view-wiki .topic')].find(x=>x.querySelector('.tname').textContent.trim().toLowerCase()==='turbofit'); const card=t.querySelector('.hcard'), body=card.querySelector('.hbody'); t.querySelector('.orb[data-k=skills]').dispatchEvent(new MouseEvent('mouseenter')); await new Promise(r=>setTimeout(r,300));
     body.innerHTML=Array.from({length:12},(_,i)=>'<div class="hrow"><span class="nm">probe-'+(i+1)+'</span></div>').join(''); body.dispatchEvent(new Event('scroll')); const fade0=/gradient/.test(getComputedStyle(body).webkitMaskImage)&&!body.classList.contains('fits');
     const view=document.getElementById('view-wiki'); const pv=view.scrollTop; card.dispatchEvent(new WheelEvent('wheel',{deltaY:120,bubbles:true,cancelable:true})); await new Promise(r=>setTimeout(r,50));
     const r={scrollable:body.scrollHeight>body.clientHeight+1, moved:body.scrollTop>0, pageMoved:view.scrollTop!==pv, fade0}; body.scrollTop=1e5; body.dispatchEvent(new Event('scroll')); r.fadeGoneAtEnd=!/gradient/.test(getComputedStyle(body).webkitMaskImage); return r; });
   ok('S ≥8 items: body scrolls (220 cap), wheel scrolls the card not the page, fade present mid-list and gone at the end', sc.scrollable&&sc.moved&&!sc.pageMoved&&sc.fade0&&sc.fadeGoneAtEnd, JSON.stringify(sc));
   await p.mouse.move(sk.x,sk.y); await p.waitForTimeout(420); const cb=await p.evaluate(()=>{ const c=document.querySelector('#view-wiki .hcard.show .hbox').getBoundingClientRect(); return {x:Math.round(c.left+c.width/2), y:Math.round(c.top+40)}; });
   await p.mouse.move(cb.x,cb.y,{steps:4}); await p.waitForTimeout(300); const onCard=await p.evaluate(()=>!!document.querySelector('#view-wiki .hcard.show.in'));
   await p.mouse.move(trow.x,trow.y+220,{steps:3}); await p.waitForTimeout(150); const at150=await p.evaluate(()=>!!document.querySelector('#view-wiki .hcard.show.in')); await p.waitForTimeout(400); const at550=await p.evaluate(()=>!document.querySelector('#view-wiki .hcard.show'));
   ok('S grace: icon→card keeps it open; leaving both closes after 250ms grace (+100ms out)', onCard&&at150&&at550, JSON.stringify({onCard,at150,at550}));
   await p.mouse.move(W-100,trow.y); await p.waitForTimeout(250); const dz=await p.evaluate(()=>({dead:document.body.classList.contains('deadzone'), cards:document.querySelectorAll('#view-wiki .hcard.show').length}));
   ok('S dead zone: no card in the right lane', dz.dead&&dz.cards===0, JSON.stringify(dz));
   await p.mouse.move(trow.x,trow.y); await p.waitForTimeout(300); await p.mouse.move(sk.x,sk.y); await p.waitForTimeout(300); await p.mouse.click(sk.x,sk.y); await p.waitForTimeout(600);
   const ck=await p.evaluate(()=>({ed:document.getElementById('view-editor').classList.contains('on'), title:document.getElementById('edTitle').textContent}));
   ok('S click-through unchanged: skills orb click opens the editor', ck.ed&&ck.title==='turbofit', JSON.stringify(ck));
   await p.evaluate(()=>{ closeEditor(false); showView('wiki'); }); await p.waitForTimeout(300); await rest(); }

 // ---- Y (v14.48): NO BAKED COLLECTIONS — BOTS/SKILLS render from .system-live.json via loadLive(); rows === profiles with SOUL.md ----
 { const fsY=require('fs'), osY=require('os'); const PROF=require('path').join(osY.homedir(),'.hermes','profiles');
   const souls=fsY.readdirSync(PROF).filter(d=>fsY.existsSync(require('path').join(PROF,d,'SOUL.md'))).length;
   try{ require('child_process').execSync('python3 '+JSON.stringify(require('path').resolve(__dirname,'scan-topics.py')),{stdio:'ignore'}); await p.evaluate(()=>loadLive('ledger')); }catch(e){} // fresh snapshot (the watcher does this live; the ledger must not depend on it running)
   await p.waitForFunction(()=>document.querySelectorAll('#bots-list .topic').length>0,{timeout:8000}).catch(()=>{});
   const y=await p.evaluate(()=>({ rows:document.querySelectorAll('#bots-list .topic').length, names:[...document.querySelectorAll('#bots-list .topic')].map(t=>t.dataset.bot), skills:document.querySelectorAll('#skills-list .topic').length, baked:(typeof LIVE_BOTS!=='undefined')||(typeof LIVE_SKILLS!=='undefined'), loader:typeof window.loadLive==='function', dots:document.querySelectorAll('#bots-list .ldot').length, meta:document.querySelector('#view-bots .heroMeta').textContent }));
   ok('Y bots-row-count === profiles-with-SOUL count ('+souls+'), incl. weaver + paladin', y.rows===souls && y.names.includes('weaver') && y.names.includes('paladin'), JSON.stringify(y.names));
   ok('Y no baked LIVE_BOTS/LIVE_SKILLS; loadLive() present; SKILLS ≥118 live rows; a status dot per bot row; hero meta labeled LIVE SCAN or CACHED', !y.baked && y.loader && y.skills>=118 && y.dots===y.rows && /LIVE SCAN|CACHED · \d+[smh] AGO/.test(y.meta), y.skills+' skills · '+y.meta); }

 // ---- AA (v14.46): pending approval cards are PINNED at the growth edge — stream: bottom, sticky. Inject pending → 3 notify() → bbox unchanged, still bottom-most, messages above; decide → unpins into the flow (block keeps a second pending) ----
 const aa=await p.evaluate(async ()=>{
   const rect=e=>{ const r=e.getBoundingClientRect(); return [Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)].join(','); };
   const card=(id,who)=>'<div class="msg approval" data-aid="'+id+'" data-who="'+who+'" data-when="12:00"><img class="avatar sm" src="assets/avatars/'+who+'.png"><span class="who">'+who+'</span><div class="txt">wants approval · protected write<div class="cmd">write SOUL.md</div></div><div class="aacts"><span class="allow-group"><button class="allow-main" data-choice="once">ALLOW</button><button class="allow-caret" data-toggle>▾</button><span class="allow-menu"><button data-choice="once">Allow</button></span></span><button data-a="deny">DENY</button></div></div>';
   const tick=()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const chat=document.getElementById('chat'), s=document.getElementById('stream'); chat.classList.add('open'); s.scrollTop=s.scrollHeight; await tick();
   s.insertAdjacentHTML('beforeend',card('aa-ledger-1','klerik')); s.scrollTop=s.scrollHeight; await tick();
   const c1=s.querySelector('[data-aid="aa-ledger-1"]'); const before=rect(c1);
   for(let i=0;i<3;i++) notify('turbosovth','AA ledger message '+i); await tick();
   const after=rect(c1); const last=s.lastElementChild; const bottomMost=last.classList.contains('pinblock')&&last.lastElementChild===c1;
   const msgs=[...s.querySelectorAll(':scope > .msg')].filter(m=>m.textContent.includes('AA ledger message')); const above=msgs.length===3&&msgs.every(m=>m.getBoundingClientRect().bottom<=c1.getBoundingClientRect().top);
   s.insertAdjacentHTML('beforeend',card('aa-ledger-2','paladin')); await tick(); const c2=s.querySelector('[data-aid="aa-ledger-2"]'); const stacked=c2.parentElement===c1.parentElement&&c1.nextElementSibling===c2;
   s.scrollTop=0; await tick(); const sr=s.getBoundingClientRect(), br=c1.parentElement.getBoundingClientRect(); const sticky=br.bottom<=sr.bottom+1&&br.top>=sr.top; s.scrollTop=s.scrollHeight;
   c1.dataset.settle='1'; c1.classList.add('dissipating'); await tick(); // what dissipate() does on decide; the observer keys on these
   const unpinned=c1.parentElement===s&&c1.nextElementSibling===c2.parentElement&&c2.parentElement.classList.contains('pinblock');
   c1.remove(); c2.remove(); msgs.forEach(m=>m.remove()); chat.classList.remove('open');
   return {same:before===after, before, after, bottomMost, above, stacked, sticky, unpinned};
 });
 ok('AA pending card PINNED: 3 new messages → bbox unchanged + still bottom-most, messages above; 2nd pending stacks in arrival order; block sticky at scrollTop 0; decided → unpins into the flow', aa.same&&aa.bottomMost&&aa.above&&aa.stacked&&aa.sticky&&aa.unpinned, JSON.stringify(aa));

 // (open the strip from the top edge right of the hero title — after Z the title can sit under y=30 and hovering it keeps the strip closed by design)
 // ---- V (v14.44): type-ahead TAGS above the nav — live candidates (wiki rows + window.LIVE skills/bots/loops + rail integrations), ≤8, ranked prefix>word-start>substring>desc; row sits between the overline and the nav lettering and GROWS the strip (never overlaps the tabs); click → the item's own view; ↑↓ Enter Esc; empty → gone ----
 await p.mouse.move(900,6); await p.waitForTimeout(300);
 const v0=await p.evaluate(()=>{ const m=q=>window._tagAhead.match(q).map(c=>c.kind+'·'+c.name); return {turb:m('turb'), wea:m('wea'), n:window._tagAhead.match('e').length, empty:window._tagAhead.match('   ').length}; });
 ok('V match("turb") ⊇ {topic·turbofit, skill·turbofit, bot·turbosovth}; topic·turbofit ranked first; ≤8; empty → none', ['topic·turbofit','skill·turbofit','bot·turbosovth'].every(x=>v0.turb.includes(x)) && v0.turb[0]==='topic·turbofit' && v0.turb.length<=8 && v0.n<=8 && v0.empty===0, JSON.stringify(v0));
 ok('V match("wea")[0] === bot·weaver (prefix beats description hits)', v0.wea[0]==='bot·weaver', JSON.stringify(v0.wea));
 await p.keyboard.type('turb'); await p.waitForTimeout(160);
 const v1=await p.evaluate(()=>{ const s=document.getElementById('topstrip'), r=document.getElementById('tagRow').getBoundingClientRect(), ol=document.getElementById('senterOverline').getBoundingClientRect(); const tabs=[...document.querySelectorAll('.navtab')].map(t=>t.getBoundingClientRect()); const tags=[...document.querySelectorAll('#tagRow .tta')]; const hit=tags.every(b=>{ const x=b.getBoundingClientRect(); const e=document.elementFromPoint(x.left+x.width/2,x.top+x.height/2); return e&&e.closest('.tta')===b; }); const kfs=tags.length?parseFloat(getComputedStyle(tags[0].querySelector('.k')).fontSize):0; return {on:s.classList.contains('on'), tags:tags.length, rowTop:Math.round(r.top), rowBottom:Math.round(r.bottom), olY:Math.round(ol.top), tabTop:Math.round(Math.min(...tabs.map(t=>t.top))), stripH:Math.round(s.getBoundingClientRect().height), hit, kfs}; });
 ok('V typed "turb" → tag row BELOW the overline and ABOVE every nav tab (no overlap), strip grew to fit (190 + row), every tag elementFromPoint-hittable, kind label ≥13px', v1.on && v1.tags>=3 && v1.rowTop>v1.olY && v1.rowBottom<v1.tabTop && v1.stripH>190 && v1.stripH>=v1.rowBottom+40 && v1.hit && v1.kfs>=13, JSON.stringify(v1));
 await p.keyboard.press('ArrowDown'); await p.waitForTimeout(60); await p.keyboard.press('ArrowDown'); await p.waitForTimeout(60);
 const v2=await p.evaluate(()=>({sel:window._tagAhead.sel(), selClass:[...document.querySelectorAll('#tagRow .tta')].findIndex(b=>b.classList.contains('sel'))}));
 ok('V ↑↓ move the selection (two ↓ → index 1, .sel on that tag)', v2.sel===1 && v2.selClass===1, JSON.stringify(v2));
 await p.keyboard.press('Escape'); await p.waitForTimeout(120);
 const v3=await p.evaluate(()=>({tags:document.querySelectorAll('#tagRow .tta').length, cls:document.getElementById('topstrip').classList.contains('tags'), h:Math.round(document.getElementById('topstrip').getBoundingClientRect().height), txt:document.getElementById('senterHiddenInput').value, on:document.getElementById('topstrip').classList.contains('on')}));
 ok('V Esc hides the tags (strip back to 190, text kept, strip still open)', v3.tags===0 && !v3.cls && v3.h===190 && v3.txt==='turb' && v3.on, JSON.stringify(v3));
 await p.keyboard.type('o'); await p.waitForTimeout(160); // typing again re-shows
 const v4=await p.evaluate(()=>{ const b=[...document.querySelectorAll('#tagRow .tta')].find(x=>x.dataset.kind==='bot'&&x.dataset.name==='turbosovth'); if(!b) return null; b.click(); return true; }); await p.waitForTimeout(500);
 const v5=await p.evaluate(()=>({view:document.querySelector('.view.on')?.id, title:document.getElementById('edTitle')?.textContent.trim(), hash:location.hash, input:document.getElementById('senterHiddenInput').value, tags:document.querySelectorAll('#tagRow .tta').length, botsTab:document.querySelector('.navtab[data-view="bots"]').classList.contains('on')}));
 ok('V click bot·turbosovth → BOTS tab + editor "turbosovth" (#bots/turbosovth, same path as the BOTS row), input cleared, tags gone', v4===true && v5.view==='view-editor' && v5.title==='turbosovth' && v5.hash==='#bots/turbosovth' && v5.input==='' && v5.tags===0 && v5.botsTab, JSON.stringify(v5));
 await p.keyboard.press('Escape'); await p.waitForTimeout(200); await p.mouse.move(900,6); await p.waitForTimeout(300); await p.keyboard.type('wea'); await p.waitForTimeout(160); await p.keyboard.press('ArrowDown'); await p.waitForTimeout(60); await p.keyboard.press('Enter'); await p.waitForTimeout(500);
 const v6=await p.evaluate(()=>({view:document.querySelector('.view.on')?.id, title:document.getElementById('edTitle')?.textContent.trim(), hash:location.hash, chrisPosts:document.querySelectorAll('#stream .msg[data-who="chris"]').length}));
 ok('V "wea" ↓ Enter → bot·weaver opens (editor "weaver", #bots/weaver) and nothing was SENT as a message', v6.view==='view-editor' && v6.title==='weaver' && v6.hash==='#bots/weaver' && v6.chrisPosts===0, JSON.stringify(v6));
 await p.keyboard.press('Escape'); await p.waitForTimeout(200); await rest();
 ok('V rest: strip closed, 190px, hero at 0 (zero-flow kept)', await p.evaluate(()=>{ const s=document.getElementById('topstrip'); return !s.classList.contains('on') && Math.round(s.getBoundingClientRect().height)===190 && Math.round(document.querySelector('.view.on .hero, #hero').getBoundingClientRect().top)===0; }));

 // ---- URGENT AUTOSAVE: bot page open + idle + close via \ / Esc / tab → ZERO /ask write posts; a real edit → exactly one ----
 { const asks=[]; await p.route('**/ask**', r=>{ asks.push(JSON.parse(r.request().postData()||'{}')); r.fulfill({status:202,contentType:'application/json',body:'{"ok":true,"id":"ledger"}'}); });
   const loadedW=()=>p.evaluate(()=>new Promise(r=>{ const s=window.edW&&window.edW.state(); if(s&&s.ready) return r(true); document.addEventListener('edW:loaded',()=>r(true),{once:true}); setTimeout(()=>r(false),8000); }));
   const openBotW=async n=>{ await p.evaluate(()=>document.querySelector('.navtab[data-view="bots"]').click()); await p.waitForTimeout(150); await p.evaluate(n=>{ const row=[...document.querySelectorAll('#bots-list .topic')].find(t=>t.dataset.bot===n); row&&row.querySelector('.thead').click(); },n); return loadedW(); };
   ok('AUTOSAVE: bot page loads', await openBotW('turbosovth'));
   for(let i=0;i<16;i++){ await p.mouse.move(200+i*30, 100+(i*41)%600); await p.waitForTimeout(500); }
   await p.evaluate(()=>document.getElementById('edBack').click()); await p.waitForTimeout(300);
   ok('AUTOSAVE: 8s idle + \\ close → 0 /ask write posts', asks.length===0, asks.length+' asks');
   ok('AUTOSAVE: reopen', await openBotW('weaver')); await p.keyboard.press('Escape'); await p.waitForTimeout(300);
   ok('AUTOSAVE: Esc close → 0 /ask', asks.length===0, asks.length+' asks');
   ok('AUTOSAVE: reopen', await openBotW('turbosovth'));
   const cc=await p.evaluate(()=>{ const el=document.querySelector('#edBody .mdfile[data-file="SOUL.md"] .mdbody p'); const r=el.getBoundingClientRect(); return {x:Math.round(r.right-4),y:Math.round(r.top+8)}; });
   await p.mouse.click(cc.x,cc.y); await p.keyboard.press('End'); await p.keyboard.type(' LEDGER-EDIT'); await p.evaluate(()=>document.getElementById('edBack').click()); await p.waitForTimeout(700);
   ok('AUTOSAVE: real edit → exactly ONE /ask for SOUL.md only, carrying the typed text', asks.length===1&&/SOUL\.md/.test(asks[0].text)&&/LEDGER-EDIT/.test(asks[0].text)&&!/AGENTS\.md/.test(asks[0].text), asks.map(a=>a.text.split('\n')[0].slice(0,70)).join(' | '));
   await p.unroute('**/ask**'); await p.evaluate(()=>document.querySelector('.navtab[data-view="wiki"]').click()); await p.waitForTimeout(200); await rest(); }

 // ---- AE (v14.53): media controls row (‹‹ ▸ ››) AND ⚙ vertical centers == nav tab title cap-height center ±1 (DOM proxy of the pixel scan in assets/scan-AE.py: play-ring box center, skip ink centers, ⚙ ink-range center vs a non-active tab's text-Range center); AB's artist gap and R2's #mPrev anchor must survive the drop ----
 await p.mouse.move(300,30); await p.waitForTimeout(250);
 const ae=await p.evaluate(()=>{ const rc=el=>{ const rg=document.createRange(); rg.selectNodeContents(el); const r=rg.getBoundingClientRect(); return (r.top+r.bottom)/2; }; const tab=document.querySelector('#topnav .navtab[data-view="feed"]')||document.querySelector('#topnav .navtab[data-view]'); const cap=(()=>{ /* true CAP-HEIGHT center via canvas metrics (the text Range box is the line box: 99→121 → 110; the cap ink is 100→116 → 108, as pixel-scanned) */ const cs=getComputedStyle(tab); const rg=document.createRange(); rg.selectNodeContents(tab); const r=rg.getBoundingClientRect(); const c=document.createElement('canvas').getContext('2d'); c.font=`${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`; const m=c.measureText(tab.textContent.trim()||'H'); const h=c.measureText('H'); const baseline=r.top+m.fontBoundingBoxAscent; return baseline-h.actualBoundingBoxAscent/2; })(); const play=document.getElementById('mPlay').getBoundingClientRect(); const pc=(play.top+play.bottom)/2; const prev=rc(document.getElementById('mPrev')); const next=rc(document.querySelector('#mCtl .mbtn[data-m="next"]')); const gear=rc(document.getElementById('navSettings')); const rgT=document.createRange(); rgT.selectNodeContents(document.getElementById('mTitle')); const gap=rgT.getBoundingClientRect().top-play.bottom; const cl=document.getElementById('composerRight').getBoundingClientRect(); const pv=document.getElementById('mPrev').getBoundingClientRect(); const R=v=>Math.round(v*10)/10; return {cap:R(cap), dPlay:R(pc-cap), dPrev:R(prev-cap), dNext:R(next-cap), dGear:R(gear-cap), artistGap:R(gap), dL:R(cl.left-pv.left), mediaBottom:Math.round(document.getElementById('media').getBoundingClientRect().bottom)}; });
 ok('AE (▸) ring center, ‹‹/›› ink centers and ⚙ ink center all == tab CAP-HEIGHT center ±1 (canvas metrics, = pixel scan 108)', Math.abs(ae.dPlay)<=1 && Math.abs(ae.dPrev)<=1 && Math.abs(ae.dNext)<=1 && Math.abs(ae.dGear)<=1, JSON.stringify(ae));
 ok('AE kept AB (artist gap ≥8) and R2 (cluster.left == #mPrev.left ±2); widget bottom inside the 190px strip', ae.artistGap>=8 && Math.abs(ae.dL)<=2 && ae.mediaBottom<=190, JSON.stringify(ae));
 // ---- AF (v14.63): media widget sits LEFT of its old slot — halfway between old x (1154.8 @1456) and the last nav title's ink right, ≥24px clear of that title; ⚙ stays flush right (box right == vw−26); voice cluster anchors to the NEW #mPrev.left / ⚙ ink right with even spacing, 26px glyphs, lift unchanged ----
 const af=await p.evaluate(()=>{ const R=v=>Math.round(v*10)/10; const rc=el=>{ const rg=document.createRange(); rg.selectNodeContents(el); return rg.getBoundingClientRect(); }; const tabs=[...document.querySelectorAll('#topnav .navtab[data-view]')]; const lastInk=rc(tabs[tabs.length-1]); const m=document.getElementById('media').getBoundingClientRect(); const gear=document.getElementById('navSettings'); const gb=gear.getBoundingClientRect(), gg=rc(gear); const prev=document.getElementById('mPrev').getBoundingClientRect(); const cl=document.getElementById('composerRight').getBoundingClientRect(); const gl=[...document.querySelectorAll('#composerRight .csq:not(#composerStop) .lucide svg')].map(e=>e.getBoundingClientRect()); const steps=gl.slice(1).map((r,i)=>r.left-gl[i].left); const ol=document.getElementById('senterOverline').getBoundingClientRect(); const half=(lastInk.right+(innerWidth-301.2 /* pre-AF widget left = vw−301.2 (measured 1154.8 @1456: ⚙ box 26 flush + ~69 box + 26 margin + 180 widget) */))/2; return {lastInkRight:R(lastInk.right), mediaLeft:R(m.left), clear:R(m.left-lastInk.right), halfBand:R(half), gearFlush:R(innerWidth-gb.right), dL:R(cl.left-prev.left), dR:R(cl.right-gg.right), stepSpread:R(Math.max(...steps)-Math.min(...steps)), glyphW:R(gl[0].width), lift:R(ol.top-Math.max(...gl.map(r=>r.bottom)))}; });
 ok('AF media widget left of its old slot: ≥24px clear of the last nav title, within ±2 of the halfway point; ⚙ box flush right (vw−26)', af.clear>=24 && Math.abs(af.mediaLeft-af.halfBand)<=2 && Math.abs(af.gearFlush-26)<=1, JSON.stringify(af));
 ok('AF voice cluster: left == NEW #mPrev.left ±2, right == ⚙ ink right ±2, even steps (spread ≤1px), 26px glyphs, ink lift 8px above the overline', Math.abs(af.dL)<=2 && Math.abs(af.dR)<=2 && af.stepSpread<=1 && af.glyphW===26 && af.lift>=6, JSON.stringify(af));
 await rest();

 // ---- AC (v14.61): ONE top-fade recipe for BOTH stream states — the mask lives on #chat (rest AND open), transparent to #heroLine.bottom then a 90px ramp. A 900-char card at rest must fade under the underline, not hard-clip at the viewport edge. ----
 const ac=await p.evaluate(async ()=>{
   const tick=()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const chat=document.getElementById('chat'), st=document.getElementById('stream'); chat.classList.remove('open'); await tick();
   const tailEl=document.querySelector('#chat .mini .tail'); const tailSnap=tailEl.innerHTML; /* notify() trims the tail to 3 — restore the pre-existing pills afterwards so later assertions (AD pills>0) see the real state */
   const LONG=('AC ledger long message. ').repeat(40).slice(0,900); notify('klerik',LONG); notify('paladin',LONG); notify('anser',LONG); await tick();
   const rd=()=>{ const cs=getComputedStyle(chat); const ln=(document.querySelector('.view.on .heroLine')||document.getElementById('heroLine')).getBoundingClientRect(); const cr=chat.getBoundingClientRect(); const fy=parseFloat(cs.getPropertyValue('--fadeY'));
     return {mask:cs.webkitMaskImage||cs.maskImage, fy, chatTop:Math.round(cr.top), lineOk:Math.abs((cr.top+fy-6)-ln.bottom)<=1, ramp:/rgba\(0, 0, 0, 0\) \d+px, rgb\(0, 0, 0\) \d+px/.test(cs.webkitMaskImage||cs.maskImage)}; };
   const tail=document.querySelector('#chat .mini .tail'); const tall=[...tail.querySelectorAll('.msg')].filter(m=>m.textContent.includes('AC ledger long')); const reaches=tall.some(m=>m.getBoundingClientRect().top<0);
   const rest=rd(); chat.classList.add('open'); st.scrollTop=st.scrollHeight; await tick(); const open=rd();
   const streamMaskGone=(getComputedStyle(st).webkitMaskImage||getComputedStyle(st).maskImage)==='none';
   chat.classList.remove('open'); [...document.querySelectorAll('#stream .msg')].filter(m=>m.textContent.includes('AC ledger long')).forEach(m=>m.remove()); tailEl.innerHTML=tailSnap;
   return {reaches, rest, open, same:rest.mask===open.mask&&rest.fy===open.fy, streamMaskGone};
 });
 ok('AC rest-state top fade == hovered fade: mask on #chat in both states, identical gradient + --fadeY, transparent to heroLine.bottom then 90px ramp; a 900-char card reaching the top is masked, not clipped', ac.reaches&&ac.same&&ac.rest.ramp&&ac.rest.lineOk&&ac.open.lineOk&&ac.streamMaskGone&&ac.rest.chatTop===14, JSON.stringify({reaches:ac.reaches,same:ac.same,fy:ac.rest.fy,lineOk:[ac.rest.lineOk,ac.open.lineOk],streamMaskGone:ac.streamMaskGone}));

 // ---- AD (v14.57): ONE #chat rides WIKI/SKILLS/BOTS/SPACE (re-homed, never cloned), hidden on FEED where the INTEGRATIONS rail lives; hover-expands + dead zone on each ----
 const ad=await p.evaluate(async ()=>{
   const tick=()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const vis=el=>{ if(!el) return false; const cs=getComputedStyle(el); if(cs.display==='none') return false; const r=el.getBoundingClientRect(); return r.width>0&&r.height>0; };
   const out={}; const ch=document.getElementById('chat');
   for(const v of ['wiki','skills','bots','senter','feed']){ showView(v); await tick();
     out[v]={count:document.querySelectorAll('#chat').length, chat:vis(ch), host:ch.dataset.host, after:ch.previousElementSibling&&ch.previousElementSibling.id, rail:vis(document.getElementById('intRail')), mini:!!document.querySelector('#chat .mini .tail')}; }
   showView('wiki'); await tick(); return out; });
 const adOn=['wiki','skills','bots','senter'].every(v=>ad[v].count===1&&ad[v].chat&&ad[v].host===v&&ad[v].after==='view-'+v&&!ad[v].rail&&ad[v].mini);
 ok('AD fleet stream present on WIKI/SKILLS/BOTS/SPACE (one #chat, re-homed after the active view), absent on FEED; INTEGRATIONS rail only on FEED', adOn&&!ad.feed.chat&&ad.feed.rail&&ad.feed.count===1, JSON.stringify(ad));
 for(const v of ['skills','bots','senter']){
   await p.evaluate(v=>{ document.querySelectorAll('.navtab').forEach(x=>x.classList.toggle('on',x.dataset.view===v)); showView(v); },v); await p.mouse.move(300,500); await p.waitForTimeout(200);
   const mr=await p.evaluate(()=>{ const r=document.querySelector('#chat .mini').getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]; });
   await p.mouse.move(mr[0],mr[1]); await p.waitForTimeout(300);
   const h=await p.evaluate(()=>{ const ch=document.getElementById('chat'); const r=ch.getBoundingClientRect(); return {open:ch.classList.contains('open'), dead:document.body.classList.contains('deadzone'), top:Math.round(r.top), h:Math.round(r.height), fadeY:parseInt(ch.style.getPropertyValue('--fadeY'))||0}; });
   await p.mouse.move(300,500); await p.waitForTimeout(250);
   const closed=await p.evaluate(()=>!document.getElementById('chat').classList.contains('open'));
   ok('AD '+v+': stream hover-expands (top 14, full height), dead zone set in the lane, fade synced, closes on leave', h.open&&h.dead&&h.top===14&&h.h>=H-40&&h.fadeY>=60&&closed, JSON.stringify(h)+' closed:'+closed);
 }
 await p.evaluate(()=>{ document.querySelectorAll('.navtab').forEach(x=>x.classList.toggle('on',x.dataset.view==='wiki')); showView('wiki'); }); await rest();

 // __MORE__

 // ---- AH (v14.56): the wall backdrop is an explicit ⚙ setting, default ON — never gated on isFS() (unreachable inside the Hermes preview webview) ----
 const ah=await p.evaluate(()=>{ const bd=document.getElementById('wallBackdrop'); const set=window._wallCur?window._wallCur():localStorage.getItem('sw.wall'); return {set, op:getComputedStyle(bd).opacity, fs:window._isFS&&window._isFS(), img:getComputedStyle(bd).backgroundImage, dim:getComputedStyle(bd,'::after').backgroundColor, z:getComputedStyle(bd).zIndex, mmZ:getComputedStyle(document.getElementById('mindmap')).zIndex}; });
 ok('AH #wallBackdrop opacity === 1 whenever the setting ≠ none (fresh profile → hermes-galactic), even with isFS() false; semi-transparent dim on ::after (α .3–.7, tuned by AI); wall z0 under mindmap z1', (ah.set==='none' ? ah.op==='0' : (ah.op==='1' && /walls\//.test(ah.img))) && ah.fs===false && /rgba\(\d+, \d+, \d+, 0\.[3-6]\d*\)/.test(ah.dim) && ah.z==='0' && ah.mmZ==='1', JSON.stringify(ah));
 ok('no page/console errors', errs.length===0, errs.slice(0,3).join(' | '));
 await b.close();
 let fail=0; for(const r of results){ console.log((r.ok?'PASS':'FAIL')+'  '+r.name+(r.detail?'  — '+r.detail:'')); if(!r.ok) fail++; }
 console.log(`\n${results.length-fail}/${results.length} passed @ ${W}x${H}`); process.exit(fail?1:0);
})().catch(e=>{ console.error('LEDGER CRASH',e); process.exit(2); });
