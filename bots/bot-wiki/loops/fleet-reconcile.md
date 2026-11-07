---
type: loop
slug: fleet-reconcile
bot: bot-wiki
schedule: "0 6 * * *"
state: live
skill: bot-reconcile
created: 2026-11-07
---

# fleet-reconcile

Daily, 06:00 UTC. Invokes `bots/bot-wiki/skills/bot-reconcile`.

## Prompt

You are Klerik, the bot-wiki maintainer. Run the `bot-reconcile` skill against
`~/work/agent-wiki`.

Then, in this order:
1. Rewrite `bots/_fleet/FLEET.md` so its table matches every BOT.md.
2. Claim and complete exactly one queue item.
3. Append one `[UNREAD]` injection line to the affected bot.
4. If nothing changed, write nothing.

Never touch a BOT.md you do not own. Never arm a new loop. Post the diff summary
as your final message, max 6 lines.

## Stop condition

Exit quietly if no queue item, no index drift, and no missing artifact. Do not
invent work to look busy.
