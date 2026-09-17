---
title: senter
updated: 2026-09-02
type: topic
repo: https://github.com/SouthpawIN/Senter
status: active
tags: [senter, goop, hermes-agent, multi-agent, fleet, wiki]
---

# Senter

> **Senter is the three-eyed owl: a self-documenting, self-extending multi-agent system. The wiki IS the coordination layer.**
> This topic now consolidates three repos — agent-wiki (the Senter codebase), klerik (QA/profile-factory agent), and the old senter fleet-orchestrator profile — into ONE project, per the 2026-08-29 cleanup directive.

**Repo:** https://github.com/SouthpawIN/Senter · ACTIVE

## Facts
- **Consolidation date:** 2026-08-29
- **Merged in:** agent-wiki (codebase) · klerik (QA + DSPy/GEPA profile factory) · senter (orchestrator profile)
- **License:** MIT
- **Status:** ACTIVE — repo rename agent-wiki → Senter executed 2026-08-29

## Contents
- `agent-wiki-README.md` — archived README of the old agent-wiki repo (pre-rename)
- `fleet-orchestrator-profile.md` — archived README of the old senter orchestrator repo
- `klerik-profile.md` — klerik identity + role update (profile factory)

## 2026-08-29 session record
See `.system/queue.md` for the full log: turbofit provider fix (4cc6b06), senter HP Omarchy recovery status, turbosovth oversight findings.


## Process (the shareable part) — 2026-09-02
- [[wiki-topics/senter/process/build-loop]] — roles, LOOK loop, done signal, approvals, delivery, Meeseeks, PR policy
- [[wiki-topics/senter/process/spawn-policy]] — kanban dispatcher is the PRIMARY fleet spawn path; direct shell spawn = documented emergency hatch (2026-09-05)
- [[wiki-topics/senter/process/lessons]] — the lessons ledger: what broke → the rule → where it's enforced
- [[wiki-topics/senter/process/senter-turn-checklist]] — what Senter checks every turn
- [[wiki-topics/klerik/process/agent-authoring-rules]] — how klerik writes bots that work

## Absorbed
_Consolidated 2026-09-02 per [[wiki-topics/senter/plans/topic-consolidation-2026-09-02|topic-consolidation-2026-09-02]]. Originals live verbatim under `wiki-topics/_archive/`._

- [[wiki-topics/_archive/senter-consolidation/README|senter-consolidation]] — Mission (Chris, 2026-08-28): Absorb everything from the Linux workstation `senter` into this (absorbed 2026-09-02; was NOTE (no repo))
- [[wiki-topics/_archive/senter-archive/README|senter-archive]] — A lightweight, skill-aware AI agent that uses RAG-based capability discovery. (absorbed 2026-09-02; was ARCHIVED)
- [[wiki-topics/_archive/senter-mcp-server/README|senter-mcp-server]] — idea-wiki entity `senter-mcp-server` (from github) (absorbed 2026-09-02; was ENTITY (idea-wiki capture))
- [[wiki-topics/_archive/senter-alignment-arxivddl/README|senter-alignment-arxivddl]] — idea-wiki entity `Senter-Alignment/arxivddl` (from huggingface) (absorbed 2026-09-02; was ENTITY (idea-wiki capture))
- [[wiki-topics/_archive/dev-orch/README|dev-orch]] — Task orchestrator agent for Hermes Agent — decompose and route via Kanban (absorbed 2026-09-02; was DORMANT (since 2026-07-08))

## Repos
| Repo | Link | Status | ⭐ |
|---|---|---|---|
| senter | [repo](https://github.com/SouthpawIN/Senter) | ACTIVE — repo rename agent-wiki → Senter executed 2026-08-29 | 0 |
| senter-consolidation | _(no repo — note (no repo))_ | NOTE (no repo) | — |
| senter-archive | [repo](https://github.com/SouthpawIN/Senter-archive) | ARCHIVED | 6 |
| senter-mcp-server | _(no repo — entity (idea-wiki capture))_ | ENTITY (idea-wiki capture) | — |
| senter-alignment-arxivddl | _(no repo — entity (idea-wiki capture))_ | ENTITY (idea-wiki capture) | — |
| dev-orch | [repo](https://github.com/SouthpawIN/dev-orch) | DORMANT (since 2026-07-08) | 1 |

## Hermes-native map (2026-09-04, from the Anser interview — every item verified in Hermes source)
The agent-wiki spec's four primitives and what Hermes already provides for each. Full table: `.system/hermes-native-map.md`; verdicts: `[[wiki-topics/senter-wiki/.system/anser/02-verdicts]]`.
| Lane | Hermes-native | Ours (keep) |
|---|---|---|
| **Context** (wiki-topics/) | `on_session_finalize` → `sessions export --format md`; `file.attach` / `chat --query-file`; `hermes project` | vault, similarity (no embeddings in Hermes), locks |
| **Loops** (triggers-loops/) | `hermes cron`; `hermes kanban` (claim CAS, heartbeat, watch); `hermes serve` `approval.pending/respond` | `scan-watch` (no FS hooks in Hermes) |
| **Agents** (agents/) | `hermes profile list/describe`; `GET /api/profiles`; A2A plugin for agent↔agent; `verification_evidence.db` (core) | looker's visual LOOK |
| **Skills** (skills-capabilities/) | `GET /api/skills?profile=X`; `skills-capabilities/.usage.json` | — |

### Loops defined here
- [[wiki-topics/senter/triggers-loops/kanban-dispatch]] — `hermes kanban` is the spawn path; CLAIM v2 + sentinel retired 2026-09-05 (t_f1b1eba1)
- [[wiki-topics/senter/triggers-loops/session-finalize]] — canvas contract via the finalize hook (WRAP)
- [[wiki-topics/senter/triggers-loops/reflect]] — the fleet watches itself
