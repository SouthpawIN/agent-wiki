---
title: What is still open on the Senter Wiki (as of 2026-09-05 17:53)?
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [question, plan, pain]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Open items

## Needs Chris
- **Spotify client ID** — *"a 2-minute thing only you can do"*: developer.spotify.com → app → redirect `http://127.0.0.1:43827/spotify/callback` → `hermes auth spotify`. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **Merge senter-wiki → senter?** umbrella 0.65 AUTO vs kept apart ([[topics-wiki/senter-wiki/wiki/decisions/2026-09-05-keep-senter-and-senter-wiki-separate|decision page]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **senter-wiki-bot** approval (`agents/senter-wiki-bot.md.proposed`) and 2 skill dedupes. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **Sidebar SOUL rewrite** — yes-and, rubber-duck, never does work, reads INDEX first; text proposed in `agents/README.md`, awaiting approval (open across three passes). ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **LOOPS semantics** — *"we can have a back and forth about concepts"*; only 2 loops had text = name+cadence at the time. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
- *"we're gonna be using the dots for one more thing"* — unspecified. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]

## Engineering, not started / partial
- Kanban claims for topic work (lock files for now) — open in three consecutive passes. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- `hermes serve approval.*` transport — bridge `/approve` is the stand-in (loop `approval-relay`). ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Tag pills (which bot a loop/skill belongs to) clip inside the fixed row → make them a hover card. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
- Browser back doesn't close the editor; reload restores `#bots-profiles/<name>` hash; Enter doesn't search while the editor is open (pre-existing). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Dead code to remove: `.heroOrbsClone` / `--dotsc` mirroring, `wikiIdots()`, `renderContext()` tagging, retired `renderItemRank` path, `#hpEqDemo` button (*"remove once Chris is
  done"*), hardcoded 5-topic `TOPICS`/`rotateHero` table (*"bridged, not yet folded in"*). ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]
- Content-card buttons queued: LOCK via `/write`, HISTORY from log.md, ASK, OPEN IN OBSIDIAN. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Similarity magnitudes low (TF-IDF 0.12 top) — a local embed server would sharpen ranking. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
- Thin-corpus misfiling by the watcher (kashik 0.08) until topics have wiki pages. ^[raw/inbox/2026-09-05.md]
- Fleet gaps for teknium: children attribute as bot=senter; approvals hit the desktop prompt. (memory)

Related: [[topics-wiki/senter-wiki/wiki/entities/headphone-eq|EQ + player]], [[topics-wiki/senter-wiki/wiki/entities/umbrella|umbrella]].

## Known-good, do not touch
Short titles leave air before the chart — *"Chris OK'd for now."* The `#fade` gradient kept but invisible. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]
