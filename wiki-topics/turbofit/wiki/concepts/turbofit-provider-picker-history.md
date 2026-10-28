---
title: TurboFit Provider — the desktop-picker history
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [turbofit, provider, provenance, consolidation]
sources: [raw/sources/2026-10-28-github-consolidation.md]
confidence: high
---

# TurboFit Provider — the desktop-picker history

> Every time the TurboFit provider vanished from (or never registered into) the Hermes desktop provider/model picker. One page, one story: the backend was never the problem.

**Absorbed 2026-10-28** from pages that had been filed in other topics (one spot for TurboFit knowledge). Source pages are now redirect stubs.

## Sources absorbed

- `wiki-topics/click-options/wiki/concepts/turbofit-provider-disappeared.md` — TurboFit Provider Disappeared (created 2026-09-14)
- `wiki-topics/click-options/wiki/concepts/turbofit-provider-still-missing-2026-09-15.md` — TurboFit Provider Still Missing from the Desktop Picker (2026-09-15) (created 2026-09-15)
- `wiki-topics/click-options/wiki/concepts/turbofit-models-under-provider.md` — TurboFit Models Grouped Under the TurboFit Provider (created 2026-09-15)
- `wiki-topics/click-options/wiki/entities/turbofit-picker-registration-gap.md` — TurboFit Picker-Registration Gap (created 2026-09-17)
- `wiki-topics/click-options/wiki/comparisons/turbofit-provider-recurring-disappearance.md` — TurboFit Provider — Recurring Disappearance Pattern (created 2026-09-17)
- `wiki-topics/click-options/wiki/concepts/runtime-config-fix-2026-09-15.md` — Runtime Config Fix — wayvnc + Provider Endpoints (created 2026-09-15)
- `wiki-topics/back-where/wiki/entities/turbofit-options-missing-after-restart.md` — TurboFit options missing after restarting the desktop app (created 2026-09-15)

---

## TurboFit Provider Disappeared

## The issue
On **2026-09-13 17:20** Chris reported a new problem: TurboFit is **no longer showing as a provider**. It had previously been there, holding his models, and now it isn't even on the list.

> "I don't see turbo fit as a provider. It was there before and it had my models and now it's not even on the list when I Click on the arrow on the desktop to show me all the models and providers and input bar here"

^[provenance: click-options/raw/inbox/2026-09-13.md]

## Where it vanishes
- The provider/model picker is the **arrow on the desktop** that expands **all the models and providers**, next to the input bar. TurboFit and its models used to appear there; now they don't.

## Status / open question
Unresolved at filing. Open questions:
- Did the TurboFit runtime/service crash or fail to launch (was it working earlier that day, alongside the password-recovery attempt)?
- Is this a model-loading failure specifically, or the whole provider vanishing from the list?
- Related to any Hermes runtime / Turbofit adaptive-local-model state?

^[provenance: click-options/raw/inbox/2026-09-13.md]

## Notes
- Same session as the Recovery Mode password reset — the day was already rocky (failed non-recovery attempts → Recovery Mode → then this provider issue).
- Related: Recovery Mode Password Reset.

---

## TurboFit Provider Still Missing from the Desktop Picker (2026-09-15)

## The escalation
On **2026-09-15**, after the runtime/config fixes (wayvnc systemd service, and the Hermes `https://`-on-plain-HTTP scheme correction) and after both models were confirmed **working through the Hermes backend** at **13:21**, Chris reported that the **TurboFit provider still does not appear in the Hermes desktop provider/model picker** — and he was frustrated.

> "I don't see the turbo fit at all in Hermes desktop providers like I fucking asked for"
>
> "I still don't see it when I click the drop down menu from the input bar I only see news portal followed by open code free followed by xai. Those are the only providers that I have"
>
> "Yeah, okay, so I still don't see it. You've had it there before. Come on now"

^[provenance: click-options/raw/inbox/2026-09-15.md]

