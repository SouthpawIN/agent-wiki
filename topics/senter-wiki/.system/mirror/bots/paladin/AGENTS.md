# Paladin — Agent Workflows (created by klerik 2026-09-02 per Chris via senter)

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
`curl -s -X POST "http://127.0.0.1:8643/post?token=$(cat ~/.hermes/senter-bridge/token)" -d '{"bot":"paladin","text":"DONE — …","status":"done"}'`