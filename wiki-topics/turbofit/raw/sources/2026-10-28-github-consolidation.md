---
title: GitHub consolidation — 2026-10-28
created: 2026-10-28
updated: 2026-10-28
type: reference
tags: [turbofit, consolidation, provenance]
---

# GitHub consolidation — 2026-10-28

Chris's directive (verbatim): *"go through my GitHub … I want everything consolidated into the agent wiki … just try to get everything into one spot."* Bot-wiki reorganisation notes were explicitly out of scope for this pass.

This file is the **provenance map** for that consolidation: what came in, from where, what was left in the repos on purpose, and what is still open.

## 1. Repos surveyed

| Repo | Read | Absorbed into the vault |
| --- | --- | --- |
| `SouthpawIN/turbofit` | full prose tree (`README`, `ROADMAP`, `CHANGELOG`, `WORKFLOWS`, `SKILL`, `after-install`, `docs/*`, `references/*.md`) | 33 reference pages (`references/`) |
| `SouthpawIN/sirvir` | README, SOUL/host contract | [sirvir](../../wiki/entities/sirvir.md) + [references/turbosovth-soul](../../references/turbosovth-soul.md) |
| `SouthpawIN/SALT-core` | README | [salt-core](../../wiki/entities/salt-core.md) |
| `SouthpawIN/model-momento` | README | [model-momento](../../wiki/entities/model-momento.md) |
| `SouthpawIN/benchmark-infographics` | README | [benchmark-infographics](../../wiki/entities/benchmark-infographics.md) |
| `SouthpawIN/southpaw-turbohaul` | README | [southpaw-turbohaul](../../wiki/entities/southpaw-turbohaul.md) |
| `SouthpawIN/turbohaul-manager` | README | [turbohaul-manager](../../wiki/entities/turbohaul-manager.md) |
| `SouthpawIN/turbohaul-llmfit` | README + SKILL | [turbohaul-llmfit](../../wiki/entities/turbohaul-llmfit.md) |

Map: [references/ecosystem](../../references/ecosystem.md).

## 2. turbofit repo → vault file map

Repo files are pinned at commit `0ff572b` (HEAD at consolidation).

