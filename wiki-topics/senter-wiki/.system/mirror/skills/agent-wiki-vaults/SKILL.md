---
name: agent-wiki-vaults
description: Build agent-wiki (GOOP) Obsidian vaults from GitHub repos.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [obsidian, agent-wiki, goop, github, vault, knowledge-base]
---

# Agent-Wiki Vaults

Build and maintain Obsidian vaults following the [agent-wiki](https://github.com/SouthpawIN/agent-wiki) (GOOP) spec: markdown is the API, the wiki is the system, topics are self-contained. Use when organizing a user's projects/repo knowledge into a wiki vault (canonical example: `~/Documents/Projects/Projects`, user SouthpawIN).

## Canonical structure

```
vault/
├── index.md                  ← single entry point
├── catalogs/                 ← fleet-dashboard, topic-index, agent-roster,
│                                skill-registry, loop-registry
├── wiki-topics/<topic-slug>/      ← one topic per repo/source
│   ├── README.md             ← human dashboard (facts + source extract)
│   ├── .system/              ← hidden machine internals
│   │   ├── continuity.md     ← agent's raw understanding (user-correctable)
│   │   ├── queue.md          ← [SKILLS]/[AGENTS]/[LOOPS] work items
│   │   └── injections.md     ← status feed ([UNREAD]/[READ])
│   └── skills-capabilities/ agents/ triggers-loops/
├── wiki-topics/_global/.system/   ← mirrors of the catalogs
├── agent-wiki-spec.md  Sources.md  Ideas.md  log.md
```

## Deep-pull workflow (GitHub source)

1. **Discover repos via API, not the web UI** — `api.github.com/users/<user>/repos?per_page=100&page=N` returned 54 repos where the rendered repos page showed ~43. Sort by `pushed` desc. Unauthenticated core limit 60/hr is enough for metadata; do NOT use the API for READMEs.
2. **READMEs via raw.githubusercontent.com** — `<user>/<repo>/<branch>/README.md`, trying default branch, `main`, `master`. Not rate-limited. Fall back to the API `readme` endpoint (base64) only if raw 404s.
3. **Classify status from `pushed_at`**: ACTIVE (pushed this month), ARCHIVED, else DORMANT (since date).
4. **Build in one scripted pass**: per-topic dashboards with cleaned README extract (strip frontmatter/badges/images/HTML), facts block (language, stars, forks, license, fork-parent, created/last-push, status), `.system/` trio, empty skills-capabilities/agents/loops dirs, catalogs, `_global` mirrors, index/Sources/Ideas/log. ~400 files for a 50-repo account.
5. **Record the vault path in memory** — the vault becomes a session canvas; user edits `.system/continuity.md` to steer the agent.

## Conventions that matter

- `.system/` is dot-prefixed → hidden in Obsidian by design; that's the debugger, keep the front-end README clean.
- Queue format: `- [ ] alias — why` under `## [SKILLS]` / `[AGENTS]` / `[LOOPS]`. Only the agent creates entries; factories claim `[~]`, done `[x]`.
- Injections: new status under `## [UNREAD]`, moved to `## [READ]` after surfacing in chat.
- Log every build pass to `log.md` with date + what changed.
- Evidence records pinned to a machine are machine-specific: a "successful runtime profile" measured on `/home/<user>` Linux is not evidence for a different host class.

## When to use

- User asks to organize their projects/ideas/repos into their Obsidian vault ("build the vault", "organize my GitHub into the wiki").
- User's vault follows the agent-wiki/GOOP structure (wiki-topics/, catalogs/, .system/) and needs a pull, refresh, or new topic.
- User says a repo/topic should be documented "like the wiki describes".

Scripts: `scripts/github-deep-pull.py collect` (API + raw READMEs → JSON cache), then `... build` (topics + catalogs from cache).

## Working as the live session canvas

Once the vault exists, it is the ongoing workspace, not a one-shot build:

- Edit notes live in the vault while the user watches in Obsidian — the user's edits to
  `.system/continuity.md` and `queue.md` are the steering wheel; honor them over code/chat defaults.
- When a working session uncovers fixes (bugs, discrepancies, upstream issues), document them
  IN the vault as they happen: numbered candidates in the relevant topic's `.system/queue.md`,
  continuity updates in `.system/continuity.md`, reusable procedures in `wiki-topics/<t>/skills-capabilities/`.
- The user may issue architectural directives that override repo defaults — record them in
  continuity as authority ("user directive: X over code default Y").
- Re-read a queue file before patching: the user or a parallel process may have edited it.

## Pitfalls

- Mac system Python is 3.9 — GOOP/turbofit-style code using `int | str` type unions needs 3.10+. Create a `uv venv --python 3.12` in the cloned repo rather than fighting system Python.
- Some repos ship no pyproject.toml/requirements — install minimal deps (e.g. pyyaml) into that venv.
- Don't keep both a Home.md and an index.md entry point — pick one and remove the stale file (Obsidian shows both).