## What this reframes
The problem is **no longer the backend**. The models respond through the Hermes runtime (13:21), but the **desktop picker never surfaces the TurboFit provider**. As of **18:05** the picker dropdown (the arrow on the desktop, next to the input bar) shows **only three providers: news portal, open code free, xai** — TurboFit is not among them.^[provenance: click-options/raw/inbox/2026-09-15.md]

So the live gap is a **picker-registration / UI-config problem**, distinct from the earlier scheme fix. The models are "there" in the backend but not registered into the desktop picker's provider list.

## Why it matters
- It is a **recurrence** of the 2026-09-13 incident ([[turbofit-provider-picker-history|TurboFit Provider Disappeared]]) — TurboFit was gone then, and is gone from the picker again now.
- It contradicts the expectation in TurboFit Models Grouped Under the TurboFit Provider: Chris wants the TurboFit provider present and selectable in the picker with all its models nested under it. That grouping was **not** visually confirmed — the provider never appears.
- It sits alongside the acceptance gate in Test Through Hermes, Not Straight to the Endpoint: the endpoint works, but the *user path through the picker* still errors/omits TurboFit.

## Status / open questions (contested)
- **16:34** — TurboFit not in desktop providers. **Contested**: backend works (13:21), picker does not show it.
- **17:25** — agent re-examined the provider configuration format "more carefully."
- **18:05** — still missing; Chris: "Come on now." Ongoing as of filing.
- Open: Is the TurboFit provider registered in Hermes' runtime config but not wired into the desktop picker's provider list? Is it a picker-config gap vs. a model-loading failure? Related to Runtime Config Fix — wayvnc + Provider Endpoints.

---

## TurboFit Models Grouped Under the TurboFit Provider

## The expectation
On **2026-09-15 12:40** Chris stated how he wants his models organized inside Hermes: **all TurboFit models live under the TurboFit provider**, alongside detected Tailscale models and available local models.

> "I want all my turbo fit models to be under my turbo fit provider."

^[provenance: click-options/raw/inbox/2026-09-15.md]

## What "done" looks like
Inside Hermes, in the provider/model picker (the arrow on the desktop that expands all models and providers — see [[turbofit-provider-picker-history|TurboFit Provider Disappeared]]):

- **TurboFit provider** present and selectable.
- Every TurboFit model nested **under** that provider, not spread across providers.
- **Tailscale models** detected and shown.
- **Local models** listed.
- Selecting/testing any of them produces **no error**.

## Why it matters
It's the opposite of the 2026-09-13 problem — there TurboFit had vanished entirely and his models went with it. Now the concern is **correct grouping and discoverability** once the provider is back.

## Status
Models confirmed "working through Hermes" as of **13:21** on 2026-09-15.^[provenance: click-options/raw/inbox/2026-09-15.md] Whether the grouping (all TurboFit models under the one provider) was visually confirmed by Chris is **not** — the provider never appears in the picker. As of **18:05** the dropdown shows only news portal, open code free, xai. This is the live gap: TurboFit Provider Still Missing from the Desktop Picker (2026-09-15).

## Notes
- Tied to the acceptance test: Test Through Hermes, Not Straight to the Endpoint.
- The picker location is the same arrow-on-desktop control from the TurboFit-provider-disappeared incident.

---

## TurboFit Picker-Registration Gap

## The gap
TurboFit models work **through the Hermes runtime** (confirmed 13:21 on 2026-09-15), but they never **persist into the Hermes desktop provider/model picker** — the arrow-on-desktop control next to the input bar that expands every model and provider. As of **2026-09-15 18:05** the picker dropdown shows **only news portal, open code free, xai**. The models are registered in the runtime config but not wired into the picker's provider list.

> "I still don't see it when I click the drop down menu from the input bar I only see news portal followed by open code free followed by xai. Those are the only providers that I have"

^[provenance: click-options/raw/inbox/2026-09-15.md]

