---
title: Fleet rosters over time
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [bot, timeline]
sources: [raw/sources/knowledge/senter-repo/README.md, raw/sources/knowledge/anser-AGENTS.md, raw/sources/knowledge/senter-SOUL.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/weaver-SOUL.md, raw/sources/knowledge/looker-SOUL.md]
confidence: high
contested: true
---

# Fleet rosters over time

The raw files carry five different fleet tables. They disagree because they were written at different dates — none is wrong for its date. Live truth is always `hermes profile list`. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

| Bot | senter repo (legacy) | anser SOUL/AGENTS (legacy) | senter SOUL (2026-08-30) | skill table (2026-09-02, pre-looker) | looker SOUL (live 2026-09-02) |
|---|---|---|---|---|---|
| senter | orchestrator/router | triage orchestrator | coordinator | coordinator | coordinator / triage |
| klerik | reviews | profile editor/reviewer | profile factory (DSPy+GEPA) | profile factory | profile factory / editor |
| anser | support | Discord tech support | — | redundancy gate + Discord heritage (08-30) | Discord support + redundancy checker |
| chizul | builds (default agent) | worker/builder | — | — | — |
| kashik | docs | guide writer | — | — | — |
| crow | research | research | — | — | — |
| frieza | infrastructure | (AGENTS list) | — | — | — |
| nous-girl | source of ideas | brainstormer/creative | — | — | — |
| sirvir | — | (AGENTS list) | → renamed turbosovth | — | — |
| dogeman | — | — | YouTube/content studio | YouTube/content | youtube builder |
| teknium | — | — | Hermes-Agent builder | Hermes fixes/PRs | hermes-agent builder |
| turbosovth | — | — | TurboFit support (never merges) | TurboFit support | turbofit builder |
| paladin | — | — | — | repo standardizer (08-30) | repo/vault structure standards |
| weaver | — | — | — | Senter Wiki UI (09-02) | Senter Wiki UI builder |
| looker | — | — | — | — (REFLECT's first proposal) | UI-QA LOOK service |

## Reading the table
- **Legacy fleet** (Discord/Kanban era; [[topics-wiki/senter/wiki/entities/senter-repo|senter repo]], [[topics-wiki/senter/wiki/entities/anser|anser]]'s files): chizul, kashik, crow, frieza, nous-girl, sirvir. None appear in any 2026-08-30+ roster; Senter's onboarding rule is to audit installed profiles for these "dead fleet members."
- **2026-08-30**: coordinator role assigned; fleet = senter, dogeman, teknium, turbosovth, klerik; anser + paladin onboarded the same day (skill) but the SOUL table was not updated — the SOUL's own instruction is "verify with `hermes profile list` each session; keep this table true."
- **2026-09-02**: weaver and paladin properly spawned by klerik; looker created from REFLECT's proposal; 9 bots (Senter's memory: "Fleet = 9 bots").
- Weaver's SOUL table (8 rows, pre-looker) and paladin's (8 rows) sit between the last two columns.

## Verdict
Use the [[topics-wiki/senter/wiki/entities/looker|looker]] SOUL roster (explicitly "live roster 2026-09-02 — mirror, do not invent") as the current list until a newer source lands; treat every other table as historical. Individual pages: [[topics-wiki/senter/wiki/entities/other-fleet-bots|other fleet bots]].
