# vault-live.html — headphone EQ, retired hover cards, feed card style (2026-09-03 evening)

## Headphone EQ (`#hpEq`)
Chris: "an EQ visualizer, small, over the widest part of the inner circle of the girl's headphones …
black dots representing the levels going up and down, because black on white will be a good contrast."

**Anchor to the wallpaper's DRAWN rect, not the viewport.** `#wallBackdrop` is `background-size:contain;
background-position:center` with asset aspect `WALL_AR=1.54`. Same math `orbColumn()` uses:
```
dw=min(W, H*WALL_AR); dh=dw/WALL_AR; il=(W-dw)/2; it=(H-dh)/2
left = il + dw*CX - w/2 ; top = it + dh*CY - h/2
```
Knobs (CSS vars on `#hpEq`, read by `place()`): `--eqCX/--eqCY` = disc centre as fraction of the
image (final 0.8282 / 0.3937), `--eqW/--eqH` = box size as % of drawn width/height (3.2 / 4.6),
`COLS=7 ROWS=6` in the IIFE. Re-`place()` on resize + once at 300ms.

**Finding the disc:** pixel-scanning the asset for "largest uniform pale square" found a hair patch —
the plate is lilac (~lum 130) with a screentone crescent, not white. What worked: `vision_analyze`
on a tight crop (`region=[1100,320,1260,480]` of `assets/wall-contain-1456x914-wallonly.png`) asking
for the innermost flat plate bbox → centre (1190,362)/(1456,914). Then 2-px nudges by fraction:
2px ≈ 0.0011 of drawn width / 0.0017 of drawn height at Chris's window.

**"They look gray, not black" — three rounds, the real causes:**
1. Not layering. z-index 1→2000 changed nothing (pixel probe found lum 0 — but that was her ink).
2. Idle dots were drawn at 14–28% opacity, and with nothing playing EVERY dot is idle → the whole
   grid read gray. 3. 3.5px circles anti-alias to gray on a 2x screen.
Fix that satisfied him: every dot always `#000`, `opacity:1`, 4.5px; level expressed by **size**
(`transform:scale(.44)` unlit → `none` lit), never by opacity. His picture is pure black/white ink
+ cross-hatch — any translucency reads as a mistake against it.

**Levels:** Web Audio analyser (`createMediaElementSource` on `#radioAudio` / `#plStage audio,video`,
`fftSize 64`, 7 bands over the low 60% of bins, max-per-band ×1.25). YouTube iframes expose no audio →
breathing pattern while `radio.state.playing`. Demo: `window.hpEq.demo(sec)` sets `__eqDemoUntil`;
the pattern = kick on cols 0–1 at 2Hz, wandering mids, hats on cols 5–6.

**Demo trigger:** `?eqdemo` in the URL is stripped by the preview pane before scripts run (same as
`#q=`). A visible `<button id="hpEqDemo">` (fixed, bottom-left, z 2001) clicked via
`drive_preview click selector=#hpEqDemo` works. Still in the file — remove once Chris is done.
Wording: "runs for 30 seconds" — saying "30 seconds from now" made him think it was delayed.

## Hover cards retired, feed cards restyled
- `wireHoverCards()` now `return`s first line (dated comment). Title lift/grow on hover kept. `.hcard`
  CSS kept intact on purpose — Chris wanted its look moved to the feed.
- **The bottom-corner feed is NOT `.post`.** It is `#chat .mini .msg` and `#stream .msg` (line ~630/639);
  `.post` is the retired Feed page. First restyle hit `.post` only and vision still saw gray → grep
  `className='msg\|#stream .msg\|.mini .msg` before styling "the feed". Style now: `background:#000;
  border:1px solid #fff`, `.who` white. Depth fade on older cards (`nth-last-child` opacity) left as-is.

## Other knobs set this pass
- Hero orbs `top: var(--heroOrbsTop, 16px)` (was 26) — labels cleared the underline.
- `--eqCX` / `--eqCY` see above; `EQ DEMO` button.
