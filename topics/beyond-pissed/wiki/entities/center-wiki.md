---
title: Center Wiki
created: 2026-09-07
updated: 2026-09-10
type: entity
tags: [tool, repo, infra, wiki]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]
confidence: high
---

# Center Wiki

The center wiki is the central workspace and orchestrator Chris wants to use across many simultaneous projects. It currently needs finishing, and at least some changes were reverted, so Chris wants a complete understanding of its current state, intended build/work/use patterns, and the surrounding fixes.

> The center wiki is the central workspace and orchestrator Chris wants to use across many simultaneous projects. It currently needs finishing, and at least some changes were even reverted so there are some things we even need to fix to get back to where we were. So we need to be simultaneously understanding, using and building the center wiki and other projects with the center wiki. ^[raw/inbox/2026-09-07.md]

## Orchestration Vision
Chris explicitly stated the center wiki's purpose as a live orchestrator across multiple simultaneous projects. He instructed: read over the center wiki, what it's supposed to be, and everything related to it and everything that's been built around it, to gain complete understanding. The work requires simultaneously understanding, using, and building the center wiki^[raw/inbox/2026-09-07.md].

## System State and Reverts
The center wiki has reverts that must be recovered before it can safely serve as the orchestrator. Understanding current file and system state is required to get back to where the work was before the reverts. Chris emphasized using "current file/system state for exact details"^[raw/inbox/2026-09-08.md].

## Live File Serving
The system serves `.system-live.json` via a `/file` route. The token used by Hermes changes when `--new-token` is invoked, requiring reads of the new token for continued system state synchronization^[raw/inbox/2026-09-08.md]. Hermes inspected how the `/file` route is handled to understand how `.system-live.json` is served^[raw/inbox/2026-09-08.md].

## Build Around It
Chris's instruction was to understand not only the center wiki itself but everything that has been built around it, and to use it to understand how everything is built and worked^[raw/inbox/2026-09-07.md]. The center vault must also be reviewed to see how the whole thing is built, worked, and used in the current fix process^[raw/inbox/2026-09-06.md].

See also: [[topics/beyond-pissed/wiki/entities/center-vault|Center Vault]], [[topics/beyond-pissed/wiki/concepts/multi-project-orchestration|Multi-Project Orchestration]], [[topics/beyond-pissed/wiki/concepts/readme-rendering-issue|README Rendering Issue]], [[topics/beyond-pissed/wiki/decisions/finish-center-wiki-and-orchestrate|Finish Center Wiki and Orchestrate]]
