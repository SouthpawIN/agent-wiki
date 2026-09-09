---
title: Hand-placement mode — let Chris drag widgets, then bake the numbers
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [skill, ui, idea]
sources:
  - raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Hand-placement mode — let Chris drag widgets, then bake

## Origin (Chris's idea, 2026-09-03, "worked first try")
After six rounds of "too low / to the right / the line runs through the gear": "you seem to be struggling — make them click-and-draggable and resizable, I'll place them, then say go." ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]

## Recipe
Temp `<script>` marked `TEMP-HUDDRAG`: disable the auto-placer (`window.placeHud=function(){}`), make each widget `position:fixed` with pointer capture (drag = move, white corner grip = `scale()`), suppress click in capture phase, and show a fixed readout box (`#hudDragOut`) with the numbers to bake — LINE y, GEAR cx/top/bottom/size/gap, PLAY cx/top, MEDIA left/top/w/scale, axis Δ. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]

## Rules learned
- **Never reload while the layer is on** — two reloads wiped his placement twice ("you're jumbling all around"). The only reload is after baking. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]
- The readout sits past the 24k `desktop_preview read` cap → read it with `screencapture` + vision over the WHOLE frame ("transcribe the black box beginning LINE y="); crop guesses missed it twice. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]
- Bake on "go", then strip the layer. Final numbers that were right: `LINE y=82 · GEAR cx1021 top24 · PLAY cx1020 top106 · MEDIA left930 top105 w180` at pane width 1152. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]
- Before baking, find every other writer of that element's style (legacy `alignCluster()` re-wrote after `placeHud`). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Applied to the [[topics/senter-wiki/wiki/entities/hud-cluster|HUD cluster]]; rule #22 in [[topics/senter-wiki/wiki/concepts/chris-ui-working-rules|working rules]].
