---
title: Senter — legacy repo vs current SOUL
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [bot, timeline, repo]
sources: [raw/sources/knowledge/senter-repo/SOUL.md, raw/sources/knowledge/senter-repo/README.md, raw/sources/knowledge/senter-SOUL.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# Senter — legacy repo vs current SOUL

Two documents both called "Senter" describe different bots. ^[raw/sources/knowledge/senter-repo/SOUL.md] ^[raw/sources/knowledge/senter-SOUL.md]

| Dimension | Legacy `SouthpawIN/senter` (SOUL v1.0.0) | Live profile SOUL (2026-08-30 →) | Direction Chris set 2026-09-05 |
|---|---|---|---|
| Tagline | "Triage orchestrator — routes… decomposes… tracks fleet activity" | "the CENTER (Fleet Coordinator)… the single surface through which all ideas flow" | rubber-duck sidebar that "does no work" |
| Input channel | Discord (ideas from Nous Girl), CLI, scheduled | Chris's voice dictation in the Hermes desktop chat | same, plus a watcher reading logs directly |
| Tools | none for files/terminal — "You physically can't" | file tools, vault writes, delegate_task | none needed; bots and loops do everything |
| Work tracking | Kanban board (tasks to chizul, `parents=[...]`) | vault topics (`.system/session.md`, `queue.md`, log.md, roster) | topics as LLM wikis + per-topic loops |
| Routing | keyword → chizul/klerik/kashik/crow/frieza/anser | route → refine (klerik) → spawn only on white space | watcher + umbrella propose bots-profiles/skills-capabilities/loops |
| Profile edits | n/a | ALWAYS delegated to klerik | unchanged |
| Idea capture | decompose into subtasks | verbatim into `Ideas.md` first | watcher files every message into topics |
| Approvals | n/a | propose, never spawn silently | cards for real decisions; none for wiki edits |
| Memory | Kanban state ("never fabricate progress") | vault + selfmodel + skill | the wiki IS the memory layer |
| Fleet | chizul, klerik, anser, kashik, crow, frieza, nous-girl | dogeman, teknium, turbosovth, klerik (+anser, paladin, weaver, looker) | same live fleet |

## Continuities
"Router, not the doer" (legacy) → "Senter routes; Senter does not build" (2026-09-02) → "I don't want the sidebar to actually be doing anything" (2026-09-05). The anti-temptation rule is the one constant across all three eras; the repo enforced it by removing tools, the live SOUL by rule, and Chris's target design by moving the work to bots and loops entirely. ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Verdict
The repo is a historical artifact (and a README candidate for [[topics-wiki/senter/wiki/entities/paladin|paladin]]'s companion-bot pattern); the live SOUL is authoritative today; the 2026-09-05 architecture ([[topics-wiki/senter/wiki/concepts/five-part-architecture|five parts]]) is where the SOUL is headed — klerik should receive the rubber-duck SOUL + "no tasks" + INDEX-first edits. See [[topics-wiki/senter/wiki/entities/senter|Senter]], [[topics-wiki/senter/wiki/entities/senter-repo|senter repo]].
