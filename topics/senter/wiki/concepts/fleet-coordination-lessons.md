---
title: Fleet coordination lessons (distilled pitfalls)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [pain, spec, decision]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Fleet coordination lessons (distilled pitfalls)

The ~65 pitfalls in the [[topics/senter/wiki/entities/skill-senter-fleet-coordination|senter-fleet-coordination skill]], grouped. Each traces to a Chris correction, mostly 2026-08-30 → 2026-09-02. Items already given their own page are linked rather than repeated. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Delivery and motion
- Delivery ≠ routing; measure with `dispatch.py status`; "Is it still working?" ⇒ run `fleet-status.sh` and answer with numbers ([[topics/senter/wiki/entities/senter-dispatch-and-sentinel|dispatch + sentinel]]).
- "Actually do all of them now" ⇒ unblock → consolidate (ONE ordered work order per bot) → parallelize by ownership seam → watch by tool-event counts.
- Delivery before reflection — checklist item 0. Chris's newest items sat 12 min while Senter wrote lessons.
- "You didn't do X" for the 3rd+ time ⇒ measure the FILE at his viewport; his preview may be stale (`?v=` pinned three versions). Reload on every version bump, same turn.
- Before replying about UI work, check what already landed (session.md headings, version string, events) and say "v14.12 is in your preview, here's what changed."
- Bot turns take 30–60 s before the first tool call; approval cards appear at the GATE, not at dispatch.
- Stale background notifications drain late — match PID against what is currently live; answer in one line.

## Briefing
- Quote Chris's exact rule as the spec; a repeat report jumps the queue as item 0 and steers the running bot.
- "Match how the Hermes desktop does it" ⇒ pull the REAL inventory from source (Lucide icons, i18n strings, state swaps), never invent glyphs.
- Feel words → numeric spec (700–900 ms ease-out, direction, particle size) + a 5-frame strip.
- "Show me what we have" ⇒ gather the real inventory first (~30 platforms / 16 plugins / ~20 API skills / 0 MCP; `osascript` for the actual wallpaper file).
- Own a bug your own brief caused ("that was my miss").
- Answer architecture questions first (yes/no + the one reason + the one consequence), then route.
- Steers are additive; a cut-off sentence gets an explicit open slot.
- After a bulk change, name the adjacent scope not touched.

## Verification
- See [[topics/senter/wiki/concepts/look-loop-verification|LOOK loop]] and [[topics/senter/wiki/concepts/preview-pane-viewport|pane viewport]]. Plus: verify a teammate's "done" against disk (md5/diff); verify structural changes with the merge checklist; a `NEEDS-CHRIS` may be a test probe; a BLOCKED child may be done; an absent live indicator may be correct.
- 3+ corrections on one feature ⇒ fix the bot's VERIFICATION gap fleet-wide, not the item. 2 repeats on one element ⇒ fresh-eyes QA by anser before the owner touches it again.
- Hover-overlay hit zones shrink under repeated "don't cover X" fixes → brief a 48–64 px floor.
- "X never happens for me" ⇒ inspect the live page (handler source, keyframes) and hand ranked suspects.

## Governance
- Route the gate over Senter's own proposals (merge table → anser). Thresholds are calibrated ([[topics/senter/wiki/decisions/2026-09-02-governance-thresholds-calibrated|decision]]).
- Fleet decisions are wiki cards ([[topics/senter/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|decision]]); process docs are the product; every standing rule → owning SOUL same turn; rules name the gate's pattern family.
- Upstream PR ledger vs Chris's fork ships now ([[topics/senter/wiki/decisions/2026-09-02-upstream-pr-policy|decision]]).

## Tooling facts
`delegate_task` placeholder rejection and steer-on-finished-child; same-file parallel children inflate each other's cost; `message_agent` fallback runner; state.db reading; ISO refresh + etch (rdisk, sudo prompt times out in background); `search_files` for multi-pattern scans (long chained greps trip the hardline parser).
