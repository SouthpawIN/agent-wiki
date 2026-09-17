---
name: recovery-repair-pattern
description: Use when fixing Hermes runtime crashes on local M1 hardware. Follow Chris's verification-first repair pattern that rebuilds from vault specs before touching files.
version: 0.1.0
distilled: 2026-09-08 09:50
topic: back-where
---
# recovery-repair-pattern
1. Stop touching files immediately after a crash or regression
2. Rebuild the target from the vault's own specs (not from partial state)
3. After any restoration, do not declare completion until the surface is checked
4. Log each compile step to log.md with the source raw items incorporated
5. Cross-link all entities and concepts to maintain wiki coherence
Verify with: 'desktop_preview open' shows reload = close all tabs, open one
Evidence: "I'm switching from 'I can't' to a concrete repair plan. I'm not touching the file again until I've rebuilt the target from the vault's own specs."

## Evidence
> I'm switching from 'I can't' to a concrete repair plan. I'm not touching the file again until I've rebuilt the target from the vault's own specs.
> The UI restoration is complete. Let me verify the final state by checking a few key elements:
