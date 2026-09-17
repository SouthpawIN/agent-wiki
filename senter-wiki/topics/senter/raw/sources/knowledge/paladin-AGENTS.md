# Paladin — Agent Workflows (created by klerik 2026-09-02 per Chris via senter)

## Working a topic queue (CLAIM v2)
Bots work OUT OF TOPICS; multiple instances of the same bot may run the same topic queue in
parallel. Claims use an ATOMIC primitive — not check-then-act (anser found that race):
1. **Claim = mkdir.** Before starting an item:
   `mkdir "$C/$ITEM" 2>/dev/null && (echo "$BOT $$ $(date -u +%FT%TZ)" > "$C/$ITEM/owner"; touch "$C/$ITEM/heartbeat") || skip`
   where `$C = topics/<topic>/.system/claims` and `$ITEM` is the item id. mkdir is atomic on
   POSIX: success means YOU own it; `EEXIST` means someone else owns it — skip to the next
   unclaimed item. Never touch another instance's claim dir.
2. **Heartbeat.** Touch `$C/$ITEM/heartbeat` every 60s while working.
3. **Reaper.** A claim whose heartbeat is older than 10 min is stale; any instance may
   `rm -r` it and re-claim. Crashed instances never block an item for good.
4. **queue.md is the LOG, not the lock.** Append `CLAIM/DONE/BLOCKED <item> <bot> <ts>` lines
   for humans. The directory is the lock; the line is the record.
5. **On finish:** write `result` (done|blocked + one line) into the claim dir, append
   `DONE <item>` or `BLOCKED <item> <why>` to queue.md, then `rm -r` the claim dir.
6. All outcome writes go to the topic's `.system/session.md` under a dated heading
   (`## YYYY-MM-DD`), append-only — never rewrite or reorder existing entries.

## Done signal
The LAST line of every reply is exactly one of:
- `DONE — <one line: what shipped, what verified it>`
- `BLOCKED — <why, what's needed>`
- `NEEDS-CHRIS — <the question>`
Never end a turn without it. Also POST it to the bridge:
`curl -s -X POST "http://127.0.0.1:8643/post?token=$(cat ~/.hermes/senter-bridge/token)" -d '{"bot":"paladin","text":"DONE — …","status":"done"}'`