---
title: Paper palette (--paper) and the wallpaper girl
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, preference, tool]
sources:
  - raw/sources/knowledge/ref-vault-live-palette.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# `--paper` and the wallpaper girl

Chris's aesthetic: pure black background, ONE off-white for everything "white" — text, borders, hollow rings, orbs, feed cards, AND the ink of the wallpaper girl.
He compares them side by side and reads any mismatch as a tint (*"cream", "warm", "sad"*). Grey is never a colour: fades are masks, state is size/presence,
opacity is not used for tone. ^[raw/sources/knowledge/ref-vault-live-palette.md]

## The knob
`:root { --paper: color-mix(in srgb, #dfe8f5 var(--paperPct, 96%), #000); }` — cool blue-white. Every palette role (`--text --muted --dim --border --accent --ok
--warn --err --tool`) and every literal `#fff` in `<style>` resolves to it. "Dimmer" = lower `--paperPct`, never `filter:brightness` (dims stars + wallpaper, breaks
`position:fixed`). Exempt: `#FFE45A` attention yellow and the all-black EQ dots. Tints tried: warm `#f2ede4`, neutral `#ececec`, cool `#e9ecef` (read as cream),
blue-white `#dfe8f5` (accepted). *"When he says cool, go visibly blue."* ([[wiki-topics/senter-wiki/wiki/decisions/2026-09-03-paper-palette-blue-white|decision]]) ^[raw/sources/knowledge/ref-vault-live-palette.md]

## The girl must BE the paper colour
Her asset is white-on-black ink at ~60 % luminance (p99 = 153/255). Working approach after three failures ([[wiki-topics/senter-wiki/wiki/comparisons/wallpaper-tint-approaches|comparison]]):
`#wallBackdrop` black; `::before`/`::after` filled with `var(--paper)` and **masked by the picture** (`mask-mode:luminance`, contain/centre), stacked twice
(0.6 ink → 0.84; `--wallInk` scales). The picture is only a mask → ink pixels are exactly `--paper`, black stays black, nothing paints outside the picture.
Pixel-verified: ink (192–200,192–200,208–216) vs UI text (200,200,216); bottom strip (0,0,0). ^[raw/sources/knowledge/ref-vault-live-palette.md]

## Measuring (before and after every tone change)
`screencapture -x`, stdlib PNG decode (`scripts/pixel-span-diff.py`), histogram her region (`max(px)>90`) vs hero/title (`>150`), classify warm (`R>B+6`) / cool /
neutral. The "warm" complaint was 17k neutral vs 1.4k cool pixels — grey, not warm. *"Report the numbers to Chris; he distrusts vision verdicts and accepts pixel
triples."* ([[wiki-topics/senter-wiki/wiki/concepts/verification-and-proof-methods|proof methods]]) ^[raw/sources/knowledge/ref-vault-live-palette.md]

## Related knobs
`--spaceGlow` star-canvas opacity behind the wiki (dead until the inline `opacity:.22` was removed; Chris settled at .46) · `--wallInk` · `--ringW`. The `#fade`
gradient is pure black and Chris wants it *"kept but invisible."* ^[raw/sources/knowledge/ref-vault-live-palette.md]
