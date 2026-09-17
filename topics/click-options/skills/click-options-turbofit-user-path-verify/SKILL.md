---
name: click-options-turbofit-user-path-verify
description: Verify TurboFit provider/model changes in Hermes.
version: 0.1.0
distilled: 2026-09-17 03:37
topic: click-options
---
# click-options-turbofit-user-path-verify
## The recurring failure
TurboFit works at the backend but never persists into the Hermes desktop provider/model picker (arrow-on-desktop next to the input bar). Confirmed working through the runtime on 2026-09-15 13:21, yet the picker on 09-15 18:05 showed only news portal / open code free / xai. Same gap recurred 09-13 (provider vanished) and 09-16 (roster came back incomplete). The root cause is picker-registration, not model loading.

## Procedure: verify a TurboFit change the way Chris will use it
1. Never test against the raw endpoint — it can pass while Hermes errors. The real test is the user path.
2. Open Hermes as a user. Expand the provider/model dropdown (arrow on the desktop next to the input bar).
3. Confirm the TurboFit provider is present and selectable in the list.
4. Confirm every TurboFit model is nested under the TurboFit provider — not scattered across providers.
5. Confirm Tailscale models are detected and shown, and local models are listed.
6. Select and test each model from Chris's roster inside Hermes. Zero errors is the pass condition.
7. If the provider is missing from the picker, it is a registration gap (what the picker reads to enumerate providers), not a model-loading failure — fix that layer, not the config.

## Pitfalls
- "Working through the Hermes runtime" does NOT mean "present in the picker." They are different layers. A backend pass is necessary, not sufficient.
- The picker dropdown is the same arrow-on-desktop control from the 09-13 disappearance incident — a regression here is a recurrence, not a new bug.
- Chris's acceptance gate is the user path, not the endpoint.

## Evidence
> "so I don't get an error when I go to test it in Hermes. Not just straight to the end point, I mean through Hermes, like, open up a terminal background and try to do it as a user."
> "I want all my turbo fit models to be under my turbo fit provider."
> "I still don't see it when I click the drop down menu from the input bar I only see news portal followed by open code free followed by xai."

## Evidence
> "so I don't get an error when I go to test it in Hermes. Not just straight to the end point, I mean through Hermes, like, open up a terminal background and try to do it as a user."
> "I want all my turbo fit models to be under my turbo fit provider."
