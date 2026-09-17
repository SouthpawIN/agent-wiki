---
title: Decision 2026-09-05 (contested): keep senter and senter-wiki separate vs umbrella's merge proposal
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, question, idea]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: medium
contested: true
aliases:
  - "Open decision: merge senter-wiki into senter? (umbrella says yes, kept apart)"
---

# Keep `senter` and `senter-wiki` separate — vs the umbrella's merge proposal

## Position A — keep separate (Senter's judgment, backend procedure rule #5)
"Topic split: `senter` = the fleet/system (process, lessons, orchestrator); `senter-wiki` = the UI surface. Keep them separate." Restated 2026-09-05 16:51: "I kept `senter` and `senter-wiki` separate (fleet vs surface/memory) and logged the merge question for the umbrella to argue with evidence." ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Position B — merge (umbrella, 2026-09-05 17:13)
"The umbrella has an opinion: **merge senter-wiki into senter (0.65, AUTO-tier by your own locked calibration)**." Under the 09-02 thresholds (auto ≥0.50) this would merge automatically. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Status: waiting on Chris
"Your call on the merge especially — the umbrella says one subject, I kept them apart. Veto goes in `wiki-topics/_global/.system/keep-separate.md`." Still open at 17:25 ("the umbrella's senter-wiki → senter merge proposal"). No decision from Chris in the raw as of 2026-09-05. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Notes
The 0.65 is suspiciously the `name_contains` floor (senter ⊂ senter-wiki) from [[wiki-topics/senter-wiki/wiki/concepts/similarity-ranking|the calibration]] — the score may be a naming artefact rather than semantic overlap. Actors: [[wiki-topics/senter-wiki/wiki/entities/umbrella|umbrella]]. Listed in [[wiki-topics/senter-wiki/wiki/queries/open-items-as-of-2026-09-05|open items]].

## Folded from `keep-senter-and-senter-wiki-separate`
- Position A dating: assistant judgment 2026-09-05 16:51 and backend procedure #5, dated 2026-09-03. ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/sources/knowledge/skill-agent-wiki-vault.md]
- Position B framing: the thresholds Chris fixed on 09-02 say this pair merges automatically. ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Status: handed to Chris as a card; no decision from Chris in the raw as of 2026-09-05 17:53. See [[wiki-topics/senter-wiki/wiki/concepts/approval-policy|approval policy]].

## Absorbed
- `decisions/keep-senter-and-senter-wiki-separate` — 2026-09-05 → archived at `wiki-topics/_archive/wiki-dedupe/senter-wiki/decisions/keep-senter-and-senter-wiki-separate.md`
