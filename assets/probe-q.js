// Q probe: ALLOW ▾ menu on the LAST approval card must stay inside the viewport (stream + FEED).
// run: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-q.js [--vp 1456x914] [--shot dir]
const {chromium}=require(process.env.PW||'playwright');
const path=require('path');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const a=process.argv.indexOf('--vp'); const [W,H]=(a>0?process.argv[a+1]:'1456x914').split('x').map(Number);
const s=process.argv.indexOf('--shot'); const SHOT=s>0?process.argv[s+1]:null;
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push('page:'+e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push('console:'+m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500);
 // inject a pending card via the real builder, as the last child of #stream (approvalCard appends at the end)
 await p.evaluate(()=>{ window.__bridge && window.__bridge.approvalCard ? 0 : 0; });
 const inject=await p.evaluate(()=>{
   const ev={id:'q-probe-'+Date.now(),bot:'klerik',ts:Date.now()/1000,kind:'approval',phase:'pending',command:'write ~/.hermes/profiles/weaver/SOUL.md',description:'protected write: profile SOUL.md'};
   if(window.__approvalCard){ window.__approvalCard(ev); return {via:'__approvalCard',id:ev.id}; }
   // fallback: synthesize same markup
   const s=document.getElementById('stream');
   s.insertAdjacentHTML('beforeend','<div class="msg approval" data-aid="'+ev.id+'" data-who="klerik" data-when="12:00"><img class="avatar sm" src="assets/avatars/klerik.png"><span class="who">klerik</span><div class="txt">wants approval · '+ev.description+'<div class="cmd">'+ev.command+'</div></div><div class="aacts"><span class="allow-group"><button class="allow-main" data-choice="once">ALLOW</button><button class="allow-caret" data-toggle>▾</button><span class="allow-menu"><button data-choice="once">Allow</button><button data-choice="session">Allow this session</button><button data-choice="always">Always allow</button></span></span><button data-a="deny">DENY</button></div></div>');
   const f=document.getElementById('feed'); if(f) f.insertAdjacentHTML('afterbegin','<div class="post approval" data-aid="'+ev.id+'" data-who="klerik" data-when="12:00"><img class="avatar" src="assets/avatars/klerik.png"><span class="who">klerik</span><div class="txt">wants approval · '+ev.description+'<div class="cmd">'+ev.command+'</div></div><div class="aacts"><span class="allow-group"><button class="allow-main" data-choice="once">ALLOW</button><button class="allow-caret" data-toggle>▾</button><span class="allow-menu"><button data-choice="once">Allow</button><button data-choice="session">Allow this session</button><button data-choice="always">Always allow</button></span></span><button data-a="deny">DENY</button></div></div>');
   return {via:'synth',id:ev.id};
 });
 // open the stream (hover the mini → chat.open), land on newest
 await p.evaluate(()=>{ const c=document.getElementById('chat'); c.classList.add('open'); const st=document.getElementById('stream'); st.scrollTop=st.scrollHeight; });
 await p.waitForTimeout(300);
 const measure=async(scope)=>p.evaluate((scope)=>{
   const card=document.querySelector(scope+' [data-aid^="q-probe-"]'); if(!card) return {err:'no card in '+scope};
   const caret=card.querySelector('.allow-caret'); caret.click();
   const g=card.querySelector('.allow-group'); const menu=card.querySelector('.allow-menu');
   const m=menu.getBoundingClientRect(); const c=card.getBoundingClientRect();
   const opts=[...menu.querySelectorAll('button')].map(o=>{ const r=o.getBoundingClientRect(); const cx=r.left+r.width/2, cy=r.top+r.height/2; const hit=document.elementFromPoint(cx,cy); return {t:o.textContent, cy:Math.round(cy), hit:hit===o}; });
   const clip=g.closest('#stream, #view-feed'); const clipR=clip.getBoundingClientRect();
   return {open:g.classList.contains('open'), up:menu.classList.contains('up'), pad:clip.style.paddingBottom||'0', menuTop:Math.round(m.top), menuBottom:Math.round(m.bottom), cardTop:Math.round(c.top), cardBottom:Math.round(c.bottom), clipBottom:Math.round(clipR.bottom), innerHeight, fits:m.bottom<=innerHeight-8 && m.top>=0 && m.bottom<=clipR.bottom && c.top>=clipR.top-1, opts, allHit:opts.every(o=>o.hit)};
 },scope);
 const stream=await measure('#stream');
 console.log('STREAM', JSON.stringify(stream));
 if(SHOT){ await p.screenshot({path:path.join(SHOT,'Q-stream-'+W+'x'+H+'.png')}); }
 // close menu, switch to FEED, scroll so the card is the bottom-most visible thing
 await p.evaluate(()=>{ document.querySelectorAll('.allow-group.open').forEach(x=>x.classList.remove('open')); document.getElementById('chat').classList.remove('open'); if(window.showView) showView('feed'); });
 await p.waitForTimeout(400);
 await p.evaluate(()=>{ const v=document.getElementById('view-feed'); const card=document.querySelector('#feed [data-aid^="q-probe-"]'); const r=card.getBoundingClientRect(); // put the card's bottom near the viewport bottom
   v.scrollTop += (r.bottom - (innerHeight-20)); });
 await p.waitForTimeout(200);
 const feed=await measure('#feed');
 console.log('FEED', JSON.stringify(feed));
 if(SHOT){ await p.screenshot({path:path.join(SHOT,'Q-feed-'+W+'x'+H+'.png')}); }
 // FEED at the edge: shrink the viewport so the card's bottom sits ~20px above the viewport bottom → downward menu must overflow → flip
 await p.evaluate(()=>{ document.querySelectorAll('.allow-group.open').forEach(x=>x.classList.remove('open')); });
 const cb=feed.cardBottom; await p.setViewportSize({width:W,height:cb+20}); await p.waitForTimeout(200);
 const feedEdge=await measure('#feed'); console.log('FEED-EDGE@'+W+'x'+(cb+20), JSON.stringify(feedEdge));
 if(SHOT){ await p.screenshot({path:path.join(SHOT,'Q-feed-edge.png')}); }
 // BUMP path: viewport so short that the menu fits neither down nor up → container padded + scrolled so card+menu are in view
 await p.evaluate(()=>{ window.__closeMenus(); });
 await p.setViewportSize({width:W,height:Math.max(180, feed.cardBottom-feed.cardTop+60)}); await p.waitForTimeout(200);
 await p.evaluate(()=>{ const v=document.getElementById('view-feed'); const card=document.querySelector('#feed [data-aid^="q-probe-"]'); v.scrollTop += card.getBoundingClientRect().top-4; });
 await p.waitForTimeout(100);
 const bump=await measure('#feed'); console.log('FEED-BUMP', JSON.stringify(bump));
 if(SHOT){ await p.screenshot({path:path.join(SHOT,'Q-feed-bump.png')}); }
 // FORCED bump: 120px-tall viewport — the menu fits neither down nor up → container padded by the overflow + scrolled; menu must end ≤ innerHeight−8
 await p.evaluate(()=>{ window.__closeMenus(); });
 await p.setViewportSize({width:W,height:120}); await p.waitForTimeout(200);
 await p.evaluate(()=>{ const v=document.getElementById('view-feed'); const caret=document.querySelector('#feed [data-aid^="q-probe-"] .allow-caret'); v.scrollTop += caret.getBoundingClientRect().top-60; });
 await p.waitForTimeout(100);
 const forced=await measure('#feed'); console.log('FEED-FORCED-BUMP@120', JSON.stringify(forced));
 if(SHOT){ await p.screenshot({path:path.join(SHOT,'Q-feed-forced-bump.png')}); }
 await p.setViewportSize({width:W,height:H});
 // after closing: padding restored, no .up left behind
 const after=await p.evaluate(()=>{ document.body.click(); return {open:document.querySelectorAll('.allow-group.open').length, up:document.querySelectorAll('.allow-menu.up').length, pads:document.querySelectorAll('[data-menu-pad]').length}; });
 console.log('AFTER-CLOSE', JSON.stringify(after));
 console.log('errors', errs.length, errs.slice(0,3));
 await b.close();
})().catch(e=>{ console.error('PROBE CRASH',e); process.exit(2); });
