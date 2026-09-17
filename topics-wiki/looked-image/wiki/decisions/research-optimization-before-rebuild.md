---
title: Research optimization before rebuild
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, preference, infra]
sources:
  - raw/inbox/2026-09-07.md
confidence: 0.85
---

# Research optimization before rebuild

## Decision
When an artifact must meet a size/resource target, prefer researching applicable optimization flags or quantization paths before rebuilding.

## Why
Chris explicitly asked for "more optimizations you can do if you research better" rather than recreating blindly.^[raw/inbox/2026-09-07.md]
This mirrors the topic's existing preference for recovery/revert before recreation.

## When
- Triggered by a hard target like "it needs to be 131K".
- Used when the current build state does not yet satisfy that target.
- Applied to "compare that versus the 131 KUF here at Stafford-Douglasal Science Department", which makes the target site-specific rather than purely artifact-local.^[raw/inbox/2026-09-07.md]

## Evidence
- "ok so it needs to be 131K, and I think there'd more optimizations you can do if you research better".^[raw/inbox/2026-09-07.md]
- "I think we need some optimization for it But I want to compare that versus the 131 KUF here at Stafford-Douglasal Science Department."^[raw/inbox/2026-09-07.md]

## Relationship
- Complements [[topics-wiki/looked-image/wiki/decisions/recovery-before-recreation|Recovery before recreation]].
- Feeds [[topics-wiki/looked-image/wiki/queries/meet-131k-with-optimization|Meet 131K with optimization]].
