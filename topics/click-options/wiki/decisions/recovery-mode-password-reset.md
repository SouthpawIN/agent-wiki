---
title: Recovery Mode Password Reset
created: 2026-09-14
updated: 2026-09-14
type: decision
tags: [decision, plan, tool, pain, timeline]
sources: [raw/inbox/2026-09-13.md]
confidence: high
---

# Recovery Mode Password Reset

## The procedure
Chris worked through a macOS **Recovery Mode** password reset. The steps he was following (and instructing/confirming):

1. Shut down — Apple Menu → Shut Down
2. Hold the power button (don't let go) until **"Loading startup options"** appears
3. Click **Options** → **Continue**
4. At the top menu bar: **Utilities → Terminal**
5. Type `resetpassword` and press Return

^[raw/inbox/2026-09-13.md]

## Outcome
The earlier non-recovery attempts **"None of them worked"** — so Chris escalated to Recovery Mode as the next step.^[raw/inbox/2026-09-13.md] He asked to "Run that and tell me which one (if any) prints **'WORKED.'**" — indicating the reset command was expected to report success.^[raw/inbox/2026-09-13.md]

## Notes
- The trigger point that gave this topic its name: the **Options → Continue** button in the macOS "Loading startup options" dialog.
- Procedure still in progress as of filing (2026-09-13 16:43); whether `resetpassword` printed WORKED was still pending.
- Related: [[click-options/wiki/concepts/turbofit-provider-disappeared|TurboFit Provider Disappeared]] (same session, a second issue surfaced).
