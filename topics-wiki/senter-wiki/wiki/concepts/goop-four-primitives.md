---
title: GOOP: Context → Skills → Bots → Loops
aliases:
  - The four primitives — Context, Skills, Bots/Agents, Loops (GOOP)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, idea, plan]
sources:
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/sources/knowledge/agent-wiki-repo/spec.md
  - raw/sources/knowledge/agent-wiki-repo/SENTER.md
  - raw/sources/knowledge/agent-wiki-repo/goop-nesting.md
  - raw/sources/knowledge/agent-wiki-repo/README.md
  - raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md
  - raw/inbox/2026-09-05-legacy-inbox.md
confidence: high
---

# GOOP four primitives

Chris's own framing (2026-09-03, saved verbatim in `topics-wiki/senter/.system/concept.md`):

> Hermes makes Skills out of repeated asks. Context -> Skills. … Bots make sense when a collection of Skills requires its own continuity/learning … When a Bot
> has a purpose, naturally a Loop springs out. Context -> Skills -> Bots -> Loops (and those four dots denote and sort by these four objects). … ALL represented
> in Markdown (knowledge base, SKILLS.md, AGENTS/SOUL/{WHATEVER}.md, and CRON/Hook scheduling).
^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

## The spec's table
| Primitive | Factory | Hermes write | Wiki path |
|---|---|---|---|
| Context | Context | `write_file` | `topics-wiki/<t>/.system/` + `README.md` |
| Loops | Loops | `cronjob(create)`, kanban | `topics-wiki/<t>/triggers-loops/` |
| Agents (Bots) | Agents | `hermes profile create` + SOUL.md | `topics-wiki/<t>/agents/` |
| Skills | Skills | `skill_manage(create)` | `topics-wiki/<t>/skills-capabilities/` |
Nesting (spec/goop-nesting): Context contains Loops which invoke Agents which load Skills; each factory's output is the next factory's input — *"idea → context →
skill → agent → loop, all automatic."* Note the two orderings coexist: Chris's emergence order (Context→Skills→Bots→Loops, which the four orbs follow) vs the spec's
containment order (Context→Loops→Agents→Skills). ^[raw/sources/knowledge/agent-wiki-repo/spec.md] ^[raw/sources/knowledge/agent-wiki-repo/goop-nesting.md]

Each primitive also has a standard file/format — Context: wiki markdown; Loops: cron/kanban config; Agents (Chris: **Bots**): `AGENTS.md`; Skills: `SKILL.md`. ^[raw/sources/knowledge/agent-wiki-repo/spec.md]
The README states the containment order the same way — "Context contains Loops which invoke Agents which load Skills". ^[raw/sources/knowledge/agent-wiki-repo/goop-nesting.md] ^[raw/sources/knowledge/agent-wiki-repo/README.md]
Both orderings are true: one is containment, the other is the growth path. The UI orbs follow Chris's order: TOPICS(context) → SKILLS → BOTS → LOOPS ([[topics-wiki/senter-wiki/wiki/entities/hero-orbs|hero orbs]]).

## GEPA lifecycle for every primitive
Collect evidence → Generate candidates → Evaluate (redundancy, contradictions, evidence alignment, safety) → Apply only an approved winner. *"Skills should emerge
from repeated evidence, not be created merely because a capability was mentioned once."* Agents only when the skill cluster is strong; Loops only after an agent
workflow is stable. ^[raw/sources/knowledge/agent-wiki-repo/SENTER.md]

## Flywheel (spec)
1 Chris speaks → session DB · 2 Context reads sessions, writes wiki pages · 3 queue items `[SKILLS] [AGENTS] [LOOPS]` · 4 factories claim `[~]`, `delegate_task`, mark `[x]`
· 5 status → `.system/injections.md` `[UNREAD]` · 6 Senter weaves it into the next reply. *"No chat command. No config file. No YAML wizard. Just edit markdown."* ^[raw/sources/knowledge/agent-wiki-repo/spec.md]

## How it actually runs today (2026-09-05)
Four spec crons became: watcher (Layer 1 filing) → topic-worker / topic-agent (skills auto-apply) → umbrella (merges, dedupe, bot promotion) → bridge approvals for
bots-profiles/loops only. See [[topics-wiki/senter-wiki/wiki/entities/topic-worker|topic-worker / compiler]], [[topics-wiki/senter-wiki/wiki/entities/umbrella|umbrella]],
[[topics-wiki/senter-wiki/wiki/concepts/approval-policy|approval policy]], [[topics-wiki/senter-wiki/wiki/comparisons/goop-v1-vs-agent-wiki|GOOP v1 vs Agent Wiki]].

## All-caps modules
An all-caps filename (`MEDIA.md`, `WALLET.md`, `RESEARCH.md`) is a user-authored GOOP module: Purpose / Allowed / Forbidden / Approval / Secret References.
*"The Markdown declares policy; Hermes and the sandbox must enforce it."* Secrets are referenced (`bitwarden://wallet/cards`), never stored. ^[raw/sources/knowledge/agent-wiki-repo/SENTER.md]

## Folded from `four-primitives-goop`

### GOOP origin
"Gentic Object-Oriented Programming" (Anser + sovthpaw, 2026-07-04): Skills = methods, Agents = classes, Loops = main/workflow; three factory meta-agents with a DSPy/GEPA pipeline and a Continuity Stream + Wiki. Agent Wiki added Context as the fourth primitive ([[topics-wiki/senter-wiki/wiki/comparisons/goop-v1-vs-agent-wiki|comparison]]). ^[raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md]

### Vocabulary Chris fixed
**Agent** = agentic harness (Hermes Agent). **Bot** = specialised sub-worker (profile with SOUL.md). **Sub-agents** = drones. In the UI and fleet, "BOTS not agents". ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

### Loops — still being defined
"LOOPS semantics still to be defined with him ('we can have a back and forth about concepts')"; only 2 loops existed on 09-03 with text = name + cadence. By 09-05 the loops lane held watcher / topic-worker / umbrella and the wiki showed 16 LOOPS. ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md] ^[raw/inbox/2026-09-05-legacy-inbox.md]

See [[topics-wiki/senter-wiki/wiki/concepts/factory-pipeline-gepa|factory pipeline]], [[topics-wiki/senter-wiki/wiki/concepts/markdown-is-the-api|Markdown is the API]].

## Absorbed
- `concepts/four-primitives-goop` — 2026-09-05 → archived at `topics-wiki/_archive/wiki-dedupe/senter-wiki/concepts/four-primitives-goop.md`
