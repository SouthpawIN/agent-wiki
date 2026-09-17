---
title: Five-part architecture (sidebar · watcher · topics · loops · approvals)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, plan, idea]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/knowledge/senter-SOUL.md]
confidence: high
---

# Five-part architecture (sidebar · watcher · topics · loops · approvals)

Hermes's playback of [[wiki-topics/senter/wiki/entities/chris|Chris]]'s 2026-09-05 16:29 brief, which Chris did not contradict (he added "fast paced… per message"). Written to `wiki-topics/senter/.system/architecture.md`. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Premise
The UI is [[wiki-topics/senter/wiki/concepts/cursor-for-markdown|Cursor for markdown]]: every vault file is an agentic artifact that can be set in motion — SKILL.md, AGENTS.md, SOUL.md, memory, loop prompts — next to the raw context that produced it. "Editing a file configures the system. That's why it's one knowledge base and not a dashboard."

## Five parts, strict separation
1. **Sidebar** (the chat) — talks to Chris, yes-and personality, rubber-ducks to pull ideas OUT of him, receives every approval. **Does no work.** Never builds, never runs loops, never gets interrupted — so he can jump between topics mid-thought. Chris: "I want the sidebar to be as unencumbered by the task as possible… All the sidebar does is maintain a conversation with the user, have a yes and personality, and to try to extract more context from the user. Kind of like rubber ducking."
2. **[[wiki-topics/senter/wiki/entities/watcher|Watcher]]** — reads Hermes logs/sessions directly as they're written and files everything into topics; no hand-off, so the sidebar never has to "remember to save."
3. **Topics** — hold ALL the context for a subject, disclosed progressively ([[wiki-topics/senter/wiki/concepts/progressive-disclosure|progressive disclosure]]; [[wiki-topics/senter/wiki/concepts/topics-are-the-work-units|topics are the work units]]).
4. **Per-topic loops** — the flywheel: context → skills → bots → loops ([[wiki-topics/senter/wiki/concepts/context-to-skills-to-bots-to-loops|concept]]).
5. **Approvals** — every artifact creation (skill, bot, loop, merge) is a card in the sidebar; yes/no in the flow of whatever he's talking about. (Later the same day Chris narrowed this: wiki edits need no approval — [[wiki-topics/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|decision]].)

## Mapped to what exists
Sidebar = default profile (rubber-duck SOUL + "no tasks" rule + INDEX-first reading); watcher = new, fed by `sessions export` / `agent.log` / bridge events, TF-IDF sorting; topic loops = `hermes cron` per topic; skills-capabilities/bots via `hermes skills` / `hermes profile create` + klerik review; approvals via `hermes serve approval.*`. Follow-up shape (16:37): per-topic workers running asynchronously (`hermes -p senter <topic>`, N cheap processes, one profile) + one opinionated umbrella senter cron (topic merge/split proposals, cross-topic skill dedupe); `hermes kanban` claims stop collisions. See [[wiki-topics/senter/wiki/entities/hermes-agent|Hermes Agent]].

## Revision at 17:46 — "I don't like the separation"
The 16:37 follow-up shape (workers + umbrella + a separate wiki compiler) was rejected by Chris the same evening. Parts 2 and 4 are now: the watcher **cuts** messages by subject ([[wiki-topics/senter/wiki/concepts/watcher-as-cutter|cutter]]) and **one agent per topic** does both the wiki rewrite and the action proposals ([[wiki-topics/senter/wiki/entities/topic-agent|topic agent]], [[wiki-topics/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|decision]]). Part 5 keeps approvals for bots-profiles/loops as cards but proposals fire on the first appearance of a subject. ^[raw/inbox/2026-09-05.md]

## Relation to the 2026-08-30 model
This is the 2026-08-30 [[wiki-topics/senter/wiki/decisions/2026-08-30-conversation-first-operating-model|conversation-first model]] with the doing removed from Senter entirely and the intake automated by the watcher. The sidebar's rubber-duck job is new wording; "never spawned silently" from 08-30 survives as the approvals lane. ^[raw/sources/knowledge/senter-SOUL.md]
