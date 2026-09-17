---
title: Repository Synchronization Discrepancy
created: 2026-09-09
updated: 2026-09-09
type: concept
tags: [infra, pain, question, plan]
sources: [raw/inbox/2026-09-09.md]
confidence: high
---

# Repository Synchronization Discrepancy

The gap between the center vault working directory (`~/Documents/Projects/Projects`) and the `agent-wiki` git repository (`~/gh-sync/agent-wiki`) that prevents updates from proceeding without risking project loss.

## State

- `~/Documents/Projects/Projects` (center vault, where Chris works) was confirmed without `.git` during 2026-09-09 diagnosis, then git was initialized and connected to the remote^[raw/inbox/2026-09-09.md].
- `~/gh-sync/agent-wiki` is a git repo on `main`; both repos share origin `https://github.com/SouthpawIN/agent-wiki`^[raw/inbox/2026-09-09.md].
- `Projects` is not a submodule of `agent-wiki`^[raw/inbox/2026-09-09.md].
- The new live issue is a continuous `scan-topics.py --watch 20` loop repacking data every 20 seconds^[raw/inbox/2026-09-09.md].
- The disconnect is now best described as **state drift and scan-loop staleness**, not network/remote fetch failure^[raw/inbox/2026-09-09.md].

## Impact

Updates were failing because the working directory had no `.git` directory, but that root cause has been addressed in working state. The remaining risk is live data repacking by the watch loop and the absence of an established sync mechanism between working copy and canonical repo^[raw/inbox/2026-09-09.md].

## Open Question

What is the intended build/work/use pattern connecting `~/Documents/Projects/Projects` and `~/gh-sync/agent-wiki`? Should Projects be a submodule, a git-linked worktree, or a separate repo with a sync hook?

See also: [[topics/beyond-pissed/wiki/entities/center-vault|Center Vault]], [[topics/beyond-pissed/wiki/entities/agent-wiki|Agent Wiki]], [[topics/beyond-pissed/wiki/decisions/fix-discrepancy-to-updates|Fix Discrepancy to Updates]], [[topics/beyond-pissed/wiki/queries/fix-integration-usage|Fix Integration Usage]]
