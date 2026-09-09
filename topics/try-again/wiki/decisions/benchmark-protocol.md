---
title: "Benchmark Protocol"
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, inference, testing, preference, apple-silicon]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Benchmark Protocol

On 2026-09-07, Chris set the exact local inference benchmark procedure for the Apple Silicon sweep. ^[raw/inbox/2026-09-07.md]

## Ordered steps

1. Warmup prompt. ^[raw/inbox/2026-09-07.md]
2. Short prompt. ^[raw/inbox/2026-09-07.md]
3. 5K prompt. ^[raw/inbox/2026-09-07.md]

## Prompt sizes

- Short: 500 tokens. ^[raw/inbox/2026-09-07.md]
- 5K prompt: 100 tokens. ^[raw/inbox/2026-09-07.md]

## Reporting

- Report tok/s for each prompt length. ^[raw/inbox/2026-09-07.md]
- Quote: "Report tok/s for each test." ^[raw/inbox/2026-09-07.md]

## Context

- Warmup is required because cold-start compilation, memory compaction, and Metal cache effects can skew tok/s. ^[raw/inbox/2026-09-07.md]
- This applies to Bonsai, Colibri, and Ornith, and any other model tested in this topic. ^[raw/inbox/2026-09-07.md]

## Cleanup rule

- Clear the previously loaded model before switching to the next candidate. ^[raw/inbox/2026-09-07.md]
- Quote: "Make sure to clear the old model off before testing the new one." ^[raw/inbox/2026-09-07.md]

## Links

- [[topics/try-again/wiki/decisions/warmup-before-speed-test|Warmup Before Speed Test]]
- [[topics/try-again/wiki/comparisons/2026-09-07-candidate-narrowing|2026-09-07 Candidate Narrowing]]
- [[topics/try-again/wiki/concepts/local-inference-benchmark-sweep|Local Inference Benchmark Sweep]]
