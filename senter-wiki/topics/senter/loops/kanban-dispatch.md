# Loop: kanban-dispatch (owner: senter · hermes kanban)
Task hand-off across the fleet: claim → heartbeat → comment → complete/attach, reaped on stale.

## Native home (verified 2026-09-04)
`hermes kanban` — claim is a SQLite CAS (`kanban_db.py:2100`), `release_stale_claims` (`:2283`), 14 `kanban_*` agent tools. Dispatcher runs inside the gateway (`kanban daemon` deprecated).

## Replaces
CLAIM v2: mkdir claims dir, 60 s heartbeat file, 10-min reaper, `queue.md` log, bridge `/post` done-lines.

## Defaults that differ
claim TTL 15 min (env `HERMES_KANBAN_CLAIM_TTL_SECONDS` only) · heartbeat-stale 1 h (hardcoded) · `kanban.dispatch_stale_timeout_seconds` 4 h.

## Cadence
Continuous (gateway). Board is empty today → nothing to migrate, but every bot prompt (looker AGENTS.md etc.) must be rewritten.

## Status
[ADOPTED 2026-09-05] The kanban dispatcher is the fleet's PRIMARY spawn path (council items 1+5; policy: [[topics/senter/process/spawn-policy]]). `senter-bridge/dispatch.py` routes items through `hermes kanban create --assignee <bot>`; direct `hermes chat -q` spawn survives only as the documented emergency hatch (`SENTER_EMERGENCY_SPAWN=1` or manual, §2 of the policy). CLAIM v2 + sentinel RETIRED 2026-09-05 (t_f1b1eba1): sentinel daemon unplugged, sentinel.py deleted, CLAIM sections replaced in all builder/looker AGENTS.md.
