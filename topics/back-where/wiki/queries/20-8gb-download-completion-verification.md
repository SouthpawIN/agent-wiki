---
title: "20.8GB download completion and loadability verification"
created: 2026-09-07
updated: 2026-09-07
type: query
tags:
  - tool
  - infra
  - question
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# 20.8GB download completion and loadability verification

## What was downloaded

Multiple download status lines appeared in one topic run: a ~13GB model file reported nearly complete, an IQ3_XXS download later reported incomplete at ~4.7GB of ~10GB, a 13GB download reported at 01:40, and the large 20.8GB model at 19.7GB/20.8GB (94%).

> "The large file is still downloading (~6.5GB / 20.8GB). Let me wait for it to complete" ^[raw/inbox/2026-09-07.md]

> "Almost done - 94% (19.7GB / 20.8GB), about 1 minute remaining. Let me wait for completion." ^[raw/inbox/2026-09-07.md]

## Verification questions

1. After completion, can the model load at Q3 quantization?
2. Does it fit in 32GB M1 RAM with 262k contacts and D flash 2?
3. What batch-size or prefill-capacity change is needed to avoid fallback?

## Status

Download was in progress at interrupt point. Verification of completion and loadability pending.

## Why this matters

Without verification of completion and loadability, it's unclear whether:
- The model is ready for use in subsequent optimization work
- A second download attempt is needed
- The file size discrepancies indicate different model variants

This query is downstream from the broader question of M1 model performance and the 27B optimization priority shift.

## Related

- [[topics/back-where/wiki/entities/model-picker-persistence|Model picker persistence until fallback]]
- [[topics/back-where/wiki/queries/model-performance-on-m1|Model performance on M1]]
- [[topics/back-where/wiki/entities/qwen3-8-27b-unleashed-selection|Qwen3.8 27B unleashed model selection]]
- [[topics/back-where/wiki/entities/hermes-model-download-in-progress|Hermes model download in progress]]
- [[topics/back-where/wiki/decisions/131k-audition-rejection|131K audition rejection and speed target]]