| Repo path | Vault path | Note |
| --- | --- | --- |
| `CHANGELOG.md` | [references/changelog.md](../../references/changelog.md) | new |
| `ROADMAP.md` | [references/product-roadmap.md](../../references/product-roadmap.md) | new |
| `SKILL.md` | [references/skill-contract.md](../../references/skill-contract.md) | new |
| `WORKFLOWS.md` | [references/workflows.md](../../references/workflows.md) | new |
| `after-install.md` | [references/install-paths.md](../../references/install-paths.md) | new |
| `docs/apple-arm64-unmeasured-gap.md` | [references/apple-arm64-unmeasured-gap.md](../../references/apple-arm64-unmeasured-gap.md) | new |
| `docs/campaigns.md` | [references/campaigns.md](../../references/campaigns.md) | new |
| `docs/freetoken-runtime.md` | [references/freetoken-runtime.md](../../references/freetoken-runtime.md) | new |
| `docs/hardware-tier-tps.md` | [references/hardware-tier-tps.md](../../references/hardware-tier-tps.md) | new |
| `docs/maple-small-device-validation.md` | [references/maple-small-device-validation.md](../../references/maple-small-device-validation.md) | new |
| `docs/model-matrix.md` | [references/model-matrix.md](../../references/model-matrix.md) | new |
| `docs/model-metadata.md` | [references/model-metadata.md](../../references/model-metadata.md) | new |
| `docs/multimodal.md` | [references/multimodal.md](../../references/multimodal.md) | replaced stale vault copy |
| `docs/remote-hermes-model-server.md` | [references/remote-hermes-model-server.md](../../references/remote-hermes-model-server.md) | new |
| `docs/runtime-backends.md` | [references/runtime-backends.md](../../references/runtime-backends.md) | new |
| `docs/turbofit-check.md` | [references/turbofit-check.md](../../references/turbofit-check.md) | new |
| `docs/turbofit-list.md` | [references/turbofit-list.md](../../references/turbofit-list.md) | new |
| `docs/windows-native-install.md` | [references/windows-native-install.md](../../references/windows-native-install.md) | new |
| `references/SOUL.md` | [references/turbosovth-soul.md](../../references/turbosovth-soul.md) | new |
| `references/api-model-rankings.md` | [references/api-model-rankings.md](../../references/api-model-rankings.md) | new |
| `references/api-pairing-matrix.md` | [references/api-pairing-matrix.md](../../references/api-pairing-matrix.md) | new |
| `references/api-tier-rankings.md` | [references/api-tier-rankings.md](../../references/api-tier-rankings.md) | new |
| `references/benchmark-analysis.md` | [references/benchmark-analysis.md](../../references/benchmark-analysis.md) | new |
| `references/benchmark-leaderboard.md` | [references/benchmark-leaderboard.md](../../references/benchmark-leaderboard.md) | new |
| `references/binary-selection.md` | [references/binary-selection.md](../../references/binary-selection.md) | new |
| `references/curated-lineup.md` | [references/curated-lineup.md](../../references/curated-lineup.md) | new |
| `references/external-benchmarks.md` | [references/external-benchmarks.md](../../references/external-benchmarks.md) | new |
| `references/fit-ladder.md` | [references/fit-ladder.md](../../references/fit-ladder.md) | replaced stale vault copy |
| `references/model-intel.md` | [references/model-intel.md](../../references/model-intel.md) | new |
| `references/model-lineup.md` | [references/model-lineup.md](../../references/model-lineup.md) | replaced stale vault copy |
| `references/research-report.md` | [references/research-report.md](../../references/research-report.md) | new |
| `references/salt-core-integration.md` | [references/salt-core-integration.md](../../references/salt-core-integration.md) | new |
| `references/scaling-ladder.md` | [references/scaling-ladder.md](../../references/scaling-ladder.md) | new |

## 3. What stayed in the repo on purpose

| Kind | Why it stays |
| --- | --- |
| `src/`, `scripts/`, `tests/`, `tools/`, `plugin_tools.py` | Code. The repo is the implementation; a vault copy would be a stale fork. |
| `references/*.json` (`fit-lists.json`, `model-catalog.json`, `engine-serve-matrix.json`, `benchmark-results.json`, …) | Machine-readable data `serve auto` reads at runtime. Vault pages LINK to them (GitHub blob URLs) rather than copying. |
| `assets/`, `promo/` | Binary art. |
| `README.md` | Generated mirror of the vault hub — edit the hub, then re-run `tools/sync-wiki-readme.sh`. |
| `CHANGELOG.md` | Absorbed as a snapshot; the repo stays authoritative for new entries. |

## 4. Collisions resolved

| Vault file | Old state | Resolution |
| --- | --- | --- |
| `references/fit-ladder.md` | hand-curated, older rung names (`GSQ-RCO 27B`) | repo version (canonical rung names + DeepSeek V4.1 top rung) wins; unique vault prose kept under a "curated notes" footer |
| `references/model-lineup.md` | said "shipped subset: 6 models" | repo version (62 artifacts / 13 families) wins |
| `references/multimodal.md` | 11-line status note | repo `docs/multimodal.md` absorbed; vault-only analysis lines kept |
| `ROADMAP.md` (topic root) | product vision roadmap | kept as-is; repo `ROADMAP.md` arrived as [product-roadmap](../../references/product-roadmap.md) — two different documents, both real |

## 5. Link integrity

Every relative link in the topic was resolved after absorption. Three fixes were structural, not cosmetic:

- `../../../../../turbofit/...` cross-repo links (which resolved to `~/Documents/turbofit`, i.e. nowhere) were rewritten to in-vault targets or GitHub blob URLs.
- `docs/x.md` → `references/x.md` after flat absorption into `references/`.
- index.md's lane lists all pointed at one skill file; regenerated to point at each real file.

## 6. Open questions (not decided silently)

