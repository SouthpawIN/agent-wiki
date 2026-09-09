---
title: Ornith 1.5 35B-A3B MLX 4-bit
created: 2026-09-07
updated: 2026-09-07
type: entity
tags:
  - model
  - turbofit
  - mlx
  - inference
  - candidate
sources:
  - raw/inbox/2026-09-07.md
  - raw/inbox/2026-09-07-from-senter-wiki.md
  - raw/inbox/2026-09-07-from-object-important.md
confidence: high
---

# Ornith 1.5 35B-A3B MLX 4-bit

Local candidate for TurboFit main on the M1 32GB box, owned by MLX, tested from `~/Models/storage/ornith/`.

## What this is

Ornith is a Mixture of Experts (MoE) model with 35B total parameters and roughly 3B active parameters per token. The tested artifact here is the MLX 4-bit build served by `mlx_lm server` on `http://127.0.0.1:11613/v1`. This is the variant Chris repeatedly wanted running on TurboFit so he could switch Hermes off weaker free models.

^[raw/inbox/2026-09-07.md]

## Provenance

Ornith is owned by TurboFit routing, not the wiki itself. See `[[turbofit-runtime-providers|TurboFit Runtime Providers]]` and `[[turbo-fit-evidence-capture|TurboFit Evidence Capture]]` for how service health should be checked when Hermes can't reach it.

^[raw/inbox/2026-09-07-from-senter-wiki.md]

## Status

- **Local server:** MLX deepgrove fork via `mlx_lm server --model ~/Models/storage/ornith --port 11613 --host 127.0.0.1` ^[raw/inbox/2026-09-07.md]
- **Config:** Hermes provider `custom:turbofit`; `providers.turbofit.api: http://127.0.0.1:11613/v1`; `model.default: ornith-1-5-35a3b-mlx` ^[raw/inbox/2026-09-07.md]
- **Context supported:** 131K claimed from server logs; throughput at that window drops sharply under prompt load ^[raw/inbox/2026-09-07.md]
- **Q3 preference note:** Chris wants GGUF vs MLX compared for new candidates and prefers the Q3 quant when page notes place it near base model quality; this page records the MLX run only ^[raw/inbox/2026-09-06.md].
- **Final configuration locked:** 2026-09-07 — Ornith MLX 4-bit configured as main provider at 131K context ^[raw/inbox/2026-09-07.md].

## Measured throughput

|| Test | Measured value |
||---|---|
|| Warmup | ~68s first run; much faster on restarts |
|| Short prompt | 15.6 tok/s at ~517 tokens in / 100 out |
|| 5K prompt | 5.7 tok/s at ~3519 tokens in / 100 out |
|| 131K-loaded server | short-context benchmark also reported at ~28-29 tok/s under lighter conditions |
|| After restart verification | 29 tok/s short prompt, 226 tok/s 5K prompt |

## Benchmark Results (vs competitors)

|| Benchmark | Ornith 1.5 | Ornith 1.0 | Qwen3.6 35B | Gemma 4 31B | Muse Glimmer 30B | Qwen3.5 397B |
||-----------|------------|------------|-------------|-------------|------------------|--------------|
|| **Terminal-Bench (Terminus-2)** | **67.8** | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
|| **Terminal-Bench (Claude Code)** | **68.5** | 62.8 | 49.2 | - | - | 48.6 |
|| **SWE-bench Verified** | **79.0** | 75.6 | 73.4 | 52.0 | - | 76.4 |
|| **SWE-bench Pro** | **59.6** | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
|| **SWE-bench Multilingual** | **71.4** | 69.3 | 67.2 | 51.7 | - | 69.3 |

## Why It Feels Smarter Than Free Models

1. **Agentic coding**: Outperforms 35B+ models on coding tasks by wide margins
2. **Continuous self-improvement**: Uses reinforcement learning to optimize task generation and solution rollouts
3. **Efficient MoE**: Gets 35B-level reasoning with 3B active parameters = faster, smarter than dense models

## Behavioral notes

Chris repeatedly asked to ignore Bonsai, Maple Colibri, and music generation noise and focus on getting Ornith up as the main provider. Three near-duplicate raw messages on 2026-09-07 at 13:18/13:20/13:30 show his exact framing: "It just needs to be configured into turbofit so I can continue with Ornith. Don't worry about bonsai."

^[raw/inbox/2026-09-07.md]

## Decision trail

Hermes-side `custom:turbofit` was retargeted to `http://127.0.0.1:11613/v1`, but Hermes timeouts occurred until restart. Chris switched his active provider to `ornith-1-5-35a3b-mlx via provider turbofit` at 14:25, and session metadata confirms the provider change; however, provider `timeout` errors (`code: timeout`, `provider: turbofit`, `model: ornith-1-5-35a3b-mlx`, `error: Connection error.`) recurred at 2026-09-07T19:26:47.525Z ^[raw/inbox/2026-09-07.md]. A full Hermes restart remains needed to confirm the live route. Until that restart and a successful completion are observed, final promotion is contested ^[raw/inbox/2026-09-07.md].

Chris's final directive at 14:25: "It just needs to be configured into turbofit so I can continue with Ornith" ^[raw/inbox/2026-09-07.md].

^[raw/inbox/2026-09-07.md]

## Related pages

- [[turbo-fit-evidence-capture|TurboFit Evidence Capture]]
- [[mtplx-main-provider|MPLX Main Provider]]
- [[unleashed-backup|Unleashed Backup]]