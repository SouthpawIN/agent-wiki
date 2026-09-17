---
title: "2026-09-02 — Fleet decisions go to the wiki as cards, not chat"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui, preference]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# 2026-09-02 — Fleet decisions go to the wiki as cards, not chat

**What.** Chris: **"if you're waiting on my call, then there should be an approval going to the wiki."** A `clarify` modal had timed out unanswered while he was working in the wiki. For any NEEDS-CHRIS (new bot, merge run, threshold lock): POST a `needs_chris` card via the [[topics/senter/wiki/entities/senter-bridge|bridge]] (`/post` with `{bot:'senter', status:'needs_chris', text:'… YES → … / NO → … reply "x yes"'}`), write the decision point into the owning plan file under `## AWAITING CHRIS`, and mention it in one line of chat. "Never block a turn on a chat-side question the wiki should be carrying." ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

**Why.** The wiki is where Chris looks; chat questions and modals get missed and stall the fleet. Cards also carry evidence (e.g. calibrated thresholds with their numbers) rather than bare questions.

**Consequences.** Bots' `NEEDS-CHRIS` [[topics/senter/wiki/concepts/done-signal|done-signal]] lines become cards; the sentinel treats a bot parked on a card as dead capacity and spawns around it; the wiki's FEED is the reply channel.

**Restated 2026-09-05** in the five-part architecture: "all the approvals need to go to the sidebar chat so just the user carries on a conversation about anything… they can jump back and forth between topics." Then narrowed: routine wiki edits should need no card at all ([[topics/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|decision]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]
