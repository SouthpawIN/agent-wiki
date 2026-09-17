---
title: Similarity, ranking and list order
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [ui, infra, decision]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# Similarity, ranking and list order

## Chris's rule
"consider the context of the entire topic … the entire file" — similarity is whole-document TF-IDF cosine, not keyword hits; skills sort "not by their title" but by their description. ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]

## Three orderings, one function
- **Default** = usage, highest first (`usageOf(kind,name)`, same series as the [[wiki-topics/senter-wiki/wiki/entities/usage-strip|usage strip]]).
- **Typed search** = relevance to `TERM` (`rankBy(items, textOf, nameOf)`; name a light tiebreaker).
- **Orb pin** = similarity to the pinned hero `ANCHOR` (`topicDoc(anchor)` vector; anchor scores `Infinity`). ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]
Page side: `SIM.vec(text)` over the live corpus; scanner supplies full `text` per topic/bot/skill/loop ([[wiki-topics/senter-wiki/wiki/entities/scan-topics|scanner]]). ^[raw/sources/knowledge/ref-vault-live-hover-usage-2026-09-03.md]

## Pipeline side (`topic-similarity.py`)
- Emits `similarity.matrix` (full pairwise) — pairs ≥0.15 only "could not rank everything". TF-IDF cosines are low (0.12 top) — order right, magnitudes not; `--provider openai` at a local embed server sharpens it. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
- **Calibration Chris locked (2026-09-02)**: auto-merge ≥0.50, propose ≥0.35; `name_contains(a,b)` floors sim to 0.65 (pocket-shop ⊂ pocket-shop-pricing); turbohaul vs turbofit share only "turbo" → apart by construction. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
- LOCK: `LOCKS` Set (localStorage `sw.locks`) + `wiki-topics/<t>/.system/lock.json` via bridge `/write`; locked pairs downgrade auto→propose; `merge-topics.py` refuses plans touching a locked topic. ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]
- The [[wiki-topics/senter-wiki/wiki/entities/umbrella|umbrella]] applies the same thresholds cross-topic — hence its 0.65 AUTO-tier verdict on senter-wiki → senter ([[wiki-topics/senter-wiki/wiki/decisions/2026-09-05-keep-senter-and-senter-wiki-separate|contested]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]
- Watcher filings carry a per-message `sim` (0.06–0.34 in the inbox); thin corpora misroute (kashik 0.08). ^[raw/inbox/2026-09-05.md]

## Context tagging (earlier CONTEXT page, now the corner feed)
`nearestTopic(txt)` evidence-gated: topic name in text (+6) or ≥2 distinctive summary words (+1 each); score <2 → UNSORTED. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

Navigation that consumes the ranking: [[wiki-topics/senter-wiki/wiki/concepts/one-page-navigation-model|one-page navigation]].
