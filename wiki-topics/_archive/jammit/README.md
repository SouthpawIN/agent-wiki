---
title: jammit
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/jammit
status: dormant
tags: [repo]
---

# jammit

> infinite ai generated radio in your terminal

**[Open on GitHub](https://github.com/SouthpawIN/jammit)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 11 / 3
- **License:** MIT
- **Fork of:** original work
- **Created:** 2025-11-27 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# Jammit: Infinite AI Music Radio

A command-line tool for infinite AI music generation and playback, powered by the ACE-Step model. Generate and queue continuous music based on text prompts, all operating silently in the background. Perfect for creating endless ambient soundscapes or themed radio stations.

## Features

*   **Infinite Music Generation:** Continuously generates new music based on your prompt.
*   **Automatic Playback & Queuing:** Generated tracks are automatically played and queued for a seamless listening experience.
*   **Absolutely Silent Operation:** No console output during generation or playback (except for errors that bypass aggressive suppression).
*   **Graceful Shutdown:** Easily stop all associated processes with `Ctrl+C`.
*   **Customizable Parameters:** Adjust generation parameters like duration, inference steps, and guidance scale.
*   **Defaults to Infinite Mode:** Designed as an "infinite radio" out-of-the-box.

## Installation

Follow these steps to set up Jammit on your system.

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/jammit.git # Replace with your actual GitHub URL
cd jammit
```

### 2. Install System Dependencies

Jammit uses `aplay` for audio playback. Install it via your system's package manager:

```bash
sudo apt-get update
sudo apt-get install -y alsa-utils
```

### 3. Set Up Python Environment

It's recommended to use a virtual environment for Python projects.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

*(Note: If you encounter issues with `torch` installation, please refer to the official PyTorch website for specific CUDA/CPU installation instructions based on your system.)*

### 4. ACE-Step Model Download

The ACE-Step model will be downloaded automatically the first time you run Jammit if it's not found locally. This might take some time depending on your internet connection.

Alternatively, you can pre-download it manually:
*(Instructions for manual pre-download will depend on the model host, typically Hugging Face. For ACE-Step/ACE-Step-v1-3.5B, you would typically use `huggingface-cli download` or clone the repository.)*
*Self-correction: The model is located in `Models/ACE-Step`. The pipeline itself handles the download using `snapshot_download`. So the current instruction is sufficient. I will just mention the expected download location for transparency.*


*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[wiki-topics/music/README|music]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
