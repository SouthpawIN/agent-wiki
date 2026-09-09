---
title: "Retained outputs folder for rejected 131K audition"
created: 2026-09-07
updated: 2026-09-07
type: entity
tags:
  - preference
  - plan
  - infra
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Retained outputs folder for rejected 131K audition

## Decision
After deciding the 131K Qwen3.8 27B unleashed audition was too slow, Chris explicitly asked for the generated outputs to be saved in a folder rather than deleted. He said the artifacts would be used later, so on-disk retention became part of the expected state before returning to 27B optimization.

> "All right, never mind. We didn't go fast enough. My neighbor left After you generate those just put them in a folder We'll do something with those later, but uh, yeah, then we need to focus back on Getting those 20 one of the 27b's optimized" ^[raw/inbox/2026-09-07.md]

## Open question
Where should the retained 131K outputs folder live, and who owns the later-use step that Chris referenced?

## Related
- [[topics/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]
- [[topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics/back-where/wiki/entities/hermes-model-download-in-progress|Hermes model download in progress]]
