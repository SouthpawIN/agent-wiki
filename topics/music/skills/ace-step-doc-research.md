---
name: ace-step-doc-research
description: Use when building the ACE-Step 1.5 4B LoRA pipeline and need to ground every step in AceStep's own documentation rather than guess. Follow the /learn loop until questions run out.
version: 0.1.0
distilled: 2026-09-15
topic: music
---
# ace-step-doc-research

Ground the ACE-Step LoRA pipeline in AceStep's official documentation, not assumptions. Chris mandated this method for the pipeline.

## The loop (repeat until exhausted)
1. Find AceStep's docs for LoRA training and prompt formatting (Hugging Face repo, README, papers, model card). Use `/learn` + web search; follow every link from an official source.
2. Extract the two things the pipeline needs: (a) the exact LoRA training recipe AceStep expects (rank, alpha, format, data layout, prompt columns), and (b) the prompt schema AceStep's inference reads best.
3. Record open follow-up questions in a notepad (a dedicated file in the topic, e.g. `wiki/ace-step-notepad.md`).
4. When research runs out, go back to the notepad and answer each open question — which generates new questions. Loop until no new questions appear.

## Rules
- Prefer AceStep's own docs over third-party tutorials; cite the source for every claim.
- Keep the notepad alive and append to it, never delete entries — the loop depends on it.
- Distinguish "AceStep says X" (cited) from "we assume X" (flag it).
- If a doc contradicts an earlier assumption (e.g. the 2026-09-07 `mlx_audio` runner note), note the conflict and defer to the current source.

## Evidence
> "which will require you to research and use /learn with all of the AceStep documentation that you can find; follow links and be inquisitive."
> "Keep a separate notepad to keep track of follow up questions, and then loop back to answer the follow up questions when you run out of things to do."
