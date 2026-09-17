---
title: Watch-pattern rate limiting
created: 2026-09-15
updated: 2026-09-15
type: entity
tags: [tool, infra, pain]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# Watch-pattern rate limiting

The Senter watcher disables **watch patterns** for a process after it fires too many times too fast, then falls back to a coarser notification mode. This is the recurring mechanism behind every "Watch patterns disabled" notice.

## What triggers it
Watch patterns are disabled when a process triggers **3 consecutive rate-limit windows**. The enforced minimum spacing between windows is **15 seconds**^[raw/inbox/2026-09-15.md].

## The fallback
Once disabled, the process switches to **`notify_on_complete` semantics**: exactly one notification is delivered when the process exits, instead of per-event watching^[raw/inbox/2026-09-15.md].

## Evidence (verbatim)
- "Watch patterns disabled for process proc_7813b9bfdd74 — 3 consecutive rate-limit windows triggered (min spacing 15s). Falling back to notify_on_complete semantics; you'll get exactly one notification when the process exits."^[raw/inbox/2026-09-15.md]
- Same notice repeated three times on 2026-09-15 13:21 for `proc_7813b9bfdd74` and once for `proc_de1870a14659`, each with different similarity scores (0.04, 0.94, 0.84)^[raw/inbox/2026-09-15.md].

## Related
- See [[topics-wiki/process-important/wiki/concepts/watch-patterns-disabled|Watch patterns disabled]] for the lifecycle and fallback behavior.
- See [[topics-wiki/process-important/wiki/decisions/notify-on-complete|notify_on_complete fallback]] for the exact fallback contract.
