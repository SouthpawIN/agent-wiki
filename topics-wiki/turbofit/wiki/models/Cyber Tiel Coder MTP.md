---
title: Cyber Tiel Coder MTP
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, omarchy]
sources: []
confidence: medium
---

# Cyber-Tiel-Coder 35B-A3B MTP

> Cyber Tiel Coder with MTP — speculative decoding for 2x faster generation.

## Research
- 35B-A3B MoE + MTP (Multi-Token Prediction)
- Draft-token speculative decoding
- 10 GGUF files for various quantization options
- Cyber variant uncensored for coding

## Runtimes

### NVIDIA GPU (CUDA) — Omarchy RTX 3090×2
llama.cpp with --spec-type draft-mtp, -ngl 99

### AMD GPU (ROCm)
llama.cpp with ROCm (if MTP supported)

### Apple Silicon (Metal) — MacBook M1 Pro
MLX with MoE support, or llama.cpp Metal

### CPU
llama.cpp AMX (MoE experts load sequentially)

## Systems
- omarchy

## Notes
Size: 183G total
Cross-references: [[topics-wiki/turbofit/index|wiki index]]
