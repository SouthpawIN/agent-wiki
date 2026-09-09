---
title: Is there a published DFlash2 speculative decoder for the base Qwen 3.8 27B model
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [question, huggingface, dflash2, qwen, mtplx]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Is there a published DFlash2 speculative decoder for the base Qwen 3.8 27B model, or is DFlash2 only available for the Unleashed/abliterated variant?

## Context

The 131K comparison between MTPLX and Unleashed + DFlash2 cannot be treated as complete until this HuggingFace lookup is resolved.^[raw/inbox/2026-09-07.md] Chris specifically asked whether a smaller draft-model path can replace or augment MTPLX's internal MTP head on the base Qwen model.

## Known findings

- **Unleashed + DFlash2**: Uses DFlash2 draft model (~1.06 GB) paired with a 12.31 GB abliterated model.^[raw/inbox/2026-09-07.md]
- **MTPLX**: Uses its own MTP (multi-token prediction) head, not an external DFlash2 model.^[raw/inbox/2026-09-06.md]
- **Ornith**: Has a DFlash2 draft variant available (`jzinno/Ornith-1.5-35B-A3B-DFlash2`, ~1GB).^[raw/inbox/2026-09-07.md]
- The raw slice includes an explicit HuggingFace-style search request for `Qwen3.8-27B-DFlash2` and similar model tags; the result of that search is not confirmed in the raw record, so the query remains open.^[raw/inbox/2026-09-07.md]

## The question

Is there a HuggingFace model tag like `Qwen3.8-27B-DFlash2` or similar that provides a DFlash2 draft for the *base* Qwen 3.8 27B model (not the Unleashed variant)? If so, could it be paired with MTPLX to improve medium-prompt throughput at 131K?

## Status

**Open** — The HuggingFace search outcome for the base Qwen model is not recorded in the raw slice. See [[queries/mtplx-dflash2-base-model-research|MTPLX DFlash2 base model research]] for related context.

## Related

- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[entities/unleashed-dflash2-131k-path|Unleashed + DFlash2 131K Path]]
- [[queries/mtplx-dflash2-base-model-research|MTPLX DFlash2 base model research]]
- [[queries/ornith-llamacpp-long-context-viability|Ornith llama.cpp long-context viability]]
- [[comparisons/131k-engine-survey-32gb-mac|131K engine survey — M1 32GB Mac]]
