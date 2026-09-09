---
title: Fix the record, not the pitch (the wiki is the agent's memory — a wrong page repeats as a wrong card)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [decision, pain, loop, spec]
sources: [raw/inbox/2026-09-05.md, raw/sources/2026-09-05-umbrella-still-runs.md]
confidence: high
---

# Fix the record, not the pitch

**Rule (Hermes, 2026-09-05 18:53):** "The senter agent keeps pitching 'governance has no owner' — because the wiki (its memory) says the umbrella was deleted, when in fact it still runs. **Fix the record, not the pitch.**" ^[raw/inbox/2026-09-05.md]

## Why it exists
The [[topics/senter/wiki/entities/topic-agent|topic agent]] reads this wiki as its memory ([[topics/senter/wiki/decisions/2026-09-05-wiki-is-hermes-memory-layer|decision]]) and pitches from it. A false statement in a page is therefore not a typo — it is a **recurring wrong card** to Chris, on every run, until the page is corrected. Here the page said the [[topics/senter/wiki/entities/umbrella|umbrella]] had been deleted; the agent dutifully proposed a governance loop; the loop already existed. Under Chris's 18:16 ruling ("stop asking me for so many decisions" — [[topics/senter/wiki/decisions/2026-09-05-preempt-decisions-complete-the-incomplete|decision]]) a repeated redundant card is exactly the pain he named.

## How to apply it
1. When a pitch repeats across runs and is rejected or superseded, ask *what page makes the agent believe this?* — not *how do I suppress this pitch?*
2. Write the correction as an **immutable raw source** (`raw/sources/<date>-<slug>.md`, verbatim, with who said it), so the fix has provenance like everything else.
3. Recompile: correct every page that carried the wrong belief, **keeping the wrong statement with its dates** and `contested: true` rather than erasing it — the wiki shows how the belief formed and when it was fixed.
4. Never filter the pitch in code. A suppressed pitch hides a wrong memory; a corrected page removes it.

## The inference error to watch for
The wrong belief came from an inference, not a quote: "worker + compiler were replaced" was read as "everything from 16:37 was replaced." Pages should distinguish *what a raw item says* from *what the compiler concluded*, and mark the latter medium-confidence. Related: [[topics/senter/wiki/concepts/markdown-is-the-api|markdown is the API]] — unlogged (or mis-logged) state is the state the fleet acts on.
