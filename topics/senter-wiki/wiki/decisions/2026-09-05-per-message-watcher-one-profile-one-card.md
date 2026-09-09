---
title: Decision 2026-09-05: per-message watcher, one senter profile, one card per proposal
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, loop, timeline, infra]
sources:
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/inbox/2026-09-05.md
confidence: high
aliases:
  - "Decision: every message · one senter profile · one card per proposal"
---

# Decision 2026-09-05: per-message watcher, one senter profile, one card per proposal

## What
"Per message, live, visible. That settles the three questions: **every message**, **one senter profile running the loops** (per-topic profiles come later, when a topic earns a bot), **one card per proposal** so the feed moves constantly." (16:35) Chris's phrase: "per message, like Cursor". ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]

## Why
Chris wants to watch the system work as he talks; batching hides motion. One profile keeps cost and complexity down until a topic earns its own bot (the [[topics/senter-wiki/wiki/entities/umbrella|umbrella]] proposes promotions). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Consequences
- The [[topics/senter-wiki/wiki/entities/senter-watcher|watcher]] was built first "since it's the piece that makes everything move". ^[raw/inbox/2026-09-05-legacy-inbox.md]
- `hermes -p senter` is the runner for [[topics/senter-wiki/wiki/entities/topic-worker|topic-worker]] and the [[topics/senter-wiki/wiki/entities/topic-wiki-compile-loop|compile loop]]. ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]
- Cards: one per pitch, APPROVE/REJECT ([[topics/senter-wiki/wiki/concepts/approval-policy|approval policy]]). ^[raw/inbox/2026-09-05.md]
- Sequence: after the watcher, topic-worker → umbrella → approvals followed the same afternoon. ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]

Status: in force.

## Folded from `2026-09-05-every-message-one-profile-one-card`
- Why (restated): motion and visibility — Chris judges the system by what he sees change in the wiki as he talks. The watcher files **every message** (not batches). ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]
- See also: [[topics/senter-wiki/wiki/concepts/ui-performs-the-fleet|UI performs the fleet]].

## Absorbed
- `decisions/2026-09-05-every-message-one-profile-one-card` — 2026-09-05 → archived at `topics/_archive/wiki-dedupe/senter-wiki/decisions/2026-09-05-every-message-one-profile-one-card.md`
