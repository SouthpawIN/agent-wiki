---
title: TurboFit Picker-Registration Gap
created: 2026-09-17
updated: 2026-09-17
type: entity
tags: [tool, pain, question, infra, decision]
sources: [raw/inbox/2026-09-15.md, raw/inbox/2026-09-16.md]
confidence: high
---

# TurboFit Picker-Registration Gap

## The gap
TurboFit models work **through the Hermes runtime** (confirmed 13:21 on 2026-09-15), but they never **persist into the Hermes desktop provider/model picker** — the arrow-on-desktop control next to the input bar that expands every model and provider. As of **2026-09-15 18:05** the picker dropdown shows **only news portal, open code free, xai**. The models are registered in the runtime config but not wired into the picker's provider list.

> "I still don't see it when I click the drop down menu from the input bar I only see news portal followed by open code free followed by xai. Those are the only providers that I have"

^[raw/inbox/2026-09-15.md]

## Why it is distinct
It is **not** the backend. The https-on-HTTP scheme fix ([[click-options/wiki/concepts/runtime-config-fix-2026-09-15|Runtime Config Fix — wayvnc + Provider Endpoints)]) made the models respond through Hermes — but that was necessary, not sufficient. The remaining failure is a **registration/UI-config** layer: whatever the picker reads to build its provider list is not receiving the TurboFit provider.

## Why it matters
- It is the **recurring root cause** across 09-13 (disappeared), 09-15 (gone from picker again), and 09-16 (roster came back incomplete — "Please, please do better"). See [[click-options/wiki/comparisons/turbofit-provider-recurring-dispearance|TurboFit Provider Recurring Disappearance Pattern]].
- It defeats the acceptance gate ([[click-options/wiki/decisions/test-through-hermes-not-endpoint|Test Through Hermes, Not Straight to the Endpoint)]) and the grouping expectation ([[click-options/wiki/concepts/turbofit-models-under-provider|TurboFit Models Grouped Under the TurboFit Provider)]).
- It is a **picker-registration** problem, not a model-loading problem — so fixes keep touching the wrong layer.

## Status (contested)
- **13:21** 2026-09-15: models pass through Hermes backend.
- **16:34–18:05** 2026-09-15: provider still absent from picker.
- **20:40** 2026-09-16: Model Zoo roster came back incomplete.
- Open: which config file/registry does the desktop picker read to enumerate providers, and why is TurboFit not written into it? Related: [[click-options/wiki/concepts/turbofit-provider-still-missing-2026-09-15|TurboFit Provider Still Missing from the Desktop Picker (2026-09-15)]].
