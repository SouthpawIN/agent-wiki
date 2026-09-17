---
title: Verify apply paths and WatchPaths landed
type: query
proposed: 2026-09-05 18:58
updated: 2026-09-10
tags: [question, verification, infra]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]
confidence: high
---

# Verify apply paths and WatchPaths landed

## Current status (2026-09-10)

**Loop apply path** — proven. The cron `e6e20c22e1b9` runs successfully. ✓

**Bot apply path** — **landed**. The `scan-topics.py` schema normalization fix (uniform `model`/`skills` schema across `scan_topics()`, `scan_vault_agents()`, `scan_bots()`) is confirmed in committed code at `assets/scan-topics.py` lines 143, 227, 185. The `name_of()` function correctly strips `.md` suffixes. The `snapshot()` function now works against uniform bot objects. ✓

**Research apply path** — pending. Requires anser to write results into the wiki page.

**Event-driven topic-agent trigger** — **NOT LANDED**. The topic agent (`assets/topic-agent.py`) still fires on a 5-minute timer, not on WatchPaths-triggered new inbox writes. See [[topics/senter/wiki/queries/event-driven-trigger-gaps-2026-09-08|event-driven trigger gaps]].

## What each path does

From the approval apply paths concept:

- **Loop** → cron job on the owning bot's profile
- **Bot** → profile creation/editing (klerik) + SOUL.md/AGENTS.md writes
- **Research** → looker writes findings into the wiki page

## Open questions

1. Should we verify the event-driven trigger implementation?
2. Is there a bot that checks if all apply paths are actually landing?

^[raw/inbox/2026-09-05.md] ^[raw/inbox/2026-09-10.md]