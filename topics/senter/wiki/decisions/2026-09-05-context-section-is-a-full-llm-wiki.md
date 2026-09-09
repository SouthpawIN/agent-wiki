---
title: "2026-09-05 — Each topic's wiki section is a full LLM wiki, not a line"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, spec, ui]
sources: [raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# 2026-09-05 — Each topic's wiki section is a full LLM wiki, not a line

**What.** Chris, 17:40: **"I still don't think you get it because the wiki for center wiki is still only one line… you should use the LLM wiki skill for the wiki section like the wiki section should be like entire thorough wikis on each individual thing It should be like all of everything that's collected about that topic with that user and all of the inputs that they put into it. This is going to be a funnel for all of the contacts for everything that the user cares or worries about across all of their digital and real life."** ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Result.** Every topic gets Karpathy's LLM-wiki structure — `SCHEMA.md`, `index.md`, `log.md`, immutable `raw/` (watcher inbox + sources), compiled `wiki/{entities,concepts,decisions,comparisons,queries}` with frontmatter, ≥2 wikilinks, provenance markers pointing back to `raw/` files, `contested: true` on conflicts, and lines Chris marks with his own HTML-comment tag never rewritten. The wiki row's WIKI section renders `index.md`. This page is part of the first compile of `topics/senter` (2026-09-05) under that rule; `topic-wiki.py init` created the skeleton earlier the same day.

**Why.** [[topics/senter/wiki/concepts/progressive-disclosure|Progressive disclosure]] is only useful if what is disclosed is complete; a one-line summary defeats the [[topics/senter/wiki/decisions/2026-09-05-wiki-is-hermes-memory-layer|memory-layer]] goal. The scope is deliberately total: "everything that the user cares or worries about across all of their digital and real life" — hence SCHEMA tags like music, money, health, family alongside bot/skill/loop.

**Also in the same message stretch (17:18–17:32).** Chris wants to SEE the compile happen: "I want to see this thing scrolling around and flying around and topics opening and being edited and being closed… the side feet going"; "make sure that the feed on the side is also populating… imagine this from the user's perspective." ([[topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]])
