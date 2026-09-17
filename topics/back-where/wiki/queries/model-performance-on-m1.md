---
title: "Model performance on M1"
created: 2026-09-06
updated: 2026-09-07
type: query
tags:
  - question
  - tool
  - infra
sources:
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-06-from-klerik.md
  - raw/inbox/2026-09-07.md
  - raw/inbox/2026-09-15.md
confidence: high
---

# Model performance on M1

## Open question

What exact batch-size or prefill-capacity change is needed so the chosen model can load at Q3 with 262k contacts and D flash 2 without falling back due to prefill timeout, and can it reach ~113 tok/s on an M1 MacBook with 32 GB RAM?

> "What exact batch-size or prefill-capacity change is needed so the chosen model can load at Q3 with 262k contacts and D flash 2 without falling back due to prefill timeout, and can it reach ~113 tok/s on an M1 MacBook with 32 GB RAM?" ^[raw/inbox/2026-09-07.md]

Can the Qwen3.8 27B unleashed Q3K exile variant reach acceptable speed at 131K on an M1 MacBook with 32 GB RAM, and what is the best achievable throughput?

What exact tuning is needed to make the 131K unleashed configuration fast enough on this hardware, given Chris explicitly rejected the current speed as insufficient?

## Rejected baseline

The 131K unleashed audition was attempted and explicitly rejected as too slow on 2026-09-07, despite Chris expecting enough RAM to complete at least one step. Outputs from that run were retained for later use rather than discarded.

> "All right, never mind. We didn't go fast enough. My neighbor left After you generate those just put them in a folder We'll do something with those later, but uh, yeah, then we need to focus back on Getting those 20 one of the 27b's optimized" ^[raw/inbox/2026-09-07.md]

> "You have 32 gigabytes, um, and the other one is testing in the background. You should have enough space to at least do a step and not get in the way." ^[raw/inbox/2026-09-07.md]

## Downstream queries

- [[topics/back-where/wiki/queries/download-completion-verification|20.8GB download completion and loadability verification]]
- [[topics/back-where/wiki/entities/131k-download-in-progress|131K model download in progress]]

## Why this matters

Chris does not want another silent fallback or retry loop. He wants configuration evidence for local performance that matches the reported 113 tok/s figure on similar hardware, and now also an explicit 131K speed target. After the rejected run, priority shifted to optimizing one of the 27B models instead of repeating the same speed test.

## Related

- [[topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics/back-where/wiki/entities/retained-outputs-folder|Retained outputs folder for rejected 131K audition]]
- [[topics/back-where/wiki/entities/freetoken-rejected-nvidia-only|FreeToken rejected as NVIDIA-only]]
- [[topics/back-where/wiki/entities/m1-mac-performance-expectation|M1 Mac performance expectation]]
- [[topics/back-where/wiki/concepts/model-prefill-fallback|Prefill timeout triggering model fallback]]
- [[topics/back-where/wiki/entities/hardware-headroom-note|Hardware headroom note for M1 32GB]]
- [[topics/back-where/wiki/queries/20-8gb-download-completion-verification|20.8GB download completion and loadability verification]]