---
title: Vault-to-repo mapping (gh-sync, agent-wiki, klerik, senter)
created: 2026-09-09
updated: 2026-09-09
type: concept
tags: [repo, infra, spec, git]
sources: [raw/inbox/2026-09-09.md]
confidence: low
---

# Vault-to-repo mapping (gh-sync, agent-wiki, klerik, senter)

A record of the repository structure that surrounds the Senter vault, as
investigated by Hermes on 2026-09-09 13:15–13:17. ^[raw/inbox/2026-09-09.md]

## The working directory

Chris's active working directory is `~/Documents/Projects/Projects` — the
vault root. This is where every topic, every wiki page, and the bridge/server
code live ([[wiki-topics/senter/wiki/concepts/markdown-is-the-api|markdown is the API]]).

## The gh-sync directory

Hermes observed a `gh-sync` directory containing three separate repos:

- **agent-wiki** — described as "the main repo"
- **klerik** — a separate repo
- **senter** — a separate repo

The exact location of `gh-sync` is unspecified in the raw item; it is
referenced relative to the working directory as a sibling or parent
location.

## open question: is ~/Documents/Projects/Projects the agent-wiki codebase?

Hermes noted the tension: the working directory is `~/Documents/Projects/Projects`,
but the README appears to describe the `agent-wiki` repo as "the agent-wiki
Senter codebase." The question raised:

> This might be a symlink, or the Projects folder might be a different
> location. Let me check what the actual relationship should be and
> initialize git if needed for updates.

Hermes's follow-up action: "Looking at the README, the Projects folder should
be the agent-wiki Senter codebase. Let me initialize it as git and connect it
to the remote."

No resolution is recorded — the investigation was in progress at the time the
raw file was filed.

## git-init resolution (2026-09-09 13:17)

Hermes diagnosed the "updates keep failing" root cause: **the Projects folder was NOT a git repository**, so there was no git to track or push changes. Hermes initialized git and connected it to the remote `https://github.com/SouthpawIN/agent-wiki`. The working directory resolves to itself under `readlink -f` (NOT a symlink). However, the exact relationship between the vault and the `gh-sync` directory's three repos (`agent-wiki`, `klerik`, `senter`) — whether the vault is a worktree, clone, or loose copy — remains unresolved. ^[raw/inbox/2026-09-09.md] ^[raw/inbox/2026-09-09-from-senter-wiki.md]

See [[wiki-topics/senter/wiki/queries/vault-repo-link-status|query: vault-repo link status]] for the standing question and [[wiki-topics/senter/wiki/decisions/2026-09-09-live-data-pipeline-verification|live data pipeline verification]] for the bridge health check that confirmed 35 topics / 69 bots / 201 skills / 81 loops.

## what this means for senter-repo.md

[[wiki-topics/senter/wiki/entities/senter-repo|senter-repo]] documents
`SouthpawIN/senter` as the legacy public repo. The `gh-sync` observation
adds nuance:

- `gh-sync/senter` may be a working clone or mirror of the legacy repo.
- `gh-sync/agent-wiki` is the canonical repo for the agent-wiki spec that
  Chris references throughout ([[wiki-topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]]).
- `gh-sync/klerik` is a separate repo for the klerik bot.

The relationship of the vault (`~/Documents/Projects/Projects`) to
`gh-sync/agent-wiki` — symlink, clone, or separate path — was not resolved
in the raw item. See [[wiki-topics/senter/wiki/queries/vault-repo-link-status|query: vault-repo link status]].

## related

- [[wiki-topics/senter/wiki/entities/senter-repo|senter repo (SouthpawIN/senter)]]
- [[wiki-topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]]
- [[wiki-topics/senter/wiki/entities/senter-bridge|senter-bridge]]
- [[wiki-topics/senter/wiki/comparisons/senter-legacy-repo-vs-current-soul|legacy repo vs current SOUL]]
