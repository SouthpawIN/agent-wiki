---
title: "Decision 2026-09-05 19:18: row dots expand around the dot under the mouse, not always to the right"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui, preference, pain]
sources:
  - raw/inbox/2026-09-05.md
confidence: high
---

# Decision 2026-09-05 19:18: the hovered dot stays under the mouse

## What Chris said
> "When I hover over any of the four dots from the list, okay, I like that it expands to the right only for the furthest one. When I hover over any other of the dots, I want it to expand from that dot that I'm hovered over. Because if I hover over the first second or third dot, then when it expands, then I'm hovering over a different one when it's highlighted. And that's a little jarring for the user that move their mouse again after hovering over it. So what I mean is, when I hover over the third dot and it expands, the third dot should still be under my mouse and everything else should grow and expand like it should, even if it goes to the right a little bit." (19:18) ^[raw/inbox/2026-09-05.md]

## The rule
Stage-1 hover of a row's four dots ([[wiki-topics/senter-wiki/wiki/concepts/row-geometry-and-dot-column|hover stages]]) currently grows the group with its right edge anchored — correct only when the pointer is on the fourth (rightmost) dot. New rule: **the expansion origin is the hovered dot.** Dot *k* keeps its centre under the cursor; dots to its left grow leftward, dots to its right grow rightward, *"even if it goes to the right a little bit."* Hovering the 4th dot is unchanged (already right-anchored).

## Why
A pointer that lands on dot 2 and, after the grow, finds itself over dot 3 forces a second mouse move — *"a little jarring."* This is the same class of complaint as the earlier "they don't need to grow anymore … they just need to shift up and show the card" ([[wiki-topics/senter-wiki/wiki/entities/hero-orbs|hero orbs]]): on hover, whatever is under the mouse must not move away from it.

## Tension to resolve (not decided by Chris)
The "doesn't jump" rule reserves the grown geometry at rest so neighbours never move and all rows' dots share both edges (*"aligned on their right sides"*). A per-dot expansion origin means the grown group's right edge can now extend past the reserved cell *"a little bit"* — Chris explicitly allowed the overflow to the right. The row's right-edge alignment at REST is unaffected; only the transient hover state may overhang. Whether the overhang may cross `--dotsc`/the girl's edge is unspecified.

## Status
Stated 19:18; Hermes acknowledged the batch ("Very nice so far continue with that workflow") and moved first to markdown rendering (19:19). Not yet reported as done in the raw. Tracked in [[wiki-topics/senter-wiki/wiki/queries/open-items-as-of-2026-09-05|open items]].
