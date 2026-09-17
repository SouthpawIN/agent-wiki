// W (v14.43) probe — bot + skill pages open in the SAME editor with a breadcrumb; \ returns to the right list.
// Run: PATH=$HOME/.hermes/node/bin:$PATH PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-W.js [--vp 1456x914] [--shot assets/look]
const {chromium}=require(process.env.PW||'playwright');
const path=require('path'), fs=require('fs');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const a=process.argv; const vp=a.indexOf('--vp'); const [W,H]=(vp>0?a[vp+1]:'1456x914').split('x').map(Number);
const sh=a.indexOf('--shot'); const SHOT=sh>0?a[sh+1]:null;
const R=[]; const ok=(n,c,d)=>R.push({n,ok:!!c,d});
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3600); // past the 3s stripArm auto-close
 const lists=await p.evaluate(()=>({bots:document.querySelectorAll('#bots-list .topic').length, skills:document.querySelectorAll('#skills-list .topic').length}));
 ok('live lists rendered (bots ≥ 8, skills ≥ 100)', lists.bots>=8&&lists.skills>=100, JSON.stringify(lists));
 await p.mouse.move(300,500);
 const loaded=()=>p.evaluate(()=>new Promise(r=>{ const s=window.edW.state(); if(s&&s.ready) return r(true); document.addEventListener('edW:loaded',()=>r(true),{once:true}); setTimeout(()=>r(false),6000); }));
 const state=()=>p.evaluate(()=>{ const q=s=>document.querySelector(s); const on=[...document.querySelectorAll('.view.on')].map(v=>v.id);
   const secs=[...document.querySelectorAll('#edBody .tbody-inner .sec')].map(s=>s.textContent.trim()).slice(0,14);
   const files=[...document.querySelectorAll('#edBody .mdfile')].map(f=>({file:f.dataset.file, chars:f.querySelector('.mdbody').innerText.length, loading:!!f.querySelector('.loading')}));
   const cr=q('#edCrumb'); const cb=cr.getBoundingClientRect(); const tb=q('#edTitle').getBoundingClientRect();
   return {on, title:q('#edTitle').textContent.trim(), crumb:[...cr.querySelectorAll('.seg')].map(x=>x.textContent).join(' / '), crumbShown:cr.classList.contains('show')&&cb.height>0, crumbAboveTitle:cb.bottom<=tb.top+1, secs, files, hash:location.hash, tab:(q('.navtab.on')||{}).textContent, editable:q('#edBody .tbody-inner')?.getAttribute('contenteditable'), avatar:q('#edAvatar').classList.contains('show')}; });
 // ---- BOT · weaver ----
 await p.evaluate(()=>{ document.querySelector('.navtab[data-view="bots"]').click(); });
 await p.waitForTimeout(200);
 await p.evaluate(()=>{ const row=[...document.querySelectorAll('#bots-list .topic')].find(t=>t.dataset.bot==='weaver'); row.querySelector('.thead').click(); });
 ok('bot: content loaded via bridge', await loaded());
 await p.waitForTimeout(250);
 const s1=await state();
 ok('bot: editor view on, title weaver', s1.on.includes('view-editor')&&s1.title==='weaver', JSON.stringify({on:s1.on,title:s1.title}));
 ok('bot: breadcrumb "BOTS / weaver", shown, above title', s1.crumb==='BOTS / weaver'&&s1.crumbShown&&s1.crumbAboveTitle, JSON.stringify({crumb:s1.crumb,shown:s1.crumbShown,above:s1.crumbAboveTitle}));
 ok('bot: SOUL.md + AGENTS.md both rendered (>400 chars each, no loading stub)', s1.files.length===2&&s1.files.every(f=>f.chars>400&&!f.loading), JSON.stringify(s1.files));
 ok('bot: SOUL.md + AGENTS.md sections present (Fleet / Hard rules / Role / Work loop)', /FLEET/i.test(s1.secs.join('|'))&&/HARD RULES/i.test(s1.secs.join('|'))&&/ROLE/i.test(s1.secs.join('|'))&&/WORK LOOP/i.test(s1.secs.join('|')), s1.secs.join(' | ').slice(0,300));
 ok('bot: body is contenteditable, pet avatar shown (bots page rule), hash #bots/weaver', s1.editable==='true'&&s1.avatar&&s1.hash==='#bots/weaver', JSON.stringify({ed:s1.editable,av:s1.avatar,hash:s1.hash}));
 if(SHOT){ fs.mkdirSync(SHOT,{recursive:true}); await p.screenshot({path:path.join(SHOT,`W-bot-weaver-${W}x${H}.png`)}); }
 // \ returns to BOTS
 await p.evaluate(()=>document.getElementById('edBack').click()); await p.waitForTimeout(250);
 const s2=await state();
 ok('bot: \\ returns to BOTS list (view-bots on, tab BOTS, crumb hidden, row body restored)', s2.on.includes('view-bots')&&!s2.on.includes('view-editor')&&/BOTS/.test(s2.tab||'')&&!s2.crumbShown, JSON.stringify({on:s2.on,tab:s2.tab,crumbShown:s2.crumbShown}));
 const rowBack=await p.evaluate(()=>{ const row=[...document.querySelectorAll('#bots-list .topic')].find(t=>t.dataset.bot==='weaver'); return {hasBody:!!row.querySelector('.tbody .tbody-inner'), summary:/ROLE/.test(row.querySelector('.tbody-inner').textContent), w:row.querySelector('.tbody').dataset.w||null}; });
 ok('bot: row body back in list with its summary (no leftover data-w)', rowBack.hasBody&&rowBack.summary&&!rowBack.w, JSON.stringify(rowBack));
 ok('bot: no edit → nothing sent', await p.evaluate(()=>!(window.__lastAskPayload)), '');
 // ---- SKILL · bot-verify-loop ----
 await p.evaluate(()=>{ document.querySelector('.navtab[data-view="skills"]').click(); }); await p.waitForTimeout(200);
 await p.evaluate(()=>{ const row=[...document.querySelectorAll('#skills-list .topic')].find(t=>t.dataset.skill==='bot-verify-loop'); row.querySelector('.thead').click(); });
 ok('skill: content loaded via bridge', await loaded()); await p.waitForTimeout(250);
 const s3=await state();
 ok('skill: editor on, title bot-verify-loop', s3.on.includes('view-editor')&&s3.title==='bot-verify-loop', JSON.stringify({on:s3.on,title:s3.title}));
 ok('skill: breadcrumb "SKILLS / devops / bot-verify-loop"', s3.crumb==='SKILLS / devops / bot-verify-loop'&&s3.crumbShown&&s3.crumbAboveTitle, JSON.stringify({crumb:s3.crumb,shown:s3.crumbShown}));
 ok('skill: SKILL.md rendered (frontmatter + LOOK loop sections)', s3.files.length===1&&s3.files[0].chars>800&&/LOOK/i.test(s3.secs.join('|'))&&/DONE/i.test(s3.secs.join('|')), JSON.stringify({files:s3.files,secs:s3.secs.slice(0,6)}));
 ok('skill: no pet avatar on a skill page, hash #skills/devops/bot-verify-loop', !s3.avatar&&s3.hash==='#skills/devops/bot-verify-loop', JSON.stringify({av:s3.avatar,hash:s3.hash}));
 if(SHOT) await p.screenshot({path:path.join(SHOT,`W-skill-bot-verify-loop-${W}x${H}.png`)});
 // round-trip fidelity: md → html → md equals source (normalized)
 const rt=await p.evaluate(()=>{ const s=window.edW.state(); const f=s.files[0]; const el=document.querySelector('#edBody .mdfile .mdbody'); const back=window.edW.toMd(el); const norm=x=>x.replace(/\s+/g,' ').trim(); const heads=t=>(t.match(/^#{1,6} .*$/gm)||[]).join('|'); return {sameText:norm(back)===norm(f.text), sameHeads:heads(back)===heads(f.text), stable:back===window.edW.toMd(el), fm:/^---\n/.test(back), a:norm(f.text).length, b:norm(back).length}; });
 ok('skill: toMd(md(x)) keeps every word + every heading + frontmatter of SKILL.md (soft-wraps re-flow) and is idempotent', rt.sameText&&rt.sameHeads&&rt.stable&&rt.fm, JSON.stringify(rt));
 // edit → \ → protected write request goes out through the bridge (/ask); intercept so nothing is actually asked
 await p.route('**/ask**', r=>{ r.fulfill({status:202, contentType:'application/json', body:'{"ok":true,"id":"probe"}'}); });
 let askBody=null; p.on('request',rq=>{ if(/\/ask/.test(rq.url())) askBody=rq.postData(); });
 await p.evaluate(()=>{ const pEl=document.querySelector('#edBody .mdfile .mdbody p'); pEl.appendChild(document.createTextNode(' PROBE-EDIT-W')); pEl.dispatchEvent(new InputEvent('input',{bubbles:true,inputType:'insertText',data:' PROBE-EDIT-W'})); /* typing fires input → edited flag (AUTOSAVE guard) */ });
 await p.evaluate(()=>document.getElementById('edBack').click()); await p.waitForTimeout(600);
 const s4=await state();
 ok('skill: \\ returns to SKILLS list', s4.on.includes('view-skills')&&/SKILLS/.test(s4.tab||'')&&!s4.crumbShown, JSON.stringify({on:s4.on,tab:s4.tab}));
 let askJ=null; try{ askJ=JSON.parse(askBody||'null'); }catch(e){}
 ok('skill: edited page → ONE /ask write request naming the real SKILL.md path + carrying the edit', !!askJ&&/bot-verify-loop\/SKILL\.md/.test(askJ.text)&&/PROBE-EDIT-W/.test(askJ.text)&&/^---\n/.test(askJ.text.split('replacing its contents:\n\n')[1]||''), askJ?askJ.text.slice(0,160).replace(/\n/g,'⏎'):'no /ask');
 // deep link
 await p.goto('about:blank'); await p.goto(FILE+'#bots/weaver',{waitUntil:'domcontentloaded'}); await p.waitForTimeout(1500);
 const s5=await state();
 ok('deep link #bots/weaver opens the bot page directly', s5.on.includes('view-editor')&&s5.title==='weaver'&&s5.crumb==='BOTS / weaver', JSON.stringify({on:s5.on,title:s5.title,crumb:s5.crumb}));
 // wiki topics unaffected: no crumb
 await p.evaluate(()=>document.getElementById('edBack').click()); await p.waitForTimeout(200);
 await p.evaluate(()=>{ document.querySelector('.navtab[data-view="wiki"]').click(); }); await p.waitForTimeout(150);
 await p.evaluate(()=>{ document.querySelector('#view-wiki .topic .thead').click(); }); await p.waitForTimeout(250);
 const s6=await state();
 ok('wiki topic: editor unchanged — no breadcrumb, no data-w', s6.on.includes('view-editor')&&!s6.crumbShown&&s6.files.length===0, JSON.stringify({crumb:s6.crumb,files:s6.files.length}));
 await p.evaluate(()=>document.getElementById('edBack').click()); await p.waitForTimeout(200);
 ok('wiki topic: \\ returns to WIKI', await p.evaluate(()=>document.getElementById('view-wiki').classList.contains('on')));
 const real=errs.filter(e=>!/avatars\/chris\.(png|svg)|ERR_FILE_NOT_FOUND/.test(e)); /* chris.png 404 is the pre-existing 'you' avatar gap ([FIXES] queue), not W */
 ok('no page/console errors (excluding the known chris-avatar 404)', real.length===0, real.slice(0,3).join(' | '));
 await b.close();
 let f=0; for(const r of R){ console.log((r.ok?'PASS':'FAIL')+'  '+r.n+(r.d?'  — '+r.d:'')); if(!r.ok) f++; }
 console.log(`\n${R.length-f}/${R.length} passed @ ${W}x${H}`); process.exit(f?1:0);
})().catch(e=>{ console.error('PROBE CRASH',e); process.exit(2); });
