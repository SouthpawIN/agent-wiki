---
name: bot-mode-profiles
description: Turn each wiki bot into a live Hermes Bot (profile) with routines.
version: 1.0.0
author: Mesh
license: MIT
metadata:
  hermes:
    tags: [hermes, bots, profiles, routines]
---

# Bot mode profiles

A Bot **is** a profile. Bot Mode is a UI over `~/.hermes/profiles/<name>/`, so
every bot here has a CLI twin and a cron twin.

## Procedure

1. **Create the profile** per bot:
   ```bash
   hermes profile create youtube --description "Cutroom — recordings to YouTube"
   ```
   Slug = wiki slug. Never rename one later without `hermes profile rename`.
2. **Install its skills** into that profile's skills dir, taken from
   `bots/<slug>/skills/*/SKILL.md`. The wiki is the source of truth; the profile
   is a deployed copy.
3. **Write the profile's SOUL/AGENTS identity** from `BOT.md`: mission, hold
   points, and the interface skill. Keep it under ~40 lines — the BOT.md has the rest.
4. **Wire routines** from `bots/<slug>/loops/*.md`: schedule = frontmatter,
   prompt = the loop's `## Prompt` body verbatim. Verify with `hermes cron list`.
5. **Avatar + section** in the Bots tab: one section per area (Media, Commerce,
   Infra, Personal).
6. **Verify parity**: `hermes -p <slug> chat -q "what is your mission"` returns the
   BOT.md mission, and the routine appears beside the Bot Chat.
7. **Keep memory per bot.** Do not share one memory across all nine — that is what
   made the topic-first wiki unreadable. Cross-bot facts go in `_fleet/`.

## Rules

- A bot without a hold-point list does not get a profile. It gets a rewrite.
- Routines that spend money are created disabled, always.
- `hermes cron list` is the audit surface; the wiki loop file is the spec.
