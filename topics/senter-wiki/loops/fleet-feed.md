# Loop: fleet-feed (owner: senter · hermes kanban watch)
Streams bot task-lifecycle events (completed, blocked, gave_up, crashed, timed_out, needs_input) into the bottom-corner feed.

## Native home (verified 2026-09-04, Anser turn 7)
`hermes kanban watch --kinds completed,blocked,gave_up,crashed,timed_out` (board-wide task_events, 0.5 s poll) and the kanban dashboard `WS /events?since=`.
`hermes kanban block --kind needs_input` = NEEDS-CHRIS.

## Replaces
cron `senter-fleet-feed` every 2 min + bridge SSE for status cards. Free-form chatter has NO cross-profile tail in Hermes — only task-lifecycle events; that is the feed's real content anyway.

## Cadence
Continuous watcher. Dispatcher lives in the gateway → `hermes gateway start` must be on.

## Status
DONE 2026-09-05 — CLAIM v2 → kanban migration complete (t_f1b1eba1); `hermes kanban watch` + fleet-tick (cron 7a2ec814f125) supersede this loop.
