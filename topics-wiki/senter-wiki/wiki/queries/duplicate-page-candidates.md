---
title: Duplicate page candidates in this wiki (two compiles wrote the same subjects)
created: 2026-09-05
updated: 2026-09-05
type: query
tags: [pain, loop, question]
sources:
  - raw/inbox/2026-09-05.md
  - log.md
confidence: high
---

# Duplicate page candidates

## Why this page exists
The two `log.md` compile entries dated 2026-09-05 (the 18:14 background run ^[raw/inbox/2026-09-05.md] and a second pass over the same 44 raw items) each created pages for the same subjects under different slugs. Both sets pass the `SCHEMA.md` floor, so nothing rejects them — but the evidence for one subject is now split across two pages and `index.md` lists both. This is the concrete cost of running two compiles over one raw set; the [[topics-wiki/senter-wiki/wiki/entities/topic-wiki-compile-loop|compile loop]] needs a slug-collision check (or a lock) before it writes, and [[topics-wiki/senter-wiki/wiki/concepts/wiki-page-quality-bar|the quality bar]] should include "one page per subject".

## Candidates (measured 2026-09-05, difflib ratio of full text; line counts in parentheses)
| page A | page B | similarity |
|---|---|---|
| `entities/hud-cluster.md` (35) | `entities/hud-cluster-gear-player-rocker.md` (46) | 0.36 |
| `entities/headphone-eq.md` (29) | `entities/headphone-eq-and-media-player.md` (49) | 0.13 |
| `entities/scan-topics.md` (36) | `entities/scan-topics-scanner.md` (37) | 0.15 |
| `entities/topic-worker.md` (27) | `entities/topic-worker-and-topic-wiki-compiler.md` (31) | 0.07 |
| `entities/wallpaper-girl.md` (26) | `entities/paper-palette-and-wallpaper-girl.md` (38) | 0.23 |
| `entities/fleet-bots.md` (33) | `entities/people-and-bots-in-this-topic.md` (35) | 0.20 |
| `concepts/four-primitives-goop.md` (43) | `concepts/goop-four-primitives.md` (52) | 0.09 |
| `concepts/chris-ui-working-rules.md` (53) | `concepts/chris-ui-working-style.md` (39) | 0.17 |
| `concepts/approval-policy.md` (34) | `concepts/proposal-and-approval-policy.md` (34) | 0.09 |
| `concepts/llm-wiki-topic-layout.md` (41) | `concepts/two-layer-llm-wiki.md` (37) | 0.07 |
| `concepts/pane-driving-and-verification.md` (55) | `concepts/verification-and-proof-methods.md` (54) | 0.25 |
| `decisions/2026-09-03-editor-is-a-card-not-a-page.md` (23) | `decisions/2026-09-03-editor-is-a-hover-card.md` (23) | 0.28 |
| `decisions/2026-09-03-mvp-checkpoint-ui-good-enough.md` (21) | `decisions/2026-09-03-mvp-checkpoint-backend-phase.md` (23) | 0.40 |
| `decisions/2026-09-05-every-topic-is-an-llm-wiki.md` (26) | `decisions/2026-09-05-topics-are-llm-wikis.md` (21) | 0.31 |
| `decisions/2026-09-05-per-message-watcher-one-profile-one-card.md` (26) | `decisions/2026-09-05-every-message-one-profile-one-card.md` (22) | 0.19 |
| `decisions/2026-09-05-keep-senter-and-senter-wiki-separate.md` (26) | `decisions/keep-senter-and-senter-wiki-separate.md` (23) | 0.33 |
| `queries/open-items-as-of-2026-09-05.md` (38) | `queries/open-items-2026-09-05.md` (42) | 0.45 |

Text similarity is low because the two compiles phrased things differently — the overlap is in *subject*, not wording, which is exactly why a filename/similarity check alone will not catch it; the merge needs a bot reading both.

## Proposed handling (not done — a structure change, so it is the umbrella/paladin's call, not this compile's)
- Keep the slug the `index.md` / other pages link to most; fold the other's unique quotes and provenance into it; leave a one-line stub or delete and rebuild `index.md`.
- Never lose a `^[raw/…]` citation or a `<!-- chris -->` line in the merge.
- Merge undated `decisions/keep-senter-and-senter-wiki-separate.md` into the dated one; decisions are dated by convention.

Related: the [[topics-wiki/senter-wiki/wiki/entities/umbrella|umbrella]] already does cross-topic skill dedupe; within-topic page dedupe is the same job one level down.
