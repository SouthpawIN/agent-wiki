---
title: Qwen 2.5 Omni 3B
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, omarchy]
sources: []
confidence: medium
---

# Qwen 2.5 Omni 3B GGUF

> Multimodal model — text, images, audio, video in one 3B model.

## Research
- Multimodal: text, image, audio, video in one model
- 3B parameters — extremely efficient for multimodal
- Uses Qwen2.5 architecture with vision/audio encoders
- 28 GGUF files for extensive quantization options

## Runtimes

### NVIDIA GPU (CUDA) — Omarchy RTX 3090×2
llama.cpp CUDA + mmproj for vision

### AMD GPU (ROCm)
llama.cpp with ROCm + mmproj

### Apple Silicon (Metal) — MacBook M1 Pro
MLX Metal (Qwen2.5 Omni well-supported)

### CPU
llama.cpp (vision encoder may be slow)

## Systems
- omarchy

## Notes
Size: 62G total
Cross-references: [[topics/turbofit/index|wiki index]]
