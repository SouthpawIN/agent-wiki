---
title: Preview-pane viewport (lessons 27–28)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, spec, pain]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Preview-pane viewport (lessons 27–28)

**The primary verification viewport is the preview PANE, not the Hermes window.** Chris reads the [[topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki]] in the Hermes desktop preview pane; for a whole day every builder ledger, screenshot and "proof" ran at 1456×914 (the window) or 1040×880 — layouts he had never seen. The dot column that measured "centred" at 1456 sat ON the girl's hand at his size, and the contain-fit wallpaper letterboxed differently. This "explains the whole orb saga and part of the backdrop saga." ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Lesson 28
Senter's first "correction" to **736 px was ALSO a guess** — it was the width of Senter's own vision crop. Never infer the pane from a screenshot.

## The only reliable source: the accessibility tree
`computer_use capture app=Hermes mode=ax pid=<pid> window_id=<id>` → in the saved elements JSON find the `AXWebArea` whose label is the wiki's `<title>` (`Senter Vault — Live`); its bounds `[x, y, w, h]` are the pane. On 2026-09-02: `[333, 128, 1151, 834]` → **1151×834 @x333**. Recipe: skill `references/pane-viewport.md`.

## Rules
1. Read the pane from the AX tree at the start of every session (and after Chris resizes); brief `w×h` verbatim as PRIMARY in every visual child (`deviceScaleFactor 2`), 1456/1040 secondary.
2. `assets/verify-wiki.js` runs its layout assertions at the pane size first.
3. When a builder's numbers say "aligned" and Chris says "wrong way", suspect the viewport before the math.
4. A vision crop for a relational judgement spans the FULL pane width of one row band: `region [paneX, rowY, paneX+w, rowY+h]`.
5. The window (1456×914) and the pane are never equated; `capture` without pid/window_id can return a 1456×31 title-bar sliver.

Feeds [[topics/senter/wiki/concepts/look-loop-verification|LOOK loop verification]] and [[topics/senter/wiki/entities/looker|looker]]'s real-window step.
