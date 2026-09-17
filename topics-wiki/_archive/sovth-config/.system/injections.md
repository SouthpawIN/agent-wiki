# Injections

## [READ]

== absorbed from senter idea-wiki (2026-08-28) ==
---
title: sovth-config
created: 2026-07-12
updated: 2026-07-12
type: entity
tags: [entity, idea-capture, provenance]
sources: ["raw/github/sovth-config-4cb70f7f59.md"]
confidence: medium
---

# sovth-config

## Current context

Southpaw's hermes-agent config toolkit: /reading-list deep-research plugin, profile character cards, ^<profile> background invocation. Distributable, universal, shareable. # 🎴 sovth-config > **An opinionated configuration for [Hermes Agent](https://github.com/NousResearch/hermes-agent).** > Distributable profiles, skills, and tools — curated, battle-tested, and kept updated with everything useful we make. **TOWARDS SELF-IMPROVEMENT** --- ## What is this? `sovth-config` is an opinionated configuration layer for [Hermes Agent](https://github.com/NousResearch/hermes-agent) — the self-improving AI agent built by [Nous Research](https://nousresearch.com). It provides a curated collection of agent profiles, skills, and plugin tools that extend Hermes with deep-research, profile management, and multi-agent orchestration capabilities. This repo is kept updated with new profiles and skills as we build them. Anything useful enough to share lands here. If it's not useful, it doesn't make the cut. ### What's inside | Layer | What it does | |-------|-------------| | **Profiles** | Character cards + profile configs for a multi-agent fleet — editors, researchers, triage orchestrators, builders, and more. Each card is a game-style README with stats, lore, and import instructions. | | **Skills** | Shareable Hermes Agent skills. First up: **turbofit** — an opinionated unified LLM backend that picks the best main + aux model for your hardware, launches them, and wires Hermes config automatically. | | **Plugin Tools** | Three (soon four) Hermes Agent plugin tools: `/reading-list` (deep-research wiki generator), `/character_card` (profile card generator), `^<profile>` (background profile invocation), and the upcoming `skill_market` (self-improving suggestion engine). | --- ## Install ### Quick install (one command) The plugin will be picked up automatically by Hermes on next launch. Verify with: ### Import profiles ### Install the turbofit skill --- ## The Profile Fleet Character cards for a multi-agent ecosystem. Each is a game-style README — Name, Class, Stats, Skills, Lore, and a one-page import tutorial. | Profile | Class | Role | |---------|-------|------| | **`klerik`** | Profile Editor | Meta-agent that reviews and surgically corrects other Hermes agent profiles. Uses DSPy + GEPA for prompt optimization. | | **`anser`** | Tech Support + Planner | Discord tech support.…

## Version policy

The latest available update marker is canonical: `https://github.com/SouthpawIN/sovth-config` (`2026-07-11T18:21:58Z`). Earlier captures remain linked in the raw source inventory.

## Related concepts

- [[concepts/agent-fleet|Agent Fleet]]
- [[concepts/model-merging-training|Model Merging Training]]
