---
title: Query — does the existing proposal-only planner run against our vault?
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [question, tool, plan]
sources: [raw/inbox/2026-09-05-legacy-inbox.md]
confidence: low
---
# Does the existing proposal-only planner run against our vault?

**Status: unanswered.** On 2026-09-05 the planner was identified as "the real engine" and the stated next step was to test it: "Let me see if it runs against our vault before writing anything of my own." ^[raw/inbox/2026-09-05-legacy-inbox.md] No result is in the raw record.

**Why it matters.** If it runs, it is the proposal stage for the whole Senter pipeline and klerik only needs the approval → spawn wire ([[topics/klerik/wiki/concepts/bot-card-approval-wire|Bot-card approval wire]]). If it does not, someone will be tempted to write a new planner — which the note explicitly warns against doing before checking. See [[topics/klerik/wiki/entities/proposal-only-planner|Proposal-only planner]].

**How to answer it.** Locate the planner in the vault, run it read-only against `~/Documents/Projects/Projects`, and record: does it start, does it read topics/, what does it propose, does it try to write anything (it should not). Log the result to `.system/session.md` and update this page.

**What 2026-09-08 reveals.** The question cannot be answered without first resolving the scan-data quality: the `scan_vault_agents()` function that would feed the planner's output also counts proposed vault agents as real bots — 68 total against 11 real fleet bots. "But the data shows 68 bots. Let me check what's in the live JSON:" followed by "Interesting! The `scan_vault_agents()` function is actually working as designed - it's detecting proposed bots from `topics/*/agents/` directory. ... The high count (68 bots) makes sense when you add all these proposed bots. But the key issue is: **the real fleet bots (anser, dogeman, klerik, etc.) should have their counts and data correct**." ^[raw/inbox/2026-09-08.md] The proposal pipeline depends on this scan output being signal-rich, not noise-polluted.
