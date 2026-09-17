---
title: The four primitives — Context, Skills, Bots/Agents, Loops (GOOP)
created: 2026-07-04
updated: 2026-09-05
type: concept
tags: [spec, idea]
sources:
  - raw/sources/knowledge/agent-wiki-repo/spec.md
  - raw/sources/knowledge/agent-wiki-repo/README.md
  - raw/sources/knowledge/agent-wiki-repo/goop-nesting.md
  - raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md
  - raw/sources/knowledge/agent-wiki-repo/SENTER.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
confidence: high
---

# The four primitives — Context, Skills, Bots/Agents, Loops (GOOP)

## Definition
Every GOOP system is made of four typed objects, each with a factory, a Hermes write mechanism and a wiki path: ^[raw/sources/knowledge/agent-wiki-repo/spec.md]

| Primitive | Hermes write | Wiki path | Standard |
|---|---|---|---|
| **Context** | `write_file` to wiki pages | `topics/<t>/.system/` + `README.md` | wiki markdown |
| **Loops** | `cronjob(create)`, kanban | `topics/<t>/loops/` | cron/kanban config |
| **Agents** (Chris: **Bots**) | `hermes profile create` + SOUL.md | `topics/<t>/agents/` | `AGENTS.md` |
| **Skills** | `skill_manage(create)` | `topics/<t>/skills/` | `SKILL.md` |

## Nesting — two orderings on record
- Spec/README: "Context contains Loops which invoke Agents which load Skills" (Context → Loops → Agents → Skills; each factory's output is the next factory's input). ^[raw/sources/knowledge/agent-wiki-repo/goop-nesting.md] ^[raw/sources/knowledge/agent-wiki-repo/README.md]
- SENTER.md and Chris (2026-09-03): the *emergence* order Context → Skills → Agents/Bots → proposed Loops — "Skills should emerge from repeated evidence … Senter proposes an Agent only when the skill cluster is strong enough … Loops are proposed only after an Agent's workflow is sufficiently stable." ^[raw/sources/knowledge/agent-wiki-repo/SENTER.md] ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]
Both are true: one is containment, the other is the growth path. The UI orbs follow Chris's order: TOPICS(context) → SKILLS → BOTS → LOOPS ([[topics/senter-wiki/wiki/entities/hero-orbs|hero orbs]]).

## GOOP origin
"Gentic Object-Oriented Programming" (Anser + sovthpaw, 2026-07-04): Skills = methods, Agents = classes, Loops = main/workflow; three factory meta-agents with a DSPy/GEPA pipeline and a Continuity Stream + Wiki. Agent Wiki added Context as the fourth primitive ([[topics/senter-wiki/wiki/comparisons/goop-v1-vs-agent-wiki|comparison]]). ^[raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md]

## Vocabulary Chris fixed
**Agent** = agentic harness (Hermes Agent). **Bot** = specialised sub-worker (profile with SOUL.md). **Sub-agents** = drones. In the UI and fleet, "BOTS not agents". ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

## Loops — still being defined
"LOOPS semantics still to be defined with him ('we can have a back and forth about concepts')"; only 2 loops existed on 09-03 with text = name + cadence. By 09-05 the loops lane held watcher / topic-worker / umbrella and the wiki showed 16 LOOPS. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

See [[topics/senter-wiki/wiki/concepts/factory-pipeline-gepa|factory pipeline]], [[topics/senter-wiki/wiki/concepts/markdown-is-the-api|Markdown is the API]].
