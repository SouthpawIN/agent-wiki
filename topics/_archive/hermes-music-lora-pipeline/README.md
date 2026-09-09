---
title: hermes-music-lora-pipeline
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/hermes-music-lora-pipeline
status: dormant
tags: [repo]
---

# hermes-music-lora-pipeline

> A Hermes-native pipeline for downloading, processing, captioning, and LoRA fine-tuning music generation models (AceStep/HeartMuLa).

**[Open on GitHub](https://github.com/SouthpawIN/hermes-music-lora-pipeline)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 5 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-11 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# Hermes-Native Music LoRA Training Pipeline

This pipeline uses Hermes Agent's built-in tooling and skills to replace external, manual steps with automated, code-driven workflows.

## Architecture Note: AceStep vs. HeartMuLa
You mentioned AceStep 1B or 3B. **AceStep is officially a 4B parameter model.**
- If you proceed with **AceStep 4B**, your 2x RTX 3090 (24GB each) hardware is sufficient for LoRA fine-tuning with `bf16` and gradient checkpointing.
- If you want a strictly **3B open-source alternative with turnkey Hermes skill support**, switch the target to **HeartMuLa 3B** (see the `ai-music-generation` skill). The pipeline below is identical; only the model imports in `4_train_lora.py` change.

## Pipeline Steps

### 0. Prerequisites
```bash
# Install dependencies
pip install yt-dlp ffmpeg-python youtube-transcript-api datasets peft transformers accelerate
```

### 1. Download Playlist
Fetches raw WAV audio and `.info.json` metadata (title, description, URL).
```bash
chmod +x 1_download.sh
./1_download.sh "https://youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```
*(For Spotify, replace `yt-dlp` with `spotdl "https://open.spotify.com/playlist/..." --format wav`)*

### 2. Process Audio
Standardizes all audio to **44.1kHz, Mono, -14 LUFS normalized**, which is the expected input format for music generation models.
```bash
chmod +x 2_process_audio.sh
./2_process_audio.sh
```

### 3. Generate Captions (Hermes Native)
Instead of manual labeling, this script uses the `youtube-transcript-api` (aligned with the `research-knowledge-retrieval` skill) to extract video transcripts and combine them with metadata to create rich, descriptive training prompts.
```bash
python3 3_generate_captions.py
```
*Output: `dataset/metadata.jsonl`*

### 4. Fine-Tune with LoRA
The `4_train_lora.py` script is scaffolded using the `mlops-training-finetuning` skill patterns.
1. Open `4_train_lora.py` and update the `MODEL_ID` and `target_modules` to match your chosen model's architecture (AceStep 4B or HeartMuLa 3B).
2. Implement the custom `DataCollator` to convert the WAV file paths into the model's expected audio tensor format.
3. Execute via Hermes `terminal` or `execute_code`:
```bash
accelerate launch --mixed_precision bf16 --num_processes 1 4_train_lora.py
```

## How to Share This Profile
Once configured, you can share this entire setup with others using **Hermes Profile Distributions**:
1. Navigate to `~/.hermes/profiles/`
2. Create a `distribution.yaml` file listing `datasets` and `peft` as required packages.

*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics/music/README|music]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
