---
title: Proposal apply path (proposed → approved → applied, per artifact type)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [infra, spec, bot, loop, skill, pain]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Proposal apply path

**Definition.** The apply path is what happens *after* a proposal in a topic is approved. The 2026-09-05 18:18 note treats it as a thing to be proven, not assumed: "approve the ones that are clearly what Chris described, and prove the apply path with one real approval." ^[raw/inbox/2026-09-05.md] The bot-card case ([[wiki-topics/klerik/wiki/concepts/bot-card-approval-wire|Bot-card approval wire]]) is one branch of it; this page is the whole tree.

**Four artifact types, four apply actions** (as laid out by klerik's topic files — `.system/queue.md` sections [SKILLS] / [AGENTS] / [LOOPS] / [CONTEXT], and the `*.md.proposed` convention):

| Proposal type | File while pending | Apply action | Proof it applied |
|---|---|---|---|
| skill | `skills-capabilities/<name>/SKILL.md` (auto-applied, no card) | write the SKILL.md | file exists AND a bot loads it |
| bot / agent | `agents/<name>.md.proposed` | klerik runs the spawn checklist → `hermes profile create` | `hermes -p <name> -q` emits `bridge/loaded` (rule 1) |
| loop | `triggers-loops/<name>.md` with a cadence | `hermes -p <owner> cron create "<cadence>" --name <name>` | `hermes -p <owner> cron list` shows the job; first tick logs |
| research / query | `wiki/queries/<slug>.md.proposed` | looker runs the question; answer lands on the page | the query page has a dated answer, `.proposed` gone |

**State on 2026-09-05 (observed at compile time).**
- skill: `bot-card-approval-spawn` written 18:01, marked "auto-applied" in the queue — the only branch that completed.
- bot: the queue lists an `agents/klerik.md.proposed` SUGGESTED at 18:01, but no such file exists in `agents/` (only `.gitkeep`). The suggestion was recorded and its artifact never materialised.
- loop: `klerik-queue-drain` approved and applied 18:18 → `cron create` **FAILED**; zero cron jobs exist for the klerik profile; file still says `status: LIVE`. See [[wiki-topics/klerik/wiki/entities/klerik-queue-drain-loop|klerik-queue-drain loop]].
- research: `wiki/queries/planner-runs-against-vault.md.proposed` (18:01) still pending — "Approve to run the research; the answer lands here."

**The pattern that keeps recurring.** Every branch except the trivial one (write a file) ends in a status flag that is set before the thing it describes is true: a card renamed but no profile ([[wiki-topics/klerik/wiki/comparisons/rename-vs-real-spawn|Rename vs real spawn]]), a loop marked LIVE with no cron job. klerik's authoring rule 8 already says it — "'on disk' ≠ 'connected'" — and the 18:18 instruction to *prove* the path is the same rule applied to the pipeline itself. The fix is structural: the status flag must be written by the verification step, never by the apply step. That is what the `proposal-apply-proof` skill (wiki-topics/klerik/skills-capabilities/) encodes.

**Owners.** klerik applies bot and loop proposals (profile and cron work is klerik's); looker runs research proposals and is the natural verifier of "did it actually apply"; weaver owns the card UI that emits approvals; senter tracks. Open question tracked in [[wiki-topics/klerik/wiki/queries/has-the-apply-path-been-proven|Has the apply path been proven?]].
