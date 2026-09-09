---
name: wiki-tone-measure
description: Use when Chris says cream/warm/gray/filter/doesn't match the girl. Measure pixel triples before and after; tone is one --paper knob; wallpaper is a luminance mask, never a filter.
version: 0.1.0
distilled: 2026-09-05
topic: senter-wiki
---
# wiki-tone-measure

Chris reads any mismatch between UI whites and the wallpaper girl's ink as a tint. Never eyeball; never answer with a vision verdict — he accepts pixel triples.

## Rules
- ONE knob: `:root { --paper: color-mix(in srgb, #dfe8f5 var(--paperPct,96%), #000) }`. Every palette role and every `#fff` in `<style>` resolves to it. Exempt: `#FFE45A` attention yellow, the black EQ dots.
- "Dimmer" = lower `--paperPct`. Never `filter:brightness` on `<html>`/containers: dims stars + wallpaper and creates a containing block that breaks `position:fixed` (HUD, cards).
- The girl is a LUMINANCE MASK (`mask-image:var(--wallImg); mask-mode:luminance; contain; center`) over flat `var(--paper)` on `#wallBackdrop::before/::after` (stacked twice; `--wallInk` scales). Never tint her with brightness/sepia/hue-rotate/multiply — each failed (see comparison page `wallpaper-tint-approaches`).
- "Cool" means visibly blue (`#dfe8f5`); `#e9ecef` still read as cream.
- Fades are masks and stay; tint complaints are colour variables. Don't soften an approved fade when he complains about tint.
- A `--*` knob that "does nothing" = an inline `style.cssText` writer wins (star canvas `opacity:.22` vs `--spaceGlow`). Grep the id for `style.`/`cssText` first.

## Measure (before AND after)
1. `screencapture -x /tmp/x.png`; decode with the stdlib PNG reader in `scripts/pixel-span-diff.py`.
2. Girl region: histogram pixels with `max(px)>90`; hero/title region: `>150`; bucket to 8 levels; compare top buckets. Classify warm `R>B+6` / cool `B>R+6` / neutral.
3. Bottom strip: sample 3 columns at y = h−50…h−150; anything non-(0,0,0) above app chrome is a layer background leaking, not the fade.
4. Report triples: e.g. ink (192–200,192–200,208–216) vs text (200,200,216); strip (0,0,0).

## Evidence
> "cream", "warm", "sad" — his words for a mismatch between her ink and the UI whites
> "is there a filter over it?" / "gray bar along the bottom"
> "I like that fade … a degree or two stronger"
