---
title: The UI performs the fleet (stage events, feed, motion)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, infra, idea]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
  - raw/sources/knowledge/ref-vault-live-demo-video.md
confidence: high
---

# The UI performs the fleet

Chris's expectation: watch fixes and fleet work land live in the wiki while he talks. On 2026-09-05 the assistant diagnosed *"why you weren't seeing motion before:
proposals were only files + feed cards; nothing told the wiki to move."* ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Stage events
Bridge `POST /stage` → `window.stage()`: the row scrolls into view, its card peeks open, changed text typewriters in, the card closes. Emitters: every watcher filing,
every worker skill/continuity write, every compile. DOM-verified live on TURBOFIT. **You always win**: any pointer-down or pinned card kills the queue; clicking the player
or feed never cancels the performance or swallows a card. Skill: `wiki-event-performance` (*"never animate from fake or polled state"*). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Feed
Watcher, worker, umbrella, stage events and GitHub items all reach the bottom-corner feed via `/post` — last window: 43 senter posts, 17 stage events. *"It updates as you
talk."* Verify by cross-checking `/post` arrivals against the events log and DOM (skill `wiki-feed-verify`). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Live diffs (19:12)
The strongest form of "performing" so far: the topic agent diffs every page it changed and the CONTEXT card repaints them GitHub-style — removed lines red/struck, added green, `+N −M` by the title, settling after 6 s; a closed card peeks 9 s unless one is pinned. Chris: *"just actually watch the wiki get edited."* Details: [[topics-wiki/senter-wiki/wiki/entities/context-card-live-diff|context card live diff]]. ^[raw/inbox/2026-09-05.md]

## Event shapes `handle(ev)` accepts
`message` (feed card + orb light + star pulse) · `tool` start/end · `skill` · `approval` pending → yellow card, decided → accepted · `bridge surface` · `wiki` (stage) · `diff` (page repaint, added 19:12). All
need `ts` (dedupe key `ts|kind|id/tool/phase`). The demo recipe drives this REAL pipeline via `window.__senterHandle` — *"never fake DOM"*
([[topics-wiki/senter-wiki/wiki/concepts/demo-video-recipe|demo video recipe]]). ^[raw/sources/knowledge/ref-vault-live-demo-video.md]

Related: [[topics-wiki/senter-wiki/wiki/entities/senter-bridge|senter-bridge]], [[topics-wiki/senter-wiki/wiki/entities/senter-watcher|watcher]].
