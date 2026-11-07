---
type: matrix
title: Model × hardware matrix
updated: 2026-11-07
source: measured from Hugging Face file trees via /api/models/<repo>/tree/main?recursive=true
tags: [turbofit, matrix, models, hardware]
---

# Model × hardware matrix

Sizes are **GiB on disk** (weights only; add KV cache). Tier bands are the ones
already in `references/fit-lists.json`, so a row here maps 1:1 onto a rung.

## The seven requested models, measured

| Model | Arch | q3-class size | Smallest | Largest | Vision | Notes |
|---|---|---|---|---|---|---|
| Arete 27B (`bartowski/NousResearch_Arete-27B-GGUF`) | dense 27B | Q3_K_S **11.64** / Q3_K_M 12.26 | IQ2_XXS 8.05 | bf16 50.1 | yes (`mmproj`, f16/bf16) | full quant ladder IQ1→Q8; imatrix present; MTP not shipped |
| Flint 40A2.5B (`orcarouter/Flint-abliterated-GGUF`) | MoE ~40B, 2.5B active | **Mix-12G 11.17** | Mix-12G 11.17 | Mix-24G 22.35 | no | not a quant ladder — two pre-baked memory envelopes (12 G / 24 G) |
| Nanbeige 33B (`abenzerps/Nanbeige4.3-33B-GSQ-RCO-GGUF`) | dense 33B | IQ3_XS **13.79** / IQ3_M 15.04 | IQ2_XXS 9.22 | Q5_K_M 22.17 | no | GSQ-RCO ladder only (no Q3_K_*), so q3 = IQ3_XS |
| Qwen 3.8 27B GSQ-RCO (`ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF`) | dense 27B | IQ3_XXS **9.40** / IQ3_S 10.96 | IQ2_XS 7.84 | IQ3_S 10.96 | yes (`mmproj` BF16) | `-mtp` variants cost +0.33 GiB; **no quant above IQ3_S** |
| Qwen 3.8 Flash Next (`ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF`) | MoE, huge | IQ3_XXS **70.63** | Q2_0 61.86 | IQ3_S 77.88 | yes | quant dirs; only 4 rungs; Strata target |
| Darwin 180B (`FINAL-Bench/Darwin-180B-RSI`) | 180B | — | — | 335.28 (safetensors) | unknown | the benchmark repo ships **safetensors only**; a community mixed quant exists — `Baekpica/Darwin-180B-RSI-Mixed-Quant-GGUF`, MQ-Q5-SSD-PLE-BF16, **125.3 GiB** across 517 files |
| DeepSeek V4.1 Flash 1017 (`ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF`) | MoE + Engram | IQ1_M **112.43** | IQ1_M 112.43 | IQ2_XS 144.57 | yes | only IQ1_M / IQ2_XXS / IQ2_XS; Strata streaming only |

## Dedicated ladder (VRAM, dense)

| Tier | Current rung | + Arete 27B | + Nanbeige 33B | + Qwen 3.8 27B GSQ | + Flint |
|---|---|---|---|---|---|
| 8–11 GB | Ternary Bonsai 2 27B | ✗ (q3 11.6 GiB + KV) | ✗ | IQ3_XXS 9.40 @ 32K, tight | ✗ |
| 12–15 GB | Underdog 27B | **Q3_K_S @ 32K** (11.6 + KV ≈ 13.5) | ✗ | IQ3_S + mtp @ 64K | Mix-12G @ 32K |
| 16–23 GB | Qwen 3.8 27B GSQ IQ3_S | **Q4_K_M @ 131K** (16.0) | IQ3_XS @ 64K | IQ3_S @ 262K | Mix-12G @ 131K |
| 24–63 GB | Qwen 3.8 27B GSQ IQ3_S @ 262K | **Q5_K_M @ 262K** (19.3) | IQ4_XS @ 131K | IQ3_S @ 262K | Mix-24G @ 262K |
| 64 GB+ | Qwen 3.8 Flash Next (Strata) | Q8_0 @ 262K (26.7) | Q5_K_M @ 262K | + Flash Next | Mix-24G |

## Unified ladder (CPU / Apple, currently MoE-only)

