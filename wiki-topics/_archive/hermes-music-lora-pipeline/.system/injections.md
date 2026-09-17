# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: hermes-music-lora-pipeline
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/hermes-music-lora-pipeline-c5a4db9e54.md"]
confidence: medium
---

# hermes-music-lora-pipeline

## Current context

A Hermes-native pipeline for downloading, processing, captioning, and LoRA fine-tuning music generation models (AceStep/HeartMuLa). # Hermes-Native Music LoRA Training Pipeline This pipeline uses Hermes Agent's built-in tooling and skills to replace external, manual steps with automated, code-driven workflows. ## Architecture Note: AceStep vs. HeartMuLa You mentioned AceStep 1B or 3B. **AceStep is officially a 4B parameter model.** - If you proceed with **AceStep 4B**, your 2x RTX 3090 (24GB each) hardware is sufficient for LoRA fine-tuning with `bf16` and gradient checkpointing. - If you want a strictly **3B open-source alternative with turnkey Hermes skill support**, switch the target to **HeartMuLa 3B** (see the `ai-music-generation` skill). The pipeline below is identical; only the model imports in `4_train_lora.py` change. ## Pipeline Steps ### 0. Prerequisites ### 1. Download Playlist Fetches raw WAV audio and `.info.json` metadata (title, description, URL). *(For Spotify, replace `yt-dlp` with `spotdl "https://open.spotify.com/playlist/..." --format wav`)* ### 2. Process Audio Standardizes all audio to **44.1kHz, Mono, -14 LUFS normalized**, which is the expected input format for music generation models. ### 3. Generate Captions (Hermes Native) Instead of manual labeling, this script uses the `youtube-transcript-api` (aligned with the `research-knowledge-retrieval` skill) to extract video transcripts and combine them with metadata to create rich, descriptive training prompts. *Output: `dataset/metadata.jsonl`* ### 4. Fine-Tune with LoRA The `4_train_lora.py` script is scaffolded using the `mlops-training-finetuning` skill patterns. 1. Open `4_train_lora.py` and update the `MODEL_ID` and `target_modules` to match your chosen model's architecture (AceStep 4B or HeartMuLa 3B). 2. Implement the custom `DataCollator` to convert the WAV file paths into the model's expected audio tensor format. 3. Execute via Hermes `terminal` or `execute_code`: ## How to Share This Profile Once configured, you can share this entire setup with others using **Hermes Profile Distributions**: 1. Navigate to `~/.hermes/profiles/<your-profile-name>` 2. Create a `distribution.yaml` file listing `datasets` and `peft` as required packages. 3. `git init`, commit the `music-lora-pipeline` folder, and push to GitHub. 4. Others can install it via: `hermes profile create --from…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/hermes-music-lora-pipeline` (`2026-07-08T20:37:14Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/creative-music|Creative Music]]
- [[concepts/model-merging-training|Model Merging Training]]
