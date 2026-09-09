---
title: Decision — re-run the senter-wiki-bot approval through the new deterministic path (2026-09-05 18:42)
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, bot, infra, plan]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# Decision — re-run the approval through the deterministic path

**What.** At 18:42 on 2026-09-05, after klerik's first bot build ended "half-made (default SOUL, no AGENTS)", the session decided not to patch the half-made profile by hand and not to re-run klerik as-is, but to "Re-run the approval through the new deterministic path" ^[raw/inbox/2026-09-05.md] — i.e. re-fire the *approval* itself so the bridge's new `_apply_approved` code writes SOUL/AGENTS from the card and klerik does only the unprotected finish. Path described in [[topics/klerik/wiki/concepts/deterministic-apply-path|Deterministic apply path]].

**Why.** The failure was structural — the [[topics/klerik/wiki/concepts/protected-file-guard|protected-file guard]] cannot be satisfied by a headless bot — and "as I suspected" says it was anticipated. Re-running the same thing would fail the same way; hand-editing the profile would be a workaround Chris has forbidden (no workarounds / temp fixes; root causes, never band-aids). Re-running the approval exercises the real production path end to end, which is also the standing instruction from 18:18: "prove the apply path with one real approval" ([[topics/klerik/wiki/decisions/2026-09-05-prove-apply-path-with-one-real-approval|Prove the apply path]]).

**Consequences for klerik.**
- klerik's lane on *new* profiles shrinks to: voice, skin, `herm/tui.json`, alias, `describe --auto`, and a read-only gap report. Its authoring rules (`process/agent-authoring-rules.md`) and the skill `skills/bot-card-approval-spawn` still describe klerik writing SOUL/AGENTS itself (step 3) — **stale**, needs updating to "bridge writes; klerik verifies".
- The handoff file klerik produced (`topics/senter-wiki/agents/senter-wiki-bot-applied-edits.md`) is richer than the bridge template (fleet table, first-move rules). If the deterministic re-run overwrites SOUL.md with the shorter template, that richer content is orphaned — a small follow-up for the senter-wiki topic.

**Open tension (question for Chris).** The bridge now writes an `AGENTS.md` for every new bot. At 18:31 Chris said to leave AGENTS.md alone ([[topics/klerik/wiki/decisions/2026-09-05-leave-agents-md-alone|Leave AGENTS.md alone]]); the *which* was ambiguous. Reading it as "don't rewrite existing AGENTS.md files" is compatible with the bridge creating a fresh one; reading it as "no AGENTS.md changes at all" is not. Flagged `contested` on that page; not blocking the re-run.

**Proof this decision is done.** Not the `## Applied` stamp — SOUL.md content ≠ the 667-byte stock default, AGENTS.md exists, and `hermes -p senter-wiki-bot -q` emits `bridge/loaded`. Tracked in [[topics/klerik/wiki/queries/did-the-deterministic-rerun-complete|Did the deterministic re-run complete?]].

**Evidence.**
> Klerik's run ended with the profile half-made (default SOUL, no AGENTS) — the protected-file guard blocked it, as I suspected. Re-run the approval through the new deterministic path: ^[raw/inbox/2026-09-05.md]
