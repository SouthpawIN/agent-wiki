---
title: Decision: when px-by-voice stalls, make widgets draggable and let Chris place them
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui, skill]
sources:
  - raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Hand-placement mode (2026-09-03, Chris's idea; worked first try)

**What.** Chris: *"you seem to be struggling — make them click-and-draggable and resizable, I'll place them, then say go."* Temp layer, readout box, bake on "go", strip.
Final readout `LINE y=82 · GEAR cx1021 top24 · PLAY cx1020 top106 · MEDIA left930 top105 w180`. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]

**Why.** Six rounds of *"too low / to the right / the line runs through the gear"* with vision crops that missed the pane. **Rules learned.** Never reload while the layer is on
(two placements wiped — *"you're jumbling all around"*); read the readout by screenshot + vision over the WHOLE frame (it sits past the 24k read cap); before baking, find every
OTHER writer of that element's style (`alignCluster`). Afterwards: *"nothing else needs to be moved but the gear icon"* → CSS-only glyph fix, no reload.
See [[topics-wiki/senter-wiki/wiki/entities/hud-cluster|HUD cluster]], [[topics-wiki/senter-wiki/wiki/concepts/chris-ui-working-rules|working style]].
