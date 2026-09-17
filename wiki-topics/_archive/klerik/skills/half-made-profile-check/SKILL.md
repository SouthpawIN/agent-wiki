---
name: half-made-profile-check
description: Use when a bot build/spawn is reported done or 'in progress'. Verify the protected files really changed before believing the card.
version: 0.1.0
distilled: 2026-09-05 18:47
topic: klerik
---
# half-made-profile-check
1) stat SOUL.md — 667 bytes / starts 'You are Hermes Agent, built by Nous Research' = stock default = not written. 2) AGENTS.md missing = not written. 3) SOUL mtime older than config.yaml/skills mtime = guard fired. 4) ls /tmp/apply-<name>-*.md — a second file starting 'Finish setup of the Hermes profile' = deterministic re-run fired. 5) only after 1–2 pass: `hermes -p <name> -q` must emit bridge/loaded. Rules: 'writing the SOUL now' is a guess unless mtime moved; half-made → re-fire the approval (bridge writes SOUL/AGENTS), never hand-edit or re-run the same klerik prompt; never route around the guard — write a handoff file and say BLOCKED; card flips from proof, not from apply. Written to wiki-topics/klerik/skills-capabilities/half-made-profile-check/SKILL.md; bot-card-approval-spawn step 3 patched to v0.2.0.

## Evidence
> Klerik is writing the SOUL now. Meanwhile, record and close out the session's canvas files, which have been stale:
> Klerik's run ended with the profile half-made (default SOUL, no AGENTS) — the protected-file guard blocked it, as I suspected. Re-run the approval through the new deterministic path:
