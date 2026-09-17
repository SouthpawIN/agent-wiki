---
name: wiki-event-performance
description: Use when wiring fleet activity into the Senter wiki UI. Emit `wiki` events from real actions so rows open/scroll/edit/close live; never animate from fake or polled state.
version: 0.1.0
distilled: 2026-09-05 17:22
topic: senter-wiki
---
# wiki-event-performance
# wiki-event-performance

The wiki must *perform* the fleet's activity, not merely re-render after it. Every real action stages a `wiki` event; the UI consumes them as a choreography (open → scroll → edit → close).

## Steps
1. Emit only from real side effects: watcher filing, worker edit/proposal write, new-subject scaffold + research dispatch, bridge approve/reject. One event per real action; no batching that hides tempo.
2. Event shape: `{kind:'wiki', op:'open'|'scroll'|'edit'|'close', target:<row id / file path>, ts}`. The `target` must resolve to a row that exists in the SKILLS/BOTS/LOOPS/topics tables.
3. UI consumer: on `open` expand the row; `scroll` bring it into view; `edit` flash the changed cell/text (paper white, no gray, no gradients); `close` collapse after the edit settles. Attention colour #FFE45A only for approvals awaiting Chris.
4. Approvals: only BOT and LOOP proposals raise an approval card; skills and wiki edits auto-apply and just perform an `edit` event.
5. New subject: scaffold the topic and dispatch an existing bot to research immediately; emit `open` on the new topic row so Chris sees it born.

## Rules
- Root-cause only: if a row does not move, fix the emitter or the row id resolution — never add a timer-driven fake animation.
- Verify in Chris's real window (wiki-look-verify) that an emitted event visibly moved the row; a log line is not proof.
- Design law applies to every transient state (pure #000 / --paper, hollow ring = active, no translucency).

## Pitfalls
- `drive_preview` strips URL query/hash — don't pass event replay via URL.
- Events referencing a `.proposed` path must re-target after approve renames the file (suffix dropped).
- Don't double-emit when the worker both writes a skill and updates continuity — one edit event per artifact.

## Evidence
> the UI *performs* the fleet's activity — rows open, scroll, edit, close as events arrive.
> a `wiki` event kind that makes rows open/scroll/edit/close as the fleet works, wired to real events
> the watcher stages every filing, the worker stages every edit/proposal, and the new-subject path dispatches a bot to research/scaffold immediately.
