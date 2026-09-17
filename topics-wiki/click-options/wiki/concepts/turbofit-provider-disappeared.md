---
title: TurboFit Provider Disappeared
created: 2026-09-14
updated: 2026-09-14
type: concept
tags: [pain, tool, question, infra, idea]
sources: [raw/inbox/2026-09-13.md]
confidence: high
---

# TurboFit Provider Disappeared

## The issue
On **2026-09-13 17:20** Chris reported a new problem: TurboFit is **no longer showing as a provider**. It had previously been there, holding his models, and now it isn't even on the list.

> "I don't see turbo fit as a provider. It was there before and it had my models and now it's not even on the list when I Click on the arrow on the desktop to show me all the models and providers and input bar here"

^[raw/inbox/2026-09-13.md]

## Where it vanishes
- The provider/model picker is the **arrow on the desktop** that expands **all the models and providers**, next to the input bar. TurboFit and its models used to appear there; now they don't.

## Status / open question
Unresolved at filing. Open questions:
- Did the TurboFit runtime/service crash or fail to launch (was it working earlier that day, alongside the password-recovery attempt)?
- Is this a model-loading failure specifically, or the whole provider vanishing from the list?
- Related to any Hermes runtime / Turbofit adaptive-local-model state?

^[raw/inbox/2026-09-13.md]

## Notes
- Same session as the Recovery Mode password reset — the day was already rocky (failed non-recovery attempts → Recovery Mode → then this provider issue).
- Related: [[click-options/wiki/decisions/recovery-mode-password-reset|Recovery Mode Password Reset]].
