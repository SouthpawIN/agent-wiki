---
title: vault-live.html (the Senter Wiki surface)
created: 2026-09-05
updated: 2026-09-06
type: entity
tags: [tool, ui, repo, spec]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-06.md
confidence: high
contested: true
---

# vault-live.html

`vault-live.html` is the Senter Wiki: a single-file app (CSS + several `<script>` blocks, ~317 KB after recovery) rendered in the Hermes desktop **preview pane**, fed by `.system-live.json` (written by the scanner, see [[topics/senter-wiki/wiki/entities/scan-topics|scan-topics scanner]]) and by the [[topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]] on `127.0.0.1:8643`. Chris steers it live by voice while watching the pane. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

Chris's framing of what it is: *\"Cursor for markdown\"* / a live second brain — *\"a Cursor x Obsidian setup where everything you talk about gets captured as Topics in a wiki … Jump between topics and it sorts and automates them all, looking for efficiencies and reusable artifacts.\"* ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

## Recovery event (2026-09-06)
A row-geometry experiment damaged the file to 271 KB with no `</style>`. Restores from `/tmp/vault-live.before.html` and `/tmp/vc139.js` regressed the page because they lacked the 2026-09-05 good-state additions. Hermes stopped touching the file, then reconstructed the known-good pieces on a clean backup:
- `window.mdRender` exposure and editor binding fix ^[raw/inbox/2026-09-06.md]
- hover-anchor behavior via `.orbs[data-anchored]` and `--orbShift` ^[raw/inbox/2026-09-06.md]
- diff badges and usage rows injected by `refreshWikiOrbs` ^[raw/inbox/2026-09-06.md]
- chat gutter closed to `right:4px` ^[raw/inbox/2026-09-06.md]
- dot cluster centered with equal auto margins ^[raw/inbox/2026-09-06.md]

The full reconstruction is recorded in [[topics/senter-wiki/wiki/decisions/2026-09-06-vault-live-recovery-and-reconstruction|vault-live recovery and reconstruction]].

## What lives on the page (state at 2026-09-06)
- **One list** — TOPICS, then SKILLS, BOTS, LOOPS sections on the same scrolling `#view-wiki` ([[topics/senter-wiki/wiki/concepts/one-page-navigation-model|one-page navigation model]]).
- **Hero** — the hover-rotating topic title (`#heroTitle`), the blank-band hit target `#heroGap` that starts header search, the four hero orbs
  (`#heroOrbs`) centred on the row-dot column, the overview line `#heroOverview` that peeks the editor card.
- **Rows** — standard anatomy on every page: `[chev][title flex][.sdots tags fixed][.usage fixed 140px][.rdiff fixed 44px][.orbs = anchor]`
  ([[topics/senter-wiki/wiki/concepts/row-geometry-and-dot-column|row geometry]]).
- **HUD cluster** (`#hudCluster`, z120) — gear + media player + volume rocker on one axis top-right "above the girl's head"
  ([[topics/senter-wiki/wiki/entities/hud-cluster|HUD cluster]]).
- **Headphone EQ** (`#hpEq`) — 7×6 black dots on the wallpaper girl's headphone plate, driven by a real Web Audio analyser
  ([[topics/senter-wiki/wiki/entities/headphone-eq|headphone EQ + player]]).
- **Bottom-corner feed** (`#chat .mini .msg` / `#stream .msg`, NOT `.post`) — black cards with 1px paper border, diagonal rest-state mask, z110/z130 open.
- **Cards** — editor card (`#view-editor`, z70) and settings card (`#warnMask.settings`, z90) ([[topics/senter-wiki/wiki/concepts/hover-card-contract|hover-card contract]]).
- **SPACE** — the `#mindmap` star canvas; dead-zone click toggles it; hub → wiki, star → scroll to that topic row.
- **Wallpaper** — `#wallBackdrop`, the ink girl used as a luminance mask over flat `--paper` ([[topics/senter-wiki/wiki/entities/wallpaper-girl|paper palette]]).
^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Z-index ladder (verified 2026-09-06)
HUD 120 · side chat 110 (130 open) · settings 90 · editor card 70 · hero 40 · row icon stacks 30 · star canvas 1 (6 in SPACE).
Clicking the player or feed never cancels the wiki's performance or closes a card — only touching the wiki itself does. ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Data inputs
- `.system-live.json` — topics (text = README + `.system/context.md`), bots (full SOUL.md), skills (SKILL.md ≤8k), loops, `similarity.matrix`, `usage` series.
- Bridge events (`/events`) — message/tool/skill/approval/bridge/wiki(stage) kinds.
- `index.md` per topic — rendered whole as the row's CONTEXT section; orb count = page count ([[topics/senter-wiki/wiki/concepts/two-layer-llm-wiki|two-layer LLM wiki]]). ^[raw/inbox/2026-09-05.md]

## Row diff + sort behavior (2026-09-06)
`refreshWikiOrbs` injects `.usage` then `.diffbadge` before `.tname`; `.rdiff` is a fixed 44px slot so usage and dots never shift. Diff values persist 24h via `localStorage('sw.diffs')` and decay to zero; the default neutral sort is `decayedDiff` → usage → updated date. The right-anchor selector `.usage + .orbs { margin-left:0; width:164px; flex:0 0 164px; justify-content:flex-end; }` keeps the dot column at the same x. ^[raw/inbox/2026-09-06.md]

## Processes around it
- bridge: launchd `com.senter.bridge` · scanner: `com.senter.scanwatch` (`scan-topics.py --watch 20`) · watcher `com.senter.watcher` · topic-worker (5 min) · umbrella (30 min) · topic-wiki compile (15 min).
- Force pane reload: `touch ~/.hermes/senter-bridge/preview-reload-needed` or `drive_preview reload`. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

## Conventions inside the file
- Code comments are dated and quote Chris: `/* 2026-09-03 (Chris): \"…\" */` — *\"it's how he audits intent later.\"*
- Every tunable is a named CSS var knob (`--paper`, `--bandInset`, `--usageW`, `--volLen`, `--eqCX/CY`, `--setNudge`, `--gearSize`, …); the skill `wiki-ui-knobs` lists them.
- Temp hooks are tagged `TEMP-…` and stripped with an `assert 'TEMP-' not in s`. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## MVP checkpoint
2026-09-03 ~20:40 — Chris: *\"the UI is at a good enough spot that we can start working on the back end.\"* UI asks from there are polish, not redesign
([[topics/senter-wiki/wiki/decisions/2026-09-03-mvp-checkpoint-backend-phase|MVP checkpoint decision]]). ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
