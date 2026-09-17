---
title: TurboFit Models Grouped Under the TurboFit Provider
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [tool, preference, idea, plan]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# TurboFit Models Grouped Under the TurboFit Provider

## The expectation
On **2026-09-15 12:40** Chris stated how he wants his models organized inside Hermes: **all TurboFit models live under the TurboFit provider**, alongside detected Tailscale models and available local models.

> "I want all my turbo fit models to be under my turbo fit provider."

^[raw/inbox/2026-09-15.md]

## What "done" looks like
Inside Hermes, in the provider/model picker (the arrow on the desktop that expands all models and providers — see [[click-options/wiki/concepts/turbofit-provider-disappeared|TurboFit Provider Disappeared]]):

- **TurboFit provider** present and selectable.
- Every TurboFit model nested **under** that provider, not spread across providers.
- **Tailscale models** detected and shown.
- **Local models** listed.
- Selecting/testing any of them produces **no error**.

## Why it matters
It's the opposite of the 2026-09-13 problem — there TurboFit had vanished entirely and his models went with it. Now the concern is **correct grouping and discoverability** once the provider is back.

## Status
Models confirmed "working through Hermes" as of **13:21** on 2026-09-15.^[raw/inbox/2026-09-15.md] Whether the grouping (all TurboFit models under the one provider) was visually confirmed by Chris is **not** — the provider never appears in the picker. As of **18:05** the dropdown shows only news portal, open code free, xai. This is the live gap: [[click-options/wiki/concepts/turbofit-provider-still-missing-2026-09-15|TurboFit Provider Still Missing from the Desktop Picker (2026-09-15)]].

## Notes
- Tied to the acceptance test: [[click-options/wiki/decisions/test-through-hermes-not-endpoint|Test Through Hermes, Not Straight to the Endpoint]].
- The picker location is the same arrow-on-desktop control from the TurboFit-provider-disappeared incident.
