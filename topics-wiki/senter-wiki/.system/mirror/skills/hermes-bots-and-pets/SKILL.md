---
name: hermes-bots-and-pets
description: Use when creating Hermes bot profiles or custom pets.
version: 1.0.0
author: turbosovth
license: MIT
tags: [hermes, bots, pets, profiles, wiki]
---

# Hermes Bots & Pets — Creator Studio

Build persistent Hermes bot profiles (isolated `~/.hermes/profiles/<name>/`) that act as specialist collaborators: their own SOUL.md, memory, skills, cron, and desktop chat. Attach custom pets (spritesheets) from anywhere — including GitHub — not just the petdex gallery.

## When to Use
- User says "new bot", "create a bot", "Agent-Wiki function", wants a named helper
- Pet from a GitHub URL (`github.com/<org>/hermes-pets/tree/main/<slug>`) or local spritesheet
- Creator-studio pattern: rant → wiki continuity → script → video (backgrounds / Shorts / cutscenes) → viral tuning

## Quick Workflows

### 1) Create a Bot Profile
```bash
hermes profile create <bot-name>            # isolated profile under ~/.hermes/profiles/<bot-name>/
# then customize:
# ~/.hermes/profiles/<bot-name>/SOUL.md  — persona, role, rules
# ~/.hermes/profiles/<bot-name>/workspace/{wiki,rants,scripts,shorts,cutscenes,trends,voice-inbox}
# ~/.hermes/profiles/<bot-name>/skills-capabilities/<topic>/SKILL.md — per-bot skills
```
Talk to it: `hermes -p <bot> chat` or `<bot> chat` wrapper. Routines are cron jobs `[bot:<name>]` that land in the bot's canonical chat.

### 2) Install a Custom Pet (beyond `hermes pets install`)

`hermes pets install <slug>` only fetches from the bundled petdex gallery (4672 entries). For a GitHub-hosted pet (e.g. `Adolanium/hermes-pets/123mikeyd`):

```bash
# 1. Fetch manifest + spritesheet via raw.githubusercontent
curl -sL "https://raw.githubusercontent.com/<org>/hermes-pets/main/<slug>/pet.json" -o /tmp/pet.json
curl -sL "https://raw.githubusercontent.com/<org>/hermes-pets/main/<slug>/spritesheet.webp" -o /tmp/spritesheet.webp
# also check via API: https://api.github.com/repos/<org>/hermes-pets/contents/<slug>

# 2. Place into every home that needs it
mkdir -p ~/.hermes/pets/<slug> && cp /tmp/pet.json /tmp/spritesheet.webp ~/.hermes/pets/<slug>/
mkdir -p ~/.hermes/profiles/<bot>/pets/<slug> && cp -r ~/.hermes/pets/<slug> ~/.hermes/profiles/<bot>/pets/
mkdir -p ~/.hermes/profiles/<active>/pets && cp -r ~/.hermes/pets/<slug> ~/.hermes/profiles/<active>/pets/

# 3. Activate (bypass gallery validation — use config set, not `hermes pets select`)
hermes config set display.pet.slug <slug>
hermes config set display.pet.enabled true
HERMES_HOME=~/.hermes/profiles/<bot> hermes config set display.pet.slug <slug>
HERMES_HOME=~/.hermes/profiles/<bot> hermes config set display.pet.enabled true
```
Verify: `cat ~/.hermes/profiles/<bot>/config.yaml | grep -A3 pet:` and `ls -lh ~/.hermes/profiles/<bot>/pets/<slug>/spritesheet.webp` (expect ~1–2MB webp, e.g. 1536x1872).

> Pitfall: `hermes pets select <custom-slug>` will fail with "not installed — run: hermes pets install <slug>" because it validates against the gallery. Always use `hermes config set` for custom slugs. `hermes pets show` may also report "no pet to show" — ignore if config.yaml holds the slug.

### 3) Creator-Studio Scaffold (Dogeman Pattern)

A reusable layout for rant-collecting YouTube bots that double as Agent-Wiki:

```
workspace/
  wiki/index.md          # living index + episode proposals + bible
  wiki/episodes/<ep>.md  # clustered rant groups -> thesis + beats
  wiki/bible.md          # characters, running bits, unresolved threads
  rants/YYYY-MM-DD-HHMM-<slug>.md
  scripts/<episode>.md   # cold open, hooks, beats, B-roll/cutscene cues
  shorts/  cutscenes/    # generated visuals (image_generate, comfyui, p5js, manim-video)
  trends/YYYY-MM-DD.md   # viral scout brief
  voice-inbox/           # raw audio drops
skills-capabilities/
  <bot>-rant-wiki/       # ingest -> transcribe -> tag -> cluster
  <bot>-video-foundry/   # backgrounds, 9:16 Shorts, interstitials
  <bot>-viral-scout/     # YouTube/X/RSS scans, title/thumb pattern mining
```

SOUL.md essentials: artsy voice (if requested), "never lose a rant", keep boss's voice intact, visuals support don't overwrite, explain viral tweaks with receipts/links, every artifact is a wiki page with backlinks. See `references/creator-studio-soullmd.md` for the Dogeman example.

## Support Files
- `references/custom-pet-install.md` — full transcript + sizes + API fallback for GitHub pet installs
- `references/creator-studio-soullmd.md` — Dogeman SOUL.md + workspace layout + skill stubs

## Hard Invariants
- `hermes-agent` is bundled/protected — do not patch it; this skill is the writable overlay.
- Pet spritesheets are RIFF WebP; desktop renders via file:// — copy, don't move.
- Profile names are lowercase alphanum; use `hermes profile list` to verify before create.
