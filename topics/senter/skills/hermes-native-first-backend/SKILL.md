---
name: hermes-native-first-backend
description: Use when a Senter backend piece is custom code. Go native.
version: 0.1.0
distilled: 2026-09-05 19:17
topic: senter
---
# hermes-native-first-backend
Rule: every custom backend piece must either name the Hermes built-in that replaces it (then retire the code) or name the exact missing Hermes capability (then file a PR-ledger entry). Inventory the flow as part → runs as → markdown; check docs/`hermes --help`/anser before assuming absence; move behaviour into SOUL/AGENTS/cron/skill markdown when native exists. UI is exempt — backend only. Intelligence (rewrite/pitch/apply) stays in hermes chat/cron/profile; only plumbing may be custom. Current custom-with-reason: watcher (no per-message hook), cutter (no classify primitive), bridge (no SSE/file proxy).

## Evidence
> If there's a way that we can get this entire flow down to just built in Hermes commands and markdown, that would be great. But with the UI, with everything like that we built, I'm not saying go back on you anything like that.
> see what of Hermes we can squeeze into each one of these lanes into topics, [skills, bots, loops]
