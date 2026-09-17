---
title: The wallpaper girl (backdrop asset)
aliases:
  - Paper palette (--paper) and the wallpaper girl
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, preference, tool]
sources:
  - raw/sources/knowledge/ref-vault-live-palette.md
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# The wallpaper girl (backdrop asset)

## What it is
Chris's desktop wallpaper — a white-on-black ink drawing of a girl with headphones (`assets/wall-contain-1456x914-wallonly.png`, aspect `WALL_AR=1.54`) drawn `contain` + centred as `#wallBackdrop`. Several UI anchors are measured off her: row-dot column ends at her fingertips (`figLeft`, `__figFrac` fallback .62), the [[topics-wiki/senter-wiki/wiki/entities/headphone-eq|EQ]] sits on her headphone plate, the [[topics-wiki/senter-wiki/wiki/entities/hud-cluster|HUD]] axis is the midpoint between the back of her head (`HEAD_BACK 0.905`) and the pane edge, her face forward is the dead zone. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]

## Rule: pin overlays to the DRAWN rect
`dw=min(W,H*AR); dh=dw/AR; il=(W-dw)/2; it=(H-dh)/2` — never the viewport. Px nudges convert to fractions (2px ≈ 0.0011 w / 0.0017 h). ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]

## She must BE the paper colour
Her asset is only ~60 % luminance (p99 = 153/255) with JPEG near-blacks. Three failed approaches (brightness filter → read warm later; sepia/hue-rotate → "still cream"; paper bg + multiply → neutral grey that reads WARM, plus a "gray bar along the bottom" from the element background under the contain image). Working: the picture is a **luminance mask** over a flat `var(--paper)` fill, stacked twice (`::before/::after`, `--wallInk`), so her ink pixels are exactly the paper colour and black stays black. Pixel-verified: ink (192–200,192–200,208–216) vs UI text (200,200,216); bottom strip (0,0,0). Details: [[topics-wiki/senter-wiki/wiki/concepts/paper-palette|paper palette]]. ^[raw/sources/knowledge/ref-vault-live-palette.md]
Mechanics: `#wallBackdrop` black; `::before`/`::after` filled with `var(--paper)` and **masked by the picture** (`mask-mode:luminance`, contain/centre), stacked twice (0.6 ink → 0.84; `--wallInk` scales); nothing paints outside the picture. The three failures are compared in [[topics-wiki/senter-wiki/wiki/comparisons/wallpaper-tint-approaches|wallpaper tint approaches]]. ^[raw/sources/knowledge/ref-vault-live-palette.md]

Anything drawn over her: solid `#000`, `opacity:1`, ≥4px; state by size, never translucency. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Folded from `paper-palette-and-wallpaper-girl`

Chris's aesthetic: pure black background, ONE off-white for everything "white" — text, borders, hollow rings, orbs, feed cards, AND the ink of the wallpaper girl.
He compares them side by side and reads any mismatch as a tint (*"cream", "warm", "sad"*). Grey is never a colour: fades are masks, state is size/presence,
opacity is not used for tone. ^[raw/sources/knowledge/ref-vault-live-palette.md]

### The knob
`:root { --paper: color-mix(in srgb, #dfe8f5 var(--paperPct, 96%), #000); }` — cool blue-white. Every palette role (`--text --muted --dim --border --accent --ok
--warn --err --tool`) and every literal `#fff` in `<style>` resolves to it. "Dimmer" = lower `--paperPct`, never `filter:brightness` (dims stars + wallpaper, breaks
`position:fixed`). Exempt: `#FFE45A` attention yellow and the all-black EQ dots. Tints tried: warm `#f2ede4`, neutral `#ececec`, cool `#e9ecef` (read as cream),
blue-white `#dfe8f5` (accepted). *"When he says cool, go visibly blue."* ([[topics-wiki/senter-wiki/wiki/decisions/2026-09-03-paper-palette-blue-white|decision]]) ^[raw/sources/knowledge/ref-vault-live-palette.md]

### Measuring (before and after every tone change)
`screencapture -x`, stdlib PNG decode (`scripts/pixel-span-diff.py`), histogram her region (`max(px)>90`) vs hero/title (`>150`), classify warm (`R>B+6`) / cool /
neutral. The "warm" complaint was 17k neutral vs 1.4k cool pixels — grey, not warm. *"Report the numbers to Chris; he distrusts vision verdicts and accepts pixel
triples."* ([[topics-wiki/senter-wiki/wiki/concepts/verification-and-proof-methods|proof methods]]) ^[raw/sources/knowledge/ref-vault-live-palette.md]

### Related knobs
`--spaceGlow` star-canvas opacity behind the wiki (dead until the inline `opacity:.22` was removed; Chris settled at .46) · `--wallInk` · `--ringW`. The `#fade`
gradient is pure black and Chris wants it *"kept but invisible."* ^[raw/sources/knowledge/ref-vault-live-palette.md]

## Absorbed
- `entities/paper-palette-and-wallpaper-girl` — 2026-09-05 → archived at `topics-wiki/_archive/wiki-dedupe/senter-wiki/entities/paper-palette-and-wallpaper-girl.md`
