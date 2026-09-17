---
title: Skill — senter-fleet-coordination
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [skill, spec]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Skill — senter-fleet-coordination

`senter-fleet-coordination` is [[topics-wiki/senter/wiki/entities/senter|Senter]]'s operating playbook: "Use when routing fleet ideas, bots, or vault logs. Senter coordinator playbook — dispatch/verify/relay, sentinel + Meeseeks + REFLECT pipeline, user's standing rules." ~60 KB, ~70 pitfalls, each traced to a Chris correction with the date. It is the densest single source on how the fleet actually runs. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Sections
1. **Operating model** (conversation-first, locked 2026-08-30) → [[topics-wiki/senter/wiki/decisions/2026-08-30-conversation-first-operating-model|decision]].
2. **Routing rules** incl. the HARD CORRECTION "Senter routes; Senter does not build" → [[topics-wiki/senter/wiki/concepts/routing-rules|Routing rules]].
3. **Fleet table** (8 bots as of 2026-09-02, pre-looker) → [[topics-wiki/senter/wiki/comparisons/fleet-rosters-over-time|rosters]].
4. **Topic mechanics (GOOP spec)** → [[topics-wiki/senter/wiki/concepts/topics-are-the-work-units|Topics are the work units]].
5. **Standing approval** → [[topics-wiki/senter/wiki/decisions/2026-08-30-standing-approval|decision]].
6. **Pitfalls** (~65 bullets) → distilled in [[topics-wiki/senter/wiki/concepts/fleet-coordination-lessons|Fleet coordination lessons]].
7. **Channel failure workarounds** (proven 2026-08-30) — DM bodies dropped in transit, bridge, voice-name map, rename ≠ rebind, gate-blocked ≠ verified, working names, companion-bot doctrine, state.db reading, post-install sanity, selfmodel, north star, preview-pane limits, ISO etch, and the (partly superseded) early vault-UI style bullets.

## Reference files it points to (in `references/`)
`fleet-dispatch.md`, `senter-bridge.md`, `build-loop.md`, `desktop-composer-inventory.md`, `pane-viewport.md`, `wiki-input-overline.md`, `wiki-backdrop.md`, `parallel-topics-and-claims.md`, `delegation-model.md`, `self-healing-pipeline.md`, `live-data-contract.md`, `music-integrations.md`, `tool-latency-audit.md`, `look-loop-addenda.md`, `vault-ui-architecture.md`. Scripts: `scripts/fleet-status.sh`, `scripts/tool-latency.sh`.

## Vault process docs it names
`topics-wiki/senter/process/build-loop.md` (pipeline/verification rules), `topics-wiki/senter/process/senter-turn-checklist.md` (item 0 = delivery before reflection), `topics-wiki/klerik/process/agent-authoring-rules.md` (klerik-owned), `topics-wiki/senter/triggers-loops/reflect.md`, `topics-wiki/senter/.system/selfmodel/`, `topics-wiki/hermes-agent/prs/` (PR ledger). Per Chris these process artifacts ARE the product ([[topics-wiki/senter/wiki/decisions/2026-09-02-process-artifacts-are-the-product|decision]]).

## Supersession note inside the skill
The early vault-UI bullets (2026-08-31: status pills, sub-labels, bot dots, orchestrator floating chat, 42% hub, inline expand) are marked SUPERSEDED by the `agent-wiki-vault-ui` skill's v6.2+ contract — "Treat `agent-wiki-vault-ui` as authoritative when the two disagree." See [[topics-wiki/senter/wiki/concepts/vault-ui-style-contract|style contract]].
