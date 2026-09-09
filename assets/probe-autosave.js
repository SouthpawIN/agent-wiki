// URGENT autosave probe — bot/skill pages open, idle 90s (default) with realistic pointer traffic, close via \ and Esc and tab switch: assert ZERO /ask write posts.
// Also: round-trip fidelity toMd(md(src)) vs the real mirror source for turbosovth/weaver SOUL+AGENTS and skill turbofit; and a REAL edit still produces exactly one write.
// Run: PATH=$HOME/.hermes/node/bin:$PATH PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-autosave.js [idleSeconds]
const {chromium}=require(process.env.PW||'playwright');
const path=require('path'), fs=require('fs');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const IDLE=+(process.argv[2]||90);
const R=[]; const ok=(n,c,d)=>R.push({n,ok:!!c,d});
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1040,height:880}});
 const asks=[]; await p.route('**/ask**', r=>{ asks.push(JSON.parse(r.request().postData()||'{}')); r.fulfill({status:202,contentType:'application/json',body:'{"ok":true,"id":"probe"}'}); });
 const posts=[]; await p.route('**/post**', r=>{ posts.push(r.request().postData()); r.fulfill({status:200,contentType:'application/json',body:'{"ok":true}'}); });
 const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3600);
 const loaded=()=>p.evaluate(()=>new Promise(r=>{ const s=window.edW.state(); if(s&&s.ready) return r(true); document.addEventListener('edW:loaded',()=>r(true),{once:true}); setTimeout(()=>r(false),8000); }));
 async function openBot(name){ await p.evaluate(()=>document.querySelector('.navtab[data-view="bots"]').click()); await p.waitForTimeout(200); await p.evaluate(n=>{ const row=[...document.querySelectorAll('#bots-list .topic')].find(t=>t.dataset.bot===n); row.querySelector('.thead').click(); }, name); return loaded(); }
 async function openSkill(name){ await p.evaluate(()=>document.querySelector('.navtab[data-view="skills"]').click()); await p.waitForTimeout(200); await p.evaluate(n=>{ const row=[...document.querySelectorAll('#skills-list .topic')].find(t=>t.dataset.skill===n); row.querySelector('.thead').click(); }, name); return loaded(); }
 // ---- round-trip fidelity against the real source ----
 for(const [kind,name] of [['bot','turbosovth'],['bot','weaver'],['skill','turbofit']]){
   ok(`${kind} ${name}: content loaded`, kind==='bot'?await openBot(name):await openSkill(name));
   const rt=await p.evaluate(()=>{ const s=window.edW.state(); return s.files.filter(f=>f.loaded).map(f=>{ const el=document.querySelector('#edBody .mdfile[data-file="'+f.label+'"] .mdbody'); const back=window.edW.fileMd(f,el); const a=String(f.text).replace(/\s+$/,''), c=back.replace(/\s+$/,''); let i=0; while(i<a.length&&a[i]===c[i]) i++; return {file:f.label, exact:a===c, srcLen:a.length, backLen:c.length, firstDiff:a===c?-1:i, ctx:a===c?'':JSON.stringify([a.slice(Math.max(0,i-40),i+60), c.slice(Math.max(0,i-40),i+60)])}; }); });
   for(const r of rt) ok(`${name}/${r.file}: toMd(md(src)) === src byte-for-byte (untouched page)`, r.exact, r.exact?`${r.srcLen} chars`:`diff@${r.firstDiff} ${r.ctx}`);
   await p.evaluate(()=>document.getElementById('edBack').click()); await p.waitForTimeout(300);
 }
 ok('no /ask after opening+closing three pages untouched', asks.length===0, asks.length+' asks');
 // ---- idle soak on a bot page with realistic pointer traffic ----
 ok('turbosovth open for soak', await openBot('turbosovth'));
 const t0=Date.now(); let i=0;
 while(Date.now()-t0 < IDLE*1000){ // wander: hero, nav strip, editor body, click into body (focus), Esc-less
   await p.mouse.move(300+((i*37)%400), 30+((i*53)%700)); if(i%7===0){ await p.mouse.move(300,30); } if(i%11===0){ const c=await p.evaluate(()=>{ const el=document.querySelector('#edBody .mdfile .mdbody p'); if(!el) return null; const r=el.getBoundingClientRect(); return {x:Math.round(r.left+10),y:Math.round(r.top+8)}; }); if(c) await p.mouse.click(c.x,c.y); }
   await p.waitForTimeout(500); i++; }
 ok(`idle soak ${IDLE}s (pointer wander + focus clicks): ZERO /ask write posts`, asks.length===0, asks.length+' asks');
 // close paths: \ , Esc, nav tab switch, type-ahead go() — all must send nothing
 await p.evaluate(()=>document.getElementById('edBack').click()); await p.waitForTimeout(300);
 ok('\\ close after soak: zero asks', asks.length===0, asks.length+'');
 ok('reopen', await openBot('weaver')); await p.keyboard.press('Escape'); await p.waitForTimeout(300); ok('Esc close: zero asks', asks.length===0, asks.length+'');
 ok('reopen', await openBot('weaver')); await p.evaluate(()=>document.querySelector('.navtab[data-view="wiki"]').click()); await p.waitForTimeout(400); await p.evaluate(()=>{ const m=document.getElementById('warnMask'); if(m){ const d=[...m.querySelectorAll('button,.btn')].find(x=>/DISCARD|STAY/i.test(x.textContent)); } }); ok('tab-switch close: zero asks', asks.length===0, asks.length+'');
 ok('skip reason recorded (no user edit)', await p.evaluate(()=>window.__edWLastSkip==='no user edit'), await p.evaluate(()=>window.__edWLastSkip));
 // ---- a REAL edit still saves: exactly one /ask for the edited file, carrying the typed text, other file untouched ----
 await p.evaluate(()=>{ const m=document.getElementById('warnMask'); if(m) m.remove(); document.querySelector('.view.on')&&0; });
 ok('reopen turbosovth for real edit', await openBot('turbosovth'));
 const c=await p.evaluate(()=>{ const el=document.querySelector('#edBody .mdfile[data-file="SOUL.md"] .mdbody p'); const r=el.getBoundingClientRect(); return {x:Math.round(r.right-4),y:Math.round(r.top+8)}; });
 await p.mouse.click(c.x,c.y); await p.keyboard.press('End'); await p.keyboard.type(' PROBE-REAL-EDIT'); await p.waitForTimeout(200);
 await p.evaluate(()=>document.getElementById('edBack').click()); await p.waitForTimeout(800);
 ok('real edit → exactly ONE /ask, SOUL.md only, carries typed text', asks.length===1 && /turbosovth\/SOUL\.md/.test(asks[0].text) && /PROBE-REAL-EDIT/.test(asks[0].text), asks.map(a=>a.text.split('\n')[0].slice(0,80)).join(' | '));
 ok('AGENTS.md (untouched) NOT sent alongside', !asks.some(a=>/AGENTS\.md/.test(a.text)));
 // partial-edit fidelity: the sent SOUL.md must equal the disk source with ONLY the edited paragraph changed (every other line byte-identical)
 { const sent=(asks[0]&&asks[0].text.split('replacing its contents:\n\n')[1])||''; const src=await p.evaluate(()=>window.__probeSrc||null);
   const srcTxt=fs.existsSync(path.join(__dirname,'..','topics/senter-wiki/.system/mirror/bots/turbosovth/SOUL.md'))?fs.readFileSync(path.join(__dirname,'..','topics/senter-wiki/.system/mirror/bots/turbosovth/SOUL.md'),'utf8'):'';
   const a=srcTxt.replace(/\s+$/,'').split('\n'), c=sent.replace(/\s+$/,'').split('\n'); const sentSet=new Set(c); const missing=a.filter(l=>l.trim()&&!sentSet.has(l)); const extra=c.filter(l=>l.trim()&&!new Set(a).has(l));
   /* only the edited paragraph's source lines may be missing (the Role/Mission block: 2 hard-wrapped lines → 1 re-serialized line carrying the typed text); every other non-blank source line must appear verbatim */
   ok('partial edit: every unedited source line verbatim; only the edited block re-serialized', srcTxt&&missing.length<=2&&missing.every(l=>/Role:|Mission:/.test(l))&&extra.length===1&&/PROBE-REAL-EDIT/.test(extra[0])&&sent.endsWith('\n'), `missing ${missing.length} (${missing.map(l=>l.slice(0,20)).join('|')}) extra ${extra.length}`); }
 ok('no page errors', errs.length===0, errs.slice(0,2).join(' | '));
 await b.close();
 let f=0; for(const r of R){ console.log((r.ok?'PASS':'FAIL')+'  '+r.n+(r.d?'  — '+r.d:'')); if(!r.ok) f++; }
 console.log(`\n${R.length-f}/${R.length} passed (idle ${IDLE}s)`); process.exit(f?1:0);
})().catch(e=>{ console.error('PROBE CRASH',e); process.exit(2); });
