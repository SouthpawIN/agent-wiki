---
title: "Compression Test — 2026-09-06"
created: 2026-09-06
updated: 2026-09-07
type: decision
tags: [person, tool, decision]
sources: ["raw/inbox/2026-09-06.md", "raw/inbox/2026-09-07.md"]
confidence: high
---

# Compression Test — 2026-09-06

On `2026-09-06`, Chris treated a "big essay summarization" task as a realistic compression test for the active Hermes session/stack.^[raw/inbox/2026-09-06.md]

## What
- Use a large-essay summarization run as the realistic compression benchmark.
- Validate whether the current model setup survives real compression without degrading behavior.
- Session under observation: `20260903_001447_7bc70a`.

## Evidence
- `2026-09-06 18:15` — system note: "Now a realistic compression test — big essay summarization"^[raw/inbox/2026-09-06.md]
- `2026-09-06 19:34` — Chris: "checking out if this model works"^[raw/inbox/2026-09-06.md]
- `2026-09-07 00:08` — Chris required removal of Maple and deletion of uncensored variant before continued testing.^[raw/inbox/2026-09-07.md]
- `2026-09-07 00:25` — Hermes reported clean measurement requires separating prompt processing from generation time.^[raw/inbox/2026-09-07.md]
- `2026-09-07 01:00` — Hermes confirmed active server pid was healthy; prior failure was stale wrong-flag process.^[raw/inbox/2026-09-07.md]

## Outcomes
- Initial compression test completed with similarity `0.07 → 0.06`, indicating model behavior was preserved.
- However, subsequent testing with `131K` context achieved `10+ tok/s` only at prompt sizes up to `8K tokens`; larger prompts triggered OOM.
- Memory math confirms `M1 32GB` cannot hold `27B` model + `131K` KV cache + system overhead simultaneously.

## Related
- [[topics/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
- [[topics/hermes-agent/wiki/concepts/model-evaluation-2026-09-06|Model Evaluation — 2026-09-06]]
- [[topics/hermes-agent/wiki/decisions/clean-model-test-precondition-2026-09-07|Clean Model Test Precondition — 2026-09-07]]