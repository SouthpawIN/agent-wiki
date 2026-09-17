---
title: sovth-config
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/sovth-config
status: dormant
tags: [repo]
---

# sovth-config

> Southpaw's hermes-agent config toolkit: /reading-list deep-research plugin, profile character cards, ^<profile> background invocation. Distributable, universal, shareable.

**[Open on GitHub](https://github.com/SouthpawIN/sovth-config)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 17 / 2
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-10 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# 🎴 sovth-config

> **An opinionated configuration for [Hermes Agent](https://github.com/NousResearch/hermes-agent).**
> Distributable profiles, skills, and tools — curated, battle-tested, and kept updated with everything useful we make.

**TOWARDS SELF-IMPROVEMENT**

## What is this?

`sovth-config` is an opinionated configuration layer for [Hermes Agent](https://github.com/NousResearch/hermes-agent) — the self-improving AI agent built by [Nous Research](https://nousresearch.com). It provides a curated collection of agent profiles, skills, and plugin tools that extend Hermes with deep-research, profile management, and multi-agent orchestration capabilities.

This repo is kept updated with new profiles and skills as we build them. Anything useful enough to share lands here. If it's not useful, it doesn't make the cut.

### What's inside

| Layer | What it does |
|-------|-------------|
| **Profiles** | Character cards + profile configs for a multi-agent fleet — editors, researchers, triage orchestrators, builders, and more. Each card is a game-style README with stats, lore, and import instructions. |
| **Skills** | Shareable Hermes Agent skills. First up: **turbofit** — an opinionated unified LLM backend that picks the best main + aux model for your hardware, launches them, and wires Hermes config automatically. |
| **Plugin Tools** | Three (soon four) Hermes Agent plugin tools: `/reading-list` (deep-research wiki generator), `/character_card` (profile card generator), `^` (background profile invocation), and the upcoming `skill_market` (self-improving suggestion engine). |

## Install

### Quick install (one command)

```bash
git clone https://github.com/SouthpawIN/sovth-config.git
ln -s $(pwd)/sovth-config/sovth_config ~/.hermes/plugins/sovth-config
```

The plugin will be picked up automatically by Hermes on next launch. Verify with:

```bash
hermes plugins
# should list: sovth-config
```

### Import profiles

```bash
# Import the whole roster (or just the ones you want)
for d in sovth-config/profiles/*/; do
    name=$(basename "$d")
    [ "$name" = "README.md" ] && continue
    ln -s "$(pwd)/$d" ~/.hermes/profiles/"$name"
done

# Or pick a few:
ln -s $(pwd)/sovth-config/profiles/klerik ~/.hermes/profiles/klerik
ln -s $(pwd)/sovth-config/profiles/nous-girl ~/.hermes/profiles/nous-girl

# Launch one
hermes -p klerik
```

### Install the turbofit skill

```bash
# If turbofit is bundled as a skill directory:
ln -s $(pwd)/sovth-config/skills/turbofit ~/.hermes/skills/turbofit

# Source the serve shim (one-time, already in ~/.bashrc after install)

*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics/hermes-agent/README|hermes-agent]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
