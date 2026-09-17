---
title: ACE-Step 1.5 4B (MLX 4bit)
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [tool, music, repo, decision]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---
# ACE-Step 1.5 4B (MLX 4bit)

A 2.06 GB MLX-quantized music model that Chris chose as the first local generation candidate on his 32 GB Mac because it fits alongside existing workloads. Hermes identified it as one of two music models to download; the other was [[wiki-topics/music/wiki/entities/minimax-music-3|MiniMax Music 3]]. ^[raw/inbox/2026-09-07.md]

## Status (2026-09-07)
- Downloaded successfully to `~/Models/storage/music/ACE-Step1.5-MLX-4bit.safetensors` (2,108 MB). ^[raw/inbox/2026-09-07.md]
- Failed to generate audio: ACE-Step "couldn't load" because the model type is not supported in `mlx_audio`, and `soundfile` was also missing. ^[raw/inbox/2026-09-07.md]
- Output folder `Beats/` is empty. ^[raw/inbox/2026-09-07.md]
- Chris later noted that an MLX/quant build "should be" available, signaling he expects this path to exist. ^[raw/inbox/2026-09-07.md]

## Standing goal (2026-09-14)
ACE-Step 1.5 4B is now the base of a standing LoRA pipeline Chris wants to build: on "go," produce a LoRA of the mp3s in his folder plus a batch of AceStep-style prompts defining that style. The pipeline must be grounded in AceStep's own documentation (via `/learn`, following links), with a notepad for follow-up questions that loops back until exhausted. See [[wiki-topics/music/wiki/decisions/2026-09-14-ace-step-lora-pipeline|2026-09-14 ACE-Step LoRA pipeline standing goal]] and [[wiki-topics/music/wiki/concepts/ace-step-lora-pipeline|ACE-Step 1.5 4B LoRA pipeline]]. ^[raw/inbox/2026-09-14.md]

## Assumptions Chris stated
- "A-C-E-S-T-E-P, you've got to find the model, download it and get it going... step 1.54-B, the largest one on there, should work just fine on here." ^[raw/inbox/2026-09-07.md]
- "If minimax music 3 does not work, I would actually like you to get both of those and get them running on this machine." ^[raw/inbox/2026-09-07.md]
- "There might be an MLX for it, or should be." ^[raw/inbox/2026-09-07.md]

## Evidence
- "The plan: 1. Download ACE-Step 1.5 (2GB) now — it'll fit alongside MTPLX" ^[raw/inbox/2026-09-07.md]
- "ACE-Step couldn't load (model type not supported in mlx_audio), and then soundfile was missing." ^[raw/inbox/2026-09-07.md]

## Open questions
- Is there a loader/runner other than `mlx_audio` that supports ACE-Step's model type?
- Is there an existing MLX/quant build for ACE-Step that avoids the current model-type blocker?
- Does ACE-Step need `soundfile` only for saving WAV, or for runtime too?
