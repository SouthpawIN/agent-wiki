---
name: wiki-feed-verify
description: Use when checking that fleet posts reach the sidebar feed. Cross-check bridge `/post` arrivals against the events log and DOM, then report counts.
version: 0.1.0
distilled: 2026-09-05 17:36
topic: senter-wiki
---
# wiki-feed-verify
# wiki-feed-verify

Verify the sidebar feed is actually receiving fleet traffic — never assume from code that a post landed.

## Steps
1. Identify the producers: watcher, topic-worker, umbrella, wiki stage events, GitHub feed items. All go through the bridge `/post` endpoint (senter-bridge, :8643).
2. Read the bridge events log for the last window and count posts per source (e.g. `senter` posts vs `stage` events vs GitHub).
3. Read the feed from the DOM of Chris's real window (AX tree / DOM, not a screenshot guess) and count rendered feed rows for the same window.
4. Compare: every logged post must have a rendered row. Report counts per source (e.g. "43 senter posts, 17 stage events").
5. Confirm liveness: send one message or trigger one stage event and watch the row appear without reload.

## Rules
- Evidence = events-log counts + DOM rows, side by side. A claim without both is not verified.
- Clicking the feed must never cancel the wiki's performance or close a card — if it does, that is a layering regression (see wiki-hit-zone-layering), file it, do not paper over it.
- If a producer is missing from the feed, fix the producer's `/post` call (root cause), not the renderer.

## Pitfalls
- Anser summaries of the log are unreliable; count from raw rows.
- Stage events and fleet posts share the feed; keep counts separate so a busy stage does not mask a silent watcher.

## Evidence
> Now the feed. Check what actually lands in the sidebar feed from the fleet — the watcher/worker posts go through `/post`, so they should be there. Verify against the events log
> Feed. Watcher, worker, umbrella, stage events all reach it: last window showed 43 senter posts, 17 stage events, plus GitHub feed items. It updates as you talk.
