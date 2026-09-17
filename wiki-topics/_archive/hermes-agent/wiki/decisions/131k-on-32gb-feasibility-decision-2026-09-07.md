---
title: "131K on 32GB Feasibility Decision — 2026-09-07"
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, preference, infra, contested]
sources: ["raw/inbox/2026-09-07.md"]
confidence: high
resolved: true
verdict: not-now
---

# 131K on 32GB Feasibility Decision — 2026-09-07

## Decision

**Not-now.** The `10+ tok/s at 131K context` target with `Qwen 3.8 27B` cannot be achieved on `M1 MacBook 32GB`. It requires a hardware upgrade to `64GB+` RAM or a faster memory bus (e.g. `M5 Max`).

## The requirement

Chris explicitly required:

> "Must be Qwen 3.8 27B variant. Target: 10+ tok/s at 131K context."
> — 2026-09-07 03:06 ^[raw/inbox/2026-09-07.md]

## The physics

> "MTPLX loads at ~20GB, KV cache at 131K needs ~12GB. That's 32GB total — zero room for macOS, Hermes Agent, or anything else."
> — 2026-09-07 00:25 ^[raw/inbox/2026-09-07.md]

**Memory breakdown on M1 32GB:**

| Component | Size |
|-----------|------|
| Qwen 3.8 27B Q3_K_XL | 12.3 GB |
| 131K KV cache (q8) | ~8 GB |
| DFlash2 draft | 1 GB |
| macOS + Hermes Agent | 6-8 GB |
| **Total** | **27.3-29.3 GB** |
| **Physical RAM** | **32 GB** |

The total either equals or exceeds physical memory, leaving no headroom for the page file or system services. ^[raw/inbox/2026-09-07.md]

## What works on this box

| Config | Context | Est. tok/s | Status |
|--------|---------|------------|--------|
| Q3_K_XL + DFlash2 | 65K | 10-12 | Stable ✅ |
| Q3_K_XL + DFlash2 | 131K | 4-5 | OOM risk ❌ |
| IQ3_XXS + DFlash2 | 131K | 3-4 | Lower quality ⚠️ |

> "MTPLX at 65K context — 10-12 tok/s, stable, no OOM"
> — 2026-09-07 00:25 ^[raw/inbox/2026-09-07.md]

## M5 Max reference point

> "The M5 Max gets 58 tok/s because it has a faster memory bus and was tested with nothing else running."
> — 2026-09-07 00:35 ^[raw/inbox/2026-09-07.md]

This is a reference, not a target for this host. The faster memory bus on M5 Max is a hardware advantage that cannot be replicated via config on M1. ^[raw/inbox/2026-09-07.md]

## Test results at 131K on M1 32GB

| Prompt size | Result |
|-------------|--------|
| 44 tokens | 8.7 tok/s ✅ |
| 3K tokens | 1.0 tok/s ✅ |
| 4K tokens | 2.2 tok/s ✅ |
| 5K tokens | 0.3 tok/s ✅ |
| 8K tokens | 0.4 tok/s ✅ |
| 10K+ tokens | **507 OOM** ❌ |

> "10+ tok/s at 131K is not happening on M1 32GB with a 27B model. It's like asking a Honda Civic to go 200mph. The engine isn't big enough."
> — 2026-09-07 05:35 ^[raw/inbox/2026-09-07.md]

## Resolution of proposed queries

This decision resolves the following previously proposed query pages:

- [[wiki-topics/hermes-agent/wiki/queries/32gb-131k-feasibility|32GB 131K Feasibility]]
- [[wiki-topics/hermes-agent/wiki/queries/m1-27b-131k-hardware-floor|M1 27B 131K Hardware Floor]]
- [[wiki-topics/hermes-agent/wiki/queries/mtplx-131k-offloading-options|MTPLX 131K Offloading Options]]
- [[wiki-topics/hermes-agent/wiki/queries/mtplx-131k-optimization|MTPLX 131K Optimization]]
- [[wiki-topics/hermes-agent/wiki/queries/27b-131k-ceiling-confirmation|27B 131K Ceiling Confirmation]]

All five were answered by the same evidence: no quantization, offloading, or flag combination can overcome the physical 32GB ceiling. The hardware-floor answer is 64GB+ Mac. ^[raw/inbox/2026-09-07.md]

## Accepted recommendation

1. Lock `MTPLX` at `65K` context as the daily driver on `M1 32GB` (`10-12 tok/s`, stable, no OOM).
2. Retain the `131K` config entry for when long-context is specifically needed (lower throughput, use `Unleashed`).
3. For `10+ tok/s at 131K`, upgrade to `64GB+` Mac (M4 Pro/Max recommended).

See also [[wiki-topics/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]] and [[wiki-topics/hermes-agent/wiki/comparisons/65k-vs-131k-context|65K vs 131K Context Comparison]].

## Later high-throughput data point (not comparable to M1)
On `2026-09-15`, `Unleashed 27B Q3_K_XL` at `262K` context reached `81.2 tok/s` with MTP — on a **GPU** machine (GPU1, 24 GB free), not on the `M1 32GB` host. This confirms large-context high throughput is achievable with GPU offload + MTP, but it does **not** reopen the M1 32GB conclusion (which remains a physical 32 GB RAM ceiling). See [[wiki-topics/hermes-agent/wiki/entities/session-20260915-262k-81tok|262K / 81.2 tok/s Milestone — 2026-09-15]].

## Related
- [[wiki-topics/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
- [[wiki-topics/hermes-agent/wiki/decisions/targeted-27b-131k-2026-09-07|Targeted 27B at 131K — 2026-09-07]]
- [[wiki-topics/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
- [[wiki-topics/hermes-agent/wiki/concepts/model-evaluation-2026-09-06|Model Evaluation — 2026-09-06]]
- [[wiki-topics/hermes-agent/wiki/concepts/streaming-throughput-measurement|Streaming Throughput Measurement]]
