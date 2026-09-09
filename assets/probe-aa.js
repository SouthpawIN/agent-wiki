// AA probe: pending approval cards are PINNED — stream (bottom), mini tail (bottom), FEED (top under hero).
// Inject a pending card, then 3 notify() messages → the card's bbox is unchanged and it is still at the growth edge; approve → it unpins into the flow.
// Run: PW=~/.hermes/hermes-agent/node_modules/playwright ~/.hermes/node/bin/node assets/probe-aa.js [--vp 1456x914] [--shot assets/look]
const {chromium}=require(process.env.PW||'playwright'); const path=require('path'); const fs=require('fs');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const a=process.argv; const vi=a.indexOf('--vp'); const [W,H]=(vi>0?a[vi+1]:'1456x914').split('x').map(Number); const si=a.indexOf('--shot'); const SHOT=si>0?a[si+1]:null;
const CARD=(cls,id,who)=>'<div class="'+cls+' approval" data-aid="'+id+'" data-who="'+who+'" data-when="12:00"><img class="avatar'+(cls==='msg'?' sm':'')+'" src="assets/avatars/'+who+'.png"><span class="who">'+who+'</span><div class="txt">wants approval · protected write<div class="cmd">write ~/.hermes/profiles/weaver/SOUL.md</div></div><div class="aacts"><span class="allow-group"><button class="allow-main" data-choice="once">ALLOW</button><button class="allow-caret" data-toggle>▾</button><span class="allow-menu"><button data-choice="once">Allow</button><button data-choice="session">Allow this session</button><button data-choice="always">Always allow</button></span></span><button data-a="deny">DENY</button></div></div>';
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error'&&!/ERR_FILE_NOT_FOUND/.test(m.text())) errs.push(m.text()); }); // baseline noise: assets/avatars/chris.{png,svg} missing (another item's chris post) — not AA's
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3600);
 await p.addInitScript(()=>{}); await p.evaluate(CARD=>{ window.__CARD=CARD; },CARD.toString());
 const R=`e=>{ const r=e.getBoundingClientRect(); return {l:Math.round(r.left),t:Math.round(r.top),r:Math.round(r.right),b:Math.round(r.bottom)}; }`;
 // ---- STREAM ----
 const st=await p.evaluate(async ([R,CARD])=>{
   const rect=eval(R); const card=eval('('+CARD+')');
   const chat=document.getElementById('chat'), s=document.getElementById('stream');
   chat.classList.add('open'); s.scrollTop=s.scrollHeight; await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   s.insertAdjacentHTML('beforeend',card('msg','aa-1','klerik')); s.scrollTop=s.scrollHeight;
   await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const c1=s.querySelector('[data-aid="aa-1"]'); const before=rect(c1);
   const inBlock0=c1.parentElement.classList.contains('pinblock'), blockLast0=s.lastElementChild.classList.contains('pinblock');
   for(let i=0;i<3;i++) notify('turbosovth','AA probe message #'+(i+1)+' — this must slot ABOVE the pinned approval, never below it');
   await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const after=rect(c1); const kids=[...s.children]; const last=kids[kids.length-1];
   const bottomMost=last.classList.contains('pinblock') && last.lastElementChild===c1;
   const msgsAbove=[...s.querySelectorAll(':scope > .msg')].filter(m=>m.textContent.includes('AA probe message')).every(m=>rect(m).b<=before.t);
   // second pending stacks below the first (arrival order)
   s.insertAdjacentHTML('beforeend',card('msg','aa-2','paladin')); await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const c2=s.querySelector('[data-aid="aa-2"]'); const stack=c2.parentElement===c1.parentElement && c1.nextElementSibling===c2 && rect(c2).t>=rect(c1).b;
   // sticky: scroll to top, block still in view
   s.scrollTop=0; await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const sr=rect(s); const blk=rect(c1.parentElement); const stickyInView=blk.b<=sr.b+1 && blk.t>=sr.t && blk.b>sr.t;
   s.scrollTop=s.scrollHeight;
   // approve aa-1 via the real path (dissipate) without the network: simulate markDone via classes the observer keys on
   window.__aaDecide=(id)=>{ document.querySelectorAll('[data-aid="'+id+'"]').forEach(el=>{ el.dataset.settle='1'; el.classList.add('dissipating'); setTimeout(()=>{ el.classList.remove('dissipating'); el.classList.add('done'); },900); }); };
   __aaDecide('aa-1'); await new Promise(r=>setTimeout(r,60));
   const unpinned=!c1.parentElement.classList.contains('pinblock') && c1.parentElement===s && c1.nextElementSibling===c1.parentElement.querySelector(':scope > .pinblock');
   const c2StillPinned=c2.parentElement.classList.contains('pinblock') && s.lastElementChild===c2.parentElement;
   return {before, after, same:JSON.stringify(before)===JSON.stringify(after), inBlock0, blockLast0, bottomMost, msgsAbove, stack, stickyInView, unpinned, c2StillPinned, dissipating:c1.classList.contains('dissipating')};
 },[R,CARD.toString()]);
 console.log('STREAM', JSON.stringify(st));
 if(SHOT){ fs.mkdirSync(SHOT,{recursive:true}); await p.screenshot({path:path.join(SHOT,`AA-stream-${W}x${H}.png`)}); }
 await p.waitForTimeout(1100);
 // ---- MINI TAIL (chat closed) ----
 const mini=await p.evaluate(async ([R,CARD])=>{
   const rect=eval(R); const card=eval('('+CARD+')');
   document.getElementById('chat').classList.remove('open'); const tail=document.querySelector('#chat .mini .tail');
   tail.insertAdjacentHTML('beforeend','<div class="msg approval" data-aid="aa-m1" data-who="klerik"><img class="avatar sm" src="assets/avatars/klerik.png"><span class="who">klerik</span> <span class="txt">⚠ approval · protected write</span></div>');
   await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const c=tail.querySelector('[data-aid="aa-m1"]'); const before=rect(c);
   for(let i=0;i<3;i++) notify('dogeman','mini probe '+i);
   await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const after=rect(c); const last=tail.lastElementChild;
   const bottomMost=last.classList.contains('pinblock')&&last.lastElementChild===c;
   const others=[...tail.querySelectorAll(':scope > .msg')]; const above=others.every(m=>rect(m).b<=before.t);
   __aaDecide('aa-m1'); await new Promise(r=>setTimeout(r,60));
   const unpinned=c.parentElement===tail;
   return {before,after,same:JSON.stringify(before)===JSON.stringify(after),bottomMost,others:others.length,above,unpinned};
 },[R,CARD.toString()]);
 console.log('MINI', JSON.stringify(mini));
 await p.waitForTimeout(1100);
 // ---- FEED (pinned at the TOP, under the sticky hero) ----
 await p.evaluate(()=>showView('feed')); await p.waitForTimeout(400);
 const fd=await p.evaluate(async ([R,CARD])=>{
   const rect=eval(R); const card=eval('('+CARD+')');
   const f=document.getElementById('feed'), v=document.getElementById('view-feed'); v.scrollTop=0;
   f.insertAdjacentHTML('afterbegin',card('post','aa-f1','klerik')); await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const c=f.querySelector('[data-aid="aa-f1"]'); const before=rect(c);
   for(let i=0;i<3;i++) f.insertAdjacentHTML('afterbegin','<div class="post" data-who="teknium" data-when="12:0'+i+'"><img class="avatar" src="assets/avatars/teknium.png"><span class="who">teknium</span><span class="when">12:0'+i+'</span><div class="txt">AA feed probe '+i+' — newest post, must sit BELOW the pinned block</div></div>');
   await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const after=rect(c); const first=f.firstElementChild; const topMost=first.classList.contains('pinblock')&&first.firstElementChild===c;
   const posts=[...f.querySelectorAll(':scope > .post')].filter(x=>x.textContent.includes('AA feed probe')); const below=posts.every(x=>rect(x).t>=before.b);
   const hero=rect(document.getElementById('feedHero')); const underHero=before.t>=hero.b-1;
   // sticky under hero while scrolling
   v.scrollTop=600; await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
   const scrolled=rect(c); const hero2=rect(document.getElementById('feedHero')); const sticky=scrolled.t>=hero2.b-1 && scrolled.t<hero2.b+40; v.scrollTop=0;
   __aaDecide('aa-f1'); await new Promise(r=>setTimeout(r,60));
   const unpinned=c.parentElement===f && (!f.querySelector(':scope > .pinblock') || (c.previousElementSibling&&c.previousElementSibling.classList.contains('pinblock'))); // block is removed when empty
   return {before,after,same:JSON.stringify(before)===JSON.stringify(after),topMost,below,underHero,heroB:hero.b,sticky,scrolledTop:scrolled.t,hero2B:hero2.b,unpinned};
 },[R,CARD.toString()]);
 console.log('FEED', JSON.stringify(fd));
 if(SHOT) await p.screenshot({path:path.join(SHOT,`AA-feed-${W}x${H}.png`)});
 const pass=st.same&&st.bottomMost&&st.msgsAbove&&st.stack&&st.stickyInView&&st.unpinned&&st.c2StillPinned&&mini.same&&mini.bottomMost&&mini.above&&mini.unpinned&&fd.same&&fd.topMost&&fd.below&&fd.underHero&&fd.sticky&&fd.unpinned&&errs.length===0;
 console.log('errors', errs.length, errs.slice(0,3)); console.log(pass?'AA PASS':'AA FAIL', W+'x'+H);
 await b.close(); process.exit(pass?0:1);
})().catch(e=>{ console.error('PROBE CRASH',e); process.exit(2); });
