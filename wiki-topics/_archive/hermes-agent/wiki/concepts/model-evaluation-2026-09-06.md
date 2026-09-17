---
title: "Model Evaluation — 2026-09-06"
created: 2026-09-06
updated: 2026-09-07
type: concept
tags: [person, tool, decision, question]
sources: ["raw/inbox/2026-09-06.md", "raw/inbox/2026-09-07.md"]
confidence: high
---

# Model Evaluation — 2026-09-06

Chris uses live Hermes sessions as evaluation environments. On 2026-09-06, he ran a realistic compression test and checked whether the active model worked.^[raw/inbox/2026-09-06.md]

## Approach
- Use actual Hermes conversation sessions as the testbed.
- Apply realistic workload: "big essay summarization".
- Observe behavior and similarity metrics across the run.
- Validate by explicit confirmation: "checking out if this model works".
- Keep the test environment clean enough for isolated model evaluation.^[raw/inbox/2026-09-07.md]
- On `M1 32GB`, treat `65K context` as the viable operating ceiling for `27B`-class models; `131K` context OOMs at `10K+` prompt sizes.^[raw/inbox/2026-09-07.md]
- Measurement discipline: tok/s must separate prompt processing from generation time; streamed metrics are required for accurate comparison.^[raw/inbox/2026-09-07.md]
- Before treating an OOM as a model failure, verify the active provider pid; stale wrong-flag attempts can produce false failures.^[raw/inbox/2026-09-07.md]
- See [[wiki-topics/hermes-agent/wiki/concepts/streaming-throughput-measurement|Streaming Throughput Measurement]] for the measurement rule.^[raw/inbox/2026-09-07.md]

## Session: 20260903_001447_7bc70a
- Compression test ran on 2026-09-06.
- Similarity: `0.07 → 0.06`
- Timestamps: `2026-09-06 18:15`, `19:34`
- Hardware constraint: `M1 MacBook 32GB` leaves no headroom when `MTPLX` (~20GB) + `131K KV cache` (~12GB) are loaded.^[raw/inbox/2026-09-07.md]
- Stable configuration: `MTPLX` at `65K context`, `10-12 tok/s`, no OOM.^[raw/inbox/2026-09-07.md]
- Hermes Agent overhead: ~`2-4GB`.^[raw/inbox/2026-09-07.md]

## Session: 20260907_030601_6012ee
- Chris initiated a second evaluation session on 2026-09-07 within the same Hermes instance.^[raw/inbox/2026-09-07.md]
- Same requirements: `Qwen 3.8 27B`, `10+ tok/s at 131K`, after clean environment setup.^[raw/inbox/2026-09-07.md]
- Outcome: interrupted at `05:38` after `20` API calls, `3400.36s`, without summary.^[raw/inbox/2026-09-07.md]
- Memory-cap evidence remained unchanged from earlier session.^[raw/inbox/2026-09-07.md]

## Evidence
- Session: `20260903_001447_7bc70a`
- Similarity: `0.07 → 0.06`
- Timestamps: `2026-09-06 18:15`, `19:34`
- Hardware constraint: `M1 MacBook 32GB` leaves no headroom when `MTPLX` (~20GB) + `131K KV cache` (~12GB) are loaded.^[raw/inbox/2026-09-07.md]
- Stable configuration: `MTPLX` at `65K context`, `10-12 tok/s`, no OOM.^[raw/inbox/2026-09-07.md]
- Hermes Agent overhead: ~`2-4GB`.^[raw/inbox/2026-09-07.md]

## Related
- [[wiki-topics/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
- [[wiki-topics/hermes-agent/wiki/decisions/compression-test-2026-09-06|Compression Test — 2026-09-06]]
- [[wiki-topics/hermes-agent/wiki/entities/session-20260907-030601|Session Check — 20260907_030601_6012ee]]
- [[wiki-topics/hermes-agent/wiki/decisions/main-provider-lock-2026-09-07|Main Provider Lock — 2026-09-07]]
- [[wiki-topics/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[wiki-topics/hermes-agent/wiki/decisions/targeted-27b-131k-2026-09-07|Targeted 27B at 131K — 2026-09-07]]