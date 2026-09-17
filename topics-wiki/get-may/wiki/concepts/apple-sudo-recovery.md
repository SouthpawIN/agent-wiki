---
title: Apple sudo recovery
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [plan, infra, preference]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-13.md]
confidence: medium
---
The established recovery path for Chris's forgotten sudo password is Apple Silicon Recovery Mode: shut down, hold the power button until "Loading startup options" appears, open Terminal from Utilities, run `resetpassword`, select the user account, and set a new password.^[raw/inbox/2026-09-13.md] Hermes warned that if FileVault is enabled, the recovery key or Apple ID may be required before Terminal is reachable.^[raw/inbox/2026-09-13.md] Chris has not yet confirmed whether FileVault is on.^[raw/inbox/2026-09-13.md]

A secondary preference surfaced in the 2026-09-12 thread: set up passwordless sudo after recovery so future privileged commands do not prompt interactively.^[raw/inbox/2026-09-12.md]

Related: [[wiki/entities/macbook-sudo-password|macOS sudo password]], [[wiki/decisions/use-balena-etcher-over-sudo-dd|use Balena Etcher over sudo dd]]
