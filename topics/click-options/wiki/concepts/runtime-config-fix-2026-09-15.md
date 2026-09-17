---
title: Runtime Config Fix — wayvnc + Provider Endpoints
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [infra, tool, pain, plan, idea]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# Runtime Config Fix — wayvnc + Provider Endpoints

## What was filed
Two `hermes` working entries on **2026-09-15** documenting runtime/config problems Chris was stepping through:

### wayvnc timeout → persistent service
- **09:40** — **wayvnc shut down after the 5-second timeout.** The fix underway was to **set up the persistent systemd service properly and test again.**^[raw/inbox/2026-09-15.md]
- Reads as a remote-desktop (wayvnc) service that was dying on a short timeout; the standing fix is a systemd unit that keeps it alive, re-tested after.

### Hermes hitting `https://` on plain-HTTP endpoints
- **11:19** — **Hermes was trying `https://` on plain HTTP endpoints.** The fix was to **correct the provider config and test both models.**^[raw/inbox/2026-09-15.md]
- The provider config had a scheme mismatch (https vs http); both models were re-tested after the correction.

## Status
Both recorded as `hermes` working logs in progress on 2026-09-15. Outcome (did the systemd service hold? did both models pass after the scheme fix?) not yet captured in `raw/`. Related infra friction: [[click-options/wiki/concepts/turbofit-provider-disappeared|TurboFit Provider Disappeared]] (the provider vanishing from the picker the prior day).
- **2026-09-15 13:21:** both models confirmed working through the Hermes backend. But the desktop picker still does not show TurboFit (16:34–18:05) — so the config fixes were necessary, not sufficient. The remaining gap is a picker-registration problem, not the scheme fix: [[click-options/wiki/concepts/turbofit-provider-still-missing-2026-09-15|TurboFit Provider Still Missing from the Desktop Picker (2026-09-15)]].

## Notes
- These are runtime/config items that touch **what you click to pick a provider/model** — same topic family as the TurboFit provider disappearing — but the root cause this day was config (scheme + service lifetime), not the picker itself. For the tab-bar discoverability issue, see [[click-options/wiki/concepts/tab-opening-quick-fixes|Tab Opening Quick Fixes]].
