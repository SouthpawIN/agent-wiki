---
title: "Stable Context Lock — 2026-09-07"
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [person, tool, decision, preference, infra]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
---

# Stable Context Lock — 2026-09-07

On `2026-09-07`, Chris received evidence that `131K` context with `MTPLX Qwen 3.8 27B` is not viable on `M1 MacBook 32GB`, and accepted `65K` context as the stable operating ceiling for this hardware class.^[raw/inbox/2026-09-07.md]

## What
- `131K` context with `27B` class MTPLX leaves no usable memory on `32GB` systems and OOMs beyond `10K+` prompt sizes.
- `65K` context is the stable lockpoint on this box, running at `10-12 tok/s` with no OOM.
- Hermes Agent itself reserves an additional `~2-4GB`, which must be treated as non-negotiable host overhead.

## Why
- This is a memory-bound hardware cap, not a model config preference.
- Retaining `131K` as default creates predictable failure modes: every long-run prompt risks crashing the session.
- The stable lock preserves usable throughput while keeping Hermes running.

## Accepted recommendation
- Lock `MTPLX` at `65K` context as main provider on `M1 32GB`.
- Retain a catalog note for `131K` under `64GB+` Mac upgrades or faster memory-bus machines.
- Use `58 tok/s` on `M5 Max` as a performance reference point, not a target for this host.

## Memory math evidence
- `Qwen 3.8 27B Q3_K_XL = 12.3GB`
- `131K KV cache with q8 = ~8GB`
- `DFlash2 draft = 1GB`
- `macOS + Hermes Agent = 6-8GB`
- **Total: 27.3-29.3GB** — exceeds `32GB` physical memory

**Alternative configurations:**
| Config | Context | Est. tok/s | Status |
|--------|---------|------------|--------|
| Q3_K_XL + DFlash2 | 65K | 10-12 | ✅ Stable |
| Q3_K_XL + DFlash2 | 131K | 4-5 | ❌ OOM risk |
| IQ3_XXS + DFlash2 | 131K | 3-4 | ⚠️ Lower quality |

## Evidence
- `2026-09-07 00:25` — Hermes-side performance table: `44 tokens → 8.7 tok/s`, `3K → 1.0`, `4K → 2.2`, `5K → 0.3`, `8K → 0.4`, `10K+ → 507 OOM`.^[raw/inbox/2026-09-07.md]
- `2026-09-07 00:25` — Hermes: `MTPLX loads at ~20GB`, `131K KV cache needs ~12GB`, combined `32GB` leaves zero headroom.^[raw/inbox/2026-09-07.md]
- `2026-09-07 00:25` — Hermes: `MTPLX at 65K context` gives `10-12 tok/s`, stable, no OOM.^[raw/inbox/2026-09-07.md]
- `2026-09-07 00:25` — Hermes: `Hermes Agent itself` needs `~2-4GB`.^[raw/inbox/2026-09-07.md]
- `2026-09-07 00:35` — Hermes: `M5 Max` gets `58 tok/s` from faster memory bus and idle system.^[raw/inbox/2026-09-07.md]
- Hermes-side evidence later stated the memory math explicitly: `Qwen 3.8 27B Q3_K_XL = 12.3GB`, `131K KV cache = ~8GB`, `DFlash2 = 1GB`, macOS+Hermes = `6-8GB`. Total matches the `32GB` limit.^[raw/inbox/2026-09-07.md]
- Hermes recommendation: lock `65K context` as main provider; keep catalog entry for future `64GB+` upgrade.^[raw/inbox/2026-09-07.md]
- Reliability note: an OOM during testing may come from a stale wrong-flag process; verify the active server pid before treating it as a model/host failure.^[raw/inbox/2026-09-07.md]

## Related
- [[wiki-topics/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
- [[wiki-topics/hermes-agent/wiki/decisions/compression-test-2026-09-06|Compression Test — 2026-09-06]]
- [[wiki-topics/hermes-agent/wiki/decisions/main-provider-lock-2026-09-07|Main Provider Lock — 2026-09-07]]
- [[wiki-topics/hermes-agent/wiki/decisions/targeted-27b-131k-2026-09-07|Targeted 27B at 131K — 2026-09-07]]