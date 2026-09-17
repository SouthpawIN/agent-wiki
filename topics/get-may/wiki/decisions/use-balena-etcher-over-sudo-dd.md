---
title: Use Balena Etcher instead of sudo dd
created: 2026-09-12
updated: 2026-09-13
type: decision
tags: [decision, preference]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-13.md]
confidence: high
---
What: Flash the Omarchy 4.0.3 ISO with Balena Etcher rather than `sudo dd` from terminal.

Why: `sudo dd` requires an interactive password in a terminal, which Hermes could not supply in background/non-TTY contexts, causing repeated failures.^[raw/inbox/2026-09-12.md] Chris grew frustrated with password guessing and said, "well then ask me for the sudo password dipshit."^[raw/inbox/2026-09-12.md] Etcher avoids that prompt by using its own privileged helper.

When: 2026-09-12 onward.

Evidence: Balina etcher download succeeded at 159MB; Chris later confirmed "use blina etcher" and that the HP was flashed and on Tailscale.^[raw/inbox/2026-09-12.md]^[raw/inbox/2026-09-13.md]

Related: [[wiki/entities/balena-etcher|Balena Etcher]], [[wiki/concepts/apple-sudo-recovery|Apple sudo recovery]]
