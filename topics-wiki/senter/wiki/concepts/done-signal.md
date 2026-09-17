---
title: Done signal (DONE / BLOCKED / NEEDS-CHRIS)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, bot]
sources: [raw/sources/knowledge/paladin-AGENTS.md, raw/sources/knowledge/weaver-AGENTS.md, raw/sources/knowledge/looker-AGENTS.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Done signal (DONE / BLOCKED / NEEDS-CHRIS)

Fleet standard, instituted after Chris said of the builders "I never know when it's done." The LAST line of every bot reply is exactly one of: ^[raw/sources/knowledge/weaver-AGENTS.md]

- `DONE — <one line: what shipped, what verified it>`
- `BLOCKED — <why, what's needed>`
- `NEEDS-CHRIS — <the question>`

"Never end a turn without it." It is also POSTed to the [[topics-wiki/senter/wiki/entities/senter-bridge|bridge]]:
`curl -s -X POST "http://127.0.0.1:8643/post?token=$(cat ~/.hermes/senter-bridge/token)" -d '{"bot":"<bot>","text":"DONE — …","status":"done"}'` (status `blocked` for a FAIL). ^[raw/sources/knowledge/paladin-AGENTS.md]

## How Senter treats each
- **DONE** on a visual item → [[topics-wiki/senter/wiki/entities/looker|looker]] runs a real-window pass before Senter relays; "when a child's DONE disagrees with the capture, the capture wins." Verify proof artifacts with vision; verify structural DONEs on disk. Plain done-lines are NOT narrated by Senter — Chris reads them in the wiki stream.
- **BLOCKED** — may already be recovered (`timed out waiting for approval` followed by a re-run without the gated construct), or the child may have finished and lost context; check events/disk before escalating.
- **NEEDS-CHRIS** — goes to the wiki as a `needs_chris` card + `## AWAITING CHRIS` in the plan file ([[topics-wiki/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|decision]]). Read the text first: a `NEEDS-CHRIS — derived from the line` was teknium's own test probe.

## Time-capped variants
Sentinel-enforced: at 12 min on one item post a progress line (done + remaining); at 20 min post `BLOCKED — <diff so far>` and exit. "Never a silent 30+ min run." Looker's third unconverged pass is `FAIL-CONVERGENCE` with all offsets. See [[topics-wiki/senter/wiki/concepts/look-loop-verification|LOOK loop]], [[topics-wiki/senter/wiki/concepts/meeseeks-model|Meeseeks model]]. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]
