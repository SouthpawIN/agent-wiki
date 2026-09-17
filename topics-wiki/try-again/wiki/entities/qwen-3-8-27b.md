---
title: Qwen 3.8 27B
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, inference, apple-silicon, testing]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Qwen 3.8 27B

On 2026-09-07, Chris made Qwen 3.8 27B the primary target for local inference speed research on Apple Silicon. ^[raw/inbox/2026-09-07.md]

## Goal and hardware target
- "Research ALL possible ways to run Qwen 3.8 27B on Apple Silicon M1 32GB at 131K context with maximum speed." ^[raw/inbox/2026-09-07.md]
- Deliverable: "specific model IDs, commands, and expected tok/s for each approach." ^[raw/inbox/2026-09-07.md]
- Later: "Report tok/s for each test." ^[raw/inbox/2026-09-07.md]

## Benchmark scope
- llama.cpp with different quants, KV cache types, and speculative decoding. ^[raw/inbox/2026-09-07.md]
- MLX via the deepgrove fork. ^[raw/inbox/2026-09-07.md]
- OMLX. ^[raw/inbox/2026-09-07.md]
- FreeToken. ^[raw/inbox/2026-09-07.md]
- Any other engines found during research. ^[raw/inbox/2026-09-07.md]

## Status
- A 2026-09-07 leaf task researching and testing all available Apple Silicon inference engines for this model failed after 3400.47s. ^[raw/inbox/2026-09-07.md]
- No per-engine tok/s, model IDs, or command results are recorded yet for Qwen 3.8 27B itself. ^[raw/inbox/2026-09-07.md]
- Covered by the warmup-before-tok/s measurement rule. ^[raw/inbox/2026-09-07.md]
- By 2026-09-07 10:37, active sweep focus shifted away from Qwen 3.8 27B toward Bonsai, Maple Colibri, and Ornith 1.5 35A3B; Qwen results are still missing. ^[raw/inbox/2026-09-07.md]

## Links
- [[topics-wiki/try-again/wiki/concepts/apple-silicon-inference-engine-testing|Apple Silicon Inference Engine Testing]]
- [[topics-wiki/try-again/wiki/concepts/turbofit-engine-options|Turbofit Engine Options]]
- [[topics-wiki/try-again/wiki/decisions/warmup-before-speed-test|Warmup Before Speed Test]]
