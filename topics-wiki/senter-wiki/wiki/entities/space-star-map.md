---
title: SPACE star map (#mindmap)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui]
sources:
  - raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-palette.md
confidence: high
---

# SPACE star map (#mindmap)

## What it is
A canvas star map of topics behind the wiki (opacity `--spaceGlow`, Chris settled at .46) that becomes the page in SPACE mode (`body.space`). Entered by clicking the dead zone (her face forward). Chris: "no way to get back to the wiki" → made navigable. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-palette.md]

## Navigation
- Canvas takes pointer only while `body.space` (MutationObserver on body class); hit-test in world space (`wx=(cx-CAM.x)/CAM.s`, radius 9px stars / 16px hub ÷ `max(CAM.s,.6)`).
- Labels only for the hovered star; hub hover shows `WIKI`.
- Hub → `showView('wiki')` + `scrollTop=0`; star → scroll `#view-wiki` to that topic row (`offsetTop − hero height − 12`) and flash `.rankAnchor` 1.8s; blank click → wiki. ^[raw/sources/knowledge/ref-vault-live-hud-place-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- SPACE hides the chrome: `#chat, #intRail, #hudCluster { display:none }`. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Bugs found
- "Hover/click does nothing" = the empty `#view-senter` (z5) sat over the canvas (z1) eating pointer events; lift the canvas in SPACE and make the empty view `pointer-events:none`. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- One camera framing: `mmHome()` used at boot, behind the wiki, on unfocus and resize — "it sits higher after I visit SPACE and stays there" = two framings. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- `--spaceGlow` was dead until the inline `cssText opacity:.22` writer was removed ([[topics-wiki/senter-wiki/wiki/concepts/chris-ui-working-rules|rule: inline style beats a knob]]). ^[raw/sources/knowledge/ref-vault-live-palette.md]
- Boot-time TDZ: `mmHome()` reading `CAM` before its `const` killed live rendering → offline fallback rows. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Demo videos include a SPACE round-trip ([[topics-wiki/senter-wiki/wiki/concepts/demo-video-recipe|demo recipe]]). Related: [[topics-wiki/senter-wiki/wiki/entities/vault-live-html|vault-live.html]].
