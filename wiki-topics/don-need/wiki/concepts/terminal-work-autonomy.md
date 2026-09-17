---
title: Terminal-work autonomy — Chris doesn't want to run the commands
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [preference, pain, tool]
sources: ["raw/inbox/2026-09-13.md"]
confidence: high
---

# Terminal-work autonomy — Chris doesn't want to run the commands

During the 2026-09-13 session Chris drew a hard line on terminal work: when the fix needed commands on his own machines (SSH into the HP, standing up a Termux SSH server on the Surface Duo), he said "please don't ask the people [me] to do it"^[raw/inbox/2026-09-13.md] and "You don't need to set up a separate SSH for that."^[raw/inbox/2026-09-13.md] His read is that the agent should do the SSH/terminal work itself — not bounce commands back at him to run.

The context was a debugging dead-end: Hermes couldn't SSH into the HP (port 22 closed) or say what was on port 443, and the next step was to spin up a Termux SSH server on a Surface Duo 2 (port 8022). Chris's objection wasn't to the debugging — it was to being asked to be the hands for it. It's the same instinct behind [[turbofit-model-fallback|TurboFit's missing-model fallback]]: "You should be thinking of yourself" and just make it work. One-time debug/teardown in this session, not a recurring job.

Related: [[freeing-disk-space-after-migration-to-hp|freeing disk space after migrating games to the HP]] (same session). See the [[wiki-topics/don-need/index.md|don-need wiki index]] for every page.
