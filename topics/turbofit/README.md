# Turbofit

**One model provider. Every machine. The best local configuration the hardware can safely sustain.**

Turbofit is a first-class [Hermes Agent](https://github.com/NousResearch/hermes-agent) provider and adaptive local-inference runtime. It inventories physical compute and total usable memory, recommends an evidence-backed ladder, launches a native backend, and exposes one OpenAI-compatible endpoint.

```text
provider: custom:turbofit
model: auto
```

**TurboFit Check** scans the machine — dedicated VRAM, unified/integrated memory, or RAM-only — and applies Auto or a selected compatible lane.

> **Wiki:** [Full Turbofit Wiki](https://github.com/SouthpawIN/turbofit/wiki) — Model Zoo, benchmarks, hardware tiers, and more.

---

## Agentic Model Lineup (TurboFit List)

> 5 models suitable for running Hermes Agent locally. Ordered by capability.

| Order | Model | Type | Parameters | Optimal Quant | Size | AIME26 | GPQA-D | DeepSWE | LCBv6 | TB4.0 |
|-------|-------|------|------------|---------------|------|--------|--------|---------|-------|-------|
| 1 | **Maple Preview** | Ternary MoE | 20B-A1B | TQ2_0-head-Q4_K | 5.5 GiB | 87.5% | 73.5% | — | 75.1% | — |
| 2 | **Cyber Tiel Coder** | Code LLM (MoE) | 35B-A3B | UD-Q4_K_XL | 22.4 GiB | — | — | — | — | — |
| 3 | **Qwen 3.8 GSQ-RCO** | LLM (Quantized) | 27B | IQ3_S | 11.8 GiB | — | 89.2% | 42.2% | 90.3% | — |
| 4 | **Qwen 3.8 Flash Next** | MoE (Qwen4 Preview) | 180B / 6B | IQ3_XXS | 47 GiB | — | 91.7% | 58.7% | 91.9% | — |
| 5 | **DeepSeek V4.1 Flash** | MoE | 763B / 16B | FP8 / UD-Q4_K_XL | 160 / ~40 GiB | — | 90.9% | 74.2% | — | 31.2% |

> **Fit rule:** model_size + KV cache ≤ tier size. KV cache ≈ 2-4GB at 262K context. GSQ-RCO IQ3_S is near-lossless and the default for all GPU tiers.

---

## Model Zoo

| Model | Type | System | Parameters | AIME26 | GPQA-D | DeepSWE | LCBv6 | TB4.0 |
|-------|------|--------|------------|--------|--------|---------|-------|-------|
| **Maple Preview** ★ | Ternary MoE | Omarchy | 20B-A1B | 87.5% | 73.5% | — | 75.1% | — |
| **Cyber Tiel Coder** ★ | Code LLM | Omarchy, MacBook | 35B-A3B | — | — | — | — | — |
| **Qwen 3.8 GSQ-RCO** ★ | LLM | Omarchy | 27B | — | 89.2% | 42.2% | 90.3% | — |
| **Qwen 3.8 Flash Next** ★ | MoE | Omarchy | 180B/6B | — | 91.7% | 58.7% | 91.9% | — |
| **DeepSeek V4.1 Flash** ★ | MoE | Omarchy | 763B/16B | — | 90.9% | 74.2% | — | 31.2% |
| **Ace Step 1.5** | Music | Omarchy | 4B | — | — | — | — | — |
| **Bonsai 27B** | LLM (Ternary) | Omarchy | 27B | — | — | — | — | — |
| **Cosmos 37B** | LLM | Omarchy | 37B | — | — | — | — | — |
| **NVIDIA Nemotron 3.5** | Enterprise MoE | Omarchy | 30B-A3B | — | — | — | — | — |
| **Qwen 2.5 Omni** | Multimodal VLM | Omarchy | 3B | — | — | — | — | — |
| **Soprano** | Creative Micro | Omarchy | 80M | — | — | — | — | — |

> ★ = on TurboFit List. For full model research, see the [wiki](https://github.com/SouthpawIN/turbofit/wiki).

---

## Hardware Tiers

### GPU (NVIDIA/AMD VRAM)

| Tier | Model | Quant | VRAM Used | Context | Notes |
|------|-------|-------|-----------|---------|-------|
| <8 GB | Maple | TQ2_0 | ~6 GiB | 131K native | SSD streaming |
| 16–64 GB | GSQ-RCO | IQ3_S | ~12 GiB | 262K+ | Near-lossless, low power |
| 96 GB | Flash Next | IQ3_XXS | ~48 GiB | 262K native | Qwen4 preview |
| 128 GB | Flash Next | IQ3_XXS | ~48 GiB | 1M | Max context |
| 256 GB | DeepSeek V4.1 Flash | FP8 | ~160 GiB | 1M | Top capability |

### CPU (System RAM)

| Tier | Model | Quant | RAM Used | Context | Notes |
|------|-------|-------|----------|---------|-------|
| <8 GB | Maple | TQ2_0 | ~6 GiB | 131K native | Minimum viable |
| 16 GB | Cyber-Tiel Coder | Q3_K_M | ~14 GiB | 262K native | MoE, fast |
| 32–48 GB | Cyber-Tiel Coder | UD-Q4_K_XL | ~22 GiB | 262K+ | Fast MoE |
| 64 GB | GSQ-RCO | IQ3_S | ~12 GiB | 262K+ | Near-lossless |
| 96+ GB | Flash Next | IQ3_XXS | ~48 GiB | 1M | Top tier |

### Unified Memory (Apple Silicon)

| Tier | Model | Quant | RAM Used | Context | Notes |
|------|-------|-------|----------|---------|-------|
| <8 GB | Maple | TQ2_0 | ~6 GiB | 131K native | 218 tok/s on M4 |
| 16 GB | Cyber-Tiel Coder | Q3_K_M | ~14 GiB | 262K native | MoE, fast |
| 32–48 GB | Cyber-Tiel Coder | UD-Q4_K_XL | ~22 GiB | 262K+ | Fast MoE |
| 64 GB | GSQ-RCO | IQ3_S | ~12 GiB | 262K+ | Near-lossless |
| 96+ GB | Flash Next | IQ3_XXS | ~48 GiB | 1M | Top tier |

---

## Visual Reference

![Model Ladder](assets/scaling-ladder.png)

![Provider Integration](assets/provider-integration.png)

![Hermes Settings](assets/hermes-desktop-turbofit-settings.png)

![Speculative Decode](assets/turbofit-2.4-spec-decode.png)

![Turbofit Hero](assets/turbofit-hero.png)

---

## Integrations

| Repo | Description |
|------|-------------|
| [SouthpawIN/TurboFit](https://github.com/SouthpawIN/turbofit) | Main Turbofit runtime |
| [deepgrove-ai/mlx-lm-deepgrove](https://github.com/deepgrove-ai/mlx-lm-deepgrove) | Maple MLX runtime |
| [RasoulNik/ssdmoe](https://github.com/RasoulNik/ssdmoe) | SSD MoE streaming |
| [tayoun/flash-moe](https://github.com/tayoun/flash-moe) | MoE streaming from SSD |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Hermes Agent runtime |

---

## Rules

1. **CPU and Unified Memory prefer MoE over dense** — Cyber-Tiel Coder for <48GB, GSQ-RCO at 64GB+
2. **IQ3_S is the default** — near-lossless, lower power, faster inference
3. **Only 5 TurboFit candidates** — Maple, Cyber-Tiel, GSQ-RCO, Flash Next, DeepSeek V4.1 Flash
4. **Math must be correct** — model size + KV cache ≤ tier size

---

## License

MIT
