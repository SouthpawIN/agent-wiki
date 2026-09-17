---
title: Ace Step 1.5 4B
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, omarchy]
sources: []
confidence: medium
---

# ACE-Step 1.5 GGUF

> Music generation model — 4B DiT decoder, 8-step turbo generation. Outperforms commercial alternatives.

## Research
- 4B DiT audio decoder, 8-step turbo (vs 20+ base)
- Platforms: Mac, AMD, Intel, CUDA
- 12-20GB VRAM required (with/without offload)
- Downloaded to Omarchy (53G, 18 GGUF files)

## Runtimes

### NVIDIA GPU (CUDA) — Omarchy RTX 3090×2
acestep.cpp with CUDA, 12-20GB VRAM on RTX 3090×2

### AMD GPU (ROCm)
Not yet tested

### Apple Silicon (Metal) — MacBook M1 Pro
acestep.cpp with Metal (if supported)

### CPU
Not recommended — too slow for audio generation

## Systems
- omarchy

## Notes
Size: 53G total
Cross-references: [[topics-wiki/turbofit/index|wiki index]]
