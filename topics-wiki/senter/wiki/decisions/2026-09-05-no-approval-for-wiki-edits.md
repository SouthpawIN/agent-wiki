---
title: "2026-09-05 — No approval needed for wiki edits; bots trigger sooner"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, preference, loop]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: medium
contested: true
contradictions: [2026-08-30-conversation-first-operating-model]
---

# 2026-09-05 — No approval needed for wiki edits; bots trigger sooner

**What.** Chris, 17:18, reacting to approval cards: **"These are the things that I don't want to have to give approval on or edits to the wiki and things like that."** Wiki edits (the watcher's filings, the topic loops' compilations, skill drafts) proceed without a card. **"I was thinking that bots need to trigger a lot sooner… when I want the side feed to be constantly going… if I talk about a new subject then it should suggest maybe researching it or maybe scaffolding it… use maybe a bot that we've used before to research a different subject, or create a new one, there isn't one like that. These are the kinds of pipelines or organizations that I want done automatically."** ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Why.** "I want the user to only have to be able to talk about their ideas to the site chat and this entire agentic, fleet and knowledge-based coordination self-edits and proposes." Cards on routine edits are friction that hides motion.

**Contested / boundary (kept with dates).**
- 2026-08-30 SOUL: bots-profiles/crons/skills are "suggested to Chris, never spawned silently"; 2026-09-05 16:29 (same day, earlier): "all the approvals need to go to the sidebar chat." Read together: **edits and proposals need no approval; creation of a bot/loop still surfaces as a card** — but the 17:18 wording ("or create a new one… done automatically") leans toward auto-creating research bots too. Unresolved; the exact line between "propose" and "spawn" for new bots is an open question for Chris.
- Standing approval (2026-08-30) already covered "act first"; this extends it from Senter's actions to the fleet's edits ([[topics-wiki/senter/wiki/decisions/2026-08-30-standing-approval|decision]]). ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

- **2026-09-05 18:16** tightened the other side: "Preempt decision, stop asking me for so many decisions. I've told you everything that I want this to be so far." Cards that ask what the wiki already answers are now themselves the failure ([[topics-wiki/senter/wiki/decisions/2026-09-05-preempt-decisions-complete-the-incomplete|decision]]). ^[raw/inbox/2026-09-05.md]

**Mechanism implications.** Wiki writes must not trip Hermes's approval gate at all (write_file/patch, not shell — the 96-card day); the [[topics-wiki/senter/wiki/entities/senter-bridge|bridge]]'s cards reserve themselves for real decisions ([[topics-wiki/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|decision]]).
