---
title: Super Qwen 3.8 27B
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, omarchy]
sources: []
confidence: medium
---

# Super Qwen 3.8 27B Abliterated

> Uncensored Qwen3.8-27B — abliterated to remove self-censorship.

## Research
- Based on Qwen3.8-27B architecture with 27B dense parameters
- Abliteration removes model self-censorship without retraining
- Dense model — no MoE, simpler to run than MoE variants
- Excellent for creative writing, coding assistance, roleplay

## Runtimes

### NVIDIA GPU (CUDA) — Omarchy RTX 3090×2
llama.cpp CUDA, -ngl 99 for full GPU offload

### AMD GPU (ROCm)
llama.cpp with ROCm (if supported)

### Apple Silicon (Metal) — MacBook M1 Pro
MLX or llama.cpp Metal, -ngl 99

### CPU
llama.cpp AMX

## Systems
- omarchy

## Notes
Size: 18G total
Cross-references: [[topics-wiki/turbofit/index|wiki index]]
