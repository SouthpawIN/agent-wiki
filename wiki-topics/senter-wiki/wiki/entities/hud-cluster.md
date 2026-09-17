---
title: HUD cluster — gear + media player on one axis
aliases:
  - HUD cluster (gear over player on one axis)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, tool]
sources:
  - raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# HUD cluster — gear + media player on one axis

## Chris's ask (2026-09-03)
"move the media player underneath the line … in the middle of that black triangular area between the back of the girl's head, the underline and the edge of the frame; the settings icon a little bigger, about the size of the white dots, directly above the play button, above the line, so you can draw an invisible line through the centre of both." ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]

## Shape that works
`#hudCluster { position:fixed; inset:0; pointer-events:none }` with **NO transform** (a transformed ancestor becomes the containing block for fixed children — first attempt landed nowhere), children `pointer-events:auto` and `position:fixed` on a shared `--hudX`, split by `--hudLineY`. Old `#media` rules (`position:relative; transform:translateY(17px); left:-26.5px`) need `!important` overrides. ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]
`--hudLineY` is the `.heroLine` bottom. Align the **play ring's** centre, not the widget box. ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]

## Placement history
1. `placeHud()` computed `--hudX` = midpoint of (back of her head = `il + dw*HEAD_BACK`, HEAD_BACK 0.905, same `WALL_AR=1.54` math as `orbColumn()`) and the pane edge; nudged `#media` so the **play ring's** centre sat on the axis. ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]
2. Six rounds of "too low / to the right / the line runs through the gear" with vision crops missing the pane (HUD at x≈1100, crops at x>1700). Chris: "you seem to be struggling — make them click-and-draggable and resizable, I'll place them, then say go." → [[wiki-topics/senter-wiki/wiki/concepts/hand-placement-mode|hand-placement mode]]. Final readout: `LINE y=82 · GEAR cx1021 top24 · PLAY cx1020 top106 · MEDIA left930 top105 w180` at pane width 1152. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]
3. Baked: media anchored from the pane's RIGHT edge (`W − 222`), every property via `setProperty(…,'important')`; gear `cx` = play-ring centre, `top` = measured hero-orb top (23px; the 16px var was 7px off), 40px. Two things undid it until found: legacy `alignCluster()` still re-writing on resize/mutation, and `placeHud`'s scheduling line lost TWICE to `s.replace` patches (`runs=0`). Proof readout `ORB t23 b63 | GEAR t23 b63 cx1020 | PLAY t106 cx1020`. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]
   - Hand-placement mechanics (Chris's idea, worked first try): temp `TEMP-HUDDRAG` layer — pointer-capture drag, white corner grip = `scale()`, clicks suppressed in capture phase, fixed readout box. **Never reload while the layer is on** — two reloads wiped his placement (*"you're jumbling all around"*). ([[wiki-topics/senter-wiki/wiki/decisions/2026-09-03-hand-placement-mode|decision]]) ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]
   - The `placeHud` scheduling line is now guarded by a comment + invocation counter. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]
4. 2026-09-04: rocker centre moved 6px left to 1140 — "Measured, not guessed: feed card right edge 1128, pane edge 1152 → midpoint 1140 … exactly your number", and the anchor made *derived*, not a nudge. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Gear glyph
Font ⚙ ink sits low-left in its em box and caps ~34px; Chris wanted it "much bigger" and centred → inline SVG cog (8 teeth, hollow hub, `fill=currentColor`), `--gearSize:30px`, `--gearNudgeX/Y`. Disc = `.orb` recipe, hollow at rest ([[wiki-topics/senter-wiki/wiki/concepts/hollow-vs-solid-rings|hollow vs solid]]). Gear click → [[wiki-topics/senter-wiki/wiki/entities/settings-card|settings card]]. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md]
Hollow/solid ring recipe shared with the active hero orb via `--ringW` (1 px, "thinner"). Gear toggles the settings card (no CLOSE button; click-off closes) ([[wiki-topics/senter-wiki/wiki/concepts/hover-card-contract|hover-card contract]]). ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Layering
HUD z120 (2026-09-05; was 58), above cards 70 and settings 90; hidden while the corner feed is expanded and in SPACE. See [[wiki-topics/senter-wiki/wiki/concepts/layer-stack|layer stack]]. ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Interactions
- Feed expanded (`#chat.open`) hides the HUD (`body:has(#chat.open) #hudCluster {display:none}`) — Chris: *"the media player is still visually in the way."*
- SPACE hides chat, `#intRail`, `#hudCluster`.
- The gear sits in the dead-zone band → its click once also fired the dead-zone handler → the "nowhere" bug
  ([[wiki-topics/senter-wiki/wiki/decisions/2026-09-03-settings-is-a-card|settings-is-a-card decision]]). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Related: [[wiki-topics/senter-wiki/wiki/entities/headphone-eq|EQ + player]].

Children: [[wiki-topics/senter-wiki/wiki/entities/music-player|music player]], [[wiki-topics/senter-wiki/wiki/entities/volume-rocker|volume rocker]].

## Absorbed
- `entities/hud-cluster-gear-player-rocker` — 2026-09-05 → archived at `wiki-topics/_archive/wiki-dedupe/senter-wiki/entities/hud-cluster-gear-player-rocker.md`
