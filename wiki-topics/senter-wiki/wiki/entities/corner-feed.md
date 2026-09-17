---
title: Corner feed (#chat .mini) — how Chris sees the fleet work
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui]
sources:
  - raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/ref-vault-live-demo-video.md
confidence: high
---

# Corner feed (#chat .mini) — how Chris sees the fleet work

## What it is
The bottom-corner stack of bot cards (`#chat .mini .msg` / `#stream .msg` — NOT `.post`, the retired Feed page). Chris: the Feed page is gone; "the Feed is the bottom-corner feed" ([[wiki-topics/senter-wiki/wiki/concepts/one-page-navigation-model|navigation model]]). Fed by [[wiki-topics/senter-wiki/wiki/entities/senter-bridge|bridge]] `/post` and events. ^[raw/sources/knowledge/ref-vault-live-eq-feed-2026-09-03.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

## Style
Cards `background:#000; border:1px solid #fff`, `.who` white — the retired hover-card look "moved to the feed". Rest-state fade is ONE `mask-image` on the stack: `to top left, #000 12%, rgba(0,0,0,.5) 42%, transparent 82%`; hover/pin = mask off. Chris: "the bottom-right corner right white, more extreme gradient going diagonal towards the upper left getting darker", then "No, I like that fade … a degree or two stronger." Lesson: never soften a fade he said he liked. ^[raw/sources/knowledge/ref-vault-live-hud-2026-09-03.md]

## Behaviour
- Expanded (`#chat.open`) out-ranks everything (z80 vs card 70; z110/130 since 2026-09-05) and hides `#hudCluster` — "the media player is still visually in the way". ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Approval cards are `#FFE45A` yellow with APPROVE / REJECT ([[wiki-topics/senter-wiki/wiki/concepts/approval-policy|approval policy]]); one card per proposal so "the feed moves constantly". ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/sources/knowledge/ref-vault-live-demo-video.md]
- 2026-09-05 17:33: receiving fleet posts — "43 senter messages, 17 wiki stage events in the last window", plus GitHub items. "It updates as you talk." ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Clicking the feed never cancels the wiki's performance ([[wiki-topics/senter-wiki/wiki/concepts/ui-performs-the-fleet|UI performs the fleet]]) and never closes a card. ^[raw/inbox/2026-09-05-legacy-inbox.md]

Related: [[wiki-topics/senter-wiki/wiki/entities/sidebar-agent|sidebar]] (the Hermes chat, separate from this in-page feed); `senter-feed-relay.py` for bot → Hermes-chat delivery.
