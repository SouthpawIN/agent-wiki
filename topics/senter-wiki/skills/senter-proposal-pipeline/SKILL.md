---
name: senter-proposal-pipeline
description: Use when a worker/umbrella emits or Chris acts on a wiki proposal. Write `.proposed` artifacts, surface them as proposed rows, approve/reject only via bridge `/approve`.
version: 0.1.0-proposed
proposed: 2026-09-05 17:13
topic: senter-wiki
---
# senter-proposal-pipeline
# Senter proposal pipeline

## Emit
1. Write the artifact in its real destination with a `.proposed` suffix (e.g. `topics/<t>/skills/<slug>/SKILL.md.proposed`, `agents/<bot>/SOUL.md.proposed`, `loops/<name>.md.proposed`). Never a side `proposals/` dir.
2. Post ONE card per proposal to the feed. Card must carry the artifact path and APPROVE / REJECT buttons.
3. Umbrella proposals (topic merge/split, cross-topic dedupe, cluster→bot) follow the same rule — proposals only, no kanban, no direct edits.

## Surface
- The scanner MUST index both `~/.hermes/**/skills` and every vault `topics/*/skills/` dir; a `.proposed` file becomes a row in SKILLS/BOTS/LOOPS marked `proposed` with its path shown.
- If a proposal isn't a visible row, it didn't happen — fix the scanner, don't describe it.

## Act
- Bridge `/approve` is the ONLY mutation path and does exactly two things: approve = rename to drop `.proposed`; reject = delete the file. Nothing else (no rewrite, no move, no side effects).
- Never approve on Chris's behalf; never leave probe/dummy proposed rows in the tables after testing.

## Pitfalls
- Testing with a probe row: remove it the same turn.
- Approval must re-trigger the scanner so the row flips from `proposed` to live immediately (everything live).

## Evidence
> Proposals need to be *visible in the wiki* — rows in SKILLS/BOTS/LOOPS marked proposed, so you can see them get proposed.
> The scanner only scans `~/.hermes/**/skills` — vault topic skills (the spec's primary location) were never rows.
> a bridge endpoint that only ever does two things (drop `.proposed` or delete), then the card buttons in the wiki
> 5 proposed rows live with their paths. Remove the probe, and make the umbrella real (kanban-free first pass — proposals only, like everything else)
