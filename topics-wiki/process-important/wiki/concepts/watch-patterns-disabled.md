---
title: Watch patterns disabled
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [infra, pain, decision]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# Watch patterns disabled

"Watch patterns disabled" is the watcher's response to a process that trips the rate limiter repeatedly. It marks a transition from fine-grained event watching to coarse completion notification.

## Trigger condition
The watcher disables patterns for a process after **3 consecutive rate-limit windows**, with a **minimum spacing of 15 seconds** between those windows^[raw/inbox/2026-09-15.md].

## Consequence
After the third consecutive trip, watching stops and the system **falls back to `notify_on_complete` semantics** — a single notification when the process exits^[raw/inbox/2026-09-15.md]. This is a deliberate degradation, not a crash: the process is still tracked, just not watched per-event.

## Observed behavior
- The notice repeated **three times** for `proc_7813b9bfdd74` at 2026-09-15 13:21, each logged with a different similarity score (0.04, 0.94, 0.84)^[raw/inbox/2026-09-15.md].
- A separate process, `proc_de1870a14659`, received the same notice at the same timestamp^[raw/inbox/2026-09-15.md].
- The raw item's own metadata flags these as `hermes:` watcher state (source: `hermes state.db messages (watcher)`), i.e. evidence about the system, not a request from Chris^[raw/inbox/2026-09-15.md].

## Related
- See [[topics-wiki/process-important/wiki/entities/process-rate-limiter|Watch-pattern rate limiting]] for the trigger and fallback mechanism.
- See [[topics-wiki/process-important/wiki/decisions/notify-on-complete|notify_on_complete fallback]] for the fallback contract.
