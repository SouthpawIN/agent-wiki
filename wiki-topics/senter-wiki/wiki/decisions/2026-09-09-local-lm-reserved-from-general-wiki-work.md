---
title: "Local LM Reserved from General Wiki Work"
created: 2026-09-09
updated: 2026-09-10
type: decision
tags: [decision, model, budget, infra]
sources:
  - raw/inbox/2026-09-09-from-turbofit.md
  - raw/inbox/2026-09-10-from-turbofit.md
confidence: high
---

## What

Local LM inference is not used for general Senter wiki work. It is reserved for local-model-as-deliverable cases only.

## Why

Chris redirected Hermes off the local model for general work on 2026-09-09 20:05; local model reserved for local-model-as-deliverable cases only (e.g. 131k-llm-tuning-on-m1).

## Evidence

- Chris 20:05: "understand that we can undo choices you make easily, so do not be afraid to make them" — proactive-completion directive applies to all wiki infra/UI work
- Hermes model budget exhaustion concern: "User wants 10+ tok/s at 131K context but has accepted this is physically impossible on current hardware"

## Contradictions

None known. This decision is consistent with the broader model-budget policy documented in [[wiki-topics/senter-wiki/wiki/concepts/model-budget-exhaustion-local-lm.md]].

## Related

- [[wiki-topics/senter-wiki/wiki/concepts/proactive-completion-directive.md|Proactive Completion Directive]]
- [[wiki-topics/senter-wiki/wiki/concepts/model-budget-exhaustion-local-lm.md|Model Budget Exhaustion]]
- [[wiki-topics/senter-wiki/wiki/entities/vault-live-html.md|Vault Live HTML]]