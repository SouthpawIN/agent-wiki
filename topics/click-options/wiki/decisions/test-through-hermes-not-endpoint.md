---
title: Test Through Hermes, Not Straight to the Endpoint
created: 2026-09-15
updated: 2026-09-15
type: decision
tags: [decision, tool, plan, pain, idea]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# Test Through Hermes, Not Straight to the Endpoint

## The decision
On **2026-09-15 12:40** Chris set the acceptance criterion for testing TurboFit models: they must be exercised **through Hermes itself**, not against the raw endpoint directly.

> "Okay, but now we need to test them through Hermes. I can open up Hermes in the back end and set these as the model. Like I want to see them turbo fit as a provider and then see my and then have it detect the tail scale models and show those there and the available local models. I want all my turbo fit models to be under my turbo fit provider. So, that means that you need to test them in Hermes endpoints, so I don't get an error when I go to test it in Hermes. Not just straight to the end point, I mean through Hermes, like, open up a terminal background and try to do it as a user."

^[raw/inbox/2026-09-15.md]

## Why
The endpoint can work while Hermes still errors — the real test is the **user path**: open Hermes, pick the provider/model, and confirm no error surfaces. That is what actually matters to Chris.

## What he expects to see
- TurboFit appearing **as a provider** inside Hermes.
- His models **under the TurboFit provider** (grouped there, not scattered).
- Tailscale models **detected and shown** in the same place.
- Available **local models** listed.
- Zero errors when he selects/tests anything in Hermes.

## How it was executed
- **12:45** — agent confirmed "running on cyber-tiel-coder-35b-a3b via a custom provider."^[raw/inbox/2026-09-15.md]
- **12:50** — "Both up. Now let me test through Hermes."^[raw/inbox/2026-09-15.md]
- **13:21** — "All background processes complete. Both models working through Hermes."^[raw/inbox/2026-09-15.md]

## Notes
- This is the **acceptance gate** for the config fixes logged in [[click-options/wiki/concepts/runtime-config-fix-2026-09-15|Runtime Config Fix — wayvnc + Provider Endpoints]] (the https-on-HTTP scheme correction was the fix; testing-through-Hermes was the check).
- Same family as the TurboFit provider vanishing from the picker: [[click-options/wiki/concepts/turbofit-provider-disappeared|TurboFit Provider Disappeared]] (2026-09-13).
- **Contested 2026-09-15:** both models pass through the Hermes backend at 13:21, but the TurboFit provider still does not appear in the desktop picker (16:34–18:05). The endpoint works; the *user path through the picker* does not. See [[click-options/wiki/concepts/turbofit-provider-still-missing-2026-09-15|TurboFit Provider Still Missing from the Desktop Picker (2026-09-15)]].
