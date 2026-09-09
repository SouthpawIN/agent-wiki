---
title: Can Ornith-1.5-35B-A3B via llama.cpp + DFlash2 maintain higher-than-0.4 tok/s at 60K+ context on an M1 32GB Mac?
created: 2026-09-07
updated: 2026-09-07
type: query
tags: [question, ornith, llama.cpp, dflash2, long-context]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Can Ornith-1.5-35B-A3B via llama.cpp + DFlash2 maintain higher-than-0.4 tok/s at 60K+ context on an M1 32GB Mac?

## Background

Ornith-1.5-35B-A3B MLX 4-bit achieved 28.5 tok/s on short prompts but dropped to ~0.4 tok/s at 60K context and OOM'd at 131K with q8_0 KV cache in MLX server mode.^[raw/inbox/2026-09-07.md] The MLX server path does not manage KV cache well for large contexts.

llama.cpp, however, is known to handle large contexts more robustly because it actually fits in RAM and has different memory management strategies.

## The hypothesis

Running Ornith through llama.cpp with DFlash2 speculative decoding might combine:
- Short-prompt speed (4-5x faster than 27B models)
- Better large-context KV cache behavior (stable at 60K+)
- Lower RAM footprint (18GB for 4-bit MLX)

## Status

**Not tested** — This was proposed as a hybrid path but not executed. DFlash2 draft for Ornith exists (`jzinno/Ornith-1.5-35B-A3B-DFlash2`, ~1GB). The 58 tok/s M5 Max README speed comes from llama.cpp, suggesting it has the memory management capability to handle long contexts better than MLX server. Later same-day Ornith tests on this box reached 15.6 tok/s on a ~517-token/100-output prompt and 5.7 tok/s on a ~3519-token/100-output prompt, but the 131K MLX path still OOMed and reduced GPU layers were not confirmed as a stable fix.^[raw/inbox/2026-09-07.md]

## Related

- [[entities/ornith-135b-mlx-35b-moe|Ornith-1.5-35B-A3B MLX 4-bit]]
- [[entities/unleashed-dflash2-131k-path|Unleashed + DFlash2 131K Path]]
- [[queries/mtplx-dflash2-base-model-research|MTPLX DFlash2 base model research]]
- [[comparisons/131k-engine-survey-32gb-mac|131K engine survey — M1 32GB Mac]]