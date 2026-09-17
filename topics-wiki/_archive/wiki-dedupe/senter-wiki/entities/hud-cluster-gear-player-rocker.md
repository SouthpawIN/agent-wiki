---
title: HUD cluster (gear over player on one axis)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, tool]
sources:
  - raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# HUD cluster (`#hudCluster`)

Chris: *"move the media player underneath the line … in the middle of that black triangular area between the back of the girl's head, the underline and
the edge of the frame; the settings icon a little bigger, about the size of the white dots, directly above the play button, above the line, so you can draw an
invisible line through the centre of both."* ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]

## Shape that works
Container `position:fixed; inset:0; pointer-events:none` with **NO transform** (a transformed ancestor becomes the containing block for fixed children);
two fixed leaves on a shared axis `--hudX`, split by `--hudLineY` (the `.heroLine` bottom). Old `#media {position:relative; transform:translateY(17px); left:-26.5px}`
rules need `!important` overrides. Align the **play ring's** centre, not the widget box. ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]

## Hand placement (Chris's idea, worked first try)
After six rounds of *"too low / to the right / the line runs through the gear"* with vision crops missing the pane, Chris: *"you seem to be struggling — make them
click-and-draggable and resizable, I'll place them, then say go."* Temp `TEMP-HUDDRAG` layer: pointer-capture drag, white corner grip = `scale()`, clicks
suppressed in capture phase, fixed readout box. **Never reload while the layer is on** — two reloads wiped his placement (*"you're jumbling all around"*). Final
readout: `LINE y=82 · GEAR cx1021 top24 · PLAY cx1020 top106 · MEDIA left930 top105 w180` at pane width 1152. Baked in `placeHud`: media anchored from the pane's
RIGHT edge (`W − 222`), gear cx = play-ring centre, top = measured hero-orb top (23 px), 40 px. ([[topics-wiki/senter-wiki/wiki/decisions/2026-09-03-hand-placement-mode|decision]]) ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]

Two things undid the bake: legacy `alignCluster()` still scheduled on resize/mutation, and `placeHud`'s scheduling line lost twice to `s.replace` (`runs=0`).
Now guarded by a comment + invocation counter. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]

## Gear glyph → SVG
Font ⚙ ink sat low-left; Chris wanted it *"much bigger."* Inline 8-tooth SVG cog, `--gearSize:30px`, optical knobs `--gearNudgeX/Y`, disc = `.orb` recipe.
Hollow/solid ring recipe shared with the active hero orb via `--ringW` (1 px, "thinner"). Gear toggles the settings card (no CLOSE button; click-off closes)
([[topics-wiki/senter-wiki/wiki/concepts/hover-card-contract|hover-card contract]]). ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Interactions
- Feed expanded (`#chat.open`) hides the HUD (`body:has(#chat.open) #hudCluster {display:none}`) — Chris: *"the media player is still visually in the way."*
- SPACE hides chat, `#intRail`, `#hudCluster`.
- The gear sits in the dead-zone band → its click once also fired the dead-zone handler → the "nowhere" bug
  ([[topics-wiki/senter-wiki/wiki/decisions/2026-09-03-settings-is-a-card|settings-is-a-card decision]]). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Related: [[topics-wiki/senter-wiki/wiki/entities/headphone-eq-and-media-player|EQ + player]].
