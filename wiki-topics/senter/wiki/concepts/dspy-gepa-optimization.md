---
title: DSPy + GEPA optimization (Klerik's intelligence layer)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [tool, skill, bot]
sources: [raw/sources/knowledge/klerik-SOUL.md, raw/sources/knowledge/klerik-AGENTS.md, raw/sources/knowledge/senter-SOUL.md]
confidence: medium
---

# DSPy + GEPA optimization (Klerik's intelligence layer)

[[wiki-topics/senter/wiki/entities/klerik|Klerik]] "doesn't just fix surface behavior — you comprehend and optimize the **intention** of other agents using programmatic prompt optimization." Senter's SOUL summarizes it as "DSPy + GEPA surgical edits." ^[raw/sources/knowledge/klerik-SOUL.md] ^[raw/sources/knowledge/senter-SOUL.md]

## DSPy
Declarative Language Model Programming: treat a SOUL.md as a **prompt program** — define a Signature for the agent's core task (`user_request + agent_context -> response_behavior`), wrap the behavioral pipeline in a Module, apply optimizers (BootstrapFewShot, MIPRO). "Instead of guessing whether 'be concise' or 'never exceed 3 sentences' works better, you can compile the agent's SOUL.md against real session data."

## GEPA
Genetic-Pareto Prompt Evolution — gradient-free, uses natural-language reflection: (1) sample trajectories from the target agent's sessions; (2) reflect in natural language, extract high-level rules; (3) propose prompt updates tested against actual failure cases; (4) Pareto synthesis merging complementary lessons. Claimed: outperforms RL (GRPO) by 6–20% with 35× fewer rollouts, MIPROv2 by 10%+. "Language is a richer learning medium than sparse scalar rewards."

## Procedure
1. Collect failure trajectories (`session_search`, or the target's `hermes_sessions.db`). 2. Build a DSPy program representing the current SOUL. 3. Define a metric for "correct behavior." 4. Run GEPA against the failure cases. 5. Extract the winning formulation; apply the *minimal* edit. 6. Validate it doesn't break behaviors the agent already gets right.

Signature used:
```python
class AgentBehavior(dspy.Signature):
    soul_md = dspy.InputField(desc="Current SOUL.md content")
    user_request = dspy.InputField(...)
    expected_behavior = dspy.InputField(...)
    actual_behavior = dspy.InputField(...)
    corrected_soul_edit = dspy.OutputField(desc="Minimal edit to SOUL.md that fixes the behavior")
```
Optimizer LM: `dspy.LM("openai/gpt-4.1-mini")`; `GEPA(metric=behavioral_metric, num_candidates=10)`. ^[raw/sources/knowledge/klerik-AGENTS.md]

## Status / confidence
Described as "not theoretical," but no raw item in this topic records a completed GEPA run on a fleet bot; all recorded klerik edits (weaver/paladin creation, rule 14, LOOK-loop rollout) were manual surgical edits. When to pick which: [[wiki-topics/senter/wiki/comparisons/manual-edit-vs-dspy-gepa|comparison]]. The fleet's actual repetition→edit machinery is the [[wiki-topics/senter/wiki/concepts/reflect-loop|REFLECT loop]].
