---
type: loop
slug: roster-sync
bot: kart-racer
schedule: "0 8 * * 1"
state: spec
skill: nrcu-roster-import
created: 2026-11-07
---

# roster-sync

Weekly. Detects new or updated NRCU characters and stages them for the game.

## Prompt

Diff the NRCU `characters/` directory against `Assets/Roster/roster.json`. New
character → add an entry with derived stats and `"locked": false`, and inject one
line naming it. Changed art → refresh the portrait and note it. Never modify a
locked entry. Never ship uncredited art.

## Stop condition

If the NRCU repo is unreachable, stop; do not fabricate roster entries.
