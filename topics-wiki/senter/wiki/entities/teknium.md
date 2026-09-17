---
title: Teknium (Hermes-Agent builder)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [bot, repo]
sources: [raw/sources/knowledge/senter-SOUL.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/looker-SOUL.md, raw/sources/knowledge/weaver-SOUL.md]
confidence: medium
---

# Teknium (Hermes-Agent builder)

**Teknium** (Chris says "tech meme"/"technium"/"tectium") is the fleet's Hermes-Agent builder: triage, core fixes, PRs against `hermes-agent` — "core fixes, not the Wiki UI." Listed in every live roster from 2026-08-30 on. ^[raw/sources/knowledge/senter-SOUL.md] ^[raw/sources/knowledge/weaver-SOUL.md]

## Standing rules that bind it
- **Upstream PR policy (Chris, 2026-09-02)**: teknium never opens PRs on repos Chris doesn't own during a session; drafts go to the ledger `topics-wiki/hermes-agent/prs/`; Chris decides at session end. Chris's own fork `SouthpawIN/hermes-agent` ships immediately. Triggered when a "submitted PR" turned out to be two local unpushed branches — and the rule had never been written into its SOUL. See [[topics-wiki/senter/wiki/decisions/2026-09-02-upstream-pr-policy|decision]]. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]
- Seam splits: when a wiki feature needs the host app (wiki → sidebar composer click-through), weaver builds against a feature-detected stub and teknium builds the real capability as an upstream draft. Later Chris asked "would it be easier if we changed the architecture?" — in-wiki input removed the Electron dependency; the composer PR was downgraded, not cancelled.

## Incidents recorded
- Its bridge report cited Senter's own server PID; a file diff proved convergence, not duplication ("verify a teammate's 'done' against disk").
- Its 5-frame gold-dust strip, checked with vision, ran bottom-right→top-left (Chris asked bottom-left→top-right) with ALLOW/DENY buttons visible in every frame — "verify a bot's proof ARTIFACT with vision before relaying its DONE."
- A `NEEDS-CHRIS — derived from the line` in the stream was teknium's own test probe, not a question.
- Open gaps filed for teknium: `delegate_task` children attribute as `bot=senter` in the bridge; their protected-write approvals go to the desktop prompt, not the wiki; `message_agent` missing from the toolset mid-session.

Related: [[topics-wiki/senter/wiki/entities/hermes-agent|Hermes Agent]], [[topics-wiki/senter/wiki/entities/senter|Senter]].
