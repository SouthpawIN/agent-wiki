---
title: notify_on_complete fallback
created: 2026-09-15
updated: 2026-09-15
type: decision
tags: [infra, decision]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# notify_on_complete fallback

Decision/behavior: when watch patterns are disabled for a process, the watcher does **not** stop tracking it — it switches to `notify_on_complete` semantics.

## What was decided
- **Trigger:** disable patterns after 3 consecutive rate-limit windows (min spacing 15s).^[raw/inbox/2026-09-15.md]
- **Fallback:** deliver exactly one notification when the process exits, rather than per-event watching.^[raw/inbox/2026-09-15.md]

## Why
The 15s minimum spacing with a 3-strike rule is a rate-protection mechanism: rapid successive events would otherwise overwhelm the watcher. The fallback preserves the essential signal (the process finished) while shedding the per-event cost.

## Evidence
- "Falling back to notify_on_complete semantics; you'll get exactly one notification when the process exits."^[raw/inbox/2026-09-15.md]

## Related
- See [[wiki-topics/process-important/wiki/entities/process-rate-limiter|Watch-pattern rate limiting]] for the trigger.
- See [[wiki-topics/process-important/wiki/concepts/watch-patterns-disabled|Watch patterns disabled]] for the lifecycle.
