---
name: bot-card-approval-spawn
description: "Use when a bot card is approved in the Senter wiki. Turn the approval into a running Hermes profile — never a rename."
version: 0.3.0
distilled: 2026-09-05 18:01
updated: 2026-09-05 (authoring-rule 16 sync: headless = bridge writes SOUL/AGENTS)
topic: klerik
---
# bot-card-approval-spawn

Turn an approved bot card into a running Hermes profile. A bot is spawned when it RUNS, not when its files exist.

## Inputs
From the card: name, role, closest bot + why not enough. Missing either → NEEDS-CHRIS card, stop.

## Steps
1. **Redundancy check**: profile list + `topics/` + Ideas.md. Overlap → propose refine/reuse instead; stop. (Bridge honors `reuse: <bot>` on the card — prefer that over a new profile.)
2. **SOUL/AGENTS — who writes them depends on the session, per authoring rule 16**:
   - **Headless (cron/oneshot): DO NOT write them.** The protected-file guard blocks a headless bot from writing another profile's SOUL/AGENTS (2026-09-05: senter-wiki-bot stalled half-made with default SOUL, no AGENTS). The senter-bridge's `_apply_approved` (server.py, kind=="agents") writes both deterministically from the card spec, creates the profile, copies `topics/<t>/skills/*`, and symlinks `.env`/`auth.json`. Klerik's job in this mode is the narrow finisher: voice/skin/tui per archetype, `herm/tui.json`, alias, `describe --auto`, then READ SOUL/AGENTS and report gaps one line each — never edit them headless.
   - **Session with a human present**: you may write them yourself — one batched `write_file` per file (rule 14: file tools only, never heredoc/inline-exec).
3. Voice/skin/tui per the archetype tables in AGENTS.md.
4. Alias + bridge symlink (`plugins/senter-bridge`) + `senter-bridge` in `plugins.enabled`.
5. Smoke: `hermes -p <name> -q "…" ` must emit `bridge/loaded`, else BLOCKED.
6. session.md + fleet roster + topic log.md, same turn.
7. Only then flip the card to running and POST DONE with before→after→proof.

## Proof of spawn (rule 1 + deterministic-path weak spot)
`SOUL.md exists` is NOT proof — the half-made default SOUL also exists. Real proof:
- `SOUL.md` differs from the stock default (diff against the bridge template or `SOUL.md.orig`)
- AGENTS.md exists and names the topic
- `-q` smoke turn emits `bridge/loaded`
- `hermes profile list` shows the bot with the intended model tier

## Pitfalls
- paladin was "spawned" twice before it existed — half-built dirs happen; inventory, don't assume (see `half-made-profile-check`).
- File tools only (rule 14); on-disk ≠ connected (rule 8); gate timeout = BLOCKED, never route around (rule 7).
- The bridge's "created" card fires on `SOUL.md exists` — apply the stricter proof above and report the gap if it doesn't hold.

## Evidence
> Approving a bot card still just renames the file; the actual `hermes profile create` via klerik is the next wire.
> A bot is spawned when it runs, not when its files exist. Definition of done: SOUL + AGENTS + model + bridge symlink + plugins.enabled + credentials on disk, AND a -q smoke turn emits bridge/loaded.
> Klerik's run ended with the profile half-made (default SOUL, no AGENTS) — the protected-file guard blocked it, as I suspected. Re-run the approval through the new deterministic path:
