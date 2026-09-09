---
type: loop
name: player-regression-check
schedule: 2h
proposed: 2026-09-05 18:27
---
# player-regression-check
owner: looker · cadence: on change to vault-live.html or the bridge source (event-driven, no polling) · status: LIVE
**Want looker to re-run the player checks (volume-on-load, mute, EQ, seek) every time vault-live.html or the bridge changes, so the iframe→bridge kind of regression can't sneak back?**

## Prompt
Capture Chris's window, run the five player checks from the player-verify SOUL, post a one-line pass/fail with capture path to topics/youtube/log.md; on fail, file a defect card to the youtube topic queue

## Evidence
> the new `<audio>` element is created at volume 1.0 — `applyVol` only runs when you move the rocker, so a freshly loaded track ignores your level until you touch it

## Applied 2026-09-05 18:56
`hermes -p looker cron create "2h" --name player-regression-check` → ok
Created job: 95e13093ff26
  Name: player-regression-check
  Schedule: every 120m
  Workdir: /Users/sovthpaw/Documents/Projects/Projects
  Next run: 2026-09-05T20:56:31.904141-05:00
