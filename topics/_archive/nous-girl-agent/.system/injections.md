# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: nous-girl-agent
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/nous-girl-agent-155b6655f4.md"]
confidence: medium
---

# nous-girl-agent

## Current context

Nous Girl agent + OmniStep Evolution Radio plugin — curated local model pet, multimodal by default, voice + music from the model # Omni VA **The desktop VA, the local model server, the OmniStep Evolution Radio, the curator agent, the Senter triage profile — all in one stack.** > TOWARDS SELF-IMPROVEMENT · curated by mu A standalone, voice-interactive, ever-evolving desktop VA that serves as a **curated local-model server manager**. The VA is the face of the model — voice and music come *from the model itself*, with a graceful fallback to Edge TTS and curated playlists when you swap to a text-only LLM. The **OmniStep Evolution Radio** lives as a plugin inside the agent. It's a perpetual radio that watches what you engage with, builds playlists reflecting your taste, trains LoRAs on what you like, and feeds the Ohm evolutionary chain for self-improvement. Notes the agent curates are handoff-ready to **Hermes Agent** for execution. **This is the front door for the personal site:** https://southpawin.github.io/ --- ## What's in the box | Component | What it does | Install | |---|---|---| | **VA** (forked from Open-LLM-VTuber) | Live2D desktop companion, voice in/out, chat log persistence | `./scripts/install.sh && ./scripts/run-assistant.sh` | | **Omni VA curator** | Headless Hermes profile: web, fetch, notes, social. Writes to `~/wiki/pet-curated/`. | `hermes profile install github.com/SouthpawIN/nous-girl-agent/agent --name evolutionary-radio` | | **Senter triage** | On-demand prioritization tier. Reads wiki, returns ranked list. | `hermes profile install github.com/SouthpawIN/nous-girl-agent/agent/senter --name senter` | | **OmniStep Evolution Radio** | Perpetual radio plugin. Self-evolving playlists. LoRAs. Ohm chain. | `./scripts/run-radio.sh start` | | **Model catalog** | Hand-curated YAML of local + API + auxiliary models. | Edit `models/curated.yaml` | | **Wiki handoff** | Shared library for VA ↔ Hermes main. | `wiki-handoff/wiki_handoff.py` | | **Eikons** | Live2D sprite library. Omni VA is default. | `assistant/sprites/` | | **Launchers** | `install.sh`, `dev.sh`, `run-assistant.sh`, `run-radio.sh`, `run-agent.sh` | `scripts/` | --- ## Quick start --- ## The two-tier architecture Three tiers, actually: **Omni VA (curation) → Senter (prioritization) → Hermes main (execution)**. Senter sits between curation and execution as an on-demand triage step. ---…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/nous-girl-agent` (`2026-07-09T00:04:27Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/creative-music|Creative Music]]
- [[concepts/local-inference|Local Inference]]
- [[concepts/model-merging-training|Model Merging Training]]
