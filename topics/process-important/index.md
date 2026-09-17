# process-important — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-15 | Total pages: 3

## Entities
- [[topics/process-important/wiki/entities/process-rate-limiter|Watch-pattern rate limiting]] — The Senter watcher disables **watch patterns** for a process after it fires too many times too fast, then falls back to a coarser notification mode. This is the

## Concepts
- [[topics/process-important/wiki/concepts/watch-patterns-disabled|Watch patterns disabled]] — "Watch patterns disabled" is the watcher's response to a process that trips the rate limiter repeatedly. It marks a transition from fine-grained event watching 

## Decisions
- [[topics/process-important/wiki/decisions/notify-on-complete|notify_on_complete fallback]] — Decision/behavior: when watch patterns are disabled for a process, the watcher does **not** stop tracking it — it switches to `notify_on_complete` semantics.

## Comparisons


## Queries


