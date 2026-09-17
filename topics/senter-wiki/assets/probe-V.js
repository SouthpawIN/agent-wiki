// probe-V.js — V (v14.44) type-ahead TAGS above the nav. Usage:
//   PATH=$HOME/.hermes/node/bin:$PATH PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-V.js [WxH] [shotDir]
// Prints per-keystroke tag lists for "turb" / "wea", ranking, geometry (tag row vs nav tabs, strip height), click → view, ↑↓/Enter/Esc, and writes LOOK shots.
const {chromium}=require(process.env.PW||'playwright');
const path=require('path'), fs=require('fs');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number);
const SHOT=process.argv[3]||null;
const out={}; const errs=[];
(async()=>{
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
  p.on('pageerror',e=>errs.push('pageerror '+e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push('console '+m.text()); });
  await p.goto(FILE); await p.waitForTimeout(3600);
  const open=async()=>{ await p.mouse.move(300,30); await p.waitForTimeout(300); };
  const state=()=>p.evaluate(()=>{ const s=document.getElementById('topstrip'), r=document.getElementById('tagRow'); const rb=r.getBoundingClientRect(); const tabs=[...document.querySelectorAll('.navtab')].map(t=>{ const x=t.getBoundingClientRect(); return {t:t.textContent.trim(), top:Math.round(x.top), bottom:Math.round(x.bottom)}; }); const tags=[...r.querySelectorAll('.tta')].map(x=>({kind:x.dataset.kind,name:x.dataset.name,sel:x.classList.contains('sel'), top:Math.round(x.getBoundingClientRect().top), bottom:Math.round(x.getBoundingClientRect().bottom)})); const ol=document.getElementById('senterOverline').getBoundingClientRect(); return {on:s.classList.contains('on'), tagsClass:s.classList.contains('tags'), stripH:Math.round(s.getBoundingClientRect().height), tagH:getComputedStyle(s).getPropertyValue('--tagH').trim(), rowTop:Math.round(rb.top), rowBottom:Math.round(rb.bottom), rowDisplay:getComputedStyle(r).display, olY:Math.round(ol.top), tabs, tags, input:document.getElementById('senterHiddenInput').value, view:document.querySelector('.view.on')?.id, edTitle:document.getElementById('edTitle')?.textContent.trim(), navPadTop:getComputedStyle(document.getElementById('topnav')).paddingTop, hash:location.hash}; });
  await open();
  // 1) per-keystroke: "turb"
  const steps=[];
  for(const ch of 'turb'){ await p.evaluate(()=>{ document.querySelectorAll('#tagRow .tta').forEach(b=>b.dataset.stale='1'); }); await p.keyboard.type(ch); await p.waitForTimeout(120); const s=await state(); const fresh=await p.evaluate(()=>[...document.querySelectorAll('#tagRow .tta')].every(b=>!b.dataset.stale)); steps.push({typed:s.input, rerendered:fresh, tags:s.tags.map(t=>t.kind+'·'+t.name)}); }
  out.turb=steps; const sT=await state(); out.turbState={stripH:sT.stripH, tagH:sT.tagH, rowTop:sT.rowTop, rowBottom:sT.rowBottom, olY:sT.olY, tabs:sT.tabs, navPadTop:sT.navPadTop, on:sT.on};
  if(SHOT){ await p.screenshot({path:path.join(SHOT,`V-turb-${W}x${H}.png`)}); }
  // every keystroke re-rendered the row (DOM nodes replaced), and the set changed where the query narrows (t→tu)
  out.perKeystrokeChanged=steps.every(s=>s.rerendered) && JSON.stringify(steps[0].tags)!==JSON.stringify(steps[1].tags);
  // 2) ranking check via API
  out.rankTurb=await p.evaluate(()=>window._tagAhead.match('turb'));
  out.rankWea=await p.evaluate(()=>window._tagAhead.match('wea'));
  out.rankHermes=await p.evaluate(()=>window._tagAhead.match('hermes'));
  out.rankLoop=await p.evaluate(()=>window._tagAhead.match('verify'));
  out.rankInt=await p.evaluate(()=>window._tagAhead.match('github'));
  out.rankDesc=await p.evaluate(()=>window._tagAhead.match('obsidian vault'));
  // 3) ↑↓ selection + Esc
  await p.keyboard.press('ArrowDown'); await p.waitForTimeout(60); const a1=await state(); await p.keyboard.press('ArrowDown'); await p.waitForTimeout(60); const a2=await state(); await p.keyboard.press('ArrowUp'); await p.waitForTimeout(60); const a3=await state();
  out.arrows={down1:a1.tags.findIndex(t=>t.sel), down2:a2.tags.findIndex(t=>t.sel), up:a3.tags.findIndex(t=>t.sel)};
  await p.keyboard.press('Escape'); await p.waitForTimeout(120); const e1=await state(); out.escOnce={tagsClass:e1.tagsClass, rowDisplay:e1.rowDisplay, input:e1.input, stripH:e1.stripH, on:e1.on};
  await p.keyboard.press('Escape'); await p.waitForTimeout(250); const e2=await state(); out.escTwice={input:e2.input, on:e2.on};
  // 4) click bot·turbosovth tag → BOTS view + editor
  await open(); await p.keyboard.type('turb'); await p.waitForTimeout(150);
  const bt=await p.evaluate(()=>{ const b=[...document.querySelectorAll('#tagRow .tta')].find(x=>x.dataset.kind==='bot'&&x.dataset.name==='turbosovth'); if(!b) return null; const r=b.getBoundingClientRect(); return {x:r.left+r.width/2,y:r.top+r.height/2, hit:document.elementFromPoint(r.left+r.width/2,r.top+r.height/2)===b||!!document.elementFromPoint(r.left+r.width/2,r.top+r.height/2)?.closest('.tta')}; });
  out.botTagHit=bt; if(bt){ await p.mouse.click(bt.x,bt.y); await p.waitForTimeout(400); }
  const c1=await state(); out.clickBot={view:c1.view, edTitle:c1.edTitle, input:c1.input, tagsClass:c1.tagsClass, hash:c1.hash, botsTabOn:await p.evaluate(()=>document.querySelector('.navtab[data-view="bots"]').classList.contains('on')), avatar:await p.evaluate(()=>document.getElementById('edAvatar').classList.contains('show')+' '+document.getElementById('edAvatar').getAttribute('src'))};
  if(SHOT){ await p.mouse.move(600,500); await p.waitForTimeout(400); await p.screenshot({path:path.join(SHOT,`V-click-bot-${W}x${H}.png`)}); }
  // 5) "wea" → bot·weaver, Enter after ArrowDown to the weaver tag
  await p.keyboard.press('Escape'); await p.waitForTimeout(200); await open(); await p.keyboard.type('wea'); await p.waitForTimeout(150);
  const sW=await state(); out.weaTags=sW.tags.map(t=>t.kind+'·'+t.name);
  const wIdx=sW.tags.findIndex(t=>t.kind==='bot'&&t.name==='weaver');
  for(let i=0;i<=wIdx;i++){ await p.keyboard.press('ArrowDown'); await p.waitForTimeout(40); }
  const selState=await state(); out.weaSel=selState.tags.find(t=>t.sel);
  if(SHOT){ await p.screenshot({path:path.join(SHOT,`V-wea-${W}x${H}.png`)}); }
  await p.keyboard.press('Enter'); await p.waitForTimeout(450);
  const c2=await state(); out.enterWeaver={view:c2.view, edTitle:c2.edTitle, input:c2.input, hash:c2.hash, streamCount:await p.evaluate(()=>document.querySelectorAll('#stream .msg[data-who="chris"]').length)};
  // 6) topic tag → editor on wiki; skill tag → editor with skills path
  await p.keyboard.press('Escape'); await p.waitForTimeout(200); await open(); await p.keyboard.type('turb'); await p.waitForTimeout(150);
  await p.evaluate(()=>{ const b=[...document.querySelectorAll('#tagRow .tta')].find(x=>x.dataset.kind==='topic'&&x.dataset.name==='turbofit'); b&&b.click(); }); await p.waitForTimeout(400);
  const c3=await state(); out.clickTopic={view:c3.view, edTitle:c3.edTitle, wikiTabOn:await p.evaluate(()=>document.querySelector('.navtab[data-view="wiki"]').classList.contains('on')), path:await p.evaluate(()=>document.querySelector('#edBody .edtools .path')?.textContent)};
  await p.keyboard.press('Escape'); await p.waitForTimeout(200); await open(); await p.keyboard.type('turbofit'); await p.waitForTimeout(150);
  await p.evaluate(()=>{ const b=[...document.querySelectorAll('#tagRow .tta')].find(x=>x.dataset.kind==='skill'&&x.dataset.name==='turbofit'); b&&b.click(); }); await p.waitForTimeout(400);
  const c4=await state(); out.clickSkill={view:c4.view, edTitle:c4.edTitle, skillsTabOn:await p.evaluate(()=>document.querySelector('.navtab[data-view="skills"]').classList.contains('on')), path:await p.evaluate(()=>document.querySelector('#edBody .edtools .path')?.textContent)};
  // 7) integration + loop tags
  await p.keyboard.press('Escape'); await p.waitForTimeout(200); await open(); await p.keyboard.type('github'); await p.waitForTimeout(150);
  await p.evaluate(()=>{ const b=[...document.querySelectorAll('#tagRow .tta')].find(x=>x.dataset.kind==='integration'); b&&b.click(); }); await p.waitForTimeout(600);
  const c5=await state(); out.clickIntegration={view:c5.view, edTitle:c5.edTitle, path:await p.evaluate(()=>document.querySelector('#edBody .edtools .path')?.textContent)};
  await p.keyboard.press('Escape'); await p.waitForTimeout(200); await open(); await p.keyboard.type('verify'); await p.waitForTimeout(200);
  const lp=await state(); out.loopTags=lp.tags.map(t=>t.kind+'·'+t.name);
  await p.evaluate(()=>{ const b=[...document.querySelectorAll('#tagRow .tta')].find(x=>x.dataset.kind==='loop'); b&&b.click(); }); await p.waitForTimeout(700);
  const c6=await state(); out.clickLoop={view:c6.view, edTitle:c6.edTitle, secGold:await p.evaluate(()=>[...document.querySelectorAll('#edBody .sec')].find(h=>h.style.color)?.textContent)};
  // 8) empty input → no row; strip back to 190; rest state unchanged (hero zero-flow)
  await p.keyboard.press('Escape'); await p.waitForTimeout(200); await open(); await p.keyboard.type('x'); await p.waitForTimeout(120); await p.keyboard.press('Backspace'); await p.waitForTimeout(150);
  const em=await state(); out.emptyInput={tagsClass:em.tagsClass, rowDisplay:em.rowDisplay, stripH:em.stripH};
  await p.mouse.move(600,600); await p.waitForTimeout(500); out.rest=await p.evaluate(()=>({heroTop:Math.round(document.querySelector('.view.on .hero, #hero').getBoundingClientRect().top), on:document.getElementById('topstrip').classList.contains('on'), stripH:Math.round(document.getElementById('topstrip').getBoundingClientRect().height)}));
  out.errors=errs;
  console.log(JSON.stringify(out,null,1));
  await b.close();
})().catch(e=>{ console.error('PROBE CRASH',e); process.exit(2); });
