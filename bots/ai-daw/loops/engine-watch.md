---
type: loop
slug: engine-watch
bot: ai-daw
schedule: "0 9 1 * *"
state: spec
skill: music-model-adapter
created: 2026-11-07
---

# engine-watch

Monthly, 1st at 09:00. Watches for music models worth adapting.

## Prompt

Check for new releases or major version bumps in the engines table in
`bots/ai-daw/engines.md`. For any real candidate, run the 6-prompt fixed eval and
append a row with scores. Adopt nothing automatically — recommend, with numbers.

## Stop condition

Skip months where nothing changed. Never download multi-GB weights from a cron
job; the eval runs interactively.