| Tier | Current rung | + Arete (dense — **policy exception**) | + Flint | + Qwen GSQ |
|---|---|---|---|---|
| 8–15 GB | Maple Preview 20B-A1B | ✗ | ✗ | IQ2_XS @ 32K (dense, slow) |
| 16–23 GB | Cyber-Tiel Coder 35B-A3B | **Q3_K_S @ 64K** ≈ 8–12 tok/s | Mix-12G @ 64K | IQ3_XXS @ 64K |
| 24–31 GB | Cyber-Tiel Coder 35B-A3B | **Q4_K_M @ 131K** | Mix-24G @ 131K | IQ3_S @ 131K |
| 32–47 GB | Cyber-Tiel Coder 35B-A3B | **Q5_K_M @ 131K** | Mix-24G @ 262K | IQ3_S @ 262K |
| 48–63 GB | Cyber-Tiel Coder 35B-A3B | **Q6_K @ 262K** | Mix-24G | + Flash Next Q2_0 61.9 |
| 64 GB+ | Qwen 3.8 Flash Next (Strata) | Q8_0 | Mix-24G | Flash Next |

## Implementation status

Ten variants of the seven models are in the catalog and offered by Auto/Check
(`SouthpawIN/turbofit` PR #51). Measured facts behind the entries:

| Model | Variants in catalog | q3-class size |
|---|---|---|
| Arete 27B | Q3_K_S, Q4_K_M, Q5_K_M, Q8_0 | 11.64 GiB, rising to 26.7 at Q8 |
| Nanbeige 4.3 33B | IQ3_XS, IQ4_XS | 13.79 GiB |
| Flint 40A2.5B | Mix-12G, Mix-24G | 11.17 GiB (envelope, not a quant) |
| Qwen 3.8 Flash Next | IQ3_XXS (plus existing Strata IQ2_XS) | 70.63 GiB |
| DeepSeek V4.1 Flash | IQ1_M | 112.43 GiB |

What shipped: catalog entries with pinned revisions, recipe families and launch
methods per context, artifact-manifest entries whose sha256 comes from HF's LFS
oid, a regenerated configuration matrix (1300 rows), and three tests that pin the
tier placement. What did **not** ship: ladder promotion. A model becomes a tier
*winner* only through the benchmark campaign, not through a catalog edit.

Two operational facts worth keeping:

- **Flint is `gated: auto` on Hugging Face.** The download needs the licence
  accepted under the user's HF account first; a 401 here is not a TurboFit bug.
- **DeepSeek's IQ1_M is five shards, not six**, and the first is a 10 MB head.
  Sizes read from a single shard will understate the artifact by two orders of
  magnitude.

## Decisions this matrix forces

1. **Arete is not a unified-ladder citizen under the current policy.** The policy
   says unified runs MoE only. Arete is dense. Adding it anyway means an explicit
   `dense-exception` rung, or the unified ladder silently lies about what fits.
   Recommendation: add it as an exception with a `dense` tag and a measured
   tok/s floor (≥ 6 tok/s at 64K) rather than edit the policy quietly.
2. **Qwen 3.8 27B GSQ-RCO tops out at IQ3_S.** "q3 or higher" is satisfied and
   *capped* — any heavier request must fall to Arete or Nanbeige, not to a
   nonexistent Q4 of the same family.
3. **Darwin has a GGUF after all — a third-party mixed quant, not the benchmark
   repo.** `FINAL-Bench/Darwin-180B-RSI` is 335 GiB of safetensors, but
   `Baekpica/Darwin-180B-RSI-Mixed-Quant-GGUF` ships MQ-Q5-SSD-PLE-BF16 at
   125.3 GiB, which is what the existing `darwin-180b-rsi-strata` entry already
   points at. The open question is not convert-or-drop; it is whether a 125 GiB
   download is acceptable as a default-adjacent artifact.
4. **VRAM is no longer the gate above 64 GB.** Flash Next (62–78 GiB) and
   DeepSeek (112–145 GiB) fit the *8 GB VRAM* claim only through Strata's
   expert streaming, which trades VRAM for host RAM and bandwidth. Those two
   rows must carry a `requires: strata-stream` field so the fit checker does not
   refuse them on physics that no longer apply.
