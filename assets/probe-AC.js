// AC probe: collapsed (rest) fleet-stream preview vs hovered/open — a tall (900-char) card that reaches the top must FADE under #heroLine in BOTH states (one recipe, mask on #chat).
// usage: PW=~/.hermes/hermes-agent/node_modules/playwright node assets/probe-AC.js [WxH] [shotdir]
// prints: the computed mask on #chat in both states, --fadeY vs #heroLine.bottom, card rects, and a pixel scan of the top-right column (luma per 10px band) from the screenshots.
const {chromium}=require(process.env.PW||'playwright'); const path=require('path'); const fs=require('fs');
const FILE='file://'+path.resolve(__dirname,'..','vault-live.html');
const [W,H]=(process.argv[2]||'1456x914').split('x').map(Number);
const dir=process.argv[3]||''; if(dir) fs.mkdirSync(dir,{recursive:true});
const LONG=('AC probe long message. ').repeat(40).slice(0,900);
const state=async(p,label)=>p.evaluate((label)=>{
  const chat=document.getElementById('chat'), st=document.getElementById('stream'); const cs=getComputedStyle(chat);
  const ln=document.getElementById('heroLine').getBoundingClientRect(); const cr=chat.getBoundingClientRect();
  const list=chat.classList.contains('open')?st:document.querySelector('#chat .mini .tail');
  const cards=[...list.querySelectorAll('.msg')].filter(m=>m.textContent.includes('AC probe long')).map(m=>{const r=m.getBoundingClientRect(); return [Math.round(r.top),Math.round(r.bottom)];});
  const fadeY=parseFloat(cs.getPropertyValue('--fadeY'));
  return {label, open:chat.classList.contains('open'), chat:[Math.round(cr.top),Math.round(cr.bottom)], mask:(cs.webkitMaskImage||cs.maskImage), fadeY, heroLineBottom:Math.round(ln.bottom), fadeStartsAtLine:Math.abs((cr.top+fadeY-6)-ln.bottom)<=1, streamTop:Math.round(st.getBoundingClientRect().top), streamMask:(getComputedStyle(st).webkitMaskImage||getComputedStyle(st).maskImage), cards};
},label);
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W,height:H}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
 await p.goto(FILE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(3500);
 await p.mouse.move(300,500); await p.waitForTimeout(300);
 await p.evaluate((L)=>{ notify('klerik',L); notify('paladin',L); notify('anser',L); },LONG); await p.waitForTimeout(250);
 const rest=await state(p,'REST'); console.log(JSON.stringify(rest));
 const restShot=path.join(dir||'/tmp',`AC-rest-${W}x${H}.png`); await p.screenshot({path:restShot});
 const mc=await p.evaluate(()=>{ const r=document.querySelector('#chat .mini').getBoundingClientRect(); return {x:r.left+r.width/2,y:r.bottom-30}; });
 await p.mouse.move(mc.x,mc.y); await p.waitForTimeout(500);
 await p.evaluate(()=>{ const st=document.getElementById('stream'); st.scrollTop=st.scrollHeight; });
 const hov=await state(p,'HOVER'); console.log(JSON.stringify(hov));
 const hovShot=path.join(dir||'/tmp',`AC-hover-${W}x${H}.png`); await p.screenshot({path:hovShot});
 console.log('errors', errs.length, errs.slice(0,3).join(' | '));
 console.log('SAME_RECIPE', rest.mask===hov.mask && rest.fadeY===hov.fadeY, '| fade begins at heroLine.bottom: rest',rest.fadeStartsAtLine,'hover',hov.fadeStartsAtLine);
 console.log('shots', restShot, hovShot);
 await b.close();
})().catch(e=>{ console.error(e); process.exit(2); });
