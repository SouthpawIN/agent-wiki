---
title: Apply path proven (2026-09-05 18:57) — two loops registered, gateways auto-installed, three bots with live crons
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [loop, bot, infra, timeline, question]
sources:
  - raw/inbox/2026-09-05.md
confidence: medium
---

# Apply path proven (18:57) — loops registered, gateways auto-installed, three bots with live crons

## What the raw says
At 18:57 the assistant reported the outcome of the card resolution planned at 18:18 ([[topics/senter-wiki/wiki/decisions/2026-09-05-resolve-cards-and-prove-apply-path|decision]]): "Both loops registered and gateways for paladin and looker auto-installed by the apply path. Three bots now have live crons that actually fire." The next step named in the same breath: "Update the wiki's record and check the feed/UI state". ^[raw/inbox/2026-09-05.md]

## What this proves
- The approval pipeline — card → [[topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]] `POST /approve` → `.proposed` dropped → apply — has now been followed through to an effect outside the vault for the first time: loops became registered Hermes crons, not just un-suffixed files. Until 18:57 the pipeline was DOM-verified only ([[topics/senter-wiki/wiki/decisions/2026-09-05-resolve-cards-and-prove-apply-path|decision]], "Why"). ^[raw/inbox/2026-09-05.md]
- The apply path does more than rename: it **auto-installs a gateway** for a bot's profile when a loop needs one (paladin, looker). This is new behaviour not recorded in the bridge's endpoint table and worth folding in there. ^[raw/inbox/2026-09-05.md]
- "Three bots now have live crons that actually fire" — read against the [[topics/senter-wiki/wiki/entities/fleet-bots|fleet roster]]: the two named (paladin, looker) plus one already-cronned bot; the raw does not name the third. ^[raw/inbox/2026-09-05.md]

## What it does NOT yet prove (open)
- Which two loops were registered is not stated. The 18:18 plan named `klerik-queue-drain` as the loop to approve; whether it was one of the two is inferred, not recorded. ^[raw/inbox/2026-09-05.md]
- "Prove a bot apply end-to-end on a real approval" (18:18) — the 18:57 line covers loops and gateways; a *bot* apply (promotion of e.g. `senter-wiki-bot`) is not claimed. Still open in [[topics/senter-wiki/wiki/queries/open-items-as-of-2026-09-05|open items]].
- By Chris's proof standard ([[topics/senter-wiki/wiki/concepts/verification-and-proof-methods|verification and proof methods]]) a cron "actually fires" only when its firing shows in the corner feed / wiki in his window; the 18:57 report is a backend claim, and "check the feed/UI state" was still the pending step. Confidence on this page is therefore **medium**.

## Where this sits in the timeline
17:43 raw layer + compile loop → 18:14 first compiles land → 18:18 card-resolution plan → **18:57 apply path proven for loops + gateways**. Continues [[topics/senter-wiki/wiki/queries/timeline-2026-09-03-to-05|the 09-03→05 timeline]].
