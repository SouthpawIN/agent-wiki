---
title: The Senter Wiki vision — Cursor × Obsidian, the wiki IS the system
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [idea, plan, spec]
sources:
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
  - raw/sources/knowledge/agent-wiki-repo/README.md
  - raw/sources/knowledge/agent-wiki-repo/spec.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# The Senter Wiki vision — Cursor × Obsidian, the wiki IS the system

## Chris's framing (verbatim, 2026-09-03)
> Hermes makes Skills out of repeated asks. Context -> Skills. … Bots make sense when a collection of Skills requires its own continuity/learning … When a Bot has a purpose, naturally a Loop springs out. Context -> Skills -> Bots -> Loops (and those four dots denote and sort by these four objects). … ALL represented in Markdown (knowledge base, SKILLS.md, AGENTS/SOUL/{WHATEVER}.md, and CRON/Hook scheduling). This is a Cursor x Obsidian setup where everything you talk about gets captured as Topics in a wiki … Jump between topics and it sorts and automates them all, looking for efficiencies and reusable artifacts. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

## The 2026-09-05 restatement
`topics/senter-wiki/README.md` describes it as "Cursor for markdown / live second brain": four lanes mapped to vault paths *and* Hermes-native writes. Per-message filing "like Cursor"; "Per message, live, visible." ^[raw/inbox/2026-09-05-legacy-inbox.md]

## The spec's version
"A self-documenting, self-extending multi-agent system where the wiki IS the coordination layer. Topics are miniature GOOP instances. Markdown is the API between human and machine." Flywheel: Chat → Comprehend → Create → Inject. ^[raw/sources/knowledge/agent-wiki-repo/spec.md] ^[raw/sources/knowledge/agent-wiki-repo/README.md]

## What it means for the product
- Input lives IN the wiki (header-as-input, editor card, approval cards), the Hermes sidebar beside it — "the whole thing operates together like a cursor setup". ^[raw/sources/knowledge/ref-vault-live-demo-video.md]
- Everything Chris says lands in a topic's `raw/` and is compiled into `wiki/` pages ([[topics/senter-wiki/wiki/concepts/llm-wiki-topic-layout|LLM-wiki topic layout]]); the row's CONTEXT section renders that index. ^[raw/inbox/2026-09-05.md]
- The four dots are the four primitives ([[topics/senter-wiki/wiki/concepts/goop-four-primitives|four primitives]]) and also the navigation ([[topics/senter-wiki/wiki/concepts/one-page-navigation-model|navigation]]). ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
- The pipeline is proposal-driven with the human as authority ([[topics/senter-wiki/wiki/concepts/approval-policy|approval policy]], [[topics/senter-wiki/wiki/concepts/factory-pipeline-gepa|factory pipeline]]). ^[raw/sources/knowledge/agent-wiki-repo/spec.md]
- The process is the product: fixes must be *seen* landing in the wiki while Chris talks ([[topics/senter-wiki/wiki/concepts/ui-performs-the-fleet|UI performs the fleet]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Milestones
- 2026-07-04 GOOP whitepaper; 07-07 agent-wiki repo ([[topics/senter-wiki/wiki/entities/agent-wiki-repo|repo]]).
- 2026-08-29 repos consolidated into Senter ([[topics/senter-wiki/wiki/decisions/2026-08-29-consolidate-repos-into-senter|decision]]).
- 2026-09-03 UI marathon; ~20:40 MVP checkpoint — "the UI is at a good enough spot that we can start working on the back end" ([[topics/senter-wiki/wiki/decisions/2026-09-03-mvp-checkpoint-ui-good-enough|decision]]).
- 2026-09-05 backend flywheel: watcher → worker → umbrella → approvals → stage → LLM-wiki compile ([[topics/senter-wiki/wiki/queries/timeline-2026-09-03-to-05|timeline]]).
