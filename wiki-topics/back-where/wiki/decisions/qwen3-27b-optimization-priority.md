---
title: "Qwen3.8 27B optimization priority"
created: 2026-09-07
updated: 2026-09-07
type: decision
tags:
  - decision
  - tool
  - infra
  - preference
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Qwen3.8 27B optimization priority

## Decision
After rejecting the 131K speed audition for being too slow, Chris explicitly redirected priority to optimizing one of the 27B models instead of continuing the 131K audition.

> "All right, never mind. We didn't go fast enough... then we need to focus back on Getting those 20 one of the 27b's optimized" ^[raw/inbox/2026-09-07.md]

## Why this model
The Qwen3.8 27B unleashed variant was identified as the preferred model with Q3K quantization, noted as:
- Smaller than alternatives
- Uncensored
- Potentially supporting deep flash^[raw/inbox/2026-09-07.md]

## Related
- [[wiki-topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[wiki-topics/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]
- [[wiki-topics/back-where/wiki/entities/m1-mac-performance-expectation|M1 Mac performance expectation]]