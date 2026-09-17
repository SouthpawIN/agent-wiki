---
title: 2026-09-10 — Hermes update blocked by parked branch + dirty tree (Senter Wiki is a separate repo)
created: 2026-09-10
updated: 2026-09-10
type: decision
tags: [decision, infra, hermes-agent, update, git, repo, resolved]
sources: [raw/inbox/2026-09-10.md]
confidence: high
---

# 2026-09-10 — Hermes update blocked by parked branch + dirty tree (Senter Wiki is a separate repo)

## The ask (Chris)

Chris, 2026-09-10 14:26: **"I need you to find what is blocking Hermes-Agent from updating, it might be my project here, which I do not want erased for the sake of updating, simply fix the discrepancy between the update and the Senter Wiki."** ^[raw/inbox/2026-09-10.md]

Root cause: the blocker was **not** the Senter Wiki project.

## Root cause

The **Hermes Agent checkout** (`~/hermes/hermes-agent`) — a *separate repo* from the Senter Wiki — was:
1. **Parked on a feature branch** `preview-composer-bridge-rebase` (not `main`).
2. **Dirty** with uncommitted changes (`hermes_cli/kanban_db.py`, `tools/kanban_tools.py`, `tools/kanban_tools_schemas.py` — kanban batch-creation feature work).

The updater (`hermes update --branch main`) refuses to switch to a clean `main` when the working tree is dirty, so the update **skipped** and `pre_update_backup` reported `ok: false` (config had `updates.pre_update_backup: False`). The `.update_check` file showed `behind: 1328` commits. ^[raw/inbox/2026-09-10.md]

The **Senter Wiki** (`~/gh-sync/agent-wiki`, GitHub `SouthpawIN/agent-wiki`) is a completely separate repository and was **never in danger** — it has its own clean working tree with one unpushed commit. The "discrepancy" was Hermes conflating its own parked checkout with the Senter Wiki project. ^[raw/inbox/2026-09-10.md]

## The fix (done)

1. Stashed the kanban changes.
2. Ran `hermes update --yes` → updated to **v0.21.1 (2026.9.7)** on `main @ 564aef2946`.
3. Restored the kanban changes via `git stash pop`.
4. Leftover autostash from 2026-08-27 (`hermes-update-autostash-20260827-165114`) still sits in the stash — review with `git stash show -p stash@{2}`, drop if stale.

**Result:** Hermes Agent updated; Senter Wiki untouched (still at `05ac790`). ^[raw/inbox/2026-09-10.md]

## Scope note

The *mechanism* (parked branch, dirty tree, `updates.auto_switch_parked_branch`, `pre_update_backup`) is **Hermes Agent internals** → `hermes-agent` per anti-scope. It's recorded here because Chris framed it as "the discrepancy between the update and the Senter Wiki" and the repo-mapping (Hermes Agent vs Senter Wiki as two repos) is a `senter` fact. See also [[topics/senter/wiki/concepts/vault-repo-mapping|vault-repo mapping]].
