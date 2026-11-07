---
type: loop
slug: corpus-refresh
bot: anser
schedule: "30 7 * * *"
state: spec
skill: x-corpus-refresh
created: 2026-11-07
---

# corpus-refresh

Daily 07:30. Keeps Anser's grounding current.

## Prompt

Run `x-corpus-refresh` for @NousResearch and @Teknium. Report only the count of
new posts and the newest timestamp. If the API fails, set `stale: true` and inject
one line so answers stop pretending to be current.

## Stop condition

One pass. On auth failure, stop for the day — repeated failures get throttled.