## Why it is distinct
It is **not** the backend. The https-on-HTTP scheme fix ([[click-options/wiki/concepts/runtime-config-fix-2026-09-15|Runtime Config Fix — wayvnc + Provider Endpoints)]) made the models respond through Hermes — but that was necessary, not sufficient. The remaining failure is a **registration/UI-config** layer: whatever the picker reads to build its provider list is not receiving the TurboFit provider.

## Why it matters
- It is the **recurring root cause** across 09-13 (disappeared), 09-15 (gone from picker again), and 09-16 (roster came back incomplete — "Please, please do better"). See [[turbofit-provider-picker-history|TurboFit Provider Recurring Disappearance Pattern]].
- It defeats the acceptance gate ([[click-options/wiki/decisions/test-through-hermes-not-endpoint|Test Through Hermes, Not Straight to the Endpoint)]) and the grouping expectation ([[click-options/wiki/concepts/turbofit-models-under-provider|TurboFit Models Grouped Under the TurboFit Provider)]).
- It is a **picker-registration** problem, not a model-loading problem — so fixes keep touching the wrong layer.

## Status (contested)
- **13:21** 2026-09-15: models pass through Hermes backend.
- **16:34–18:05** 2026-09-15: provider still absent from picker.
- **20:40** 2026-09-16: Model Zoo roster came back incomplete.
- Open: which config file/registry does the desktop picker read to enumerate providers, and why is TurboFit not written into it? Related: TurboFit Provider Still Missing from the Desktop Picker (2026-09-15).

---

## TurboFit Provider — Recurring Disappearance Pattern

## The pattern
Across three days the TurboFit provider (and the models nested under it) has failed to survive in the Hermes **desktop provider/model picker** — the arrow-on-desktop control next to the input bar. The failures are distinct in flavor but share one root: TurboFit works at the backend, yet never lands in the picker's provider list.

| Date | What happened | Backend | Picker |
|------|---------------|---------|--------|
| **2026-09-13** | TurboFit provider vanished entirely; models went with it. | unknown | gone |
| **2026-09-15** | After scheme + wayvnc fixes, both models pass **through Hermes** at **13:21**, but the picker (16:34–18:05) shows only **news portal, open code free, xai**. | working | missing |
| **2026-09-16 20:40** | Chris's Model Zoo list came back **incomplete** on the TurboFit list — "Please, please do better." | unconfirmed | unconfirmed |

^[provenance: click-options/raw/inbox/2026-09-13.md · raw/inbox/2026-09-15.md · raw/inbox/2026-09-16.md]

## What ties them together
1. **The backend is not the test.** Chris's acceptance gate (Test Through Hermes, Not Straight to the Endpoint) is the user path: open Hermes, pick the provider/model, no error. The endpoint passing does **not** prove the picker shows it.
2. **The gap is picker-registration, not model loading.** As of **2026-09-15 18:05** the provider is "there" in the runtime config but not wired into the picker's provider list (TurboFit Provider Still Missing from the Desktop Picker (2026-09-15)). That is the recurring failure mode.
3. **The expectation is grouping + completeness.** Chris wants **all his TurboFit models under the TurboFit provider**, discoverable, no gaps (TurboFit Models Grouped Under the TurboFit Provider), and the Model Zoo roster fully populated (Model Zoo Models for the TurboFit List).

## Why it is a pattern, not an incident
- 09-13 was a **disappearance** ([[turbofit-provider-picker-history|TurboFit Provider Disappeared]]).
- 09-15 was a **recurrence** — back after the fix, gone from the picker again.
- 09-16 is a **new shape of the same gap**: even the roster he asked for came back incomplete, which reads as the picker-registration problem bleeding into the model population ("Please, please do better").

The through-line: TurboFit is repeatedly **not persisting into the picker's provider list**, and each fix that touches the backend leaves the picker gap open.

## Open question (contested)
Is there a single registration step that keeps re-failing — a config the picker reads but the fixes never write? Until that one root is found, each day produces a new variant of the same missing-provider symptom. Related: Runtime Config Fix — wayvnc + Provider Endpoints.

