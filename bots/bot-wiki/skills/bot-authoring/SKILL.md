---
name: bot-authoring
description: Create or reshape a bot that owns one topic.
version: 1.0.0
author: Klerik
license: MIT
metadata:
  hermes:
    tags: [bots, wiki, schema, authoring]
---

# Bot authoring

Use when Chris names a new project, or an existing bot has drifted into two
missions.

## Procedure

1. **Name it.** One kebab-case slug (the topic) and one callsign (the entity).
   `pocketshop` / `Binder`. The callsign is for conversation; the slug is for paths.
2. **Write the mission as an outcome**, not a task list. Bad: "scan cards, price
   cards, list cards." Good: "every card in the four boxes is listed or binned,
   and no listing goes live without Chris's click."
3. **List the hold points before the skills.** What may this bot never do alone?
   If the answer is "nothing", the bot is dangerous — find the real hold point.
4. **Seed exactly three skills.** One for the main loop, one for the expensive
   step, one for recovery. More than three at birth means the mission is unclear.
5. **Seed at most one loop**, and leave it `state: spec` until a manual run
   passes. Loops that were never run by hand fail silently forever.
6. **Write `Needs from Chris` as decisions**, not requests for permission.
   Bad: "need access to eBay." Good: "eBay OAuth: run `get_ebay_token.py` on
   omarchy and paste the refresh token into `.env`."
7. **Register it** in `bots/_fleet/FLEET.md` and add one `[BOTS]` line nowhere —
   the bot is live in the index the moment its BOT.md exists.
8. **Validate**: `python -m senter_agent . --json` parses it; the slug in
   frontmatter equals the directory name.

## Shape check (fail any → rewrite)

- [ ] Could a fresh agent start work from BOT.md alone? (names paths, commands, accounts)
- [ ] Does every skill name a trigger and a stop condition?
- [ ] Is each loop bound to a skill and a schedule?
- [ ] Is every blocker one line with an exact action?
- [ ] Public-facing copy says **sovthpaw**?

## Anti-patterns

- A bot whose skills describe its domain instead of instructing an executor.
- A "misc" bot. Split it.
- A loop with no stop condition — it will run until it costs money.
- BOT.md longer than ~120 lines: the excess belongs in a skill or in continuity.
