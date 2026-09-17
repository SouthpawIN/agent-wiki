---
title: Layout for bots and sessions — how the one-page model frames them
created: 2026-09-09
updated: 2026-09-09
type: concept
tags: [ui, question, spec]
sources:
  - raw/inbox/2026-09-09.md
confidence: high
---

# Layout for bots and sessions — how the one-page model frames them

Chris: *\"ok so how do I see my bots and sessions in this layout? Look at the Hermes Desktop and fix the layout, also My updates keep failing. I think that's something to do with the project that we're working on.\"* ^[raw/inbox/2026-09-09.md]

> This is a **layout** question, not a new feature ask — Chris is asking where **bots** and **sessions** already live within the one-page navigation he locked in on 2026-09-03 ([[topics-wiki/senter-wiki/wiki/concepts/one-page-navigation-model|navigation model]]). The answer already exists; the gap is discoverability.

## Where each lives (per the one-page model)
|- **Bots → BOTS section**. The four hero orbs (TOPICS · SKILLS · BOTS · LOOPS) are section selectors on the single wiki list. Clicking BOTS (`showView('bots')`) re-sorts the same row list to bots, sorted by SOUL role text, not title ([[topics-wiki/senter-wiki/wiki/entities/fleet-bots|fleet bots]], [[topics-wiki/senter-wiki/wiki/concepts/one-page-navigation-model|navigation]]). The standard row anatomy (`.tname` → `.sdots` → `.usage` → `.rdiff` → `.orbs`) is reused unchanged — no special bot row template. ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
|- **Sessions → CORNER FEED**. Sessions are not a separate page. They surface as the bottom-corner stack of bot cards (`#chat .mini .msg`) — the live stream of dispatched tasks, approvals, and card activity. The Feed page was retired: *"the Feed is the bottom-corner feed."* ([[topics-wiki/senter-wiki/wiki/entities/corner-feed|corner feed]])
|- **Both → side chat is separate**. The Hermes desktop sidebar (the conversational `senter` front) is distinct from the in-page corner feed; the corner feed is the wiki surface for fleet activity. ([[topics-wiki/senter-wiki/wiki/entities/sidebar-agent|sidebar agent]])

## What Chris's question triggered (2026-09-09)
Chris's 13:01 question *"ok so how do I see my bots and sessions in this layout?"* combined with *"My updates keep failing"* led to a deeper inspection of the workspace and vault-live.html. This surfaced three additional findings beyond the navigation answer:

1. **Update failures — root cause:** the vault `~/Documents/Projects/Projects/` was not a git repository ([[topics-wiki/senter-wiki/wiki/decisions/2026-09-09-vault-git-init|git init]]).
2. **Bridge FILE_CAP bypass:** `.system-live.json` (~2.8 MB) was rejected with HTTP 413 by the 2 MB `/file` cap; patched to bypass for that file. ([[topics-wiki/senter-wiki/wiki/entities/senter-bridge|bridge FILE_CAP fix]])
3. **Incomplete orb rename:** the `mkTopic()` JS factory still emits `data-k="ctx"` and `data-k="agents"` even though baked rows use `data-k="wiki"` and `data-k="bots"` ([[topics-wiki/senter-wiki/wiki/entities/orb-label-renaming|orb label renaming]]).

## Related
|- [[topics-wiki/senter-wiki/wiki/concepts/standard-row-anatomy|Standard row anatomy]] — every page has exactly the same layout; bots reuse `mkTopic()+initTopic()`.
|- [[topics-wiki/senter-wiki/wiki/concepts/wiki-page-quality-bar|Wiki page quality bar]] — a page that only restates is below the bar; it should surface the next question.
