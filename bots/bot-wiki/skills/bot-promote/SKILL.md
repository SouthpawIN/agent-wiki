---
name: bot-promote
description: Move a bot from seeding to live after its loop passes by hand.
version: 1.0.0
author: Klerik
license: MIT
metadata:
  hermes:
    tags: [bots, loops, promotion]
---

# Bot promotion

A bot is `seeding` until its loop has been executed manually end-to-end once,
with output Chris can look at.

## Gate

Run the loop's procedure by hand. It must:

1. Produce an artifact at a path the BOT.md predicted, not somewhere new.
2. Be idempotent — a second run changes nothing or appends one line.
3. Fail loudly — break an input on purpose and confirm it reports, not guesses.
4. Cost nothing unexpected — check `hermes cron list` for the interval and the
   model it will use.

## Then

1. `state: spec` → `state: live` in the bot's `## Loops` table.
2. Arm it: `cronjob_manage` create with the schedule from `loops/<slug>.md`,
   prompt = that file's `## Prompt` body verbatim.
3. `status: seeding` → `status: live` in frontmatter and `FLEET.md`.
4. Log one line: schedule, first fire time, what it will write.

## Demotion

If a live loop fails twice in a row, demote it to `spec`, do not "fix it in
prod". State the failing invocation in the log.
