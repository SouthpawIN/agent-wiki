# Dogeman — Agent Workflows (verification standard, added 2026-09-02 per Chris via klerik)

## Verify (LOOK loop)
After EVERY change that produces a visible artifact (thumbnails, visuals, scripts rendered

**LOOK step is a SERVICE: call looker.** Spawn the looker profile (it owns looking, never
fixing) and hand it: the artifact path, the ask restated as a YES/NO question + measurable
offset, and real-window context. It returns a short verdict report (PASS/FAIL/FAIL-
CONVERGENCE + measured px offsets + screenshot paths). Act on the verdict yourself — fix,
re-ask, max 3 passes, then BLOCKED with the offsets looker reported.
for review), run the `bot-verify-loop` skill (fleet standard):
1. Numeric probes first (lint, parse) — necessary, not sufficient.
2. Screenshot at the user's real Hermes window size (computer_use app=Hermes) AND at a
   fixed reference size (1280x800).
3. vision_analyze with the ask restated as a yes/no question + measured offset.
4. Fix and loop — max 3 passes. Unconverged after 3 → report BLOCKED with measured offsets.

## Working a topic queue (kanban)
Bots work OUT OF TOPICS; the kanban dispatcher is the only spawn path (spawn-policy.md).
The board replaces the old mkdir-claim protocol — no claim dirs, heartbeats, or reaper.
1. **Claim = your card.** Work the kanban cards assigned to you (the kanban_* tools). The
   dispatcher owns assignment and stale-claim reclaim; never take another bot's card.
2. **One card, one instance.** Parallel instances get parallel cards — no shared-file
   locks to coordinate.
3. **queue.md is the LOG, not the lock.** Append `DONE <item>` / `BLOCKED <item> <why>`
   lines for humans; the board is the state of record.
4. **On finish:** `kanban_complete` (summary + metadata), or `kanban_block` with a reason
   when genuinely stuck — never just stop.
5. All outcome writes go to the topic's `.system/session.md` under a dated heading
   (`## YYYY-MM-DD`), append-only — never rewrite or reorder existing entries.

## Done signal
The LAST line of every reply is exactly one of:
- `DONE — <one line: what shipped, what verified it>`
- `BLOCKED — <why, what's needed>`
- `NEEDS-CHRIS — <the question>`
Never end a turn without it. Also POST it to the bridge:
`curl -s -X POST "http://127.0.0.1:8643/post?token=$(cat ~/.hermes/senter-bridge/token)" -d '{"bot":"dogeman","text":"DONE — …","status":"done"}'`

## Tooling
All file/vault writes use the file tools (`write_file`/`patch`). Never: inline interpreter flags (`-c`/`-e` on any interpreter — python, python3, node, any venv path), pipe-to-interpreter (`… | python3`), heredoc-to-interpreter (`python3 <<EOF`), or shell appends (`>>`, `tee`) to vault/profile files. For logic, save a script file (`assets/*.py`) and run it by path. WHY: each of those patterns generates an approval card Chris must click — 96 today.
