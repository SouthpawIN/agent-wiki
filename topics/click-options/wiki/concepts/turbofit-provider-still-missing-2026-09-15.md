---
title: TurboFit Provider Still Missing from the Desktop Picker (2026-09-15)
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [pain, tool, question, ui, infra]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# TurboFit Provider Still Missing from the Desktop Picker (2026-09-15)

## The escalation
On **2026-09-15**, after the runtime/config fixes (wayvnc systemd service, and the Hermes `https://`-on-plain-HTTP scheme correction) and after both models were confirmed **working through the Hermes backend** at **13:21**, Chris reported that the **TurboFit provider still does not appear in the Hermes desktop provider/model picker** — and he was frustrated.

> "I don't see the turbo fit at all in Hermes desktop providers like I fucking asked for"
>
> "I still don't see it when I click the drop down menu from the input bar I only see news portal followed by open code free followed by xai. Those are the only providers that I have"
>
> "Yeah, okay, so I still don't see it. You've had it there before. Come on now"

^[raw/inbox/2026-09-15.md]

## What this reframes
The problem is **no longer the backend**. The models respond through the Hermes runtime (13:21), but the **desktop picker never surfaces the TurboFit provider**. As of **18:05** the picker dropdown (the arrow on the desktop, next to the input bar) shows **only three providers: news portal, open code free, xai** — TurboFit is not among them.^[raw/inbox/2026-09-15.md]

So the live gap is a **picker-registration / UI-config problem**, distinct from the earlier scheme fix. The models are "there" in the backend but not registered into the desktop picker's provider list.

## Why it matters
- It is a **recurrence** of the 2026-09-13 incident ([[click-options/wiki/concepts/turbofit-provider-disappeared|TurboFit Provider Disappeared]]) — TurboFit was gone then, and is gone from the picker again now.
- It contradicts the expectation in [[click-options/wiki/concepts/turbofit-models-under-provider|TurboFit Models Grouped Under the TurboFit Provider]]: Chris wants the TurboFit provider present and selectable in the picker with all its models nested under it. That grouping was **not** visually confirmed — the provider never appears.
- It sits alongside the acceptance gate in [[click-options/wiki/decisions/test-through-hermes-not-endpoint|Test Through Hermes, Not Straight to the Endpoint]]: the endpoint works, but the *user path through the picker* still errors/omits TurboFit.

## Status / open questions (contested)
- **16:34** — TurboFit not in desktop providers. **Contested**: backend works (13:21), picker does not show it.
- **17:25** — agent re-examined the provider configuration format "more carefully."
- **18:05** — still missing; Chris: "Come on now." Ongoing as of filing.
- Open: Is the TurboFit provider registered in Hermes' runtime config but not wired into the desktop picker's provider list? Is it a picker-config gap vs. a model-loading failure? Related to [[click-options/wiki/concepts/runtime-config-fix-2026-09-15|Runtime Config Fix — wayvnc + Provider Endpoints]].
