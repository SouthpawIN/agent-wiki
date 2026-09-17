---
title: "Compile pre-planning — pre-prompting before context is sorted into the wiki (Chris's 19:18 ask)"
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [idea, plan, question, spec]
sources:
  - raw/inbox/2026-09-05.md
confidence: medium
---

# Compile pre-planning

## The ask (Chris, 19:18)
> "Very nice so far continue with that workflow. Let's continue working looking for anything that might be useful for anyone these steps such as any kind of pre-prompting or pre-planning can be gone into when context is being sorted into the wiki." ^[raw/inbox/2026-09-05.md]

Two things are in that sentence:
1. **"continue with that workflow"** — the 19:06→19:12 loop (he states a layout pain by voice → the fix lands in his pane → DOM-proven → he watches the wiki change) is approved as the working mode. ^[raw/inbox/2026-09-05.md]
2. **"useful for anyone"** — he wants the compile step (raw → wiki) to gain a *pre-prompting / pre-planning* stage that would help any user of Senter, not a one-off tweak for his vault.

## What "sorting context into the wiki" is today
The [[topics-wiki/senter-wiki/wiki/entities/topic-wiki-compile-loop|topic-wiki compile loop]] gives one senter bot run per topic the SCHEMA, index, log tail and the new raw items, and asks for pages. The one worked example of quality so far is the [[topics-wiki/senter-wiki/wiki/concepts/wiki-page-quality-bar|page quality bar]] (verbatim quotes, provenance, the *why*, supersession, contested flags, missed open questions). The known failure is the [[topics-wiki/senter-wiki/wiki/queries/duplicate-page-candidates|17 duplicate page pairs]] from two compiles over one raw set — evidence that the compiler lacks a *plan before it writes* (which existing pages to update vs create). ^[raw/inbox/2026-09-05.md]

## Candidate shape (assistant synthesis, not decided)
A pre-plan step before any page is written: read index → list the entities/decisions in the new raw → map each to *update existing page X* or *create slug Y* → only then write. This is exactly the plan/apply split Chris already lives with in Hermes ("plan" skill) and matches the GEPA stages Collect → Generate → Evaluate → Apply in [[topics-wiki/senter-wiki/wiki/concepts/factory-pipeline-gepa|the factory pipeline]]. Whether the pre-plan is a prompt section, a separate bot pass, or a Hermes-native planning primitive is open; Chris's preference points native ([[topics-wiki/senter-wiki/wiki/concepts/collapse-toward-hermes-native|collapse toward Hermes-native]]).

## Open
- Which pre-prompting techniques are worth adopting (Karpathy's LLM-wiki practices, plan-then-write, schema-first extraction) — research candidate.
- Chris said "for anyone" — the output should be a shareable skill/prompt, not a vault-specific hack.
