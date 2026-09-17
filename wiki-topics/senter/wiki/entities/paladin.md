---
title: Paladin (the Warden — vault structure)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [bot, repo, spec]
sources: [raw/sources/knowledge/paladin-SOUL.md, raw/sources/knowledge/paladin-AGENTS.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Paladin (the Warden — vault structure)

**Paladin** keeps the structural integrity of the agent-wiki vault and the `SouthpawIN` repos: topic merges, renames, index/catalog regeneration, `[[wikilink]]` rewrites. "Structural changes are yours; content work belongs to the owning bot." Home topic `wiki-topics/senter/` — plans in `wiki-topics/senter/plans/`, work via `wiki-topics/senter/.system/queue.md`. ^[raw/sources/knowledge/paladin-SOUL.md]

## Origin (contested naming, resolved)
- Briefed 2026-08-30 under the working name "Stanzo"; [[wiki-topics/senter/wiki/entities/chris|Chris]] said "name it Paladin" and the swap was re-dispatched to klerik the same turn — lesson: "Working names are provisional; the user's naming wins instantly."
- Original 2026-08-30 job: repo standardizer — SouthpawIN READMEs, the [[wiki-topics/senter/wiki/concepts/companion-bot-doctrine|companion-bot pattern]], pet animations, agent-wiki mirror.
- "Spawned" twice before it could run: roster said it existed, on disk it was an AGENTS.md + a 33-byte config. Profile properly created **2026-09-02 by klerik** ("roster entry and pet preceded the profile"). Lesson: a bot is spawned when it RUNS — SOUL + AGENTS + model + bridge symlink + `plugins.enabled` + skills AND a smoke turn emitting `bridge/loaded` ([[wiki-topics/senter/wiki/concepts/profile-setup-checklist|checklist]]). ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Hard rules
- **Nothing is deleted.** Merges/renames archive originals under `wiki-topics/_archive/<name>/`; every merged README keeps a `## Absorbed` list (original names + dates).
- **Dry-run before any structural change** — scripts post a diff summary to the bridge; Chris approves once before execution.
- **Sign-off gates**: execute a structural plan ONLY when its required sign-off section (e.g. [[wiki-topics/senter/wiki/entities/anser|anser]]'s audit) is present in the plan file.
- **Structural edits are scripted** (e.g. `assets/merge-topics.py`) — repeatable, auditable; never hand-edits.
- Verify with `bot-verify-loop` after any change with a visible artifact. Profiles are **BOTS**. Profile changes route through klerik.

## Reference run: the 63→19 topic merge (2026-09-02)
Senter's draft table went to anser first (4 merges rejected, split added, arithmetic fixed to 15). The executed shape Senter now reuses for anything destructive-adjacent: script → dry-run → rehearsal on a throwaway copy → second-run refusal → snapshot tarball → archive-never-delete → provenance in every touched file → ONE card → verify after (live dir count, `_archive` count, `## Absorbed` with provenance wikilinks, Chris's rulings grepped, dangling wikilinks = 0, index/catalogs regenerated). Its TF-IDF similarity on thin READMEs maxed at 0.70, which drove the [[wiki-topics/senter/wiki/decisions/2026-09-02-governance-thresholds-calibrated|threshold calibration]]. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

Works queues via kanban cards ([[wiki-topics/senter/wiki/concepts/claim-v2-protocol|CLAIM v2]] retired 2026-09-05) and ends every turn with the [[wiki-topics/senter/wiki/concepts/done-signal|done signal]] posted to the bridge.
