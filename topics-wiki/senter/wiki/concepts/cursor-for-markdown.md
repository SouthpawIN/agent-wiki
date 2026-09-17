---
title: Cursor for markdown (the premise)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [idea, spec, ui, timeline]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Cursor for markdown (the premise)

[[topics-wiki/senter/wiki/entities/chris|Chris]]'s one-line framing of the whole Senter project, 2026-09-05 16:29:

> "think of the UI as cursor for markdown. The reason why we're doing that is because markdown can be used for agentic context artifacts that can be set in the motion. Such as skills.md, agents.md, memory.md, soul.md, all of these. So these can all be edible in one big knowledge base. And then also we include context with that." ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Lineage
- 2026-08-31 north star: **"Cursor for Obsidian"** — vault = knowledge base + orchestration + review layer + LIVE UI; Chris watches it morph in Obsidian with the chat as a side window; skills-capabilities/agents created live from clean templates. Build order then: selfmodel layer (done) → approvals routed to chat → project-update digest stream → vault template system. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]
- 2026-09-05: Obsidian dropped as a requirement (the [[topics-wiki/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] renders the vault itself); "Cursor" now means the *editing cadence*: "fast paced… live editing just like cursor… not per session, I want to per message, just like when you talk to cursor every message at its code base." → [[topics-wiki/senter/wiki/decisions/2026-09-05-per-message-watcher|decision]].

## What "Cursor" implies here
1. Every file is executable configuration — editing SOUL.md changes a bot; editing SKILL.md changes a procedure ([[topics-wiki/senter/wiki/concepts/markdown-is-the-api|Markdown is the API]]).
2. Edits happen continuously and visibly: "I should be able to watch the wiki move around on its own, edit on its own, skills and bots and loops getting proposed all the time."
3. The knowledge base and the agentic flows are one thing: "edit the user's ideas into a knowledge and agentic flows… also be able to orchestrate those flows in action… a auto wiki, a live acting second brain."
4. It is a memory layer: "this is supposed to be basically a memory layer for Hermes agent" ([[topics-wiki/senter/wiki/decisions/2026-09-05-wiki-is-hermes-memory-layer|decision]]) and a funnel "for everything that the user cares or worries about across all of their digital and real life."

Related: [[topics-wiki/senter/wiki/concepts/five-part-architecture|Five-part architecture]], [[topics-wiki/senter/wiki/concepts/context-to-skills-to-bots-to-loops|flywheel]].
