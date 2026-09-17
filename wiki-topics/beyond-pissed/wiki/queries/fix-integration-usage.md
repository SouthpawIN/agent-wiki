---
title: Fix Integration Usage
created: 2026-09-06
updated: 2026-09-10
type: query
tags: [question, plan]
sources: [raw/inbox/2026-09-06.md, raw/inbox/2026-09-08.md, raw/inbox/2026-09-09.md, raw/inbox/2026-09-10.md]
confidence: medium
---
# Fix Integration Usage

What is the intended build/work/use pattern of the center vault in the current fix pipeline?

<!-- chris --> You need to look through the center vault and see how this whole thing will be built and how it's supposed to be worked and how it's supposed to be used in that process right now in the fixes. ^[raw/inbox/2026-09-06.md]

## Current State

Chris emphasized using "current file/system state for exact details" — never operate on stale assumptions^[raw/inbox/2026-09-08.md].

## Repository Structure Discrepancy

Hermes found that `~/Documents/Projects/Projects` was not a git repository, then initialized git and connected it to origin (`https://github.com/SouthpawIN/agent-wiki`)^[raw/inbox/2026-09-09.md]. `~/gh-sync/agent-wiki` is also on `main` with the same origin^[raw/inbox/2026-09-09.md]. `Projects` is still not a submodule of `agent-wiki`^[raw/inbox/2026-09-09.md]. The open issue is now the intended sync mechanism and handling live scan-loop output. On 2026-09-10 Hermes continued verifying the git state and the JSON file directly alongside this effort^[raw/inbox/2026-09-10.md].

See also: [[wiki-topics/beyond-pissed/wiki/entities/center-vault|Center Vault]], [[wiki-topics/beyond-pissed/wiki/decisions/ship-today|Ship Today]], [[wiki-topics/beyond-pissed/wiki/entities/center-wiki|Center Wiki]], [[wiki-topics/beyond-pissed/wiki/concepts/multi-project-orchestration|Multi-Project Orchestration]], [[wiki-topics/beyond-pissed/wiki/decisions/fix-discrepancy-to-updates|Fix Discrepancy to Updates]]
