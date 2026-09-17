---
name: wiki-derived-anchors
description: Use when placing or nudging any wiki element by pixels. Measure both reference edges from the DOM and express the position as a derived value, never a hand nudge.
version: 0.1.0-proposed
proposed: 2026-09-05 17:06
topic: senter-wiki
---
# wiki-derived-anchors
# Wiki derived anchors

Chris's instinct for a nudge is usually exact — but the fix is written as a derivation from measured edges so it stays true on resize and the number is explainable.

## Steps
1. Read the two reference edges from the live DOM (e.g. feed-card right edge 1128, pane edge 1152). Never eyeball a screenshot.
2. Compute the target (midpoint 1140) and compare with the current position (1146) — state the delta and that it matches his call.
3. Write the position as a CSS var / calc fed by the placer that owns the reference (EQ placer writes `--eqLeft`; volume JS writes `fill.height` / `knob.bottom` as percentages and CSS builds the look off those).
4. Anchor to the element that does not change with value (track, pane, wallpaper) — not one that collapses (fill at 0 volume).
5. Record the knob and its tuned value in wiki-ui-knobs.

## Rules
- 'Measured, not guessed' — quote the numbers in the done line.
- One owner per reference edge; other elements read its var.
- Percent-driven values from JS stay in JS; the visual is CSS on top.

## Pitfalls
- Caps sitting on `#mVolFill` land on the level at volume 0.
- A nudge that is not derived drifts the next time the wallpaper or pane resizes.

## Evidence
> Feed card right edge = 1128, pane edge = 1152 → centre 1140. Rocker centre is 1146 → move 6px left (your instinct was exact). Set the anchor so it's *derived*, not a nudge
> The bottom cap sits on `#mVolFill`, which collapses to 0 height at volume 0 so its dot lands on the level instead of the track end. Anchor both end caps to the track, not the fill
> The zone's left edge is written by the EQ placer (`--eqLeft`), so it tracks the wallpaper on resize.
> The JS sets `fill.height` and `knob.bottom` as percentages — I can build the whole look in CSS off those two values
