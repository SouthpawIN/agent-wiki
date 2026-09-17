---
title: "Streaming Throughput Measurement"
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [tool, decision, preference, pain]
sources: ["raw/inbox/2026-09-07.md"]
confidence: medium
---

# Streaming Throughput Measurement

Accurate tok/s reporting for local Hermes inference requires separating prompt-processing time from generation time.^[raw/inbox/2026-09-07.md]

## Rule
- Use streamed measurement, not aggregate timing.
- Prompt tokens and generated tokens should be measured in distinct stages.
- A measurement script that conflates the two produces misleading tok/s values for context-length comparison.

## Need for Improvement
On `2026-09-07 02:35`, Hermes noted: "I need to improve the script with streaming to separate prompt processing from generation time for accurate tok/s."^[raw/inbox/2026-09-07.md]

This indicates the current measurement approach is incomplete and needs to be addressed to produce reliable performance comparisons across different context lengths.

## Evidence
- `2026-09-07 02:35` — Hermes: "I need to improve the script with streaming to separate prompt processing from generation time for accurate tok/s."^[raw/inbox/2026-09-07.md]

## Related
- [[topics-wiki/hermes-agent/wiki/concepts/model-evaluation-2026-09-06|Model Evaluation — 2026-09-06]]
- [[topics-wiki/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
- [[topics-wiki/hermes-agent/wiki/entities/session-20260907-030601|Session Check — 20260907_030601_6012ee]]