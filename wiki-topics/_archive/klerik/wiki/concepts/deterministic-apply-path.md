---
title: Deterministic apply path (bridge writes SOUL/AGENTS from the approved spec; klerik finishes setup)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [infra, bot, plan, decision, spec]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# Deterministic apply path

**Definition.** The second-generation bot-card apply wire, introduced 2026-09-05 after the first klerik spawn stalled on the [[wiki-topics/klerik/wiki/concepts/protected-file-guard|protected-file guard]]. Instead of asking klerik (an LLM, headless) to author the two protected files, the senter-bridge writes them *deterministically* — template + the text Chris approved on the card — and only then hands klerik the remaining, unprotected checklist steps. The 18:42 note names it: "Re-run the approval through the new deterministic path." ^[raw/inbox/2026-09-05.md]

**The steps, as implemented in `~/.hermes/plugins/senter-bridge/server.py` (`_apply_approved`, kind == "agents").**
1. Card has `reuse: <bot>` → no new profile; card gets `## Applied … Reuses profile` and the fleet bot serves the topic. (Fleet reuse is the default; see the redundancy gate in [[wiki-topics/klerik/wiki/entities/klerik|klerik]].)
2. Otherwise `hermes profile create <name>` if the dir is missing.
3. SOUL.md = `## SOUL.md (draft)` section of the card + a fixed **Voice** block ("Chris dictates by voice; stray audio arrives garbled — never ask him to repeat. Root causes, never band-aids. Report what changed, what is verified, what is left.").
4. AGENTS.md = role paragraph, "Read first (progressive disclosure): wiki-topics/<t>/index.md → one page → one section", the card's `## First task`, the skills carried, and two rules (work only inside the topic; proposals for other topics are cards).
5. Copy `wiki-topics/<t>/skills-capabilities/*` into the profile's `skills-capabilities/`; re-symlink `.env` and `auth.json`.
6. Run klerik with a *narrow* prompt: voice + skin per archetype, `herm/tui.json`, `hermes profile alias`, `hermes profile describe --auto`, then **read** SOUL/AGENTS and report (not edit) gaps one line each. 15 turns, 600 s.
7. Append `## Applied` with klerik's last line; card → done if SOUL.md exists, else blocked; fleet `changed` event.

**What changed versus the first attempt.** First run: one 30-turn prompt to klerik that included "write SOUL.md from the spec's SOUL draft … write AGENTS.md with its role" (`/tmp/apply-senter-wiki-bot-1788650447.md`, 18:20). Deterministic run: klerik never touches a protected file. Side-by-side in [[wiki-topics/klerik/wiki/comparisons/klerik-authored-vs-bridge-authored-profile|klerik-authored vs bridge-authored profile]].

**Where klerik still adds value.** Voice/skin/theme judgement per archetype, alias, auto-describe, and the *gap report* — klerik becomes the reviewer of a profile it did not author, which is closer to its original SOUL ("review the behavior of other Hermes agent profiles … surgically correct") than being a file-writer.

**18:47 — the path itself is gated.** Running the re-run from a CLI session trips that session's security gate: "it sees a rename + a POST that writes SOUL files as a protected-file write" ^[raw/inbox/2026-09-05.md]. So deterministic ≠ unattended: the write still needs one human nod in whichever session triggers it. The bridge running under launchd (approve from the wiki feed) may not have such a gate — untested. See [[wiki-topics/klerik/wiki/concepts/approval-security-gate|Approval security gate]].

**Weak spots noted at compile time (not yet raised as cards).**
- The `## Applied` stamp and the "created" card fire on `SOUL.md exists` — which is true even for the half-made default SOUL. Proof should be *SOUL.md differs from the stock default* and a `-q` smoke emitting `bridge/loaded` (klerik rule 1; [[wiki-topics/klerik/wiki/concepts/proposal-apply-path|Proposal apply path]] proof table). Same class of bug as `klerik-queue-drain` being LIVE with zero cron jobs.
- All bridge cards attribute as `bot: senter`, so a klerik step failing shows up in the feed as senter's failure.
- Nothing in the path writes `.system/session.md` in the topic or the fleet roster — klerik's checklist steps 7–8 are dropped.
