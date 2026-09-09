# vault-live.html — HUD column (gear over player) + feed diagonal fade (2026-09-03, late)

## HUD cluster as ONE vertical axis (`#hudCluster`)
Chris: "move the media player underneath the line … in the middle of that black triangular area between
the back of the girl's head, the underline and the edge of the frame; the settings icon a little bigger,
about the size of the white dots, directly above the play button, above the line, so you can draw an
invisible line through the centre of both."

Shape that works: two `position:fixed` children on a shared axis `--hudX`, split by `--hudLineY`:
```
#hudCluster           { position:fixed; inset:0; pointer-events:none; }   /* NO transform here */
#hudCluster > *       { pointer-events:auto; }
#hudCluster .navgear  { position:fixed; left:var(--hudX); top:calc(var(--hudLineY) - 14px - 40px);
                        transform:translateX(-50%); width/height:40px; font-size:2.6em !important; }
#hudCluster #media    { position:fixed !important; left:var(--hudX) !important;
                        top:calc(var(--hudLineY) + 18px) !important; transform:translateX(-50%) !important; }
```
`placeHud()` (in the HUD IIFE): `--hudLineY` = `.heroLine` rect bottom of the active view; `--hudX` =
midpoint of (back of her head, pane right edge) where head-back = `il + dw*HEAD_BACK` (HEAD_BACK 0.905 of
the drawn wallpaper, same `WALL_AR=1.54` contain/centre math as `orbColumn()`); then one rAF pass nudges
`#media`'s `margin-left` so the **play ring's** centre (not the widget box) sits on `--hudX`. Runs on
load/50ms/400ms, `fonts.ready`, `resize`, `senter:navigated`. Knobs: `HEAD_BACK`, gear gap `-14px`,
player drop `+18px`, gear 40px (= hero orb size).

**Traps hit:**
- The old `#media` rule had `position:relative; transform:translateY(17px)` and a `left:-26.5px` — the
  new fixed rule needs `!important` on position/left/top/transform or the widget stays where it was.
- First attempt put `transform:translateX(-50%)` on `#hudCluster` itself → a transformed ancestor becomes
  the containing block for `position:fixed` children, so nothing landed where the vars said. Container =
  `inset:0`, untransformed; transforms only on the leaves.
- **Vision said "not present" three times while the elements WERE on screen** — my crops assumed the pane
  ran to x=2560 and the cluster sat at x≈1100 (pane is narrower than the screen). Before trusting a
  "missing element" verdict, dump `getBoundingClientRect()` of the element to a visible fixed `<button>`
  and read it via `drive_preview click`'s `acted` string (it echoes the button text). That readout gave
  `gear[1077,28 40x40] media[1007,100] hudX=1097px lineY=82px` in one round.

## Feed rest-state fade (`#chat .mini`)
Chris: "when my mouse is not over them … a little more intense; the bottom-right corner right white, more
extreme gradient going diagonal towards the upper left getting darker." Then, on seeing a softened
version: "No, I like that fade … a degree or two stronger — when I mouse over it [it goes solid anyway]."

One `mask-image` on the STACK (not per-card opacity steps):
```
#chat .mini { --fadeNear:12%; --fadeFar:82%;
  mask-image:linear-gradient(to top left, #000 var(--fadeNear), rgba(0,0,0,.5) 42%, rgba(0,0,0,0) var(--fadeFar)); }
#chat .mini:hover, #chat .mini.pin { mask-image:none; }
#chat .mini .msg, …:nth-last-child(2), …:nth-last-child(3) { opacity:1; }   /* old step-fade retired */
```
Lesson: when the hover state is "everything solid", the rest state can be as aggressive as he likes —
don't soften it defensively; he pushed it harder twice.
