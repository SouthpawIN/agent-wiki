// probe-AD.js — fleet stream (#chat) presence per view. One element, re-homed per view; absent on FEED; intRail only on FEED.
// run: PW=~/.hermes/hermes-agent/node_modules/playwright ~/.hermes/node/bin/node assets/probe-AD.js [WxH] [shotdir]
const {chromium}=require(process.env.PW||'playwright');
const path=require('path'), fs=require('fs');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number);
const shots=process.argv[3]||'';
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3600);
 const out={};
 for(const v of ['wiki','skills','bots','senter','feed']){
   await p.mouse.move(300,500); await p.waitForTimeout(150);
   await p.evaluate(v=>{ document.querySelectorAll('.navtab').forEach(x=>x.classList.toggle('on',x.dataset.view===v)); showView(v); if(window.placePlus) try{placePlus()}catch(e){} },v);
   await p.waitForTimeout(250);
   const rest=await p.evaluate(()=>{
     const ch=document.getElementById('chat'), mini=document.querySelector('#chat .mini'), rail=document.getElementById('intRail');
     const vis=el=>{ if(!el) return false; const cs=getComputedStyle(el); if(cs.display==='none'||cs.visibility==='hidden') return false; const r=el.getBoundingClientRect(); return r.width>0&&r.height>0; };
     const mr=mini?mini.getBoundingClientRect():null;
     return {chatCount:document.querySelectorAll('#chat').length, chatVisible:vis(ch), chatHide:ch.classList.contains('hide'), host:ch.dataset.host||null, prevSibling:ch.previousElementSibling&&ch.previousElementSibling.id, parent:ch.parentElement.tagName,
       miniRect:mr&&[Math.round(mr.left),Math.round(mr.top),Math.round(mr.right),Math.round(mr.bottom)], railVisible:vis(rail), pills:document.querySelectorAll('#chat .mini .tail .msg').length};
   });
   let hover=null;
   if(rest.chatVisible&&rest.miniRect){
     const [l,t,r,bt]=rest.miniRect; await p.mouse.move((l+r)/2,(t+bt)/2); await p.waitForTimeout(300);
     hover=await p.evaluate(()=>{ const ch=document.getElementById('chat'), st=document.getElementById('stream'); const r=ch.getBoundingClientRect(); const cs=getComputedStyle(ch);
       const ln=document.querySelector('.view.on .heroLine'); const lnB=ln?Math.round(ln.getBoundingClientRect().bottom):null;
       return {open:ch.classList.contains('open'), dead:document.body.classList.contains('deadzone'), top:Math.round(r.top), height:Math.round(r.height), fadeY:st.style.getPropertyValue('--fadeY'), mask:(cs.webkitMaskImage||cs.maskImage||'').slice(0,40), heroLineBottom:lnB, pin:document.querySelectorAll('#stream .pinblock').length}; });
     if(shots) await p.screenshot({path:path.join(shots,'AD-'+v+'-open-'+W+'x'+H+'.png')});
     if(v==='skills'&&shots){ /* fade proof: overflow the stream so cards run up under the ramp, then shoot */ await p.evaluate(()=>{ for(let i=0;i<14;i++) notify('turbosovth','AD fade proof message '+i+' — long enough to wrap onto a second line so the column overflows the viewport'); const st=document.getElementById('stream'); st.scrollTop=st.scrollHeight/2; }); await p.waitForTimeout(250); await p.screenshot({path:path.join(shots,'AD-skills-fade-'+W+'x'+H+'.png')});
       hover.fadeScan=await p.evaluate(()=>{ const ch=document.getElementById('chat'); const cs=getComputedStyle(ch); return {mask:(cs.webkitMaskImage||cs.maskImage).replace(/\s+/g,' ').slice(0,140), fadeY:ch.style.getPropertyValue('--fadeY')}; });
       await p.evaluate(()=>{ [...document.querySelectorAll('#stream .msg, #chat .mini .msg')].filter(m=>m.textContent.includes('AD fade proof')).forEach(m=>m.remove()); }); }
     // dead zone: hover a row (if any) with pointer in the lane
     const dz=await p.evaluate(()=>{ const row=document.querySelector('.view.on .thead'); if(!row) return {rows:0}; const r=row.getBoundingClientRect(); return {rows:1, x:Math.round(Math.min(r.right-30, innerWidth-60)), y:Math.round(r.top+r.height/2), name:row.querySelector('.tname')?.textContent, rowRight:Math.round(r.right), laneLeft:innerWidth-478}; });
     if(dz.rows){ await p.mouse.move(300,500); await p.waitForTimeout(250); await p.mouse.move(dz.x,dz.y); await p.waitForTimeout(200); /* stream closed → the row itself sits under the pointer, inside the lane */
       hover.deadzone=await p.evaluate((dz)=>{ const at=document.elementFromPoint(dz.x,dz.y); const row=at&&at.closest('.thead'); const d=document.body.classList.contains('deadzone'); if(!row) return {dead:d,hovered:false,at:at&&(at.id||at.className||at.tagName),x:dz.x,y:dz.y,inLane:dz.x>dz.laneLeft}; const cs=getComputedStyle(row); const tn=row.querySelector('.tname'); const af=getComputedStyle(row,'::after'); return {dead:d,hovered:true,inLane:dz.x>dz.laneLeft,bg:cs.backgroundColor,rail:cs.borderLeftColor,minH:cs.minHeight,tname:tn?getComputedStyle(tn).fontSize:null,underlineW:af.width}; },dz); }
     await p.mouse.move(300,500); await p.waitForTimeout(250);
     hover.closedAfterLeave=await p.evaluate(()=>!document.getElementById('chat').classList.contains('open'));
   } else if(shots) await p.screenshot({path:path.join(shots,'AD-'+v+'-rest-'+W+'x'+H+'.png')});
   out[v]={rest,hover};
 }
 console.log(JSON.stringify(out,null,1)); console.log('errors:',errs.length,errs.slice(0,3));
 await b.close();
})().catch(e=>{ console.error('CRASH',e); process.exit(2); });
