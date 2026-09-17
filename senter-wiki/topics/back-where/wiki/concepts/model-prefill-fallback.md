---
title: "Prefill timeout triggering model fallback"
created: 2026-09-06
updated: 2026-09-06
type: concept
tags:
  - tool
  - pain
  - preference
  - infra
sources:
  - raw/inbox/2026-09-06.md
  - raw/inbox/2026-09-06-from-klerik.md
  - raw/inbox/2026-09-07.md
confidence: high
---

# Prefill timeout triggering model fallback

## What happened
Chris observed that the runtime swapped models during the session. He concluded the cause was prefill taking too long, not true incompatibility, and wanted a configuration change instead of silent model replacement.

> "No, no, you need to actually check the box before it says something like that and check the actual load Because it can actually do it. It's just the pre-fill. The pre-fill is taking too long So what we need to do is we need to adjust the batch size There is more than enough space to fit this model at Q3 with 262k contacts and the D flash 2 model and run everything else more than enough" ^[raw/inbox/2026-09-06.md]

## Prescription
Increase batch-size or prefill capacity so the intended model fits at Q3 with 262k contacts alongside D flash 2, rather than letting the runtime swap models.

## Runtime evidence
The session showed repeated automatic model changes during the incident, which Chris treated as symptom rather than acceptable behavior.

^[raw/inbox/2026-09-06-from-klerik.md]

## Related
- [[topics/back-where/wiki/entities/model-picker-persistence|Model picker persistence until fallback]]
- [[topics/back-where/wiki/queries/restoration-and-billing|Restoration and billing]]
- [[topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]
