# Topic similarity — 2026-09-03T10:46:41 (method: tfidf, v1.2.0)

19 topics · 171 pairs · 18 clusters (link ≥ 0.3)
Thresholds for method `tfidf` (LOCKED by chris 2026-09-02; calibrated by chris (approved senter's calibration run) on 2026-09-02 against `topics/senter/plans/topic-consolidation-2026-09-02.md#anser-audit`): auto ≥ 0.5 · propose 0.35–0.5 · shared name-stem is always >= propose

Tier counts: auto=1, none=7

## Top 5 pairs

| # | a | b | score | tier | stem |
|--:|---|---|------:|------|:----:|
| 1 | senter | senter-wiki | 0.650 | auto | ✓ |
| 2 | omnisenter-models | senter | 0.236 | none |  |
| 3 | evolutionary | music | 0.202 | none |  |
| 4 | legacy-bots | nous-community | 0.192 | none |  |
| 5 | hermes-agent | nous-community | 0.172 | none |  |

## Clusters

- **c0** hue 0° — _wiki · entity · senter_ — senter, senter-wiki
- singletons (no tint, hue=null): 17 — anser, burner-phone, crow, dev-tooling, evolutionary, hermes-agent, kashik, klerik, legacy-bots, memento, music, nous-community, omnisenter-models, pirouette-framework-core-003, pocket-shop, turbofit, youtube

## Score distribution (all pairs ≥ 0.15 kept)

- 0.92–1.00: 0
- 0.80–0.92: 0
- 0.60–0.80: 1
- 0.50–0.60: 0
- 0.40–0.50: 0
- 0.35–0.40: 0
- 0.30–0.35: 0
- 0.15–0.30: 7

<!-- end generated — hand-written sections below survive re-runs -->



## Senter calibration against the human merge table (2026-09-02)
TF-IDF on thin READMEs tops out at 0.70 — the draft 0.92/0.80 bars would never fire. Calibrated against anser's SIGNED merge table (ground truth): 32 pairs the humans merged score 0.70 → 0.39; 43 pairs they kept apart top out at **0.46** (one outlier: senter-alignment-arxivddl ↔ senter-omni-data — same family, defensible either way), then 0.38 and below.
**Proposed thresholds (TF-IDF scale, method-tagged so they re-calibrate if we switch to embeddings):**
- **≥ 0.50 → auto-merge candidate** (paladin dry-run → one card → merge on approval). Every pair ≥0.50 today is a pair the humans already merged. Zero false positives.
- **0.35 – 0.50 → propose** (`⇄ merge?` glyph in the wiki). Catches the rest of the human merges (test scaffolds 0.45, llmc↔veiled 0.42, dev-* 0.37) with a handful of judgment calls mixed in — exactly where a human should look.
- **< 0.35 → color-group only.**
- **Name-stem rule** (`pocket-shop` / `pocket-shop-*`) always ≥ propose regardless of score — that pair scores low on text but is an obvious merge.
Governance: thresholds live in `assets/topic-similarity.py` as `THRESHOLDS[method]`; changing them is a paladin task with a card. Re-run on topic create/rename + nightly; every auto-merge candidate still goes through the dry-run card — "auto" means "proposed without a human noticing first," never "merged without a human."

## Before/after — tfidf v1.0.0 (2026-09-02T18:14:47) → tfidf v1.1.0 (2026-09-02T18:23:12)

top-20 union = 20 pairs · Δ = new − old score

| a | b | old # | old score | old tier | new # | new score | new tier | Δ |
|---|---|------:|----------:|----------|------:|----------:|----------|---:|
| sovthpaw-omnisenter-base-16b | sovthpaw-omnistep-new | 1 | 0.699 | group | 1 | 0.699 | auto | +0.000 |
| sovthpaw-omnistep-12a3b | sovthpaw-omnistep-new | 2 | 0.666 | propose | 2 | 0.666 | auto | +0.000 |
| southpaw-turbohaul | turbohaul-manager | 3 | 0.663 | group | 3 | 0.663 | auto | +0.000 |
| sovthpaw-omni-senter-3b | sovthpaw-omnistep-new | 4 | 0.635 | group | 4 | 0.635 | auto | +0.000 |
| sovthpaw-omni-senter-3b | sovthpaw-omnisenter-base-16b | 5 | 0.584 | group | 5 | 0.584 | auto | +0.000 |
| sovthpaw-omni-senter-3b | sovthpaw-omnistep-12a3b | 6 | 0.549 | group | 6 | 0.549 | auto | +0.000 |
| sovthpaw-omnisenter-base-16b | sovthpaw-omnistep-12a3b | 7 | 0.539 | group | 7 | 0.539 | auto | +0.000 |
| senter-alignment-arxivddl | sovthpaw-senter-omni-data | 8 | 0.463 | group | 8 | 0.463 | propose | +0.000 |
| sovthpaw-omni-senter-3b | sovthpaw-senter-omni-data | 9 | 0.463 | group | 9 | 0.463 | propose | +0.000 |
| hermes-test-skill | nous-test | 10 | 0.452 | group | 10 | 0.452 | propose | +0.000 |
| llmc | veiled | 11 | 0.417 | group | 11 | 0.417 | propose | +0.000 |
| sovthpaw-omnistep-new | sovthpaw-senter-omni-data | 12 | 0.409 | group | 12 | 0.409 | propose | +0.000 |
| hermes-test-skill | test-bot | 13 | 0.394 | group | 13 | 0.394 | propose | +0.000 |
| sovthpaw-omnisenter-base-16b | sovthpaw-senter-omni-data | 14 | 0.383 | group | 14 | 0.383 | propose | +0.000 |
| senter-alignment-arxivddl | sovthpaw-omni-senter-3b | 15 | 0.376 | group | 15 | 0.376 | propose | +0.000 |
| dev-coder | dev-review | 16 | 0.366 | group | 16 | 0.366 | propose | +0.000 |
| evolutionary-training | omnisenter-blog | 17 | 0.363 | group | 17 | 0.363 | propose | +0.000 |
| omnisenter-blog | southpawin-github-io | 18 | 0.356 | none | 18 | 0.356 | propose | +0.000 |
| dev-orch | dev-review | 19 | 0.347 | group | 19 | 0.347 | group | +0.000 |
| nous-test | test-bot | 20 | 0.338 | group | 20 | 0.338 | group | +0.000 |

## Before/after — tfidf v1.1.0 (2026-09-02T18:23:12) → tfidf v1.2.0 (2026-09-02T18:34:26)

top-20 union = 27 pairs · Δ = new − old score

| a | b | old # | old score | old tier | new # | new score | new tier | Δ |
|---|---|------:|----------:|----------|------:|----------:|----------|---:|
| omnisenter-models | senter | – | – | – | 1 | 0.239 | none | – |
| evolutionary | music | – | – | – | 2 | 0.201 | none | – |
| legacy-bots | nous-community | – | – | – | 3 | 0.190 | none | – |
| hermes-agent | nous-community | – | – | – | 4 | 0.171 | none | – |
| klerik | senter | 41 | 0.195 | none | 5 | 0.156 | none | -0.038 |
| music | nous-community | – | – | – | 6 | 0.152 | none | – |
| senter | senter-wiki | 71 | 0.127 | propose | 7 | 0.141 | propose | +0.015 |
| sovthpaw-omnisenter-base-16b | sovthpaw-omnistep-new | 1 | 0.699 | auto | – | – | – | – |
| sovthpaw-omnistep-12a3b | sovthpaw-omnistep-new | 2 | 0.666 | auto | – | – | – | – |
| southpaw-turbohaul | turbohaul-manager | 3 | 0.663 | auto | – | – | – | – |
| sovthpaw-omni-senter-3b | sovthpaw-omnistep-new | 4 | 0.635 | auto | – | – | – | – |
| sovthpaw-omni-senter-3b | sovthpaw-omnisenter-base-16b | 5 | 0.584 | auto | – | – | – | – |
| sovthpaw-omni-senter-3b | sovthpaw-omnistep-12a3b | 6 | 0.549 | auto | – | – | – | – |
| sovthpaw-omnisenter-base-16b | sovthpaw-omnistep-12a3b | 7 | 0.539 | auto | – | – | – | – |
| senter-alignment-arxivddl | sovthpaw-senter-omni-data | 8 | 0.463 | propose | – | – | – | – |
| sovthpaw-omni-senter-3b | sovthpaw-senter-omni-data | 9 | 0.463 | propose | – | – | – | – |
| hermes-test-skill | nous-test | 10 | 0.452 | propose | – | – | – | – |
| llmc | veiled | 11 | 0.417 | propose | – | – | – | – |
| sovthpaw-omnistep-new | sovthpaw-senter-omni-data | 12 | 0.409 | propose | – | – | – | – |
| hermes-test-skill | test-bot | 13 | 0.394 | propose | – | – | – | – |
| sovthpaw-omnisenter-base-16b | sovthpaw-senter-omni-data | 14 | 0.383 | propose | – | – | – | – |
| senter-alignment-arxivddl | sovthpaw-omni-senter-3b | 15 | 0.376 | propose | – | – | – | – |
| dev-coder | dev-review | 16 | 0.366 | propose | – | – | – | – |
| evolutionary-training | omnisenter-blog | 17 | 0.363 | propose | – | – | – | – |
| omnisenter-blog | southpawin-github-io | 18 | 0.356 | propose | – | – | – | – |
| dev-orch | dev-review | 19 | 0.347 | group | – | – | – | – |
| nous-test | test-bot | 20 | 0.338 | group | – | – | – | – |
