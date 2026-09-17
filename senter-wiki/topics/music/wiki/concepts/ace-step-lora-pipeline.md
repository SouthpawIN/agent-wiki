---
title: ACE-Step 1.5 4B LoRA pipeline
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [music, idea, plan, tool, infra]
sources: [raw/inbox/2026-09-14.md, raw/inbox/2026-09-15.md]
confidence: high
---
# ACE-Step 1.5 4B LoRA pipeline

On 2026-09-14, Chris set a standing goal that shifts the music topic from *getting a model to run* to *building a repeatable generation pipeline* around the model he already chose on 2026-09-07, [[topics/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]]. ^[raw/inbox/2026-09-14.md]

## The goal, in Chris's words
"I am going to download mp3s to a folder, and when I say go, I want both a LoRA and a batch of prompts that effectively define that music style in the best way that AceStep expects." ^[raw/inbox/2026-09-14.md]

Two outputs are required on the trigger word "go":
1. A LoRA trained on the mp3s in Chris's folder. ^[raw/inbox/2026-09-14.md]
2. A batch of prompts that best define that music style the way AceStep expects them. ^[raw/inbox/2026-09-14.md]

## How Chris wants it built
The pipeline must be grounded in AceStep's own documentation, not guessed. ^[raw/inbox/2026-09-14.md]
- "which will require you to research and use /learn with all of the AceStep documentation that you can find" ^[raw/inbox/2026-09-14.md]
- "follow links and be inquisitive" ^[raw/inbox/2026-09-14.md]
- "Keep a separate notepad to keep track of follow up questions, and then loop back to answer the follow up questions when you run out of things to do." ^[raw/inbox/2026-09-14.md]

So the process is explicitly open-ended and self-propagating: research until questions run out, then answer them, then keep going. ^[raw/inbox/2026-09-14.md]

## Why it matters
This is the topic's first *product* intent rather than a *candidate* hunt. On 2026-09-07 the whole topic was about whether any music model would run at all on the 32 GB Mac; now Chris has picked Ace-Step 1.5 4B as the base and wants a working LoRA + prompting workflow on top of it. ^[raw/inbox/2026-09-14.md] It also reframes the earlier blockers: the [[topics/music/wiki/concepts/mlx-audio-support-limits|mlx_audio model-type rejection]] and [[topics/music/wiki/concepts/local-music-memory-budget|memory budget]] were about *running a model once*; a LoRA pipeline is a longer, multi-stage build that may need different tooling (training, not just inference). ^[raw/inbox/2026-09-07.md]

## Open questions
- Does the LoRA train on the Mac (fits the memory budget) or off-device?
- What is AceStep's expected LoRA training format and prompt schema, and has it been read from the source?
- Where do the LoRA output, the prompt batch, and the notepad live in the vault?
- How does this relate to the [[topics/music/wiki/queries/local-music-generation-blockers|existing local-music blockers]] — is the pipeline meant to run locally once ACE-Step runs, or is it a separate track?

## Related
- [[topics/music/wiki/entities/ace-step|ACE-Step 1.5 4B (MLX 4bit)]]
- [[topics/music/wiki/decisions/2026-09-07-music-model-priority|2026-09-07 local music model priority]]
- [[topics/music/wiki/queries/local-music-generation-blockers|What blocks local music generation right now?]]
- [[topics/music/wiki/concepts/mlx-audio-support-limits|mlx_audio model support limits]]
