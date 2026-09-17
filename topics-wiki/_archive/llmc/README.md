---
title: llmc
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/llmc
status: dormant
tags: [repo]
---

# llmc

> LLMC — LLM + MC. Your lyric and song companion. Hermes Agent profile.

**[Open on GitHub](https://github.com/SouthpawIN/llmc)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 5 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-21 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# LLMC — Song Forger & Creative Music Agent

## What LLMC Does

LLMC is a creative music agent — "an LLM that's also an MC." It collaborates with the user to write lyrics in the Mc.Baldiee prose register (metaphorical, cosmic, never explicit) and generates full songs via ACE-Step, a local music generation model. The workflow: discuss themes → write lyrics → generate songs → deliver to Discord → add to Evolutionary Radio playlist.

- **Writes lyrics** in Mc.Baldiee style — lighthouse metaphors, cosmic imagery, implicit truths through concrete scenes
- **Generates songs** via ACE-Step API (local, GPU-accelerated, ~2-3s per track on RTX 3090)
- **Tracks everything** in a lyric journal — every version, every session, every song
- **Delivers** to Discord as two-message format: audio file + lyrics with metadata
- **Builds playlists** for Evolutionary Radio — every batch feeds the radio's track queue

## Quick Start

### Install
```bash
hermes profile install https://github.com/SouthpawIN/llmc
```

### Verify
```bash
hermes profile list
```

### Run
```bash
hermes chat --profile llmc
```

## Example Prompts

- *"Write a song about the moment you realize you've outgrown someone — not angry, just distant, like watching a ship disappear over the horizon"*
- *"I've got these lines: 'the architect's hands were never shaking / the blueprint was wrong from the start.' Build a full song around them."*
- *"Generate a batch of 3 songs — dark cinematic rap, completely distinct themes. No shared metaphors between songs."*
- *"What's in the lyric journal from last session? Let me see what we wrote."*
- *"Push the latest batch to Discord and add it to the Evolutionary Radio playlist."*
- *"Change the style — give me an industrial dark trap track, GHOSTEMANE-style distortion, 140 BPM."*

## Key Features
- **Mc.Baldiee prose register** — metaphorical, cosmic, never explicit. Translates themes into imagery.
- **ACE-Step integration** — local music generation at `http://127.0.0.1:8001`, GPU-accelerated, 50 inference steps for full quality
- **Anti-repetition system** — every song in a batch has completely distinct lyrical themes, no shared metaphors
- **Batch workflow** — theme discussion → lyric writing → song generation → Discord delivery → playlist integration
- **Style diversity** — 5 preset styles (dark cinematic rap, ambient spoken word, orchestral, industrial trap, boom bap), rotated per batch
- **Duration mastery** — ACE-Step's audio_duration is a cap, actual duration from line count. 60+ lines reliably hits 300s (5:00)

*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics-wiki/music/README|music]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
