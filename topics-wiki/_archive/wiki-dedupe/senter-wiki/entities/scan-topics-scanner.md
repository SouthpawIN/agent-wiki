---
title: scan-topics.py scanner + .system-live.json
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [tool, infra]
sources:
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# scan-topics.py scanner

`assets/scan-topics.py --watch 20` (launchd `com.senter.scanwatch`) watches the vault + `~/.hermes/profiles/*` and rewrites `.system-live.json`;
[[topics-wiki/senter-wiki/wiki/entities/vault-live-html|the page]] re-renders from it. Loop page: `triggers-loops/scan-watch.md` (custom, KEEP — Hermes has no filesystem hooks). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## What it emits
- `topics[]` with `text` = README + `.system/context.md` (+ concept/rules/continuity/hermes-native-map; never session.md/queue.md — 100k+ churn; 40k cap).
- `bots[]` text = full SOUL.md; `skills[]` text = full SKILL.md (8k cap); `loops[]` from `~/.hermes/cron/jobs.json`, every `profiles/*/cron/jobs.json`,
  hooks, and vault `topics-wiki/*/triggers-loops/*.md` (H1 `# Loop: <name> (owner: <bot>)`, `## Cadence`, `## Status` → a LOOP row even before a cron exists).
- `similarity.matrix` — full pairwise TF-IDF (the thresholded `pairs` could not rank everything); `scan-topics.write()` does `live.update(snap)` so the key survives.
- `usage` — `scan_usage()`: 98-day per-item-per-day mention series from `~/.hermes/state.db messages_fts` (read-only sqlite); paints the heat strip and drives the default sort.
- `repos_of(readme)` — frontmatter `repo:` + `## Repos` table rows; `REPO[name]='SouthpawIN/'+repos[0]`. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Fixes on 2026-09-05
- **Root fix**: `topics-wiki/*/skills-capabilities/` was never scanned — *"the spec's primary skill location was invisible."* Now first-class, plus `.proposed` skills-capabilities/agents/loops
  as PROPOSED rows. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Reads `index.md` as the topic's CONTEXT ([[topics-wiki/senter-wiki/wiki/concepts/two-layer-llm-wiki|two-layer wiki]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Pitfalls
- Add every new snapshot key to the watcher's changed-keys tuple or it never refreshes.
- A stale `--watch` process kept overwriting the file with pre-change fields → `pgrep -fl scan-topics`; launchd now prevents recurrence.
- **Restarting** (`launchctl kickstart -k gui/$(id -u)/com.senter.scanwatch`) needs Chris's approval each time (kills running agents) — batch edits, restart once.
- After writing lane files, confirm in `.system-live.json` that the topic `text` contains a phrase from the new file and new loops appear in `loops[]`;
  if not, the include list or 40k cap is the bug, not the watcher. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
