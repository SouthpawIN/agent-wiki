---
title: Multi-Project Orchestration
created: 2026-09-07
updated: 2026-09-08
type: concept
tags: [plan, tool, infra, preference]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md]
confidence: high
---

# Multi-Project Orchestration

Chris intends to work on many projects simultaneously, using the center wiki as the orchestrator for all of them. The wiki is therefore not just documentation but the coordination surface.

> The purpose is I want you to have a complete understanding because what we're going to be doing is we're going to be working on many projects simultaneously using this wiki as an orchestrator for all of them. You will understand when you read it. At the same time this center wiki still needs to be finished and in fact a few steps were even reverted so there are some things we even need to fix to get back to where we were. So we need to be simultaneously understanding, using and building the center wiki and other projects with the center wiki. ^[raw/inbox/2026-09-07.md]

## Using Current System State
Chris emphasized using "current file/system state for exact details" — never operate on stale assumptions. The system state is dynamic: the token used by Hermes changes when `--new-token` is invoked, requiring reads of the new token for continued system state synchronization^[raw/inbox/2026-09-08.md].

## Reverts to Recover
The center wiki has reverts that must be recovered before it can safely serve as the orchestrator across multiple projects^[raw/inbox/2026-09-08.md].

See also: [[topics/beyond-pissed/wiki/entities/center-wiki|Center Wiki]], [[topics/beyond-pissed/wiki/decisions/ship-today|Ship Today]], [[topics/beyond-pissed/wiki/concepts/beyond-pissed|Beyond Pissed]], [[topics/beyond-pissed/wiki/decisions/finish-center-wiki-and-orchestrate|Finish Center Wiki and Orchestrate]]
