---
title: Is there a `Qwen3.8-27B-DFlash2` or equivalent DFlash2 variant for the base Qwen
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [question, huggingface, dflash2, qwen, mtplx]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Is there a `Qwen3.8-27B-DFlash2` or equivalent DFlash2 variant for the base Qwen model on HuggingFace, and does it improve medium-prompt throughput at 131K on Apple Silicon?

The 131K comparison cannot be treated as complete until this HuggingFace lookup is resolved.^[raw/inbox/2026-09-07.md] Chris specifically asked whether a smaller draft-model path can replace or augment MTPLX's internal MTP head.

## What was researched

Hermes surveyed local-serving paths and found:
- llama.cpp + DFlash2: reported ~5 tok/s at 131K.^[raw/inbox/2026-09-07.md]
- MTPLX (MTP): ~7 tok/s short prompts, OOM on a 507-token long generation.^[raw/inbox/2026-09-07.md]
- Unleashed + DFlash2: 6.0 tok/s short, 0.8 tok/s medium; 12.31 GB model + 1.06 GB draft.^[raw/inbox/2026-09-07.md]

## Status

**Open** — The raw record does not include the explicit HuggingFace search outcome for a base Qwen 3.8 27B DFlash2 model. Chris's original request was to check HuggingFace for `Qwen3.8-27B-DFlash2` models. See also the proposed research query at [[queries/base-qwen-dflash2-availability|base Qwen DFlash2 availability]].

## Related

- [[entities/unleashed-dflash2-131k-path|Unleashed + DFlash2 131K Path]]
- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[comparisons/131k-engine-survey-32gb-mac|131K engine survey — M1 32GB Mac]]