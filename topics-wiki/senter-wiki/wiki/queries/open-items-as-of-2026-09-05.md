---
title: "Open items and things waiting on Chris (as of 2026-09-05 19:19)"
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [question, plan, pain]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
aliases:
  - "What is still open on the Senter Wiki (as of 2026-09-05 17:53)?"
---

# Open items and things waiting on Chris (as of 2026-09-05 19:19)

> Superseded by [[topics-wiki/senter-wiki/wiki/queries/open-items-as-of-2026-09-06|open items 2026-09-06]]. Archived for provenance; do not edit.

## Chris's latest asks (19:06–19:18), not yet reported done
- **Row dots expand from the hovered dot** — *"when I hover over the third dot and it expands, the third dot should still be under my mouse."* [[topics-wiki/senter-wiki/wiki/decisions/2026-09-05-row-dots-expand-from-hovered-dot|decision]] ^[raw/inbox/2026-09-05.md]
- **All markdown renders in the CONTEXT card** — *"the title is actually pop up as titles on this stuff within the context."* Hermes was checking `md()` vs page syntax at 19:19. [[topics-wiki/senter-wiki/wiki/entities/context-card-live-diff|live diff card]] ^[raw/inbox/2026-09-05.md]
- **Pre-prompting / pre-planning for the compile step**, "useful for anyone" — [[topics-wiki/senter-wiki/wiki/concepts/compile-pre-planning|compile pre-planning]]. ^[raw/inbox/2026-09-05.md]
- **"organize this by sections and command"** — sections done; "command" undefined. ^[raw/inbox/2026-09-05.md]
- Context orb number vs *"I don't want any numbers indicating what's in the wiki"* — unsettled ([[topics-wiki/senter-wiki/wiki/decisions/2026-09-05-context-is-the-wiki-with-live-diffs|contested decision]]).
- ~~Card overlaps chat/player~~ and ~~CONTEXT as index list~~ — closed 19:12, DOM-proven (card edge 684 vs chat 698; pages rendered by section with live `+N −M` diffs). ^[raw/inbox/2026-09-05.md]

## Waiting on Chris
- **Spotify client ID** — only he can create it (developer.spotify.com → app → redirect `http://127.0.0.1:43827/spotify/callback` → `hermes auth spotify`). [[topics-wiki/senter-wiki/wiki/entities/music-player|music player]] ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **senter-wiki → senter merge** — umbrella says merge (0.65); Senter kept apart; veto file `topics-wiki/_global/.system/keep-separate.md`. [[topics-wiki/senter-wiki/wiki/decisions/2026-09-05-keep-senter-and-senter-wiki-separate|decision (contested)]] ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **`senter-wiki-bot`** promotion (4 skills, no agent) — APPROVE/REJECT card. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **Two skill dedupes** proposed by the umbrella. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **Sidebar SOUL rewrite** — proposed text in `topics-wiki/senter-wiki/agents/README.md`. [[topics-wiki/senter-wiki/wiki/entities/sidebar-agent|sidebar agent]] ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Not done (engineering)
- Kanban claims — lock files for now; restated 19:12 as the next native candidate ([[topics-wiki/senter-wiki/wiki/concepts/collapse-toward-hermes-native|collapse toward native]]). ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]
- `hermes serve approval.*` transport — bridge `/approve` is the stand-in; restated 19:12. ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]
- Watcher thin-corpus misclassification (kashik 0.08) — self-heals as wikis fill. ^[raw/inbox/2026-09-05.md]
- Wiki record of the newly live crons (which two loops, which third bot) — "Update the wiki's record" was the stated next step; the raw does not name them. ^[raw/inbox/2026-09-05.md]
- Within-topic duplicate pages from two compiles over one raw set ([[topics-wiki/senter-wiki/wiki/queries/duplicate-page-candidates|17 candidate pairs]]).
- Dead code to remove when convenient: `.heroOrbsClone` / `--dotsc` mirroring, `wikiIdots()`, hardcoded 5-topic `TOPICS`/`rotateHero` table (bridged, not folded in). ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
- `.sdots` tag pills clip in the fixed row → planned hover card like the old GitHub mark. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
- Editor-card buttons queued: LOCK (bridge `/write`), HISTORY (log.md), ASK, OPEN IN OBSIDIAN. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Open conversations
- Where merge/split governance lives now that the umbrella collapsed into the topic agent — surfaced by the senter compile, unanswered. ^[raw/inbox/2026-09-05.md]
- LOOPS semantics — "we can have a back and forth about concepts". ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
- "we're gonna be using the dots for one more thing" — unspecified. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]

## Earlier snapshot (17:53)
Folded from `open-items-2026-09-05`. Status as recorded at 17:53; items not struck through above were still open at 19:19 — nothing here is marked closed unless the sections above say so.

### Needs Chris (17:53)
- **Spotify client ID** — *"a 2-minute thing only you can do"*: developer.spotify.com → app → redirect `http://127.0.0.1:43827/spotify/callback` → `hermes auth spotify`. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **Merge senter-wiki → senter?** umbrella 0.65 AUTO vs kept apart ([[topics-wiki/senter-wiki/wiki/decisions/2026-09-05-keep-senter-and-senter-wiki-separate|decision page]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **senter-wiki-bot** approval (`agents/senter-wiki-bot.md.proposed`) and 2 skill dedupes. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **Sidebar SOUL rewrite** — yes-and, rubber-duck, never does work, reads INDEX first; text proposed in `agents/README.md`, awaiting approval (open across three passes). ^[raw/inbox/2026-09-05-legacy-inbox.md]
- **LOOPS semantics** — *"we can have a back and forth about concepts"*; only 2 loops had text = name+cadence at the time. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
- *"we're gonna be using the dots for one more thing"* — unspecified. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]

### Engineering, not started / partial (17:53)
- Kanban claims for topic work (lock files for now) — open in three consecutive passes. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- `hermes serve approval.*` transport — bridge `/approve` is the stand-in (loop `approval-relay`). ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Tag pills (which bot a loop/skill belongs to) clip inside the fixed row → make them a hover card. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
- Browser back doesn't close the editor; reload restores `#bots-profiles/<name>` hash; Enter doesn't search while the editor is open (pre-existing). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Dead code to remove: `.heroOrbsClone` / `--dotsc` mirroring, `wikiIdots()`, `renderContext()` tagging, retired `renderItemRank` path, `#hpEqDemo` button (*"remove once Chris is done"*), hardcoded 5-topic `TOPICS`/`rotateHero` table (*"bridged, not yet folded in"*). ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md] ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md]
- Content-card buttons queued: LOCK via `/write`, HISTORY from log.md, ASK, OPEN IN OBSIDIAN. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Similarity magnitudes low (TF-IDF 0.12 top) — a local embed server would sharpen ranking. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
- Thin-corpus misfiling by the watcher (kashik 0.08) until topics have wiki pages. ^[raw/inbox/2026-09-05.md]
- Fleet gaps for teknium: children attribute as bot=senter; approvals hit the desktop prompt. (memory)

### Known-good, do not touch (17:53)
Short titles leave air before the chart — *"Chris OK'd for now."* The `#fade` gradient kept but invisible. ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]

Filed because these are the questions Chris will ask next session; update rather than duplicate.

## Absorbed
- `queries/open-items-2026-09-05` — archived at `topics-wiki/_archive/wiki-dedupe/senter-wiki/queries/open-items-2026-09-05.md`
