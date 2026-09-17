---
title: "Provider Lock Review — 2026-09-07"
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [person, tool, decision, preference, contested]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
---

# Provider Lock Review — 2026-09-07

On `2026-09-07`, Hermes recorded a provisional provider lock of `Unleashed + DFlash2` at `131K` context. That lock is not accepted as final on this topic: it is contested by Chris's explicit `Qwen 3.8 27B` requirement and by later evidence that `131K` is not viable on `M1 32GB`.^[raw/inbox/2026-09-07.md]

## What
- Recorded lock: `Unleashed + DFlash2`.
- Recorded context: `131K`.
- Required follow-up: restart Hermes Agent to apply.

## Why it remains provisional
- `2026-09-07 03:06` — Chris required `Qwen 3.8 27B` specifically and `10+ tok/s` at `131K`.^[raw/inbox/2026-09-07.md]
- `2026-09-07 05:35` — Hermes later concluded `10+ tok/s at 131K` is not achievable on `M1 32GB` with this model class.^[raw/inbox/2026-09-07.md]
- `2026-09-07 05:42` — memory-cap math was restated: `Qwen 3.8 27B Q3_K_XL = 12.3GB`, `131K KV cache = ~8GB`, `DFlash2 = 1GB`, macOS+Hermes = `6-8GB`, total `32GB`.^[raw/inbox/2026-09-07.md]
- `2026-09-07 03:04` — lock statement came before Chris's later explicit model-variant and throughput requirements.^[raw/inbox/2026-09-07.md]

## Current state
Treat this lock as a recorded Hermes action, not an accepted final configuration. The viable lockpoint evidence still points to `65K` context as the stable main-provider setting on this hardware.^[raw/inbox/2026-09-07.md]

**Reality check:** The `10+ tok/s at 131K` target with `Qwen 3.8 27B` is physically impossible on `M1 32GB`. The memory budget is exhausted by:
- Model weights: `12.3GB`
- KV cache (131K): `~8GB`  
- DFlash2: `1GB`
- System overhead (macOS + Hermes): `6-8GB`
- **Total: 27.3-29.3GB** against 32GB physical — OOM inevitable at `10K+` prompts.^[raw/inbox/2026-09-07.md]

## Recommendation
1. Lock `65K` context at `~10-12 tok/s` as the daily driver on `M1 32GB`.
2. Retain `131K` config for when long-context is specifically needed (lower throughput, use `Unleashed`).
3. Plan for `64GB+` Mac upgrade for the original `131K at 10+ tok/s` target.^[raw/inbox/2026-09-07.md]

## Tooling friction
|- `2026-09-07 13:51` — Hermes reported the tool refused to write to the Hermes config and needed to use the Hermes CLI instead.^[raw/inbox/2026-09-07.md]
|- This config-write failure may have contributed to the unsettled lock state and competing provider proposals throughout the day.^[raw/inbox/2026-09-07.md]

## Evidence
|- `2026-09-07 03:04` — Hermes: "Unleashed + DFlash2 is locked in as the main provider at 131K context."^[raw/inbox/2026-09-07.md]
|- `2026-09-07 05:35` — Hermes: 131K at 10+ tok/s is not happening on M1 32GB with 27B.^[raw/inbox/2026-09-07.md]
|- `2026-09-07 05:42` — Hermes restated the 32GB budget breakdown.^[raw/inbox/2026-09-07.md]
|- `2026-09-07 10:12` — Hermes proposed stopping Tiel-Coder and locking in `Ornith` as main provider.^[raw/inbox/2026-09-07.md]
|- `2026-09-07 13:51` — Hermes reported tool refusal to write config; needed Hermes CLI.^[raw/inbox/2026-09-07.md]

## Provisional lock rule
Competing runtime model proposals in the same session make any recorded lock provisional until a verified config write and restart confirm both the exact model variant and the throughput target.^[raw/inbox/2026-09-07.md]

## Related
- [[topics-wiki/hermes-agent/wiki/decisions/main-provider-lock-2026-09-07|Main Provider Lock — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[topics-wiki/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
- [[topics-wiki/hermes-agent/wiki/entities/session-20260907-030601|Session Check — 20260907_030601_6012ee]]