---
name: center-wiki-orchestration
description: Use when working with center wiki as live orchestrator.
version: 0.1.0
distilled: 2026-09-08 09:57
topic: beyond-pissed
---
# center-wiki-orchestration
# Center wiki orchestration

When Chris is orchestrating multiple projects through the center wiki, the workflow requires three concurrent tracks:

## Understand (current state first)
Always read current file/system state for exact details before making changes. Check for reverts that need recovery.

## Use (live orchestration)
Operate the wiki as the coordination surface — it is not just documentation but the live orchestrator.

## Build (additive only)
Make changes that surface in the wiki immediately observable.

### Key rules:
- Never operate on stale assumptions about file/system state — always read current state first.
- Reverts must be identified and recovered before the wiki can safely serve as orchestrator.
- Changes must be visible in the wiki in real-time; a fix Chris cannot see is not done.

### Evidence:
- "The center wiki has reverts that must be recovered before it can safely serve as that orchestrator." ^[raw/inbox/2026-09-08.md]
- "use current file/system state for exact details" ^[raw/inbox/2026-09-08.md]
- "we need to be simultaneously understanding, using and building the center wiki" ^[raw/inbox/2026-09-07.md]

## Evidence
> The center wiki has reverts that must be recovered before it can safely serve as that orchestrator. ^[raw/inbox/2026-09-08.md]
> use current file/system state for exact details ^[raw/inbox/2026-09-08.md]
> we need to be simultaneously understanding, using and building the center wiki ^[raw/inbox/2026-09-07.md]
