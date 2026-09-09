# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: sirvir
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/sirvir-e7a312251c.md"]
confidence: medium
---

# sirvir

## Current context

Sirvir — model fleet manager & intelligence engine for Hermes Agent. Autonomous model lifecycle manager: local serving, benchmarking, auto-scaling, API fallback, HuggingFace scanning, creator tracking, backend optimization, budget monitoring. # Sirvir — Model Fleet Manager & Intelligence Engine **Sirvir** is an autonomous Hermes Agent profile that manages your entire model layer — local serving, benchmarking, auto-scaling, API fallback, HuggingFace scanning, creator quality tracking, backend optimization, token budget monitoring, and external app endpoint serving. > *TOWARDS SELF-IMPROVEMENT* --- ## Table of Contents - [What Sirvir Does](#what-sirvir-does) - [Install](#install) - [Quick Start](#quick-start) - [When to Use Sirvir](#when-to-use-sirvir) - [Example Prompts](#example-prompts) - [Commands](#commands) - [Sub-Skills](#sub-skills) - [Cron Jobs](#cron-jobs) - [Interactions with Other Agents](#interactions-with-other-agents) - [Optimization Priority](#optimization-priority) - [Hardware Tiers](#hardware-tiers) - [Profile Image](#profile-image) --- ## What Sirvir Does Sirvir is the **infrastructure owner** for your model fleet. He doesn't just serve models — he actively manages their entire lifecycle: | Responsibility | What It Means | |---------------|---------------| | **Local model serving** | Launches, wires, and monitors local llama-server instances via turbofit | | **External app endpoints** | Spins up OpenAI-compatible endpoints for ANY app, not just Hermes | | **HuggingFace scanning** | Continuously scans for new GGUF models matching your archetypes | | **Creator quality tracking** | Maintains a database of model creators and their track records | | **API model benchmarks** | Competitive intelligence on all monitored API models (local vs API) | | **Auto-backend optimization** | Tests llama.cpp / vLLM / Ollama / SGlang per model, finds the fastest | | **Token budget monitoring** | Tracks real spend from Hermes state.db against a monthly budget | | **Model suggestions** | Recommends models based on hardware, use case, and budget | | **Consolidated logging** | All activities stream to Discord, blog, and GitHub simultaneously | | **VRAM scaling** | Auto-detects pressure, walks scaling ladder, never kills mid-response | --- ## Install ### Prerequisites Sirvir requires the [turbofit](https://github.com/SouthpawIN/turbofit) skill — it's the core…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/sirvir` (`2026-07-12T21:31:22Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/local-inference|Local Inference]]
- [[concepts/model-merging-training|Model Merging Training]]
