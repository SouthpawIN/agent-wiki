# Settings as a card + the "nowhere" bug (vault-live.html, 2026-09-03 late)

## Symptom
Chris: "When I back out of settings, I'm in nowhere — the back room, a blank space." Later, after the
card conversion: "when I open the settings page I still see the list and everything else disappear."

## Root cause (DOM readout, one round)
Temp hook on `#navSettings` click → `document.title='SET body='+body.className+' views='+[...'.view.on']+
' viewWikiDisp='+getComputedStyle(view-wiki).display` → read via `drive_preview elements max=1`:

    body=deadzone views= wikiRows=19 wikiRect=0,0,0,0 viewWikiDisp=none maskZ=90 maskBg=rgba(0,0,0,0) maskPE=none

The gear lives in the right-hand dead-zone band. Its click reached the settings handler AND the dead-zone
click handler (`.navtab` was excluded, `#hudCluster` was not → `body.deadzone` was true). That handler
calls `showView('senter')`; `#view-senter` had been retired, so `showView` removed `.on` from every view
and returned — nothing left on. The old 72%-black `#warnMask` dimmer made it look like a modal page.

## Fixes (all root-cause)
1. Dead zone excludes chrome + cards: `mousemove` uses `closest('.hero, #hudCluster, #warnMask, #view-editor')`;
   the click handler's ignore list gained `#hudCluster, #view-editor`.
2. `showView`: `if(!target){ view-wiki.classList.add('on'); return; }` — never end with zero views on.
3. Settings close path: `close()` removes the mask, and if `body.space` or the wiki isn't on → `showView('wiki')`.

## Card presentation
```css
#warnMask.settings { background:transparent; align-items:flex-start; justify-content:flex-end;
  padding:var(--setY,72px) var(--setR,26px) 0 0; box-sizing:border-box; z-index:90; pointer-events:none; }
#warnMask.settings .warn { pointer-events:auto; background:#000; width:auto; flex:1 1 auto;
  margin-left:calc(var(--setL,26px) + var(--setNudge,40px)); box-sizing:border-box; }
```
JS on open: `--setY = gear.bottom+12`, `--setR = innerWidth - gear.right`, `--setL = #heroLine.left`.
Chris's sizing sequence: "a lot wider — to where the other cards start" (→ `--edX`), "too far left — to the
edge of the title and the line" (→ `#heroLine.left`), "shift it about 10 pixels" → "and about 30 more" (→
`--setNudge` 40px). Keep the nudge a named knob; he tunes by feel.

Click-off (shell is pointer-transparent, so listen on document):
```js
const off=e=>{ if(!m.isConnected){ document.removeEventListener('pointerdown',off,true); return; }
  if(e.target.closest('#warnMask .warn')||e.target.closest('#navSettings')) return;
  e.preventDefault(); e.stopImmediatePropagation(); document.removeEventListener('pointerdown',off,true); close();
  const eat=ev=>{ ev.preventDefault(); ev.stopImmediatePropagation(); };
  document.addEventListener('pointerup',eat,{capture:true,once:true});
  document.addEventListener('click',eat,{capture:true,once:true});
  setTimeout(()=>document.removeEventListener('click',eat,{capture:true}),400); };
setTimeout(()=>document.addEventListener('pointerdown',off,true),0); // not the opening click
```
Same swallow contract as the editor card: the closing press must not reach the page underneath, the next
press must.

## Other overlays that share `#warnMask`
`askBox`, discard-warn, wallpaper `pick()` also create `#warnMask` (no `.settings` class) and still get the
dimmer — intentional for true modals. Several handlers hold state while `#warnMask` exists
(`navHide`, strip hover); the settings variant inherits that, which is fine.
