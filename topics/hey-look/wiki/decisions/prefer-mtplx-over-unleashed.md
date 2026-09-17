---
title: Prefer MTPLX over Unleashed
created: 2026-09-06
updated: 2026-09-07
type: decision
tags: [decision, mtplx, unleashed, speed, mac]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-07.md]
confidence: high
contested: true
---

# Prefer MTPLX over Unleashed

Chris decided to keep the speed-optimized MTPLX build as the primary path for the Qwen 27B model, and to remove Unleashed if it is slower or confusing.^[raw/inbox/2026-09-06.md]

## What was decided

- Use the specific MTPLX build optimized for speed that Chris selected, not Unleashed.^[raw/inbox/2026-09-06.md]
- If Unleashed is slower, remove it from this system.^[raw/inbox/2026-09-06.md]
- Hermes aligned to this by targeting MTPLX as main after testing.^[raw/inbox/2026-09-06.md]

## New evidence on 2026-09-07

Hermes later tested Unleashed + DFlash2 head-to-head with MTPLX at 131K on the same box.^[raw/inbox/2026-09-07.md] That comparison showed MTPLX slightly faster on short prompts, Unleashed slightly faster on medium prompts, and Unleashed using ~7GB less RAM; Unleashed was also noted as uncensored/abliterated.^[raw/inbox/2026-09-07.md] Chris defined the port-mapped protocol as port 11613 for MTPLX and port 11606 for Unleashed + DFlash2, with explicit prompt shapes: short prompt 500 tokens, medium 5K prompt/100 tokens, long generation 1000 tokens.^[raw/inbox/2026-09-07.md] A later head-to-head on the same day confirmed MTPLX 6.9 tok/s vs Unleashed 6.0 tok/s on short prompts, MTPLX 0.6 tok/s vs Unleashed 0.8 tok/s on medium prompts, MTPLX ~20GB RAM vs Unleashed ~13GB, and Unleashed uncensored/abliterated.^[raw/inbox/2026-09-07.md]

In the same raw slice, Hermes tested Ornith-1.5-35B-A3B MLX 4-bit as an alternative path; it reached 28.5 tok/s on short prompts on this box, but dropped to ~0.4 tok/s at 60K context and OOM'd at 131K with q8_0 KV cache, after which Hermes explored reduced GPU layers as a mitigation.^[raw/inbox/2026-09-07.md] That result reopened the trade-off: Ornith is the fastest short-context option, but it is not a stable 131K path in MLX server mode on this hardware.^[raw/inbox/2026-09-07.md]

## 2026-09-15 confirmation

The Unleashed + DFlash2 path was actually made to work through Hermes on the Mac on 2026-09-15 after a reasoning-budget problem (empty content) was resolved with `--reasoning off` (85.7 tok/s).^[raw/inbox/2026-09-15.md] Both models now respond through Hermes with reasoning traces, DFlash2 is set up as an alternative service, and the 81 tok/s MTP config remains the default — consistent with keeping MTPLX as the primary speed path while Unleashed+DFlash2 is available as a fallback.^[raw/inbox/2026-09-15.md] The earlier empty-content failures are now understood to have been a token-budget cause, not a draft-method cause; see [[concepts/unleashed-dflash2-reasoning-budget|Unleashed + DFlash2 reasoning-budget constraint]].

## Why it matters

Chris's constraint is a 32GB Mac; the decision implies a local-model serving choice that directly affects throughput, RAM headroom, censorship behavior, and operational simplicity for long-context work.^[raw/inbox/2026-09-06.md]

## Next state

Choose one operating path for this box, or accept a context-length split: 65K for maximum speed on MTPLX, 131K q8/swap for longer context with lower throughput, or 131K on Unleashed + DFlash2 for lower RAM use and uncensored output.^[raw/inbox/2026-09-06.md]^[raw/inbox/2026-09-07.md]

## Related

- [[entities/qwen-27b-mtplx-optimized-speed|Qwen 27B MTPLX Optimized Speed]]
- [[concepts/mtplx|MTPLX]]
- [[queries/mtplx-131k-benchmark-request|MTPLX 131K benchmark request]]
- [[queries/mtplx-131k-systematic-retest|MTPLX 131K systematic retest]]
- [[queries/mtplx-131k-vs-unleashed-dflash2|MTPLX 131K vs Unleashed + DFlash2]]
- [[comparisons/mtplx-131k-speed-report-comparison|MTPLX 131K Speed Report Comparison]]
- [[comparisons/mtplx-65k-vs-131k|MTPLX 65K vs 131K]]
