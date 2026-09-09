---
title: Chris (sovthpaw)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [person, preference, pain]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/senter-SOUL.md, raw/sources/knowledge/weaver-AGENTS.md]
confidence: high
---

# Chris (sovthpaw)

Chris — GitHub `SouthpawIN`, macOS user `sovthpaw` — is the owner and sole user of [[topics/senter/wiki/entities/senter|Senter]] and the fleet. He directs everything live from the Hermes desktop app, mostly by **voice dictation**, while watching the [[topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki]] in the preview pane. He works with the Hermes Agent team and wants fleet-found core gaps upstreamed via a PR ledger. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## How he works
- Dictates; codenames arrive mangled (Claire = klerik, answer = anser, center = senter…). Never ask him to repeat. ([[topics/senter/wiki/concepts/voice-dictation-name-map|name map]]) ^[raw/sources/knowledge/senter-SOUL.md]
- Tunes UI by micro-increments and locks exact numbers; each tweak must be reloaded in his preview and *visually* verified. Reverses just-made requests after seeing them — normal iteration ("closer, don't change much" ⇒ patch only the named deltas). ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]
- Granted standing approval 2026-08-30: "when I ask for things I want you to assume that you have my approval." ([[topics/senter/wiki/decisions/2026-08-30-standing-approval|decision]])
- Wants to WATCH work land live: "I should be seeing it update live… We need to start using this as we're building it." A fix he can't see = not done.

## His vision, in his words (2026-09-05)
> "think of the UI as cursor for markdown… markdown can be used for agentic context artifacts that can be set in the motion. Such as skills.md, agents.md, memory.md, soul.md… these can all be edible in one big knowledge base."
> "I want the sidebar to be as unencumbered by the task as possible. I don't want the sidebar to actually be doing anything."
> "not per session, I want to per message, just like when you talk to cursor… this is like a auto wiki, a live acting second brain."
> "This is going to be a funnel for all of the contacts for everything that the user cares or worries about across all of their digital and real life."
See [[topics/senter/wiki/concepts/cursor-for-markdown|Cursor for markdown]], [[topics/senter/wiki/decisions/2026-09-05-per-message-watcher|per-message watcher]]. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Pains (things that make him furious or lose trust)
- Repeating an ask 3+ times; "routed/queued" reads as stalling; "you didn't do X" often meant his preview was stale.
- Being told what he "should" see without a capture of his window: "you're entirely guessing — what you're saying is not there… instead of lying or coming up with dummy data." ([[topics/senter/wiki/concepts/look-loop-verification|LOOK loop]])
- Band-aids: "you put a band-aid over it I would like you to not work like that" — root-cause fixes only.
- Senter doing the work itself: "you're doing a lot of these edits yourself when in fact what you should be doing is using the agent wiki… creating or adjusting workers to do the task." ([[topics/senter/wiki/decisions/2026-09-02-senter-never-builds|decision]])
- Queues and waiting: "don't queue tasks, don't make me wait several minutes for a task to start… many in parallel"; "things tend to die when they go in the pending."
- Approval clicks he shouldn't need: 96 approval cards in one day from interpreter one-liners; 2026-09-05: "These are the things that I don't want to have to give approval on or edits to the wiki." ([[topics/senter/wiki/decisions/2026-09-05-no-approval-for-wiki-edits|decision]])
- Not seeing motion: "I'm not seeing things move in the UI like I thought that I would." ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Preferences (standing)
- Terminology: profiles are **BOTS**, never "agents". Many parallel Meeseeks; first action in seconds.
- Decisions come to him as **wiki cards**, not chat questions or `clarify` modals ([[topics/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|decision]]).
- The process itself is the product: "this is exactly how I intend people to use this product" ([[topics/senter/wiki/decisions/2026-09-02-process-artifacts-are-the-product|decision]]).
- Aesthetic: white on black, no blue tints, no rounded corners ([[topics/senter/wiki/concepts/vault-ui-style-contract|style contract]]).
- Music while working: asked for "Humanity's Last Breath — Godhood" played live with the EQ and the girl's headphones reacting ([[topics/senter/wiki/concepts/media-player-controls|media player]]).
- Every steer is ADDITIVE ("treat this as a steer" keeps prior items running).
- Once the spec is stated, he wants completions, not questions: "Preempt decision, stop asking me for so many decisions" (18:16) → "Yes, I'm whatever you need keep going" (18:48). A card that the wiki already answers is a failure ([[topics/senter/wiki/decisions/2026-09-05-preempt-decisions-complete-the-incomplete|decision]]). ^[raw/inbox/2026-09-05.md]
- Prefers native over bespoke once the shape is known, and separates backend from UI when he says so: "get this entire flow down to just built in Hermes commands and markdown… But with the UI… I'm not saying go back on anything… the backend stuff could probably work to be a lot more efficient now that we know what the idea is for the intended flow" (19:06) → [[topics/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|decision]]. Pattern: build custom to discover the flow, then collapse onto built-ins. ^[raw/inbox/2026-09-05.md]
- Timeline of his decisions: [[topics/senter/wiki/queries/senter-timeline|Senter timeline]].
