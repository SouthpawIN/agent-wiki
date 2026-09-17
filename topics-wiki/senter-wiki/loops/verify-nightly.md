# Loop: verify-nightly (owner: weaver · cron)

Nightly regression pass over the live Senter Wiki build.

## What runs
1. Run the regression ledger against the live build:
   `node ~/Documents/Projects/Projects/assets/verify-wiki.js`
2. If the ledger passes clean: done-post to bridge, nothing else.
3. If any assertion fails (regression): for EACH failing assertion —
   - Append to `topics-wiki/senter-wiki/.system/queue.md` as a `[FIXES]` item:
     `- <assertion name>: <measured failure> (ledger <date>)`
   - CLAIM the item per `## Working a topic queue` before fixing it.
4. Done-post to bridge:
   `curl -s -X POST "http://127.0.0.1:8643/post?token=$(cat ~/.hermes/senter-bridge/token)" -d '{"bot":"weaver","text":"DONE — verify-nightly: N assertions passed / M regressions filed","status":"done"}'`
   (use status "blocked" + BLOCKED line if the ledger itself cannot run).

## Cron line (proposed — senter/Chris to register)
`hermes -p weaver chat -q "Run the verify-nightly loop: read topics-wiki/senter-wiki/triggers-loops/verify-nightly.md and execute it against the live build."`
Schedule: nightly, off-peak (e.g. cron `30 3 * * *` local time).
Note: cron sessions run in-process (no -q argv) → senter-bridge does not arm → the
protected-write card path does not apply; queue/session writes are vault files, not
protected instruction files.


## Registered 2026-09-02
Cron job `654c28d3c385` (senter profile) · `30 3 * * *` · spawns weaver -q with this file as the brief. First run 2026-09-03 03:30 CDT. NOTE: fires only while the Hermes gateway is running (`hermes gateway start`) — gateway was not running at registration.
