// S (v14.47) probe — unified hover cards on the TURBOFIT wiki row: 4 orbs + each integration logo.
// Run: PATH=$HOME/.hermes/node/bin:$PATH PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-s.js [--vp 1456x914] [--shot assets/look]
const {chromium}=require(process.env.PW||'playwright'); const path=require('path'); const fs=require('fs');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const a=process.argv; const vi=a.indexOf('--vp'); const [W,H]=(vi>0?a[vi+1]:'1456x914').split('x').map(Number); const si=a.indexOf('--shot'); const SHOT=si>0?a[si+1]:null;
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3600);
 const out={vp:W+'x'+H, cards:{}};
 const row=await p.evaluate(()=>{ const t=[...document.querySelectorAll('#view-wiki .topic')].find(x=>x.querySelector('.tname').textContent.trim().toLowerCase()==='turbofit'); const r=t.querySelector('.thead').getBoundingClientRect(); return {x:Math.round(r.left+60), y:Math.round(r.top+r.height/2)}; });
 await p.mouse.move(row.x,row.y); await p.waitForTimeout(350);
 const icons=await p.evaluate(()=>{ const t=[...document.querySelectorAll('#view-wiki .topic')].find(x=>x.querySelector('.tname').textContent.trim().toLowerCase()==='turbofit'); return t._hcard.icons.map(ic=>{ const r=ic.getBoundingClientRect(); return {id:ic.dataset.k||ic.dataset.kind, x:Math.round(r.left+r.width/2), y:Math.round(r.top+r.height/2)}; }); });
 for(const ic of icons){
   const restY=await p.evaluate(({x,y})=>{ const el=document.elementFromPoint(x,y); const ico=el&&el.closest('.orb,.iwrap'); if(!ico) return null; const g=ico.classList.contains('iwrap')?ico.querySelector('.idot'):ico; const r=g.getBoundingClientRect(); const m=new DOMMatrixReadOnly(getComputedStyle(g).transform); return {top:r.top-(m.m42||0), h:r.height}; },ic);
   await p.mouse.move(ic.x, ic.y); await p.waitForTimeout(420);
   const m=await p.evaluate(({x,y,restY})=>{ const t=[...document.querySelectorAll('#view-wiki .topic')].find(x=>x.querySelector('.tname').textContent.trim().toLowerCase()==='turbofit');
     const card=t.querySelector('.hcard'), box=card.querySelector('.hbox'), body=card.querySelector('.hbody'), head=card.querySelector('.hhead');
     const ico=t.querySelector('.orb.hov, .iwrap.hov'); const g=ico&&(ico.classList.contains('iwrap')?ico.querySelector('.idot'):ico); const ir=ico?ico.getBoundingClientRect():null; const gr=g?g.getBoundingClientRect():null; const rise=g&&restY? Math.round(restY.top-gr.top):null;
     const cap=ico? (ico.classList.contains('orb')? getComputedStyle(ico,'::before') : getComputedStyle(ico.querySelector('.icap'))) : null;
     const br=box.getBoundingClientRect(); const rows=[...body.querySelectorAll('.hrow,.hp,.ilink,.iadd')].map(e=>e.textContent.trim().replace(/\s+/g,' ').slice(0,70));
     const mask=getComputedStyle(body).webkitMaskImage||getComputedStyle(body).maskImage;
     const occl=[0.25,0.5,0.75].map(fx=>[0.3,0.6,0.9].map(fy=>{ const e=document.elementFromPoint(br.left+br.width*fx, br.top+br.height*fy); return !!(e&&e.closest('.hcard')); })).flat();
     return {shown:card.classList.contains('show')&&card.classList.contains('in'), boxOpacity:+getComputedStyle(box).opacity, rise, capOpacity:cap?+cap.opacity:null, capText:ico? (ico.classList.contains('orb')? ico.dataset.label : ico.querySelector('.icap').textContent):null,
       head:head.textContent.trim().replace(/\s+/g,' '), rows, box:{l:Math.round(br.left),t:Math.round(br.top),r:Math.round(br.right),b:Math.round(br.bottom),w:Math.round(br.width),h:Math.round(br.height)}, iconCx:ir?Math.round(ir.left+ir.width/2):null,
       inViewport: br.left>=0&&br.top>=0&&br.right<=innerWidth&&br.bottom<=innerHeight, onTop: occl.every(Boolean), border:getComputedStyle(box).borderTopColor, bg:getComputedStyle(box).backgroundColor, bodyMaxH:getComputedStyle(body).maxHeight, hasFade:/gradient/.test(mask)||body.classList.contains('fits'), fits:body.classList.contains('fits'), scrollable:body.scrollHeight>body.clientHeight+1 }; },{...ic,restY});
   out.cards[ic.id]=m;
   if(SHOT){ fs.mkdirSync(SHOT,{recursive:true}); await p.screenshot({path:path.join(SHOT,`S-${ic.id}-${W}x${H}.png`)}); }
 }
 // scroll + fade with ≥8 items: inject 10 skill rows into the snapshot for a synthetic topic-less check using the same renderer path
 await p.mouse.move(row.x,row.y); await p.waitForTimeout(400);
 const scrollT=await p.evaluate(async()=>{ const t=[...document.querySelectorAll('#view-wiki .topic')].find(x=>x.querySelector('.tname').textContent.trim().toLowerCase()==='turbofit');
   const card=t.querySelector('.hcard'), body=card.querySelector('.hbody'); const orb=t.querySelector('.orb[data-k=skills]'); orb.dispatchEvent(new MouseEvent('mouseenter',{bubbles:false}));
   await new Promise(r=>setTimeout(r,300));
   body.innerHTML=Array.from({length:12},(_,i)=>'<div class="hrow"><span class="nm">probe-skill-'+(i+1)+'</span></div>').join(''); body.dispatchEvent(new Event('scroll'));
   const before=body.scrollTop, sh=body.scrollHeight, ch=body.clientHeight; const mask0=getComputedStyle(body).webkitMaskImage;
   const view=document.getElementById('view-wiki'); const pv=view.scrollTop;
   card.dispatchEvent(new WheelEvent('wheel',{deltaY:120,bubbles:true,cancelable:true}));
   await new Promise(r=>setTimeout(r,50));
   const res={sh,ch,scrollable:sh>ch+1, before, after:body.scrollTop, pageScrollBefore:pv, pageScrollAfter:view.scrollTop, fadeAtTop:/gradient/.test(mask0)&&!body.classList.contains('fits'), maxH:getComputedStyle(body).maxHeight};
   body.scrollTop=sh; body.dispatchEvent(new Event('scroll')); res.fadeAtEnd=!/gradient/.test(getComputedStyle(body).webkitMaskImage);
   body.scrollTop=60; body.dispatchEvent(new Event('scroll'));   /* leave it mid-list so the LOOK shot shows the fade */
   return res; });
 out.scroll=scrollT;
 if(SHOT) await p.screenshot({path:path.join(SHOT,`S-scroll-${W}x${H}.png`)});
 // grace: leave icon → card within 250ms stays; leave both → closes ~100ms after grace
 const skills=icons.find(i=>i.id==='skills'); await p.mouse.move(skills.x,skills.y); await p.waitForTimeout(420);
 const cb=await p.evaluate(()=>{ const c=document.querySelector('#view-wiki .hcard.show .hbox').getBoundingClientRect(); return {x:Math.round(c.left+c.width/2), y:Math.round(c.top+40)}; });
 await p.mouse.move(cb.x, cb.y, {steps:4}); await p.waitForTimeout(300);
 const stillOpen=await p.evaluate(()=>!!document.querySelector('#view-wiki .hcard.show.in'));
 await p.mouse.move(row.x, row.y+200, {steps:3}); await p.waitForTimeout(150); const openAt150=await p.evaluate(()=>!!document.querySelector('#view-wiki .hcard.show.in'));
 await p.waitForTimeout(400); const closedAt550=await p.evaluate(()=>!document.querySelector('#view-wiki .hcard.show'));
 out.grace={stillOpenOnCard:stillOpen, openAt150msAfterLeave:openAt150, closedAt550ms:closedAt550};
 // dead zone: pointer in the right lane → no card
 await p.mouse.move(W-100, row.y); await p.waitForTimeout(200);
 out.deadzone={bodyDead:await p.evaluate(()=>document.body.classList.contains('deadzone')), cards:await p.evaluate(()=>document.querySelectorAll('#view-wiki .hcard.show').length)};
 // click-through unchanged: click the skills orb → editor opens at SKILLS
 await p.mouse.move(row.x,row.y); await p.waitForTimeout(300); await p.mouse.move(skills.x,skills.y); await p.waitForTimeout(300); await p.mouse.click(skills.x,skills.y); await p.waitForTimeout(600);
 out.click={editorOn:await p.evaluate(()=>document.getElementById('view-editor').classList.contains('on')), title:await p.evaluate(()=>document.getElementById('edTitle').textContent)};
 out.errors=errs;
 console.log(JSON.stringify(out,null,1)); await b.close();
})().catch(e=>{ console.error('PROBE CRASH',e); process.exit(2); });
