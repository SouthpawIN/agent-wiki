# Fit Ladder — the TurboFit List (canonical)

> **The Fit Ladder is the source of truth for the UI.** The canonical Fit lives here (mirrored from `wiki/index.md` § TurboFit List): **two ladders that converge on Flash Next**, ordered by capability. `serve auto` builds the fit chain from these ladders, picks the largest sustainable rung, and walks down the chain on OOM/timeout — **the Fit List IS the fallback chain** (the adaptive fit chain).

## Fit calculation

```
Required: model_size + KV_cache ≤ tier_size
KV_cache ≈ 2-4 GB at 262K context (q8_0 KV)
Comfortable: model_size + 2 GB ≤ tier_size
```

## The TurboFit List — 5 models, ordered by capability

| # | Model | Type | Params | Optimal Quant | Size | AIME26 | GPQA-D | DeepSWE | LCBv6 | TB4.0 |
|---|-------|------|--------|---------------|------|--------|--------|---------|-------|-------|
| 1 | **Maple Preview** | Ternary MoE | 20B-A1B | TQ2_0-head-Q4_K | 5.5 GiB | 87.5% | 73.5% | — | 75.1% | — |
| 2 | **Cyber Tiel Coder** | Code LLM (MoE) | 35B-A3B | UD-Q4_K_XL | 22.4 GiB | — | — | — | — | — |
| 3 | **Qwen 3.8 GSQ-RCO** | LLM (quant) | 27B | IQ3_S | 11.8 GiB | — | 89.2% | 42.2% | 90.3% | — |
| 4 | **Qwen 3.8 Flash Next** | MoE (Qwen4 Preview) | 180B / 6B | IQ3_XXS | 47 GiB | — | 91.7% | 58.7% | 91.9% | — |
| 5 | **DeepSeek V4.1 Flash** | MoE | 763B / 16B | FP8 / UD-Q4_K_XL | 160 / ~40 GiB | — | 90.9% | 74.2% | — | 31.2% |

> GSQ-RCO IQ3_S benchmarks (AIME25 100%, GPQA-D 89.2%, DeepSWE 42.2%, LCBv6 90.3%) are from the model card; Maple LCBv6 is LiveCodeBench v6.

## The two ladders (converge on Flash Next)

Dense does not run well on CPU / Unified memory, so the tiers split into two ladders:
- **Ladder 1 — Dedicated (GPU / VRAM):** dense is fine — `Bonsai 2 → Underdog 27B → GSQ-RCO 27B → Flash Next`.
- **Ladder 2 — Unified (CPU / Apple Silicon):** MoE only, no dense — `Maple → Cyber-Tiel (in place of GSQ-RCO 27B) → Flash Next → DeepSeek V4.1` (DeepSeek V4.1 is the top rung, **above** Flash Next).

## Cross-cutting rules (every rung)
- **MTP on whenever we can** — every one of these models has MTP (multi-token prediction) available in some form; turn it on at each rung.
- **Mind the power bill (kWh / hour).** IQ3_S is lossless, so there's no reason to push a heavier quant (and a higher power draw) past it — 32 GB and 48 GB both stay on GSQ-RCO @ IQ3_S.

## GPU (NVIDIA/AMD VRAM — ≤16 GB assumes system RAM available for MoE offload + KV)

| Tier | Model | Quant | Size | VRAM Used | Context | Notes |
|------|-------|-------|------|-----------|---------|-------|
| 8-11 GB | Bonsai 2 | Q2 | ~8-9 GiB | ~9 GiB | 131K | Dense ternary GGUF; prism-llama.cpp; MTP on |
| 12-15 GB | Underdog 27B | pq2 | ~12-13 GiB | ~13 GiB | 131K | Dense ternary GGUF; prism-llama.cpp; MTP on |
| 16 GB | GSQ-RCO 27B | IQ3_S | 11.8 GiB | ~12 GiB | 131K | Near-lossless; MTP on; Cyber-Tiel Q3_K_M also fits (~14 GiB) |
| 24 GB | GSQ-RCO 27B | IQ3_S | 11.8 GiB | ~12 GiB | 262K | More KV headroom; MTP on |
| 32 GB | GSQ-RCO 27B | IQ3_S (lossless) | 11.8 GiB | ~12 GiB | 262K+ | Lossless — don't up the power bill past it; MTP on |
| 48 GB | GSQ-RCO 27B | IQ3_S (lossless) + MTP | 11.8 GiB | ~12 GiB | 262K+ | Same IQ3_S as 32 GB, MTP on |
| 64 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native | MoE; both ladders converge (Strata on 2×3090) |
| 96 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native, 1M w/ YaRN | Qwen4 preview, beats Claude Opus 4.6 |
| 128 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 1M | Max context for Flash Next |

