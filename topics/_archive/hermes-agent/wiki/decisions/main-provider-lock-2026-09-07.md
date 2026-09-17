---
title: "Main Provider Lock — 2026-09-07"
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [person, tool, decision, preference, infra, contested]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
---

# Main Provider Lock — 2026-09-07

On `2026-09-07`, Hermes side locked `Unleashed + DFlash2` as the main provider at `131K` context and instructed a Hermes Agent restart to pick up the change.^[raw/inbox/2026-09-07.md]

## What
- Provider lock recorded: `Unleashed + DFlash2`.
- Context: `131K`.
- Action taken: restart Hermes Agent to apply.

## Contested state
This lock is contested by Chris's later decision in the same raw file: the active target must be `Qwen 3.8 27B` with `10+ tok/s` at `131K` context.^[raw/inbox/2026-09-07.md]

**Evidence of impossibility on M1 32GB:**
- `Qwen 3.8 27B Q3_K_XL = 12.3GB`
- `131K KV cache = ~8GB`
- `DFlash2 draft = 1GB`
- `macOS + Hermes Agent = 6-8GB`
- **Total: 27.3-29.3GB** — exceeds physical memory, causing OOM at `10K+` prompt sizes.^[raw/inbox/2026-09-07.md]

- Earlier evidence in the same session also supported `65K` context as the stable lockpoint on `M1 32GB`.^[raw/inbox/2026-09-07.md]
- Hermes-side evidence later upgraded this from a config question to a memory-cap conclusion.^[raw/inbox/2026-09-07.md]

## Current status
|- Treat the provider lock as provisional: `131K` at `10+ tok/s` is **not achievable** on `M1 32GB` with a `27B` model class.
|- Viable lockpoint: `65K` context at `~10-12 tok/s` with no OOM.^[raw/inbox/2026-09-07.md]
|- If `131K` is required for long-context work, switch to `Unleashed` when needed; use `65K` as the daily driver.^[raw/inbox/2026-09-07.md]
|- The lock remained unsettled through repeated follow-up questions ("What do you want to lock in?") and competing proposals such as locking in `Ornith` as main provider.^[raw/inbox/2026-09-07.md]

## Evidence
- `2026-09-07 03:04` — Hermes: "Unleashed + DFlash2 is locked in as the main provider at 131K context. Restart Hermes Agent to pick up the change."^[raw/inbox/2026-09-07.md]
- `2026-09-07 03:06` — Chris: "Must be Qwen 3.8 27B variant. Target: 10+ tok/s at 131K context."^[raw/inbox/2026-09-07.md]
- `2026-09-07 05:35` — Hermes: physical memory cannot achieve 10+ tok/s at 131K on M1 32GB; recommended 65K as daily driver.^[raw/inbox/2026-09-07.md]
- `2026-09-07 05:42` — Hermes restated the 32GB budget breakdown.^[raw/inbox/2026-09-07.md]

## Related
- [[topics/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[topics/hermes-agent/wiki/decisions/targeted-27b-131k-2026-09-07|Targeted 27B at 131K — 2026-09-07]]
- [[topics/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]