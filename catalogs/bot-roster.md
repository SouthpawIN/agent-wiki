---
title: Bot Roster
created: 2026-11-07
updated: 2026-11-07
type: catalog
tags: [bots, registry, hermes, profiles]
---

# Bot Roster

Every bot, its Hermes profile, and its state. A bot **is** a profile — the wiki
`BOT.md` is the design doc, `~/.hermes/profiles/<slug>/` is the runtime.

| Bot | Callsign | Hermes profile | Status | Loops |
|---|---|---|---|---|
| [[bots/bot-wiki/BOT\|bot-wiki]] | Klerik | `bot-wiki` | live | 1 live |
| [[bots/hermes/BOT\|hermes]] | Mesh | `hermes` | seeding | 0 live |
| [[bots/turbofit/BOT\|turbofit]] | TurboSouth | `turbofit` | seeding | 0 live |
| [[bots/pocketshop/BOT\|pocketshop]] | Binder | `pocketshop` | seeding | 0 live |
| [[bots/youtube/BOT\|youtube]] | Cutroom | `youtube` | seeding | 0 live |
| [[bots/anser/BOT\|anser]] | Anser | `anser` | seeding | 0 live |
| [[bots/kart-racer/BOT\|kart-racer]] | Apex | `kart-racer` | seeding | 0 live |
| [[bots/ai-daw/BOT\|ai-daw]] | Riff | `ai-daw` | seeding | 0 live |
| [[bots/ssi/BOT\|ssi]] | Beacon | `ssi` | blocked | 0 live |

## Provisioning a bot

```bash
hermes profile create <slug> --description "<mission, one line>"
# install skills from bots/<slug>/skills/*/SKILL.md
# routines from bots/<slug>/loops/*.md
hermes -p <slug> chat -q "what is your mission"
```

See [[bots/hermes/skills/bot-mode-profiles/SKILL|bot-mode-profiles]] for the full
procedure, and [[BOT_SCHEMA|BOT_SCHEMA]] for what a bot must contain.

## Archive

A paused or retired bot stays in `bots/` with `status: paused` and a closing log
line. Nothing is deleted; the reason survives.
