---
title: "131K audition rejection and speed target"
created: 2026-09-07
updated: 2026-09-07
type: decision
tags:
  - decision
  - preference
  - plan
  - pain
sources:
  - raw/inbox/2026-09-07.md
  - raw/inbox/2026-09-15.md
confidence: high
---

# 131K audition rejection and speed target

## Decision

After running an audition of the 131K unleashed 27B model configuration, Chris explicitly rejected the result as too slow. The generated outputs were retained in a folder for later use rather than discarded, and priority shifted to optimizing a 27B model for better performance.

> "All right, never mind. We didn't go fast enough. My neighbor left After you generate those just put them in a folder We'll do something with those later, but uh, yeah, then we need to focus back on Getting those 20 one of the 27b's optimized" ^[raw/inbox/2026-09-07.md]

## Speed target

Chris had expected the 32GB M1 MacBook to handle at least one step of the 131K configuration without issues. The performance fell short of acceptable thresholds.

> "You have 32 gigabytes, um, and the other one is testing in the background. You should have enough space to at least do a step and not get in the way." ^[raw/inbox/2026-09-07.md]

## Next action

The explicit directive is to shift focus to getting one of the 27B models optimized, with the rejection artifacts saved for potential later analysis.

> "...then we need to focus back on Getting those 20 one of the 27b's optimized" ^[raw/inbox/2026-09-07.md]

## Related

- [[topics-wiki/back-where/wiki/entities/retained-outputs-folder|Retained outputs folder for rejected 131K audition]]
- [[topics-wiki/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics-wiki/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]