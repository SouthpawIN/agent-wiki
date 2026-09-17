---
title: scan-topics.py — the vault scanner
aliases:
  - scan-topics.py scanner + .system-live.json
created: 2026-09-05
updated: 2026-09-10
type: entity
tags: [tool, infra]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-10.md
confidence: high
---

# scan-topics.py — the vault scanner

## What it is
`assets/scan-topics.py --watch 20` (launchd `com.senter.scanwatch`) walks the vault and writes `.system-live.json`, the snapshot [[topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]] renders. `scan-topics.write()` does `live.update(snap)` so keys written by other pipelines (e.g. `similarity`) survive watcher rewrites. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
It watches the vault + `~/.hermes/profiles/*`. Loop page: `loops/scan-watch.md` (custom, KEEP — Hermes has no filesystem hooks). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## What it emits
- **topics** — `text` = README + `.system/context.md` (+ `concept/rules/context/continuity/hermes-native-map.md`; never `session.md`/`queue.md`, 100k+ churn), 40k text cap; `repos_of(readme)` collects frontmatter `repo:` + `## Repos` rows. ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
- **bots** `text` = full SOUL.md; **skills** `text` = full SKILL.md (8k cap); **loops** `desc` = prompt (`scan_loops()`: `~/.hermes/cron/jobs.json` + every `profiles/*/cron/jobs.json` + hooks; plus vault `topics/<t>/loops/*.md` with H1 `# Loop: <name> (owner: <bot>)`). ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
  - Loop pages also carry `## Cadence`, `## Status` → a LOOP row even before a cron exists. `repos_of` result: `REPO[name]='SouthpawIN/'+repos[0]`. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- **usage** — `scan_usage()`: 98-day series per topic/bot/skill from `~/.hermes/state.db` `messages_fts` (read-only sqlite). Feeds the [[topics/senter-wiki/wiki/entities/usage-strip|usage strip]] and the default list order ([[topics/senter-wiki/wiki/concepts/similarity-ranking|similarity and ranking]]). ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]
- **similarity.matrix** — full pairwise TF-IDF from `topic-similarity.py` (pairs-only ≥0.15 could not rank everything). ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## Root fix 2026-09-05
"The scanner only scans `~/.hermes/**/skills` — vault topic skills (the spec's primary location) were never rows." `topics/*/skills/` is now first-class, plus `.proposed` skills/agents/loops so proposals are visible as rows ([[topics/senter-wiki/wiki/concepts/approval-policy|approval policy]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]
Chris's framing: *"the spec's primary skill location was invisible."* Same day: the scanner reads `index.md` as the topic's CONTEXT ([[topics/senter-wiki/wiki/concepts/two-layer-llm-wiki|two-layer wiki]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Pitfalls
- A stale `--watch` process kept overwriting `.system-live.json` with pre-change fields → `pgrep -fl scan-topics`, kill, relaunch (launchd now prevents this). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- 2026-09-10: a stale watch process was overwriting `.system-live.json` with pre-fix bot schema (`skills: []` instead of `skills: 0`). Kill the old process (`pgrep -fl scan-topics`), then restart via launchd so the corrected scanner runs. ^[raw/inbox/2026-09-10.md]
- Add every new snapshot key to the watcher's changed-keys tuple or the UI never refreshes it. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Restarting (`launchctl kickstart -k gui/$(id -u)/com.senter.scanwatch`) needs Chris's approval each time — it kills running agents; batch scanner edits and restart once. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- After writing lane files, confirm in `.system-live.json` that the topic's `text` contains a phrase from the new file and the loops appear in `loops[]`; if not, the include list or the 40k cap is the bug. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
  - (…the bug is the include list or cap — not the watcher.) ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

See also [[topics/senter-wiki/wiki/entities/launchd-services|launchd services]].

## Absorbed
- `entities/scan-topics-scanner` — 2026-09-05 → archived at `topics/_archive/wiki-dedupe/senter-wiki/entities/scan-topics-scanner.md`
