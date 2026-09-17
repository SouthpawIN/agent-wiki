---
title: Revert-or-recreate decision
created: 2026-09-06
updated: 2026-09-06
type: decision
tags: [decision, preference, infra]
sources:
  - raw/inbox/2026-09-06.md
confidence: 0.85
---

# Revert-or-recreate decision

## Decision
Prefer reverting to a known good visual state when possible; if revert is not possible, recreate it to match the screenshot.

## Why
Chris explicitly said: “try to recreate this as best you can or even better” and “revert back to this if you can.”^[raw/inbox/2026-09-06.md]

## When
- Triggered when an output no longer matches a known-good screenshot that Chris references.
- Applies after failure signals like “This is a screenshot from what you screwed up earlier.”^[raw/inbox/2026-09-06.md]

## Relationship
- Surfaces whenever [[topics-wiki/looked-image/wiki/concepts/visual-revert-target|visual revert target]] is in use.
- Depends on whether [[topics-wiki/looked-image/wiki/queries/locate-memory-shard|locate memory shard for revert target]] succeeds.

## Evidence
- “It was supposed to look like this. This is a screenshot from what you screwed up earlier.”^[raw/inbox/2026-09-06.md]
