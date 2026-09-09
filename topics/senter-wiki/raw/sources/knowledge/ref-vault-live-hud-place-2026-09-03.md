# vault-live.html — HUD hand-placement + late fixes (2026-09-03, evening/late)

Context: gear (⚙) + media player on one vertical axis by the hero underline. Six rounds of
"too low / to the right / the line runs through the gear" with vision crops that kept missing
the pane (HUD at x≈1100, crops at x>1700). Chris: "you seem to be struggling — make them
click-and-draggable and resizable, I'll place them, then say go."

## Hand-placement layer (temp; strip on "go")

```js
/* TEMP-HUDDRAG */ (function(){
  window.placeHud=function(){};            // hands off while Chris drives
  const ro=document.createElement('div'); ro.id='hudDragOut';
  ro.style.cssText='position:fixed;left:8px;bottom:8px;z-index:9999;font:11px monospace;color:#fff;background:#000;border:1px solid #fff;padding:6px 8px;pointer-events:none;white-space:pre';
  document.body.appendChild(ro);
  const lineY=()=>{ const ln=document.querySelector('.view.on .heroLine'); return ln?Math.round(ln.getBoundingClientRect().bottom):0; };
  function mk(el){ const r=el.getBoundingClientRect(), st=el.style;
    ['position','left','top','transform','margin','z-index','cursor','transform-origin'].forEach(k=>st.removeProperty(k));
    [['position','fixed'],['left',r.left+'px'],['top',r.top+'px'],['transform','none'],['transform-origin','top left'],['margin','0'],['z-index','2002'],['cursor','move'],['overflow','visible']].forEach(([k,v])=>st.setProperty(k,v,'important'));
    el.dataset.scale='1';
    const h=document.createElement('div'); h.style.cssText='position:absolute;right:-9px;bottom:-9px;width:14px;height:14px;background:#fff;border:1px solid #000;cursor:nwse-resize;z-index:3;pointer-events:auto'; el.appendChild(h);
    let mode=null,sx=0,sy=0,ox=0,oy=0,os=1;
    el.addEventListener('pointerdown',e=>{ mode=(e.target===h)?'size':'move'; sx=e.clientX; sy=e.clientY; ox=parseFloat(el.style.left); oy=parseFloat(el.style.top); os=parseFloat(el.dataset.scale)||1; el.setPointerCapture(e.pointerId); e.preventDefault(); e.stopPropagation(); },true);
    el.addEventListener('pointermove',e=>{ if(!mode) return; if(mode==='move'){ st.setProperty('left',(ox+e.clientX-sx)+'px','important'); st.setProperty('top',(oy+e.clientY-sy)+'px','important'); } else { const sc=Math.max(.4,os+(e.clientX-sx)/120); el.dataset.scale=sc.toFixed(3); st.setProperty('transform','scale('+sc+')','important'); } out(); });
    el.addEventListener('pointerup',()=>{ mode=null; out(); });
    el.addEventListener('click',e=>{ e.stopPropagation(); e.preventDefault(); },true); }
  // out(): write LINE y, GEAR cx/top/bottom/size/scale/gap→line, PLAY cx/top/gap, MEDIA left/top/w/scale, axis Δ into ro.textContent
})();
```

Rules learned:
- **Never reload while the layer is on.** Chris placed twice; two reloads wiped both. The only
  reload is after baking.
- The readout box sits at the bottom of the DOM → past `desktop_preview read`'s 24k cap. Read
  it with `screencapture` + `vision_analyze` over the WHOLE frame with "transcribe the black
  box beginning LINE y=" (a crop guess missed it twice).
- Final readout that was right: `LINE y=82 · GEAR cx1021 top24 · PLAY cx1020 top106 · MEDIA
  left930 top105 w180` at pane width 1152.

## Bake (`placeHud`, owns gear + player)

- Media: exact numbers, anchored from the pane's RIGHT edge (`W − 222`) so it survives resize;
  every property via `style.setProperty(k,v,'important')` (old `#media {position:relative;
  transform:translateY(17px)}` rules otherwise win).
- Gear: `cx = play ring centre` (measured in rAF after media lands), `top = measured hero-orb
  top` (23px; the CSS var 16px was 7px off because the orb's own line-height offsets it), 40px.
- Two things undid the bake until found: (1) legacy `alignCluster()` still scheduled on resize +
  a subtree MutationObserver → re-wrote media/gear after placeHud (`return;` at its top now);
  (2) placeHud's scheduling line was lost to `s.replace` twice → `runs=0`. Now guarded by a
  comment and an invocation counter.
- Proof readout (one round, then removed): `ORB t23 b63 | GEAR t23 b63 cx1020 | PLAY t106 cx1020`.

## Gear glyph → SVG

Font ⚙ inside the 40px disc: box centred (cx 1020.0/cy 43.0) but INK low-left, and Chris
wanted it "much bigger". Replaced with an inline SVG cog (8 teeth, hollow hub,
`fill=currentColor`), `position:absolute; left:50%; top:50%; translate(-50%,-50%)`,
`--gearSize:30px`, `--gearNudgeX/Y` optical knobs. Disc = `.orb` recipe: `#fff` bg, black
glyph, no border.

## SPACE navigation

`#mindmap` canvas is `pointer-events:none` behind pages; in SPACE it must be interactive:
- `pointerEvents = body.space ? 'auto' : 'none'` via MutationObserver on `body.class`.
- `mmHit(cx,cy)`: world coords `wx=(cx-CAM.x)/CAM.s`; radius 9px stars / 16px hub ÷ `max(CAM.s,.6)`.
- Labels: only `MM_HOVER`'s label (white, ring at `r*2.2`); hub hover shows `WIKI`.
- Click hub → `mmUnfocus(); showView('wiki'); #view-wiki.scrollTop=0`. Click star → find
  `#view-wiki .topic` by `.tname` text, `scrollTop = row.offsetTop − hero.height − 12`, flash
  `.rankAnchor` 1.8s.
- The driver can't click canvas coordinates; this path is verified by code identity with the
  orb handler, and by Chris trying it.

## Feed fade (rest state)

`#chat .mini` mask `to top left`: `#000 12%, rgba(0,0,0,.5) 42%, transparent 82%`; hover/pin =
mask off. He asked for it "a degree or two stronger" after seeing the strong version.