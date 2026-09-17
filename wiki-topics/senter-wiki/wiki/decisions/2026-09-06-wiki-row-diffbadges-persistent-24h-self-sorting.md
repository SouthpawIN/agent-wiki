---
title: "Decision 2026-09-06: wiki row diff badges, 24h persistence, and self-organizing sort"
created: 2026-09-06
updated: 2026-09-06
type: decision
tags: [decision, ui, preference, pain]
sources:
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-06.md
confidence: medium
contested: true
---

# Decision 2026-09-06: wiki row diff badges, 24h persistence, and self-organizing sort

## Chris's ask (2026-09-06 01:05)
> "I want the diffs to be persistent for 24 hours from the last time it went to zero. So if no activity for 24 hours in that topic, then that diff resets... I want the topics to self-organize, like when the user is not searching anything, just neutral by default to self-organize by those diffs and usage." ^[raw/inbox/2026-09-06.md]

## First implementation and breakage (01:13–01:14)
Hermes added a fixed-width `.rdiff` slot and JS `paintDiffs()` / `decayedDiff` sort, but broke row geometry:
> "No, I'm talking about in the main page in the main list where I see all the wikis... I see one diff for a cleric and All of the usage she has shifted them over a bit I did not want them shifted over I want them exactly where they were with the usage numbers in between them" (Chris, 01:14) ^[raw/inbox/2026-09-06.md]

## Revert (01:27–01:30)
All `rdiff`, `paintDiffs`, and `decayedDiff` mentions were removed and the proven right-anchor selector restored. ^[raw/inbox/2026-09-06.md]

## Rebuilt without breaking geometry (02:14–02:20)
- **Diff badges** — `fmtDiff(n)` emits `+N`/`-N` with `.up`/`.dn` coloring. `mkTopic` accepts `diffbadge` and `usage` params and inserts them before `.tname`. `refreshWikiOrbs` reads `.system-live.json`, computes day-over-day delta from `usage.topics`, and renders `.usage` then `.diffbadge`. ^[raw/inbox/2026-09-06.md]
- **24h persistence** — each `act:diff` event stamps `lastDiffAt`; `paintDiffs()` keeps numbers visible for 24h, then zeros them. State survives reload via `localStorage('sw.diffs')`. ^[raw/inbox/2026-09-05.md]
- **Self-organizing sort** — default neutral sort is `decayedDiff` first (24h window, linear fade, scaled 10×), then usage, then updated date. Skipped while a topic page is open so the editor doesn't lose its place. ^[raw/inbox/2026-09-06.md]
- **Geometry guard** — the proven right-anchor selector chain is preserved: `.view .thead .usage + .orbs { margin-left:0; width:164px; flex:0 0 164px; justify-content:flex-end; }`. The 44px `.rdiff` slot sits between usage and dots without moving them. ^[raw/inbox/2026-09-06.md]

## Status
Implemented and verified JS-clean. Chris confirmed local vision shows the wiki matching the desired layout. ^[raw/inbox/2026-09-06.md]

## Conflicts
- 01:13 implementation broke proven row geometry; rolled back at 01:27.
- 02:14 implementation kept geometry intact but required rethinking insertion order and anchor selectors.

## Related
[[wiki-topics/senter-wiki/wiki/decisions/2026-09-05-row-dots-expand-from-hovered-dot|row dots expand]], [[wiki-topics/senter-wiki/wiki/decisions/2026-09-05-content-card-stops-at-side-chat|content card stops at side chat]], [[wiki-topics/senter-wiki/wiki/entities/usage-strip|usage strip]]
