---
title: "2026-09-05 — Preempt decisions; stop asking; find what isn't complete and complete it"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, preference, pain, plan, loop]
sources: [raw/inbox/2026-09-05.md, raw/sources/2026-09-05-umbrella-still-runs.md]
confidence: high
contested: true
contradictions: [2026-09-02-fleet-decisions-as-wiki-cards]
---

# 2026-09-05 — Preempt decisions; stop asking; find what isn't complete and complete it

**What.** At 18:16, after the topic agents' first pitches had landed as cards, [[topics-wiki/senter/wiki/entities/chris|Chris]] said, in full: **"Preempt decision, stop asking me for so many decisions. I've told you everything that I want this to be so far Continue building looking for things that aren't complete yet and complete them."** ^[raw/inbox/2026-09-05.md]

Three instructions in one line:
1. **Preempt decisions** — when the answer is already derivable from what he has said, decide it and act; do not surface it.
2. **Stop asking** — the volume of decision cards itself is the complaint, not any one card. "So many decisions" is the pain.
3. **Completion sweep** — the standing work order from here on is *look for the incomplete and finish it*, not *propose the next thing*. He considers the spec delivered ("I've told you everything that I want this to be so far").

**Why.** The whole point of the [[topics-wiki/senter/wiki/decisions/2026-08-30-standing-approval|standing approval]] and the [[topics-wiki/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|no-approval-for-wiki-edits]] rulings was motion without permission dialogs. The 17:53 topic agents pitched correctly — but pitched things Hermes already knew were gaps, turning known work into questions. A card that asks Chris something the wiki already answers is a decision being pushed back up to him. ^[raw/inbox/2026-09-05.md]

**How Hermes read it (18:18).** "The topic agents are pitching exactly the right things — including two I'd already noted as gaps (event-driven instead of 5-min timer; governance orphaned). Do them myself rather than via cards." The two named gaps:
- the [[topics-wiki/senter/wiki/entities/topic-agent|topic agent]] fires on a 5-minute timer, which violates "per message" / "live live live — no timed loaders" ([[topics-wiki/senter/wiki/concepts/live-data-contract|live-data contract]]) → make it event-driven on new `raw/inbox` writes;
- topic merge/split **governance was orphaned** when the umbrella script was deleted at 17:53 ([[topics-wiki/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|one agent per topic]]) — the locked thresholds ([[topics-wiki/senter/wiki/decisions/2026-09-02-governance-thresholds-calibrated|.35 / .50]]) need a new home. ^[raw/inbox/2026-09-05.md]
  **Corrected 18:53 (contested, dates kept):** the umbrella was *not* deleted — `assets/umbrella.py` / `com.senter.umbrella` (every 30 min) kept running and still owns governance ([[topics-wiki/senter/wiki/entities/umbrella|umbrella]]). The "orphaned" belief was this wiki's inference; it made the agent re-pitch a governance loop every run. "Fix the record, not the pitch" ([[topics-wiki/senter/wiki/concepts/fix-the-record-not-the-pitch|concept]]). ^[raw/sources/2026-09-05-umbrella-still-runs.md]

**Made concrete (18:0x):** approvals APPLY — loop card → `hermes cron create`, bot card → profile + SOUL/AGENTS (klerik finishes voice/skin/alias), research card → looker writes the answer into the page. See [[topics-wiki/senter/wiki/concepts/approval-apply-paths|approval apply paths]]. ^[raw/sources/2026-09-05-umbrella-still-runs.md]

**Contested / boundary (kept with dates).**
- **2026-09-02**: "if you're waiting on my call, then there should be an approval going to the wiki" → [[topics-wiki/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|decisions become cards]]. **2026-09-05 18:16**: "stop asking me for so many decisions." These do not cancel; they bound each other. Cards remain the *channel* for anything genuinely new; the *bar* for what counts as genuinely new rose sharply. A pitch is legitimate only when the wiki does not already contain Chris's answer. Anything the fleet itself already flagged as a gap is work, not a question.
- Still outside the preemption: spending, deletion, publishing — the irreversible set from 2026-08-30 was never loosened.

**Test for a card.** Before pitching, the topic agent should be able to answer: *is there a quote in this wiki that decides this?* If yes → do it and log it. If it is a fleet-known gap → do it and log it. Only if neither → card. See [[topics-wiki/senter/wiki/concepts/proactive-suggestion-doctrine|proactive suggestion doctrine]] for the pitch order that still applies once something passes the test.

**Proof it was followed (18:20).** The first completion Hermes ran under this ruling was the loop-approval path end to end — see [[topics-wiki/senter/wiki/concepts/loop-apply-path|loop apply path]]: approve → real cron `e6e20c22e1b9` on klerik, probe cleaned, wiki verified to pick it up. ^[raw/inbox/2026-09-05.md]

**Ratified (18:48).** Thirty-two minutes later, with no new decision put to him, Chris closed the loop in one line: **"Yes, I'm whatever you need keep going."** Read as a blanket confirmation of the 18:16 mode — he is not waiting to be asked, he is waiting to *see* completions land. This is the last Chris line of the day in this topic; it converts "preempt" from a reaction to a standing state: the fleet holds the completion sweep open until he says otherwise. ^[raw/inbox/2026-09-05.md]
