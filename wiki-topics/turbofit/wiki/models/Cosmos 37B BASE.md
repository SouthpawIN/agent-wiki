---
title: Cosmos 37B BASE
created: 2026-09-16
updated: 2026-09-16
type: model
tags: [model, omarchy]
sources: []
confidence: medium
---

# Cosmos 37B BASE GGUF

> Large 37B dense model. Foundational model for complex reasoning tasks.

## Research
- 37B dense parameter model
- Large context window support (check GGUF for n_ctx)
- 10 GGUF files for extensive quantization options
- Best for complex tasks where smaller models fail

## Runtimes

### NVIDIA GPU (CUDA) — Omarchy RTX 3090×2
llama.cpp CUDA, needs offload (184GB total)

### AMD GPU (ROCm)
llama.cpp with ROCm (if supported)

### Apple Silicon (Metal) — MacBook M1 Pro
llama.cpp Metal (heavy offload to unified memory)

### CPU
llama.cpp AMX (very slow at this size)

## Systems
- omarchy

## Notes
Size: 184G total
Cross-references: [[wiki-topics/turbofit/index|wiki index]]
