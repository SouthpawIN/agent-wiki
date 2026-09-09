---
name: watcher-per-message-filing
description: Use when building or tuning the Senter watcher. File every Hermes message into a topic inbox as it lands; no session-end batching, no sidebar hand-off.
version: 0.1.0-proposed
proposed: 2026-09-05 17:05
topic: senter
---
# watcher-per-message-filing
# Per-message watcher filing

1. Tail Hermes's message table / agent.log directly; act on every new message, not on session end.
2. Score each message against the topic corpus (TF-IDF snapshot the scanner writes); append to topics/<t>/.system/inbox.md with timestamp, author, session id, similarity.
3. Below threshold → _inbox/unsorted.md plus a 'new topic?' proposal card.
4. Emit a feed card per filing so Chris watches the wiki move as he talks.
5. Reload the corpus whenever the scanner rewrites the snapshot; run as launchd so it never needs the sidebar to remember.
6. Every N filings on a topic, trigger the topic worker (GEPA generate+evaluate) — do not wait for a session to close.

Pitfalls: session-level batching was explicitly rejected; a hand-off from the sidebar defeats the design.

## Evidence
> a watcher can just programmically watch the logs as they're being populated and then sort all of those in the topics
> not per session, I want to per message, just like when you talk to cursor every message at its code base, I want this to edit the user's ideas into a knowledge and agentic flows
