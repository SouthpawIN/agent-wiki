---
name: senter-watcher
description: Use when the watcher (com.senter.watcher) misfiles, stalls, or needs tuning. Per-message filing of Hermes chat into topics.
version: 1.0.0
---
# senter-watcher
`assets/senter-watcher.py --follow` (launchd `com.senter.watcher`, venv python — `/usr/bin/python3` is TCC-blocked from ~/Documents).
Tails `~/.hermes/state.db` `messages` by rowid (cursor `~/.hermes/senter-bridge/watcher.cursor`), 1.5s poll, WAL-safe read-only.

## What it does per message (user/assistant, non-cron, ≥20 chars)
1. TF-IDF cosine against every topic's `text` in `.system-live.json` (same corpus the wiki's similarity uses; reloads on snapshot mtime).
2. score ≥ `NEW_TOPIC_FLOOR` (0.06) → append to `topics/<best>/.system/inbox.md` (`## time · role · session · sim`), card `FILED → topic`.
3. else → `topics/_inbox/unsorted.md` + card `PROPOSAL · new topic?` with top terms (status needs_chris).
4. every `SKILL_EVERY` (12) filings on a topic → card `PROPOSAL · skill candidate` from recurring imperative lines.

## Operate
- Status: `launchctl print gui/$(id -u)/com.senter.watcher | grep pid`; log `~/.hermes/senter-bridge/watcher.log`.
- Replay N messages: write `max(rowid)-N` to the cursor file, `launchctl kickstart -k gui/$(id -u)/com.senter.watcher`.
- Misfiling → the topic corpus is thin: enrich `topics/<t>/README.md`/`.system/*` (the scanner rebuilds `text`), not the code.
- It never summarises. Raw text only (fenced code stripped, 4000-char cap). Summaries are the topic worker's job.

## Pitfalls
- Cards go through the bridge `POST /post` with `X-Senter-Token`; if the bridge is down filings still happen, cards don't.
- Do not file cron sessions — they are the loops themselves (feedback loop).
