---
title: NVIDIA Nemotron 3.5
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, omarchy]
sources: []
confidence: medium
---

# NVIDIA Nemotron 3.5 Lightning

> Enterprise MoE model — 30B total, 3B active. Lightning variant for low-latency inference.

## Research
- 30B total / 3B active MoE architecture
- Enterprise focus: reliable, production-ready
- Lightning variant optimized for inference speed
- FP4 quantization for smallest storage footprint

## Runtimes

### NVIDIA GPU (CUDA) — Omarchy RTX 3090×2
llama.cpp CUDA, --layer-split for multi-GPU

### AMD GPU (ROCm)
llama.cpp with ROCm (if FP4 supported)

### Apple Silicon (Metal) — MacBook M1 Pro
llama.cpp Metal (if FP4 supported)

### CPU
llama.cpp AMX

## Systems
- omarchy

## Notes
Size: 115G total
Cross-references: [[wiki-topics/turbofit/index|wiki index]]
