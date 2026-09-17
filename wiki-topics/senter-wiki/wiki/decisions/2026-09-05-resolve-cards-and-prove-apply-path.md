---
title: Decision 2026-09-05 18:18: resolve the pending cards by proving the apply path, not by clearing them
created: 2026-09-05
updated: 2026-09-05 18:57
type: decision
tags: [decision, loop, bot, plan]
sources:
  - raw/inbox/2026-09-05.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: medium
---

# Decision 2026-09-05 18:18: resolve cards by proving the apply path

## What
After the compiles landed, the next step recorded for the pending APPROVE/REJECT cards was: "approve `klerik-queue-drain` (proves the loop apply path live), reject the ones I just did myself, and prove a bot apply end-to-end on a real approval". Each pitch is one card with APPROVE/REJECT; skills auto-apply without a card. ^[raw/inbox/2026-09-05.md]

## Why
Approvals exist only for bots and loops because "they cost money and run unattended" ([[wiki-topics/senter-wiki/wiki/decisions/2026-09-05-approvals-only-bots-and-loops|decision]]). The bridge's `POST /approve` had been DOM-verified to show cards and rows, but no approval had yet been followed through to a bot actually *doing* the approved thing — which by Chris's rule ("a fix he can't see = not done") means the approval pipeline was unproven. Approving a real loop (`klerik-queue-drain`) and one real bot apply is the proof. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Rules embedded
- Cards for work already done by hand get **rejected**, not approved — a card must never approve a no-op.
- The first approval of each kind (loop, bot) is a **test of the plumbing**, so pick one whose effect is visible in the wiki.
- ~~Outcome not yet in raw as of 18:18~~ — **Outcome (18:57):** "Both loops registered and gateways for paladin and looker auto-installed by the apply path. Three bots now have live crons that actually fire." The loop half of the proof landed; the bot-apply half and the feed/UI check ("Update the wiki's record and check the feed/UI state") were the next step. Detail: [[wiki-topics/senter-wiki/wiki/queries/apply-path-proven-2026-09-05|apply path proven]]. ^[raw/inbox/2026-09-05.md]

Mechanics: [[wiki-topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]] `/approve` drops `.proposed` or deletes; the apply step behind it registers the loop as a Hermes cron and auto-installs the bot's gateway if missing (seen 18:57). ^[raw/inbox/2026-09-05.md]
