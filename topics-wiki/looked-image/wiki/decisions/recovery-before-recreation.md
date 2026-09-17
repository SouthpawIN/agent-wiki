---
title: Recovery before recreation
created: 2026-09-06
updated: 2026-09-06
type: decision
tags: [decision, preference, infra]
sources:
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-07.md
confidence: 0.85
---

# Recovery before recreation

## Decision
When a state has diverged from a known-good screenshot, the first action is to search for a local memory shard; only if no shard exists should the state be rebuilt to match the screenshot.

## Why
Chris said: “try to recreate this as best you can or even better. Try to find somewhere on this computer where there may be a memory shard of what this was and And fix it revert back to this if you can.”^[raw/inbox/2026-09-06.md]

## Order of operations
1. Search for a local memory shard via [[topics-wiki/looked-image/wiki/queries/locate-memory-shard|locate memory shard for revert target]].
2. If found, revert to that state.
3. If not found, recreate from [[topics-wiki/looked-image/wiki/entities/screenshot-2026-09-05-4-38-59-pm|Screenshot 2026-09-05 4.38.59 PM]].
4. The underlying preference is [[topics-wiki/looked-image/wiki/concepts/visual-revert-target|visual revert target]]: use the known-good image as the source of truth.

## Relationship
- Supersedes [[topics-wiki/looked-image/wiki/decisions/revert-or-recreate|revert-or-recreate decision]] with explicit precedence: shard search first.
- Applies after failure signals like “This is a screenshot from what you screwed up earlier.”^[raw/inbox/2026-09-06.md]

## Evidence
- “It was supposed to look like this. This is a screenshot from what you screwed up earlier.”^[raw/inbox/2026-09-06.md]
- “Try to find somewhere on this computer where there may be a memory shard of what this was and And fix it revert back to this if you can.”^[raw/inbox/2026-09-06.md]
