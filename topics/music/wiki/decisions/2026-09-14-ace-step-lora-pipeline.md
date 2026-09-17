---
title: 2026-09-14 ACE-Step LoRA pipeline standing goal
created: 2026-09-15
updated: 2026-09-15
type: decision
tags: [decision, music, plan, idea, tool]
sources: [raw/inbox/2026-09-14.md, raw/inbox/2026-09-15.md]
confidence: high
---
# 2026-09-14 ACE-Step LoRA pipeline standing goal

On 2026-09-14, Chris chose to build a repeatable LoRA pipeline on top of [[topics/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]]. This is a standing goal, not a one-off: it activates whenever Chris says "go." ^[raw/inbox/2026-09-14.md]

## What
When Chris says "go," the pipeline produces two things from the mp3s he has downloaded to a folder:
1. A LoRA of that music style. ^[raw/inbox/2026-09-14.md]
2. A batch of prompts that "effectively define that music style in the best way that AceStep expects." ^[raw/inbox/2026-09-14.md]

## Why
Chris wants a working, on-demand generation workflow rather than another model to test. The earlier 2026-09-07 effort was about *whether a model would run at all*; this is about *making the chosen model produce his own style*. ^[raw/inbox/2026-09-14.md]

## How (method Chris mandated)
- Research must come from AceStep's own documentation, via `/learn`, following links and being inquisitive. ^[raw/inbox/2026-09-14.md]
- Maintain a separate notepad for follow-up questions and loop back to answer them when research runs out. ^[raw/inbox/2026-09-14.md]
- The process is open-ended and self-propagating until questions are exhausted. ^[raw/inbox/2026-09-14.md]

## When
Standing, triggered by the word "go." No deadline stated. ^[raw/inbox/2026-09-14.md]

## Evidence
- "Can we get AceStep 1.5 4B and make a pipeline to make LoRAs of it." ^[raw/inbox/2026-09-14.md]
- "when I say go, I want both a LoRA and a batch of prompts that effectively define that music style in the best way that AceStep expects" ^[raw/inbox/2026-09-14.md]
- "which will require you to research and use /learn with all of the AceStep documentation that you can find; follow links and be inquisitive." ^[raw/inbox/2026-09-14.md]
- "Keep a separate notepad to keep track of follow up questions, and then loop back to answer the follow up questions when you run out of things to do." ^[raw/inbox/2026-09-14.md]

## Conflicts / open
- Not yet reconciled with the [[topics/music/wiki/queries/local-music-generation-blockers|2026-09-07 blockers]] (ACE-Step never ran under `mlx_audio`; a LoRA pipeline needs training tooling, which is a different problem than the inference blocker). ^[raw/inbox/2026-09-07.md]
- Whether ACE-Step actually runs locally yet is still unresolved and now gates whether the pipeline runs on the Mac at all. ^[raw/inbox/2026-09-14.md]

## Related
- [[topics/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]]
- [[topics/music/wiki/concepts/ace-step-lora-pipeline|ACE-Step 1.5 4B LoRA pipeline]]
- [[topics/music/wiki/decisions/2026-09-07-music-model-priority|2026-09-07 local music model priority]]
