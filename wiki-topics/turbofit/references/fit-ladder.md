# Fit Ladder

The Fit Ladder is how Turbofit keeps a model **running at maximum quality for the exact VRAM you have** — instead of the `ollama run → OOM → restart` loop. Two independent ladders, chosen by your hardware.

> Current doctrine (2026-10). Supersedes the older "Tier S / SF / F / C" framing in `curated-lineup.md`.
> Canonical data: [`fit-lists.json`](../../../../../turbofit/fit-lists.json) and [`model-catalog.json`](../../../../../turbofit/model-catalog.json) in the product repo. Narrative: [`ROADMAP.md`](../ROADMAP.md).

## Ladder 1 — GPU-dedicated (VRAM only, e.g. RTX 3090 24GB)

A dense or MoE model sized to the card.

| Step | Model | VRAM | Why |
|---|---|---|---|
| S | Qwen3.5-397B-A17B (MoE, 17B active) | 24GB | Best dense/MoE at 24GB |
| SF | Qwen3.5-35B-A3B (MoE, 3B active) | 24GB | Always-on, 1M ctx, aux |
| SF | GLM-5.1 (744B MoE, 40B active) | 24GB | Strongest local coder |
| F | Llama-3.3-70B | 24GB | Dense fallback |
| F | Qwen3-30B-A3B (MoE) | 24GB | Fast MoE |
| F | Qwen3.5-27B (dense) | 24GB | Dense reasoning |
| C | Qwen2.5-72B-Instruct-1M (8448 ctx) | 24GB | Long-ctx dense |

## Ladder 2 — Unified memory (Mac / Apple Silicon, no VRAM ceiling)

MoE is the only practical dense-free path in unified memory.

| Step | Model | Note |
|---|---|---|
| S | Qwen3-30B-A3B (MoE, 3B active) | Fits M1 8GB |
| S | Qwen3.5-35B-A3B (MoE, 3B active) | 1M ctx always-on |

## VRAM tiers (local)
- **24GB** — RTX 3090 (Ladder 1)
- **8GB** — Apple M1 (Ladder 2)
- **4GB** — M1 low / small Mac
- **2GB** — Raspberry Pi 5 (tiny quant only)

## Recovery order (when VRAM pressure rises)
1. **Main is protected** until the last step.
2. **MoE expert offload** is the first pressure valve.
3. **Context drops** only when absolutely necessary.
4. **API aux** kicks in when the local aux can't fit.

Each step preserves maximum intelligence while respecting VRAM.