1. **Two benchmark stores.** TurboFit keeps `references/benchmark-results.json`; [model-momento](../../wiki/entities/model-momento.md) keeps its own SQLite history. Neither has been nominated as the long-term truth. Candidate: Model Momento ingests TurboFit's JSON.
2. **Legacy line retirement.** `turbohaul-manager` / `southpaw-turbohaul` are documented but not archived. Nothing was deleted in this pass.
3. **Duplicate wiki pages inside this topic** (e.g. `Maple` vs `Maple Preview 8B`, `Cyber Tiel Coder 35B-A3B` vs `Cyber Tiel Coder MTP`, `Qwen 3.8 27B Base` vs `Unleashed`) are merge candidates — flagged, not merged.

## 7. Cross-topic sweep (same day, second pass)

The first pass made the repos single-homed. This pass did the same for the **vault**: TurboFit knowledge had been filed into seven unrelated topics by the watcher's cutter. Content was merged into canonical TurboFit pages; every source page is now a redirect stub (same filename, so inbound links still resolve).

| Was filed in | Page(s) | Now lives in |
| --- | --- | --- |
| `click-options` | turbofit-provider-disappeared · turbofit-provider-still-missing-2026-09-15 · turbofit-models-under-provider · turbofit-picker-registration-gap · turbofit-provider-recurring-disappearance · runtime-config-fix-2026-09-15 | [turbofit-provider-picker-history](../../wiki/concepts/turbofit-provider-picker-history.md) |
| `click-options` | test-through-hermes-not-endpoint | [turbofit-picker-is-the-acceptance-test](../../wiki/decisions/turbofit-picker-is-the-acceptance-test.md) |
| `click-options` | model-zoo-models-for-turbofit-list | [model-zoo-list-lands-in-turbofit-list](../../wiki/decisions/model-zoo-list-lands-in-turbofit-list.md) |
| `back-where` | turbofit-options-missing-after-restart | [turbofit-provider-picker-history](../../wiki/concepts/turbofit-provider-picker-history.md) |
| `try-again` | turbofit-m1-testing-status | [turbofit-m1-testing-status](../../wiki/concepts/turbofit-m1-testing-status.md) |
| `both-smarter` | turbo-fit-lane-rules · turbo-fit-rule-tracking-2026-09-16 | [turbofit-standing-rule-tracking](../../wiki/decisions/turbofit-standing-rule-tracking.md) |
| `dispatched-m2s-new` | turbofit-model-pages | [turbofit-per-model-pages](../../wiki/decisions/turbofit-per-model-pages.md) |
| `add-one` | turbo-fit-benchmark · turbo-fit-tokens-per-second-column | already owned here ([turbo-fit-benchmark](../../wiki/entities/turbo-fit-benchmark.md), [turbofit-list-tok-s-column](../../wiki/decisions/turbofit-list-tok-s-column.md)) — source pages stubbed |

**In-topic duplicates merged the same pass** (model page vs entity page vs `sources: []` stub for the same model):

| Duplicate | Canonical page |
| --- | --- |
| `wiki/models/Maple Preview 8B.md` (unsourced 8B claim) + `wiki/entities/maple.md` | [Maple](../../wiki/models/Maple.md) — the 8B figures kept as a clearly-flagged *unverified* section |
| `wiki/models/Cyber Tiel Coder MTP.md` (unsourced variant stub) + `wiki/entities/tiel-coder.md` | [Cyber Tiel Coder 35B-A3B](../../wiki/models/Cyber Tiel Coder 35B-A3B.md) |

Two pages had also been appended **twice** by earlier merge passes (`Maple`, `Cyber Tiel Coder 35B-A3B`); the second copy was removed, keeping the copy that carries `^[raw/…]` provenance.

Still open: the two benchmark stores ([model-momento](../../wiki/entities/model-momento.md) SQLite vs `references/benchmark-results.json`), and whether the absorbed prose should be deleted from the product repo now that the vault owns it (repo currently keeps its own copies of `docs/*.md` and `references/*.md`).
