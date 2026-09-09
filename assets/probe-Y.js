// probe-Y.js — Y (v14.48): no baked collections. Proves BOTS/SKILLS render from .system-live.json via loadLive(),
// rows === profiles-with-SOUL.md, a throwaway profile appears on fleet/changed + disappears when removed, cached fallback labels itself.
//   PATH=$HOME/.hermes/node/bin:$PATH PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-Y.js [--vp 1456x914] [--shot assets/look]
const {chromium}=require(process.env.PW||'playwright'); const path=require('path'), fs=require('fs'), os=require('os'), cp=require('child_process');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const a=process.argv.indexOf('--vp'); const [W,H]=(a>0?process.argv[a+1]:'1456x914').split('x').map(Number);
const sh=process.argv.indexOf('--shot'); const SHOT=sh>0?process.argv[sh+1]:null;
const PROF=path.join(os.homedir(),'.hermes','profiles'); const SCAN=path.resolve(__dirname,'scan-topics.py');
const soulCount=()=>fs.readdirSync(PROF).filter(d=>fs.existsSync(path.join(PROF,d,'SOUL.md'))).length;
const R=[]; const ok=(n,c,d)=>R.push({n,ok:!!c,d});
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE+'?view=bots',{waitUntil:'domcontentloaded'});
 await p.waitForFunction(()=>document.querySelectorAll('#bots-list .topic').length>0,{timeout:8000}).catch(()=>{});
 await p.waitForTimeout(600);
 const state=()=>p.evaluate(()=>({ bots:[...document.querySelectorAll('#bots-list .topic')].map(t=>t.dataset.bot), skills:document.querySelectorAll('#skills-list .topic').length,
   meta:document.querySelector('#view-bots .heroMeta').textContent, baked:(typeof LIVE_BOTS!=='undefined')||(typeof LIVE_SKILLS!=='undefined'), live:!!(window.LIVE&&LIVE.bots&&LIVE.bots.length),
   dots:[...document.querySelectorAll('#bots-list .ldot')].map(d=>d.dataset.state), pets:[...document.querySelectorAll('#bots-list .thead img.avatar')].filter(i=>i.complete&&i.naturalWidth>0).length, monos:document.querySelectorAll('#bots-list .thead .avatar.mono').length }));
 let s=await state(); const N=soulCount();
 ok('Y no baked constants in scope (LIVE_BOTS/LIVE_SKILLS undefined)', !s.baked);
 ok('Y BOTS rows === profiles with SOUL.md ('+N+')', s.bots.length===N, JSON.stringify(s.bots));
 ok('Y weaver + paladin present', s.bots.includes('weaver')&&s.bots.includes('paladin'));
 ok('Y every row has a status dot (idle at boot unless the bridge said otherwise)', s.dots.length===N && s.dots.every(Boolean), JSON.stringify(s.dots));
 ok('Y avatar on every row: pet when assets/avatars/<bot>.png exists, else monogram', s.pets+s.monos===N, s.pets+' pets + '+s.monos+' monograms / '+N);
 ok('Y SKILLS ≥118 rows from live scan, bot-verify-loop present', s.skills>=118 && await p.evaluate(()=>!![...document.querySelectorAll('#skills-list .topic .tname')].find(x=>x.textContent.trim()==='bot-verify-loop')), s.skills+' rows');
 ok('Y hero meta says LIVE SCAN (not cached) with bot count', /LIVE SCAN/.test(s.meta) && s.meta.includes(N+' bots'), s.meta);
 if(SHOT){ fs.mkdirSync(SHOT,{recursive:true}); await p.screenshot({path:path.join(SHOT,`Y-bots-${W}x${H}.png`)}); }
 // live status dot from a bridge-shaped event
 await p.evaluate(()=>botStatus('weaver','working'));
 ok('Y botStatus(weaver, working) → dot working', (await p.evaluate(()=>document.querySelector('#bots-list .topic[data-bot="weaver"] .ldot').dataset.state))==='working');
 // throwaway profile: appears on fleet/changed, disappears when removed
 const tmp=path.join(PROF,'_y-probe-bot'); fs.mkdirSync(tmp,{recursive:true}); fs.writeFileSync(path.join(tmp,'SOUL.md'),'# Y Probe\n\nThrowaway probe bot for the Y ledger — delete me.\n');
 try{
  cp.execSync('python3 '+JSON.stringify(SCAN),{stdio:'ignore'});
  await p.evaluate(()=>window.postMessage({kind:'fleet/changed'},'*')); // same path handle() takes for the SSE event
  await p.waitForFunction(()=>[...document.querySelectorAll('#bots-list .topic')].some(t=>t.dataset.bot==='_y-probe-bot'),{timeout:8000}).catch(()=>{});
  s=await state(); ok('Y throwaway profile with SOUL.md appears after fleet/changed (rows '+s.bots.length+' === SOUL dirs '+soulCount()+')', s.bots.includes('_y-probe-bot') && s.bots.length===soulCount(), JSON.stringify(s.bots));
  ok('Y monogram avatar for the pet-less probe bot', await p.evaluate(()=>!!document.querySelector('#bots-list .topic[data-bot="_y-probe-bot"] .avatar.mono')));
  // V type-ahead sees it too (reads rows lazily)
 } finally { fs.rmSync(tmp,{recursive:true,force:true}); }
 cp.execSync('python3 '+JSON.stringify(SCAN),{stdio:'ignore'});
 await p.evaluate(()=>loadLive('fleet/changed'));
 await p.waitForFunction(()=>![...document.querySelectorAll('#bots-list .topic')].some(t=>t.dataset.bot==='_y-probe-bot'),{timeout:8000}).catch(()=>{});
 s=await state(); ok('Y probe bot gone after removal + rescan (rows '+s.bots.length+' === '+N+')', !s.bots.includes('_y-probe-bot') && s.bots.length===N);
 // cached fallback: break the bridge token so vaultFetch fails → last-good copy, labeled
 await p.evaluate(()=>{ window.__bridgeToken='bad-token'; return loadLive('probe-offline'); });
 s=await state(); ok('Y offline → last-good localStorage copy, hero meta labeled CACHED · <age> AGO, rows intact', /CACHED · \d+[smh] AGO/.test(s.meta) && s.bots.length===N, s.meta);
 await p.evaluate(()=>{ window.__bridgeToken=null; return loadLive('probe-online'); }); s=await state(); ok('Y back online → LIVE SCAN label', /LIVE SCAN/.test(s.meta), s.meta);
 ok('no page/console errors (401s from the deliberate offline step excluded)', errs.filter(e=>!/401/.test(e)).length===0, errs.filter(e=>!/401/.test(e)).slice(0,3).join(' | '));
 await b.close(); let f=0; for(const r of R){ console.log((r.ok?'PASS':'FAIL')+'  '+r.n+(r.d?'  — '+r.d:'')); if(!r.ok) f++; } console.log(`\n${R.length-f}/${R.length} passed @ ${W}x${H}`); process.exit(f?1:0);
})().catch(e=>{ console.error('PROBE CRASH',e); process.exit(2); });
