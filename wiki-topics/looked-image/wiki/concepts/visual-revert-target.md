---
title: Visual revert target
created: 2026-09-06
updated: 2026-09-06
type: concept
tags: [preference, ui, decision]
sources:
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-07.md
confidence: 0.8
---

# Visual revert target

A concept introduced by this topic: restore a broken or incorrect state by reference to a known-good visual artifact instead of verbal description.

## Behavior
- Chris treats a screenshot as more authoritative than a recreated approximation when reverting a UI change.
- He asks for both recreation and local evidence search, with preference for actual revert if possible.
- This concept feeds directly into [[wiki-topics/looked-image/wiki/decisions/revert-or-recreate|revert-or-recreate decision]].

## Quote
- “It was supposed to look like this. This is a screenshot from what you screwed up earlier.”^[raw/inbox/2026-09-06.md]
- Related optimization example: “ok so it needs to be 131K, and I think there'd more optimizations you can do if you research better.”^[raw/inbox/2026-09-07.md]
- Hermes-side research output: `--paged-kv-quantization q8` was offered as a candidate optimization.^[raw/inbox/2026-09-07.md]
