---
title: Decision 2026-09-09 — bots and sessions are already surfaced, no new layout needed
created: 2026-09-09
updated: 2026-09-09
type: decision
tags: [decision, ui, layout]
sources:
  - raw/inbox/2026-09-09.md
confidence: high
---

# Decision 2026-09-09 — bots and sessions are already surfaced, no new layout needed

**What.** Chris asked *\"how do I see my bots and sessions in this layout?\"* on 2026-09-09 13:01. The one-page navigation model already maps bots and sessions to existing surface areas: bots → BOTS section (orb click re-sorts the same row list); sessions → corner feed (`#chat .mini`). No new page, card, or row template is required. ^[raw/inbox/2026-09-09.md]

**Why.** The 2026-09-03 one-page decision was explicit: \"*instead of having different pages for context, skills, bots and loops — just use the front wiki page and have that reorder by what we're searching for … a top wiki for Topics, then below that sections for Skills, Bots, and Loops, all on the same list.*\" ([[topics-wiki/senter-wiki/wiki/concepts/one-page-navigation-model|navigation model]]) The standard row reuses `mkTopic()+initTopic()` for every kind — bots included — so a separate bot row template would be the divergence-bug the skill warns against. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

**Supersedes.** Nothing — this is a clarification of [[topics-wiki/senter-wiki/wiki/concepts/one-page-navigation-model|the one-page navigation model]] against a discoverability question, not a behavior change.

## Evidence
- Chris: *\"how do I see my bots and sessions in this layout?\"* — 2026-09-09 13:01. ^[raw/inbox/2026-09-09.md]
- BOTS section sorts bots by SOUL role, reuses the standard row anatomy. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Corner feed is the live session stream: *\"the Feed is the bottom-corner feed.\"* ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Open question
Where do **session history details** (per-session transcripts/logs) live for a given bot — the corner feed shows live cards but Chris may want a deeper drill. Left as an open item pending his next phrasing.

## Related
|- [[topics-wiki/senter-wiki/wiki/concepts/one-page-navigation-model|One-page navigation model]]
|- [[topics-wiki/senter-wiki/wiki/entities/corner-feed|Corner feed]]
|- [[topics-wiki/senter-wiki/wiki/entities/fleet-bots|Fleet bots]]
|- [[topics-wiki/senter-wiki/wiki/concepts/standard-row-anatomy|Standard row anatomy]]
|- [[topics-wiki/senter-wiki/wiki/entities/orb-label-renaming|Orb label renaming]]
|- [[topics-wiki/senter-wiki/wiki/decisions/2026-09-09-vault-git-init|vault git init]]
