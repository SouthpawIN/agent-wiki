---
title: MTPLX session budget override
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, mtplx, memory, hardware, mac, benchmark]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# MTPLX session budget override

Chris explicitly directed an override of `MTPLX_SESSION_BANK_MAX_BYTES` and `MTPLX_SESSION_BANK_PER_SESSION_BYTES` with sizes expressed as `12G` or `12GiB`.^[raw/inbox/2026-09-07.md] He issued the override twice; both runs produced the same observable effect: MTPLX became ready with model identifier `mtplx-qwen38-27b-optimized-speed`, a reachable chat UI at `http://127.0.0.1:11613/`, and an OpenAI-compatible API at `http://127.0.0.1:11613/v1`.^[raw/inbox/2026-09-07.md]

## What was decided

Chris chose to set the session-budget environment variables himself, using explicit size strings.^[raw/inbox/2026-09-07.md] This was an answer to Hermes's unresolved question about whether MTPLX could be pushed to use more RAM.^[raw/inbox/2026-09-07.md]

## What happened after

Hermes reported the override took effect:

- MTPLX warmed the model in 2.7s and reached 14.55 tok/s during prewarm.^[raw/inbox/2026-09-07.md]
- Background warmup completed in 67.398s across steps including `gqa_packed_pipelines` and ladder warmup contexts of 512 and 2560.^[raw/inbox/2026-09-07.md]
- The instance became reachable at chat UI `http://127.0.0.1:11613/` and OpenAI-compatible API base `http://127.0.0.1:11613/v1`.^[raw/inbox/2026-09-07.md]
- Model identifier: `mtplx-qwen38-27b-optimized-speed`.^[raw/inbox/2026-09-07.md]

## Why it matters

This is the first direct, stated resolution to whether the 32GB Mac can be forced beyond the ~24GB engine budget Hermes observed. Chris set the variables twice, both times using explicit size strings like `12G` or `12GiB`.^[raw/inbox/2026-09-07.md] The override took effect in both runs: 14.54-14.55 tok/s prewarm, ~67-91s background warmup, and a usable local chat UI at `http://127.0.0.1:11613/` with OpenAI-compatible API at `http://127.0.0.1:11613/v1`.^[raw/inbox/2026-09-07.md] However, a stable large-prompt measurement at 131K is still missing.^[raw/inbox/2026-09-07.md]

## Related

- [[decisions/qwen-27b-32g-mac-operating-mode|Qwen 27B 32GB Mac operating mode]]
- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[concepts/mtplx|MTPLX]]
- [[concepts/memory-budget-mtplx|MTPLX Memory Budget]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
- [[concepts/mtplx-65k-stable-benchmark|MTPLX 65K Stable Benchmark]]
- [[concepts/mtplx-131k-memory-overcommit|MTPLX 131K Memory Overcommit]]
