---
name: wiki-approval-apply-proof
description: Use when a bot/loop card is approved in the wiki. Prove the apply landed (cron registered, gateway present, first fire in Chris's feed) before calling it done.
version: 0.1.0
distilled: 2026-09-05 19:00
topic: senter-wiki
---
# wiki-approval-apply-proof
Written to topics/senter-wiki/skills/wiki-approval-apply-proof/SKILL.md — 8 hops: pick a card whose effect is visible (reject hand-done ones) → approve → .proposed gone → cron listed for the bot profile → gateway present → first tick produces a feed card (wiki-feed-verify) → capture Chris's real pane (wiki-look-verify) → name loop/bot/cadence in launchd-services.md + done-line. Pitfalls: registered ≠ fires; never leave 'two loops / three bots' unnamed; bot apply and loop apply are separate proofs.

## Evidence
> approve `klerik-queue-drain` (proves the loop apply path live), reject the ones I just did myself, and prove a bot apply end-to-end on a real approval
> Both loops registered and gateways for paladin and looker auto-installed by the apply path. Three bots now have live crons that actually fire. Update the wiki's record and check the feed/UI state
