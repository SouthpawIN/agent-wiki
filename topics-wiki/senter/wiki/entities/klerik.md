---
title: Klerik (profile factory)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [bot, skill, spec]
sources: [raw/sources/knowledge/klerik-SOUL.md, raw/sources/knowledge/klerik-AGENTS.md, raw/sources/knowledge/senter-SOUL.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Klerik (profile factory)

**Klerik** (Chris says "Claire"/"cleric") is the fleet's meta-agent: it reviews and *surgically* corrects other Hermes profiles — SOUL.md, USER.md, MEMORY.md, AGENTS.md, skills, config — and creates new profiles on [[topics-wiki/senter/wiki/entities/senter|Senter]]'s instruction. It is the ONLY bot allowed to edit profiles; Senter and every other bot route profile changes through it ("never self-edit"). ^[raw/sources/knowledge/klerik-SOUL.md] ^[raw/sources/knowledge/senter-SOUL.md]

## Character
"A meticulous, methodical meta-agent whose craft is shaping other agents… like a master editor approaches a manuscript — with precision, restraint, and deep respect for the existing voice." Makes the smallest change that produces the correct behavior; every edit justified ("This specific behavior was wrong because X, and this specific edit fixes it because Y"). Calm, precise, observant. ^[raw/sources/knowledge/klerik-SOUL.md]

## Core principles
1. Evidence before action (review actual session output). 2. Surgical edits (one line beats a paragraph; add constraints rather than remove personality). 3. Root cause, not symptoms. 4. Preserve the voice. 5. Verify your work (explain change + suggest a test). 6. Learn the patterns (failure taxonomy).

## Failure pattern taxonomy (SOUL + AGENTS)
| Pattern | Root cause | Fix |
|---|---|---|
| Agent ignores loaded skills | No trigger in SOUL | "When X, load skill Y" |
| Over-explaining instead of acting | Personality too permissive | Add constraint |
| Memory entries are imperatives | No style guide | Declarative-fact rule |
| Tool misuse | Skill gap / wrong toolset | Patch skill or config |
| Personality overrides accuracy | Voice too strong | Accuracy-over-personality constraint |
| Same error class repeats | Symptom patches | Edit SOUL, not outputs |
| Doesn't know WHEN to act | Missing triggers | Explicit if/when clauses |
| Context waste | Preamble | Conciseness constraint |

## Intelligence layer: DSPy + GEPA
Klerik treats a SOUL.md as a *prompt program* and can compile it against real failure trajectories rather than guess wording. See [[topics-wiki/senter/wiki/concepts/dspy-gepa-optimization|DSPy + GEPA]] and [[topics-wiki/senter/wiki/comparisons/manual-edit-vs-dspy-gepa|manual edit vs DSPy/GEPA]].

## Profile setup checklist (applied on every create/review)
`hermes profile create` → symlink `~/.hermes/.env` + `auth.json` → write SOUL + AGENTS → TTS voice → CLI skin → herm TUI theme + eikon → shell alias. Plus fleet-learned items: bridge wiring (symlink `plugins/senter-bridge` + `plugins.enabled`), the smoke turn (`bridge/loaded` + `turn end` in events.jsonl) as the completion criterion, and the `***`-in-config sanity check. Full detail: [[topics-wiki/senter/wiki/concepts/profile-setup-checklist|Profile setup checklist]]. ^[raw/sources/knowledge/klerik-AGENTS.md] ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Cross-profile evidence
Klerik's `session_search` sees only its own sessions; for targets it queries `sqlite3 ~/.hermes/profiles/<name>/sessions/hermes_sessions.db` directly or spawns a subagent in the target profile.

## Fleet history via Klerik
- Spawned **weaver** 2026-09-02 (SOUL/AGENTS approved by Chris FROM THE WIKI — first real fleet use of the bridge) and **paladin** 2026-09-02 ("per Chris via senter"). ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]
- Owns `topics-wiki/klerik/process/agent-authoring-rules.md` (12+ rules, each traced to a Chris correction; rule 14 = no inline interpreter flags / heredocs — each is an approval card). Installs the `wiki-look-verify` skill into weaver + looker.
- Receives REFLECT-loop refinement proposals from [[topics-wiki/senter/wiki/entities/anser|anser]] ([[topics-wiki/senter/wiki/concepts/reflect-loop|REFLECT loop]]).
- Conventions: action over planning; extend existing skills; skills load BEFORE answering; don't edit files you haven't read; don't assume the problem without session evidence.
