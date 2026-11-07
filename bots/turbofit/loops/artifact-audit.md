---
type: loop
slug: artifact-audit
bot: turbofit
schedule: "0 7 * * 1"
state: spec
skill: artifact-audit
created: 2026-11-07
---

# artifact-audit

Monday 07:00. Detects HF drift in every catalog source.

## Prompt

Run `artifact-audit` for every distinct source in
`references/model-catalog.json`. Write `bots/turbofit/.system/last-audit.md`.
If any pinned revision moved, mark affected rungs stale and inject one line
naming the repo and what changed. Do not edit the catalog.

## Stop condition

Read-only always. If the HF API rate-limits, stop and report; retrying burns the
remaining budget for the rest of the day.