> IQ3_S = near-lossless, recommended where it fits. Only move to FP16 at 64 GB+. Flash Next QSA gives ~4.9× decode speedup vs dense attention at 262 K; IQ3_XXS is the sweet spot for 64 GB+.

## CPU (system RAM — model + KV must fit in RAM)

| Tier | Model | Quant | Size | RAM Used | Context | Notes |
|------|-------|-------|------|----------|---------|-------|
| 8-15 GB | Maple | TQ2_0 | 5.5 GiB | ~6 GiB | 131K native | MoE; stands in for Bonsai 2 / Underdog (dense) |
| 16 GB | Cyber-Tiel Coder | Q3_K_M | ~14 GiB | ~16 GiB | 262K native | MoE, 3B active; faster than GSQ-RCO on CPU |
| 32 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K native | Fast on CPU |
| 48 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K+ | More KV headroom |
| 64 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native | Both ladders converge (Cyber-Tiel stood in for GSQ-RCO 27B) |
| 96 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native | Flash Next entry tier |
| 128 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 1M w/ YaRN | Max context |
| top | DeepSeek V4.1 Flash | FP8 / UD-Q4_K_XL | large (MoE) | — | 181K | 763B MoE — top rung, **above** Flash Next; 1017 update, Strata engine; pending: does it fit the target tier? |

## Unified memory (Apple Silicon — shared CPU/GPU RAM)

| Tier | Model | Quant | Size | RAM Used | Context | Notes |
|------|-------|-------|------|----------|---------|-------|
| 8-15 GB | Maple | TQ2_0 | 5.5 GiB | ~6 GiB | 131K native | MoE; 218 tok/s on M4; stands in for Bonsai 2 / Underdog |
| 16 GB | Cyber-Tiel Coder | Q3_K_M | ~14 GiB | ~16 GiB | 262K native | MoE, 3B active; faster than GSQ-RCO |
| 32 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K native | 22+4 = 26 GB ✓ |
| 48 GB | Cyber-Tiel Coder | UD-Q4_K_XL | 22.4 GiB | ~23 GiB | 262K+ | M2 Max/Ultra territory |
| 64 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native | Candidate-only on Apple — no macOS engine yet |
| 96 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 262K native | M4 Ultra |
| 128 GB | Flash Next | IQ3_XXS | 47 GiB | ~48 GiB | 1M w/ YaRN | Max Flash Next |
| top | DeepSeek V4.1 Flash | FP8 / UD-Q4_K_XL | large (MoE) | — | 181K | 763B MoE — top rung, **above** Flash Next; 1017 update, Strata engine |

> ★ = on the TurboFit List. Models without ★ are Model Zoo only.

## Live catalog (shipped subset)

The currently-automated, downloadable set (`model-catalog.json` / `fit-lists.json`) — the **shipped subset** of the list above, being automated now: `Qwen3.5-397B-A17B` (MoE), `Qwen3.5-27B`, `GLM-5.1` (744 B MoE, strongest local coder), `Llama-3.3-70B`, `Qwen3-30B-A3B`, `Qwen3.5-35B-A3B` (1 M ctx), `Qwen2.5-72B-Instruct-1M` (8448 ctx).

## Recovery order (when VRAM/RAM pressure rises)

The main model is protected until the last step · MoE expert offload is the first pressure valve · context drops only when absolutely necessary · API aux kicks in when the local aux can't fit.

> Full model detail: [`wiki/models/`](../wiki/models/) (one page per model) · Fit UI: [`wiki/models/hardware-tiers.html`](../wiki/models/hardware-tiers.html) · [`wiki/models/leaderboard.html`](../wiki/models/leaderboard.html) · Canonical: [`fit-lists.json`](https://github.com/SouthpawIN/turbofit/blob/main/fit-lists.json) · [`model-catalog.json`](https://github.com/SouthpawIN/turbofit/blob/main/model-catalog.json)
