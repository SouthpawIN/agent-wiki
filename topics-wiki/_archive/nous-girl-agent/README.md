---
title: nous-girl-agent
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/nous-girl-agent
status: dormant
tags: [repo]
---

# nous-girl-agent

> Nous Girl agent + OmniStep Evolution Radio plugin — curated local model pet, multimodal by default, voice + music from the model

**[Open on GitHub](https://github.com/SouthpawIN/nous-girl-agent)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 5 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-08 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# Omni VA

**The desktop VA, the local model server, the OmniStep Evolution Radio, the curator agent, the Senter triage profile — all in one stack.**

> TOWARDS SELF-IMPROVEMENT · curated by mu

A standalone, voice-interactive, ever-evolving desktop VA that serves as a **curated local-model server manager**. The VA is the face of the model — voice and music come *from the model itself*, with a graceful fallback to Edge TTS and curated playlists when you swap to a text-only LLM.

The **OmniStep Evolution Radio** lives as a plugin inside the agent. It's a perpetual radio that watches what you engage with, builds playlists reflecting your taste, trains LoRAs on what you like, and feeds the Ohm evolutionary chain for self-improvement. Notes the agent curates are handoff-ready to **Hermes Agent** for execution.

**This is the front door for the personal site:** https://southpawin.github.io/

## What's in the box

| Component | What it does | Install |
|---|---|---|
| **VA** (forked from Open-LLM-VTuber) | Live2D desktop companion, voice in/out, chat log persistence | `./scripts/install.sh && ./scripts/run-assistant.sh` |
| **Omni VA curator** | Headless Hermes profile: web, fetch, notes, social. Writes to `~/wiki/pet-curated/`. | `hermes profile install github.com/SouthpawIN/nous-girl-agent/agent --name evolutionary-radio` |
| **Senter triage** | On-demand prioritization tier. Reads wiki, returns ranked list. | `hermes profile install github.com/SouthpawIN/nous-girl-agent/agent/senter --name senter` |
| **OmniStep Evolution Radio** | Perpetual radio plugin. Self-evolving playlists. LoRAs. Ohm chain. | `./scripts/run-radio.sh start` |
| **Model catalog** | Hand-curated YAML of local + API + auxiliary models. | Edit `models/curated.yaml` |
| **Wiki handoff** | Shared library for VA ↔ Hermes main. | `wiki-handoff/wiki_handoff.py` |
| **Eikons** | Live2D sprite library. Omni VA is default. | `assistant/sprites/` |
| **Launchers** | `install.sh`, `dev.sh`, `run-assistant.sh`, `run-radio.sh`, `run-agent.sh` | `scripts/` |

## Quick start

```bash
# 1. Clone
git clone https://github.com/SouthpawIN/nous-girl-agent
cd nous-girl-agent

# 2. Install
./scripts/install.sh

# 3. Run everything (VA + radio + agent + bridge, with logs)
./scripts/dev.sh

# Or run individually:
./scripts/run-assistant.sh     # the Live2D VA
./scripts/run-radio.sh start  # the radio plugin
./scripts/run-agent.sh   # the curator agent
```

## The two-tier architecture

```
┌─────────────────────────────────────────────────────────────┐
│ Tier 1 — VA (Omni VA)                              │

*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics-wiki/nous-community/README|nous-community]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