---

## Runtime Config Fix — wayvnc + Provider Endpoints

## What was filed
Two `hermes` working entries on **2026-09-15** documenting runtime/config problems Chris was stepping through:

### wayvnc timeout → persistent service
- **09:40** — **wayvnc shut down after the 5-second timeout.** The fix underway was to **set up the persistent systemd service properly and test again.**^[provenance: click-options/raw/inbox/2026-09-15.md]
- Reads as a remote-desktop (wayvnc) service that was dying on a short timeout; the standing fix is a systemd unit that keeps it alive, re-tested after.

### Hermes hitting `https://` on plain-HTTP endpoints
- **11:19** — **Hermes was trying `https://` on plain HTTP endpoints.** The fix was to **correct the provider config and test both models.**^[provenance: click-options/raw/inbox/2026-09-15.md]
- The provider config had a scheme mismatch (https vs http); both models were re-tested after the correction.

## Status
Both recorded as `hermes` working logs in progress on 2026-09-15. Outcome (did the systemd service hold? did both models pass after the scheme fix?) not yet captured in `raw/`. Related infra friction: [[turbofit-provider-picker-history|TurboFit Provider Disappeared]] (the provider vanishing from the picker the prior day).
- **2026-09-15 13:21:** both models confirmed working through the Hermes backend. But the desktop picker still does not show TurboFit (16:34–18:05) — so the config fixes were necessary, not sufficient. The remaining gap is a picker-registration problem, not the scheme fix: TurboFit Provider Still Missing from the Desktop Picker (2026-09-15).

## Notes
- These are runtime/config items that touch **what you click to pick a provider/model** — same topic family as the TurboFit provider disappearing — but the root cause this day was config (scheme + service lifetime), not the picker itself. For the tab-bar discoverability issue, see Tab Opening Quick Fixes.

---

## TurboFit options missing after restarting the desktop app

## The observation

On 2026-09-15 Chris restarted the Hermes desktop app on the MacBook and found the **TurboFit** options gone — they did not come back after the restart. ^[provenance: back-where/raw/inbox/2026-09-15.md]

> "Okay, so I just restarted this desktop app on the MacBook and I don't see those turbo-fit options" ^[provenance: back-where/raw/inbox/2026-09-15.md]

This is a UI regression on his own hardware: the TurboFit controls that were present before the restart are absent after it. It lands squarely in back-where's scope — Chris's runtime/UI issue on local M1 hardware — rather than generic wiki-UI work (weaver) or upstream Hermes code (teknium PR ledger). ^[provenance: back-where/raw/inbox/2026-09-15.md]

## Context: an interrupted turn

The restart observation came right after a system note that Chris's previous turn had been interrupted mid-run — the app or its backend stopped before the turn finished, and he was told to check current state before redoing anything. ^[provenance: back-where/raw/inbox/2026-09-15.md] A second interruption note followed at 18:12, this time flagging that a background process (`proc_53905ab10dea`) matched the watch pattern "mesh". ^[provenance: back-where/raw/inbox/2026-09-15.md] So the missing TurboFit options appeared inside a session that was itself being interrupted, not in a clean fresh start.

## Relation to the double-GPU model work

The TurboFit concern sits in the same session as the Q3K XL / Unleashed double-GPU choice — the desktop app Chris restarted is the one carrying his TurboFit-tuned models. The prior session's 13:21 report ("Both models verified working through Hermes") did not survive into this post-restart turn, where the TurboFit surface itself was already missing. ^[provenance: back-where/raw/inbox/2026-09-15.md]

## Status

Open as of 2026-09-15 18:12. The TurboFit options had not returned after the desktop-app restart, and the turn was still interrupted (background process matching "mesh" still active). No recovery action recorded. ^[provenance: back-where/raw/inbox/2026-09-15.md]

## Related

- Q3K XL / Unleashed double-GPU choice
- UI layout regression after diff view change
- End-to-end verification before declaring done
