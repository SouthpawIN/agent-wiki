---
title: TurboFit Provider — Recurring Disappearance Pattern
created: 2026-09-17
updated: 2026-09-17
type: comparison
tags: [tool, pain, question, infra, preference, timeline]
sources: [raw/inbox/2026-09-13.md, raw/inbox/2026-09-15.md, raw/inbox/2026-09-16.md]
confidence: high
---

# TurboFit Provider — Recurring Disappearance Pattern

## The pattern
Across three days the TurboFit provider (and the models nested under it) has failed to survive in the Hermes **desktop provider/model picker** — the arrow-on-desktop control next to the input bar. The failures are distinct in flavor but share one root: TurboFit works at the backend, yet never lands in the picker's provider list.

| Date | What happened | Backend | Picker |
|------|---------------|---------|--------|
| **2026-09-13** | TurboFit provider vanished entirely; models went with it. | unknown | gone |
| **2026-09-15** | After scheme + wayvnc fixes, both models pass **through Hermes** at **13:21**, but the picker (16:34–18:05) shows only **news portal, open code free, xai**. | working | missing |
| **2026-09-16 20:40** | Chris's Model Zoo list came back **incomplete** on the TurboFit list — "Please, please do better." | unconfirmed | unconfirmed |

^[raw/inbox/2026-09-13.md · raw/inbox/2026-09-15.md · raw/inbox/2026-09-16.md]

## What ties them together
1. **The backend is not the test.** Chris's acceptance gate ([[click-options/wiki/decisions/test-through-hermes-not-endpoint|Test Through Hermes, Not Straight to the Endpoint]]) is the user path: open Hermes, pick the provider/model, no error. The endpoint passing does **not** prove the picker shows it.
2. **The gap is picker-registration, not model loading.** As of **2026-09-15 18:05** the provider is "there" in the runtime config but not wired into the picker's provider list ([[click-options/wiki/concepts/turbofit-provider-still-missing-2026-09-15|TurboFit Provider Still Missing from the Desktop Picker (2026-09-15)]]). That is the recurring failure mode.
3. **The expectation is grouping + completeness.** Chris wants **all his TurboFit models under the TurboFit provider**, discoverable, no gaps ([[click-options/wiki/concepts/turbofit-models-under-provider|TurboFit Models Grouped Under the TurboFit Provider]]), and the Model Zoo roster fully populated ([[click-options/wiki/decisions/model-zoo-models-for-turbofit-list|Model Zoo Models for the TurboFit List]]).

## Why it is a pattern, not an incident
- 09-13 was a **disappearance** ([[click-options/wiki/concepts/turbofit-provider-disappeared|TurboFit Provider Disappeared]]).
- 09-15 was a **recurrence** — back after the fix, gone from the picker again.
- 09-16 is a **new shape of the same gap**: even the roster he asked for came back incomplete, which reads as the picker-registration problem bleeding into the model population ("Please, please do better").

The through-line: TurboFit is repeatedly **not persisting into the picker's provider list**, and each fix that touches the backend leaves the picker gap open.

## Open question (contested)
Is there a single registration step that keeps re-failing — a config the picker reads but the fixes never write? Until that one root is found, each day produces a new variant of the same missing-provider symptom. Related: [[click-options/wiki/concepts/runtime-config-fix-2026-09-15|Runtime Config Fix — wayvnc + Provider Endpoints]].
