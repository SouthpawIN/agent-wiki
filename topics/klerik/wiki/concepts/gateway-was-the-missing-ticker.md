---
title: Gateway was the missing ticker (root cause of "loop never ticks": klerik/paladin/looker had no gateway; now auto-installed on cron create)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [infra, loop, bot, pain, decision]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# Gateway was the missing ticker

**Definition.** A Hermes cron job fires only if that profile's gateway process is running; `hermes cron create` registers the job but does not start anything that will tick it. On 2026-09-05 three fleet bots — klerik, paladin, looker — had no gateway at all, so every loop approved onto them was registered and permanently silent. The 18:58 close-out names this as the root cause and the fix: "Root cause of 'loop never ticks' found and fixed: klerik/paladin/looker had no gateway, so no cron could ever fire." ^[raw/inbox/2026-09-05.md] The fix is in the approve wire: "gateway auto-installed if that profile had none." ^[raw/inbox/2026-09-05.md]

**How it surfaced.** The symptom was recorded across three compiles of [[topics/klerik/wiki/entities/klerik-queue-drain-loop|klerik-queue-drain]]: `cron list` printing "⚠ Gateway is not running — jobs won't fire automatically", `cron runs` empty, `LIVE` flag set anyway. The 18:47 stand-up still called it "proven: live" while it had zero runs ([[topics/klerik/wiki/comparisons/claimed-completed-vs-verified-on-disk|Claimed completed vs verified on disk]]). Between 18:48 and 18:50 a gateway appeared for klerik and the job fired at 18:50:25.

**Evidence at 19:07 (this compile).** `~/Library/LaunchAgents/` contains `ai.hermes.gateway-klerik.plist`, `ai.hermes.gateway-looker.plist`, `ai.hermes.gateway-paladin.plist`; `launchctl list` shows all three running (pids 5306, 5634, 5635). klerik's `cron runs e6e20c22e1b9` → one `completed` execution at 18:50:25 and an output file at 18:56:40. klerik also carries a second job, `7a2ec814f125 fleet-tick every 15m` (last run 19:00:05) — not filed in raw, present on disk.

**Why this was the real fix and not a band-aid.** Chris's rule is root causes, never band-aids. The candidate band-aids were all pitched and swept as [[topics/klerik/wiki/concepts/build-process-chatter|build-process chatter]]: "gateway-up-first-tick" (bring the gateway up once), "first-tick-witness" (have looker watch for a tick). Neither would stop the next bot from being born gateway-less. Installing the gateway *as part of* cron create on the owning bot makes the class of failure impossible for every future loop — which is exactly what the 18:55 approval of two more loops was meant to exercise ([[topics/klerik/wiki/decisions/2026-09-05-approve-two-kept-loops-via-real-path|Approve the two kept loops via the real path]]).

**Remaining proof gap.** paladin's and looker's gateways run, but their jobs have not ticked yet (looker's is 2-hourly; paladin's 30-minute job was created ~18:55 and shows no run at 19:07 — first tick expected ~19:25). Tracked in [[topics/klerik/wiki/queries/did-the-kept-loops-tick|Did the two kept loops tick?]].
