---
name: wiki-hand-placement
description: Use when px-by-voice placement stalls after 2–3 rounds. Make the widgets draggable/resizable, let Chris place them, read the numbers, bake on 'go', strip the layer.
version: 0.1.0
distilled: 2026-09-05
topic: senter-wiki
---
# wiki-hand-placement

Chris's own procedure (2026-09-03, worked first try) for positioning fixed widgets (gear, player, rocker) when "too low / to the right" rounds are not converging.

## Steps
1. Say what you are doing in one line; do NOT reload first.
2. Inject a `TEMP-HUDDRAG` script: disable the auto-placer (`window.placeHud=function(){}`), for each widget strip inline position rules and set `position:fixed; left/top` from its current rect with `!important`, `cursor:move`, z 2002; pointer-capture drag = move, a 14px white corner grip = `scale()`; suppress `click` in capture phase; append a fixed readout box (bottom-left, monospace, `pointer-events:none`) that prints LINE y, GEAR cx/top/bottom/size/scale/gap→line, PLAY cx/top/gap, MEDIA left/top/w/scale, axis Δ.
3. **Never reload while the layer is on** — two reloads wiped two placements ("you're jumbling all around"). Any other fix he asks for mid-placement must be CSS-only, no reload.
4. When he says "go": read the readout by `screencapture -x` + `vision_analyze` over the WHOLE frame ("transcribe the black box beginning LINE y=") — it sits past the 24k `desktop_preview read` cap and crop guesses missed it twice.
5. Bake: write exact numbers into the placer anchored from a stable edge (pane RIGHT edge `W − N` so it survives resize), every property via `style.setProperty(k,v,'important')`. Align the meaningful glyph (play ring centre), not the widget box.
6. Before trusting the bake, `grep -n "<id>.*\.style\.\|getElementById('<id>')"` and retire every OTHER writer (a legacy `alignCluster()` re-wrote the widgets after `placeHud`). Keep an invocation counter (`window.__placeHudRuns++`) and read it back — the scheduling line was lost twice to `s.replace` patches (`runs=0`).
7. Strip the layer; `assert 'TEMP-HUDDRAG' not in s`; run `scripts/vault-live-check.py`; ONE reload; prove with a rect readout (`ORB t23 b63 | GEAR t23 b63 cx1020 | PLAY t106 cx1020`).

## Evidence
> "you seem to be struggling — make them click-and-draggable and resizable, I'll place them, then say go."
> "you're jumbling all around" (after a reload wiped his placement)
> "nothing else needs to be moved but the gear icon"
