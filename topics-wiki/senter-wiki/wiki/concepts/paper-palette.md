---
title: The paper palette — one off-white, true black, no grey
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, preference]
sources:
  - raw/sources/knowledge/ref-vault-live-palette.md
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
confidence: high
---

# The paper palette — one off-white, true black, no grey

## Chris's aesthetic
Pure black background, ONE off-white for everything "white" — text, borders, hollow rings, orbs, feed cards, AND the ink of the [[topics-wiki/senter-wiki/wiki/entities/wallpaper-girl|wallpaper girl]]. He compares them side by side and reads any mismatch as tint ("cream", "warm", "sad", "is there a filter over it?", "gray bar"). Grey is never a colour: fades are masks, state is size/presence, opacity is not used for tone. ^[raw/sources/knowledge/ref-vault-live-palette.md]

## The knob
`:root { --paper: color-mix(in srgb, #dfe8f5 var(--paperPct, 96%), #000); }` — cool blue-white. Every palette role (`--text --muted --dim --border --accent --ok --warn --err --tool`) and every literal `#fff` in `<style>` resolves to it. "Dimmer" = lower `--paperPct`, never `filter:brightness` (dims stars + wallpaper, and creates a containing block that breaks fixed HUD/cards). Warm `#f2ede4`, neutral `#ececec`, cool `#e9ecef` all read cream to him; blue-white `#dfe8f5` accepted — "when he says cool, go visibly blue." ^[raw/sources/knowledge/ref-vault-live-palette.md]

## Exempt colours
- `#FFE45A` **attention yellow** = approvals, LOCK on, pending, mute hover. Never for typing/focus — he rejected a yellow hero title immediately ("don't like how the title turned yellow"). Keep `.approval` out of any white-border rule so the yellow survives. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-palette.md]
- All-black [[topics-wiki/senter-wiki/wiki/entities/headphone-eq|EQ]] dots. ^[raw/sources/knowledge/ref-vault-live-palette.md]

## Measuring, not eyeballing
`screencapture -x`, stdlib PNG decode (`scripts/pixel-span-diff.py`), histogram the region; classify warm (`R>B+6`) / cool (`B>R+6`) / neutral. "Warm" complaints were 17k neutral vs 1.4k cool pixels — grey, not warm. Bottom strip sampled at y = h−50…h−150 must be (0,0,0). "Report the numbers to Chris; he distrusts vision verdicts and accepts pixel triples." ^[raw/sources/knowledge/ref-vault-live-palette.md]

## Related knobs
`--wallInk` (her ink strength), `--spaceGlow` (.46), `--ringW` (1px, "thinner") — see [[topics-wiki/senter-wiki/wiki/concepts/hollow-vs-solid-rings|hollow vs solid rings]] and [[topics-wiki/senter-wiki/wiki/queries/ui-knob-registry|knob registry]]. Do NOT soften the diagonal feed mask when he complains about tint — mask = approved fade; tint = colour variables. ^[raw/sources/knowledge/ref-vault-live-palette.md]
