---
name: wiki-fix-the-record-not-the-pitch
description: Use when an agent re-pitches a rejected item. Fix the page.
version: 0.1.0
distilled: 2026-09-05 18:58
topic: senter
---
# wiki-fix-the-record-not-the-pitch
Trigger: same pitch in 2+ compiles, or a pitch answered 'it already exists'. Steps: (1) grep the topic wiki for the page that makes the agent believe it; (2) verify reality first (launchctl list, hermes cron list, ls assets/) — never swap one inference for another; (3) write the correction as an immutable raw/sources/<date>-<slug>.md, verbatim, with who said it; (4) recompile every page carrying the belief — keep the wrong statement with dates, add **Corrected <time>:**, set contested: true, add the raw path to sources; (5) close the item on the timeline/open-items and log a compile line; (6) never re-pitch and never add a code filter — a suppressed pitch hides a wrong memory. Pitfall: the error came from reading 'worker + compiler replaced' as 'everything replaced' — separate what a raw item SAYS from what you CONCLUDE.

## Evidence
> The senter agent keeps pitching "governance has no owner" — because the wiki (its memory) says the umbrella was deleted, when in fact it still runs. Fix the record, not the pitch
> Preempt decision, stop asking me for so many decisions. I've told you everything that I want this to be so far
