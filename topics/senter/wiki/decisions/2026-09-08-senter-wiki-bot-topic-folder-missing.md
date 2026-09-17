---
title: Senter-wiki-bot topic folder missing (clarified: folder exists)
created: 2026-09-08
updated: 2026-09-08
type: decision
tags: [decision, infra, bot,Clarification]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md]
confidence: high
---

# Senter-wiki-bot topic folder missing (clarified: folder exists)

**The initial gap.** The `senter-wiki-bot` profile exists but on 2026-09-08 09:56 the scan-topics.py investigation suggested it had no topic folder with proper structure. Hermes noted: "The `senter-wiki-bot` profile exists but has no topic to serve."

**Investigation result.** On 2026-09-08, further inspection revealed the folder already exists:
- `topics/senter-wiki/` exists at `/Users/sovthpaw/Documents/Projects/Projects/topics/senter-wiki/`
- It has the standard anatomy: `README.md`, `.system/`, `wiki/` (with entities/, concepts/, decisions/, queries/), `skills/`, `bots/`, `loops/`
- The wiki section contains content indexed at `wiki/index.md` with 415 lines

**What exists now.** As of 2026-09-08, the `topics/senter-wiki/` folder is properly scaffolded with:
```
topics/senter-wiki/
├── README.md (v14.x)
├── .system/
│   └── architecture.md (five-part architecture, published 2026-09-05)
├── wiki/
│   ├── entities/ (senter, senter-wiki-ui, etc.)
│   ├── concepts/ (look loop, five-part architecture, vault-ui style, etc.)
│   ├── decisions/ (multiple decisions including autonomous completion)
│   └── queries/ (senter-timeline, event-driven-trigger-gaps)
├── skills/ (multiple skills)
├── loops/ (various loops)
└── BRIEF.md (updated 2026-09-08 with new learnings)
```

**What this means.** The "missing topic folder" was a temporary gap during the investigation phase. The folder already exists and contains the proper structure. The senter-wiki topic is a live topic with content, and the `senter-wiki-bot` profile should serve it.

**Check needed.** Verify that the `senter-wiki-bot` profile is correctly configured to serve the `senter-wiki` topic. This may require updating the bot's SOUL or AGENTS to point to the correct topic name.

**Related.** [[topics/senter/wiki/entities/senter|siten]]; [[topics/senter/wiki/entities/senter-wiki-ui|senter-wiki-ui]]; [[topics/senter/wiki/concepts/topics-are-the-work-units|topics are work units]].

**Verified live (2026-09-09 13:32).** The 2026-09-09 pipeline check confirmed the `senter-wiki` topic is properly populated: "senter-wiki topic now properly populated" in the `/system-live.json` served by `com.senter.bridge`. ^[raw/inbox/2026-09-09.md]

^[raw/inbox/2026-09-07.md] ^[raw/inbox/2026-09-08.md]