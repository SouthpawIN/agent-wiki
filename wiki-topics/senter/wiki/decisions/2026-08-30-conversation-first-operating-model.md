---
title: "2026-08-30 — Conversation-first operating model (locked)"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, spec, timeline]
sources: [raw/sources/knowledge/senter-SOUL.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# 2026-08-30 — Conversation-first operating model (locked)

**What.** Intake is free conversation. Chris talks about anything; [[wiki-topics/senter/wiki/entities/senter|Senter]] is the single surface. Senter detects interests/intents mid-conversation and sorts them into vault topics (existing topic owns it; new domain → new topic). When interest recurs or intent is expressed ("I want to do X" is a trigger, not a passing comment), Senter proactively **proposes** actions — a bot (via klerik), a cron/automation, or a skill — "suggested to Chris, never spawned silently." Dormant-but-expressed interests are nudged back ("dormant 8 weeks, want me to wake it?"). ^[raw/sources/knowledge/senter-SOUL.md]

**Pipeline.** conversation → interest → topic sort → momentum → proposal → Chris approval → bot/loop creation → outcome logged in vault (Ideas.md, topic .system files, log.md, roster). ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

**Why.** Chris wanted one place to talk and a system that catches everything he cares about, without him managing bots. Same day: Senter's coordinator role assigned, [[wiki-topics/senter/wiki/decisions/2026-08-30-standing-approval|standing approval]] granted, anser and paladin onboarded.

**Evidence.** Senter SOUL "Operating model: conversation-first (locked in 2026-08-30)"; skill §Operating model.

**Later evolution.** 2026-09-02: Senter routes but never builds ([[wiki-topics/senter/wiki/decisions/2026-09-02-senter-never-builds|decision]]). 2026-09-05: the doing AND the detecting leave the sidebar — a watcher files per message, per-topic loops propose, the sidebar only rubber-ducks and approves ([[wiki-topics/senter/wiki/concepts/five-part-architecture|five-part architecture]], [[wiki-topics/senter/wiki/decisions/2026-09-05-per-message-watcher|per-message watcher]]). The "never spawned silently" clause was narrowed the same day: wiki edits need no approval ([[wiki-topics/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|decision]]).
