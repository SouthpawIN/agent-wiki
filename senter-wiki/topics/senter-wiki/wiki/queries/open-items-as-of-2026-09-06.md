---
title: Open items and things waiting on Chris (as of 2026-09-06)
created: 2026-09-06
updated: 2026-09-06
type: query
tags: [question, plan, pain]
sources:
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-06.md
confidence: high
aliases:
  - "What is still open on the Senter Wiki (as of 2026-09-06)?"
---

# Open items and things waiting on Chris (as of 2026-09-06)

## Closed since 2026-09-05 19:19
- ~~Row dots expand from hovered dot~~ — implemented with `--orbShift` transform; hovered dot stays under cursor. ^[raw/inbox/2026-09-06.md]
- ~~All markdown renders in CONTEXT card~~ — `window.mdRender` exposed; 256 headings, 404 list items rendered. ^[raw/inbox/2026-09-05.md]
- ~~Content card overlaps chat/player~~ — right edge stops at side chat (4px gap). ^[raw/inbox/2026-09-05.md]
- ~~Wiki row diff badges + usage~~ — implemented without breaking dot column. ^[raw/inbox/2026-09-06.md]
- ~~vault-live.html boot crash~~ — `window.mdRender` binding restored player, settings, wallpaper, nav. ^[raw/inbox/2026-09-06.md]

## Waiting on Chris
- **Spotify client ID** — only he can create it. ^[raw/inbox/2026-09-05.md]
- **Maple MLX Metal kernel fix** — Maple is too slow/OOMs for compression workloads; keep compression on Nous for big contexts or drop Unleashed context window. ^[raw/inbox/2026-09-06.md]
- **Aux vision model** — vision moved to free `stepfun-3.7-flash`; flaky. Chris wants a free Metal-supported alternative. ^[raw/inbox/2026-09-06.md]

## Engineering open
- **Wiki topic live README re-render** — baked HTML doesn't update when README.md changes; need a live `mdRender` step in `openEditor`. ^[raw/inbox/2026-09-06.md]
- **Similarity ranking** — local embed server would sharpen TF-IDF. ^[raw/inbox/2026-09-05.md]
- **Dead code removal** — `.heroOrbsClone` / `--dotsc` mirroring, `wikiIdots()`, hardcoded `TOPICS` table. ^[raw/inbox/2026-09-05.md]
- **Kanban claims / approval transport** — lock files and bridge `/approve` stand-ins. ^[raw/inbox/2026-09-05.md]

## Open conversations
- Where merge/split governance lives now that the umbrella collapsed into the topic agent. ^[raw/inbox/2026-09-05.md]
- "We're gonna be using the dots for one more thing" — unspecified. ^[raw/inbox/2026-09-05.md]

## Absorbed
- `queries/open-items-as-of-2026-09-05` — archived as of this update.
