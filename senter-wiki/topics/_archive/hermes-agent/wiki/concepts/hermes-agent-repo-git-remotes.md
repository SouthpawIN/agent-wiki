---
title: "hermes-agent Repo Git Remotes — 2026-09-10"
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [tool, infra, repo, plan]
sources: ["raw/inbox/2026-09-10.md"]
confidence: medium
---

# hermes-agent Repo Git Remotes — 2026-09-10

Investigated on `2026-09-10` whether the `gh-sync/agent-wiki` repo is the same as the Hermes Agent checkout. Findings:

- The `agent-wiki` repo is a **separate** repo from the Hermes Agent checkout.
- The Hermes Agent checkout at `~/.hermes/hermes-agent` is a git repo with **two remotes**:
  - `fork` → `https://github.com/SouthpawIN/hermes-agent.git` (Chris's fork)
  - `origin` → `https://github.com/NousResearch/hermes-agent.git` (official)
- The checkout was parked on branch `preview-composer-bridge-rebase` with uncommitted kanban changes, which blocked the updater from switching to `main` (dirty working tree).

## Resolution
- Changes were applied cleanly via stash; `origin/main` reached "already up to date" and Chris's changes preserved. A working-tree conflict remained briefly after.^[raw/inbox/2026-09-10.md]

## Significance for this topic
- The repo maintenance pattern: keep a personal `fork`, track official `origin`, and never let a dirty working tree block the upstream update. Aligns with the standing preference for markdown + built-in tooling over custom code, and the upstreaming of core gaps via the PR ledger rather than in-session PRs.
- This is hermes working (evidence about the repo), not a request to act.

## Related
- [[topics/hermes-agent/wiki/entities/model-check-20260903|Model Check — 20260903_001447_7bc70a]]
- [[topics/hermes-agent/wiki/concepts/active-model-provider-churn|Active Model / Provider Churn]]
