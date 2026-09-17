---
name: background-job-liveness-check
description: Use when a launchd/cron/WatchPaths job is claimed running. Prove it ticked from artifacts, never from the job being listed or the log being buffered.
version: 0.1.0
distilled: 2026-09-05 18:35
topic: klerik
---
# background-job-liveness-check
Written to wiki-topics/klerik/skills-capabilities/background-job-liveness-check/SKILL.md. Steps: (1) listed ≠ firing — after `cron list` run `cron runs <id>`; 'No cron execution attempts' = not running; a 'Gateway is not running' warning means it never will until `hermes gateway install`. (2) buffered log ≠ clean — read the per-tick artifact instead (wiki-topics/*/log.md compile line, .system/session.md, Chris-sender inbox block). (3) sweep the set: `grep -L <today> wiki-topics/*/log.md` lists topics that did not compile. (4) set LIVE only from that proof, else REGISTERED, NOT FIRING (<reason>) with real output. (5) honor Chris vetoes: skip and log SKIPPED any tick that edits a file he said to leave alone. Pitfalls: ticker_heartbeat mtime only proves a process lived; a retried cron create can silently succeed and orphan an older FAILED note.

## Evidence
> the topic agents are running on the 17 thin topics too — check the log for failures, and check the watcher is actually cutting live
> The agent job is running its first `--all` pass right now (WatchPaths fired). Log is buffered until it exits.
> ⚠ Gateway is not running — jobs won't fire automatically.
