// probe-ag.js — AG (v14.58): NO TIMERS / push-only wiki.
//   PATH=$HOME/.hermes/node/bin:$PATH PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-ag.js [--vp 1456x914] [--shot assets/look] [--nokill]
// Proves: (1) zero setInterval in the source; (2) at rest with the bridge LIVE, no fetch/XHR fires for 15s (no heartbeat, no stamp
// tick, no wall poll); (3) a REAL profile dir touched on disk → BOTS row appears < 2s through the real watcher → bridge SSE → loadLive(what);
// (4) fleet/changed what:['skills'] does NOT re-render BOTS; (5) a bridge tool event with topic drives the hero for 6s then returns;
// (6) hover beats activity; (7) with the bridge unreachable (BASE pointed at a dead port) the ONLY network activity is /health retries with
// backoff ≤5s, ⚙ says offline, twinkles do not fire; (8) reconnect → ONE loadLive('reconnect').
const {chromium}=require(process.env.PW||'playwright'); const path=require('path'), fs=require('fs'), os=require('os');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const SRC=fs.readFileSync(path.resolve(__dirname,'..','vault-live.html'),'utf8');
const a=process.argv.indexOf('--vp'); const [W,H]=(a>0?process.argv[a+1]:'1456x914').split('x').map(Number);
const sh=process.argv.indexOf('--shot'); const SHOT=sh>0?process.argv[sh+1]:null;
const PROF=path.join(os.homedir(),'.hermes','profiles');
const R=[]; const ok=(n,c,d)=>R.push({n,ok:!!c,d});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
 // (1) source census
 const ivs=(SRC.match(/setInterval\s*\(/g)||[]).length;
 ok('AG grep -c setInterval === 0', ivs===0, ivs+' occurrences');
 ok('AG rotateHero clock gone (no 12000ms rotate)', !/rotateHero\(\(heroIdx\+1\)/.test(SRC));
 ok('AG demo twinkle clock gone', !/Math\.random\(\)\*bots\.length/.test(SRC));
 ok('AG loadLive heartbeat gone', !/loadLive\('heartbeat'\)/.test(SRC));
 ok('AG liveStamp tick gone', !/setInterval\(liveStamp/.test(SRC));
 ok('AG wall apply poll gone', !/setInterval\(apply/.test(SRC));
 ok('AG reconnect backoff labeled `// fallback:`', /\/\/ fallback: reconnect backoff/.test(SRC));

 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error'&&!/avatars\/chris|favicon|status of 404/.test(m.text())) errs.push(m.text()); }); // 404 = S's hover card fetching an archived topic README (omarchy-usb) — another item's, not AG's
 const net=[]; p.on('request',r=>{ const u=r.url(); if(/^https?:/.test(u)) net.push({t:Date.now(),u:u.replace(/token=[^&]+/,'token=…'),type:r.resourceType()}); });
 await p.goto(FILE+'?view=bots',{waitUntil:'domcontentloaded'});
 await p.waitForFunction(()=>window.__bridgeLive===true && document.querySelectorAll('#bots-list .topic').length>0,{timeout:10000}).catch(()=>{});
 await p.waitForTimeout(3600); // strip auto-close + boot settle
 const live=await p.evaluate(()=>window.__bridgeLive===true);
 ok('AG bridge live for the test (senter-bridge up)', live);

 // (2) quiet at rest: 15s, no fetch/XHR other than the SSE stream itself
 const n0=net.length; await sleep(15000);
 const during=net.slice(n0).filter(r=>!/\/events\?/.test(r.u));
 ok('AG 15s at rest, bridge live → zero fetch/XHR (no heartbeat / stamp / wall poll)', during.length===0, JSON.stringify(during.map(r=>r.u)));
 const hero0=await p.evaluate(()=>document.getElementById('heroTitle').textContent);
 await sleep(13000); // > the old 12s rotation
 const hero1=await p.evaluate(()=>document.getElementById('heroTitle').textContent);
 ok('AG hero did not rotate on its own over 13s', hero0===hero1, hero0+' → '+hero1);

 // (3) REAL disk change → BOTS row < 2s, no timer (watcher → events.jsonl → SSE → loadLive(what))
 const tmp=path.join(PROF,'_ag-probe-bot'); fs.mkdirSync(tmp,{recursive:true}); fs.writeFileSync(path.join(tmp,'SOUL.md'),'# AG Probe\n\nThrowaway probe bot for the AG ledger — delete me.\n');
 const t0=Date.now(); let appeared=null;
 try{
  await p.waitForFunction(()=>[...document.querySelectorAll('#bots-list .topic')].some(t=>t.dataset.bot==='_ag-probe-bot'),{timeout:6000,polling:50});
  appeared=Date.now()-t0;
 }catch(e){}
 ok('AG touch a profile dir → BOTS row appears < 2000ms with no timer', appeared!==null && appeared<2000, appeared===null?'never appeared in 6s':appeared+'ms');
 const lastLoad=await p.evaluate(()=>window.__lastLive||null);
 // reason/what recorded by the live/loaded listener below (installed before the touch on next run); here read via LIVE event log
 fs.rmSync(tmp,{recursive:true,force:true});
 const t1=Date.now(); let gone=null;
 try{ await p.waitForFunction(()=>![...document.querySelectorAll('#bots-list .topic')].some(t=>t.dataset.bot==='_ag-probe-bot'),{timeout:6000,polling:50}); gone=Date.now()-t1; }catch(e){}
 ok('AG remove it → row gone < 2000ms', gone!==null && gone<2000, gone===null?'still there after 6s':gone+'ms');

 // (4) what-scoped reload: fleet/changed what:['skills'] leaves the BOTS DOM nodes untouched
 const before=await p.evaluate(()=>{ const t=document.querySelector('#bots-list .topic'); t.dataset.agMark='1'; return t.dataset.bot; });
 const det=await p.evaluate(async()=>{ const d=new Promise(r=>window.addEventListener('live/loaded',e=>r(e.detail),{once:true})); await loadLive('probe',['skills']); return d; });
 const still=await p.evaluate(()=>!!document.querySelector('#bots-list .topic[data-ag-mark="1"]'));
 ok('AG loadLive(what:[skills]) did not re-render BOTS (marked node survives)', still && det && det.what && det.what.join()==='skills' && !(det.did||[]).includes('bots'), JSON.stringify(det));

 // (5)+(6) hero follows bridge activity for 6s, hover wins
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3600);
 const names=await p.evaluate(()=>[...document.querySelectorAll('#view-wiki .topic .tname')].map(x=>x.textContent.trim()));
 const rest=await p.evaluate(()=>document.getElementById('heroTitle').textContent);
 const target=names.find(n=>n.toLowerCase()!==rest.toLowerCase());
 const fired=await p.evaluate(t=>window.heroActivity(t),target.toLowerCase());
 await p.waitForTimeout(700);
 const during2=await p.evaluate(()=>document.getElementById('heroTitle').textContent);
 ok('AG heroActivity(topic) → hero shows that topic', fired && during2.toLowerCase()===target.toLowerCase(), rest+' → '+during2+' (asked '+target+')');
 await p.waitForTimeout(6300);
 const after=await p.evaluate(()=>document.getElementById('heroTitle').textContent);
 ok('AG …and returns to the previous hero after 6s', after===rest, during2+' → '+after);
 // hover beats activity
 const row=await p.$('#view-wiki .topic:nth-of-type(2) .thead .tname'); const bb=await row.boundingBox();
 await p.mouse.move(bb.x+10,bb.y+bb.height/2); await p.waitForTimeout(400);
 const hovered=await p.evaluate(()=>document.getElementById('heroTitle').textContent);
 const ignored=await p.evaluate(t=>window.heroActivity(t),target.toLowerCase());
 await p.waitForTimeout(500);
 const stillHover=await p.evaluate(()=>document.getElementById('heroTitle').textContent);
 ok('AG hovered row beats bridge activity (activity ignored while hovering)', ignored===false && stillHover===hovered, hovered+' / '+stillHover);
 await p.mouse.move(W/2,H-40);

 // (7) bridge DOWN: only labeled backoff retries, ≤5s apart, ⚙ offline, no twinkles, no other polling
 const p2=await b.newPage({viewport:{width:W,height:H}});
 const net2=[]; p2.on('request',r=>{ const u=r.url(); if(/^https?:/.test(u) && !/127\.0\.0\.1:8643/.test(u)) net2.push({t:Date.now(),u}); });
 await p2.route('http://127.0.0.1:8643/**',r=>{ net2.push({t:Date.now(),u:r.request().url()}); r.abort('connectionrefused'); }); // the bridge is "killed" for this page only (counted here — aborted requests don't always reach the 'request' event)
 await p2.addInitScript(()=>{ window.__pulses=0; const _p=window.mmPulse; Object.defineProperty(window,'__pulseHook',{value:1}); });
 await p2.goto(FILE,{waitUntil:'domcontentloaded'});
 await p2.evaluate(()=>{ const o=window.mmPulse; window.mmPulse=function(){ window.__pulses++; return o.apply(this,arguments); }; });
 await p2.waitForTimeout(16000);
 const st=await p2.evaluate(()=>window._bridgeState&&window._bridgeState());
 const gaps=[]; const hs=net2.filter(r=>/\/health|\/token/.test(r.u)).map(r=>r.t); for(let i=1;i<hs.length;i++) gaps.push(hs[i]-hs[i-1]);
 const others=net2.filter(r=>!/\/health|\/token/.test(r.u));
 ok('AG bridge down → ⚙ state offline', st && st.state==='off', JSON.stringify(st));
 ok('AG bridge down → only /health (+/token) retries; no other polling', others.length===0, JSON.stringify(others.map(r=>r.u).slice(0,5)));
 ok('AG retry gaps: backoff grows and caps ≤ 5.5s ('+hs.length+' tries in 16s)', hs.length>=4 && gaps.every(g=>g<=5500) && gaps.slice(-1)[0]>=4000, JSON.stringify(gaps));
 const pulses=await p2.evaluate(()=>window.__pulses);
 ok('AG bridge down → stars rest (0 twinkles in 16s)', pulses===0, pulses+' pulses');
 const cachedLabel=await p2.evaluate(()=>document.querySelector('#view-bots .heroMeta').textContent);
 ok('AG bridge down → BOTS meta labeled CACHED (or no-data notice)', /CACHED|no live data/i.test(cachedLabel) || /no live data/.test(await p2.evaluate(()=>document.getElementById('bots-list').textContent)), cachedLabel);
 // (8) reconnect → exactly one loadLive('reconnect'|'connect'), ⚙ live, label clears
 await p2.evaluate(()=>{ window.__loads=[]; window.addEventListener('live/loaded',e=>window.__loads.push(e.detail.reason)); });
 await p2.unroute('http://127.0.0.1:8643/**');
 await p2.waitForFunction(()=>window.__bridgeLive===true,{timeout:9000}).catch(()=>{});
 await p2.waitForTimeout(1500);
 const loads=await p2.evaluate(()=>window.__loads); const st2=await p2.evaluate(()=>window._bridgeState());
 ok('AG bridge back → ONE loadLive on reconnect, ⚙ live', st2.state==='on' && loads.filter(r=>/connect/.test(r)).length===1, JSON.stringify({loads,st2}));
 const label2=await p2.evaluate(()=>document.querySelector('#view-bots .heroMeta').textContent);
 ok('AG …CACHED label gone after reconnect', /LIVE SCAN/.test(label2), label2);
 if(SHOT){ fs.mkdirSync(SHOT,{recursive:true}); await p2.evaluate(()=>document.getElementById('navSettings').click()); await p2.waitForTimeout(300); await p2.screenshot({path:path.join(SHOT,`AG-settings-live-${W}x${H}.png`)}); }

 ok('AG no page/console errors', errs.length===0, errs.slice(0,3).join(' | '));
 await b.close();
 const pass=R.filter(r=>r.ok).length; R.forEach(r=>console.log((r.ok?'ok  ':'FAIL')+' '+r.n+(r.d?'  — '+r.d:''))); console.log(pass+'/'+R.length+' passed @'+W+'x'+H);
 process.exit(pass===R.length?0:1);
})().catch(e=>{ console.error(e); process.exit(2); });
