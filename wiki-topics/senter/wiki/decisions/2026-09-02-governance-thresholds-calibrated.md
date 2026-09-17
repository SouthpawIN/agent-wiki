---
title: "2026-09-02 — Governance thresholds calibrated against Chris's decisions (propose ≥ .35, auto ≥ .50)"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, spec, infra]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# 2026-09-02 — Governance thresholds calibrated against Chris's decisions (propose ≥ .35, auto ≥ .50)

**What.** Similarity thresholds for topic merge/split governance are **calibrated against decisions Chris already made, never guessed.** Locked values: **propose ≥ 0.35, auto-candidate ≥ 0.50**, plus the rule "shared name-stem always proposes." Stored as `THRESHOLDS[method]` so a switch from TF-IDF to embeddings re-calibrates instead of silently drifting; "auto" still cards before merging. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

**Why.** [[wiki-topics/senter/wiki/entities/paladin|Paladin]]'s TF-IDF similarity maxed at 0.70 on thin READMEs; Senter's draft bars (0.92 auto / 0.80 propose) would never have fired.

**Recipe.** Take the human-approved table as ground truth ([[wiki-topics/senter/wiki/entities/anser|anser]]'s signed 63→19 merge list) → score every pair as merged/not-merged → highest non-merged score = 0.46; merged scores ranged 0.70 → 0.39 → set auto just above the highest false positive (≥ 0.50 → 0 false positives), propose-band across the rest (0.35–0.50) → post the numbers as a `needs_chris` card WITH the evidence ([[wiki-topics/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|cards decision]]). Chris approved and locked.

**Reaffirmed 2026-09-05 17:13.** When building the umbrella pass, Hermes noted: "There's already a Chris-approved, locked calibration (propose ≥ .35, auto ≥ .5). The umbrella must use those thresholds, not mine." The [[wiki-topics/senter/wiki/entities/watcher|watcher]]'s per-message filing reports its similarity (`sim 0.12` etc.) against the same scale. ^[raw/inbox/2026-09-05-legacy-inbox.md]
