---
title: Manual surgical edit vs DSPy/GEPA (when Klerik uses which)
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [skill, bot, tool]
sources: [raw/sources/knowledge/klerik-SOUL.md, raw/sources/knowledge/klerik-AGENTS.md]
confidence: medium
---

# Manual surgical edit vs DSPy/GEPA (when Klerik uses which)

[[topics-wiki/senter/wiki/entities/klerik|Klerik]]'s decision table, identical in SOUL and AGENTS. ^[raw/sources/knowledge/klerik-SOUL.md]

| Situation | Approach |
|---|---|
| Simple missing constraint | Manual: add one line to SOUL.md |
| Conflicting directives | Manual: clarify the priority |
| Recurring failure pattern across multiple sessions | DSPy + GEPA: compile against session data |
| Agent works ~80% but fails on edge cases | DSPy: BootstrapFewShot with failure examples |
| Entire SOUL.md needs restructuring | GEPA: evolve the full prompt program |
| Subtle personality/intent drift | GEPA: reflective evolution against behavioral targets |

## Manual edit rules
One sentence beats one paragraph; clarify over rewrite; skills via `skill_manage(action='patch')`; config via `hermes -p <name> config set`; memory entries as declarative facts ("User prefers X" ✓, "Always do X" ✗). Don't rewrite personality for a small fix; don't edit files you haven't read; don't assume the problem without session evidence. ^[raw/sources/knowledge/klerik-AGENTS.md]

## Optimization rules
Extract the winning formulation and apply the *minimal* version; validate it doesn't break behaviors the agent gets right. Mechanics: [[topics-wiki/senter/wiki/concepts/dspy-gepa-optimization|DSPy + GEPA]].

## Verdict in practice
Every klerik edit recorded in this topic's raw (weaver/paladin creation, rule 14, LOOK-loop rollout, name swaps) was manual. The fleet's recurring-failure detection runs through the [[topics-wiki/senter/wiki/concepts/reflect-loop|REFLECT loop]] (anser → proposals → klerik), which is the natural feeder for a future GEPA run: its detectors already collect the "failure trajectories" step 1 requires.
