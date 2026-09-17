---
title: Bot naming convention — remove .md extension from display names
created: 2026-09-08
updated: 2026-09-09
type: entity
tags: [ui, bot, decision, completed]
sources:
  - raw/inbox/2026-09-08.md
confidence: high
---

# Bot naming convention

## Problem
Bot names were displaying with `.md` extensions in the UI: `librarian-bot.md` instead of `librarian-bot`.

> "Remove `.md` extension from bot names in the senter-wiki topic (e.g., `librarian-bot.md` should be `librarian-bot`)."
> ^[raw/inbox/2026-09-08.md]

## Root cause
The `scan_bots()` function reads `.md` files in the `bots/` directory and uses the filename (including extension) as the bot's display name. The UI layer (`renderBots` / `mkTopic`) was also not stripping the extension when generating labels.

## Resolution
The bot name display logic now strips the `.md` extension so bots appear as `librarian-bot`, `senter-wiki-bot`, etc. — not `librarian-bot.md`.
^[raw/inbox/2026-09-08.md]

## See also
- [[topics/senter-wiki/wiki/entities/fleet-bots|Fleet bots]]
- [[topics/senter-wiki/wiki/entities/senter-wiki-topic-folder|Senter-wiki topic folder]]
- [[topics/senter-wiki/wiki/concepts/librarian-progressive-disclosure|Librarian]]
