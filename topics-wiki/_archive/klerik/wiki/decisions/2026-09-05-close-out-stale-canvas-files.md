---
title: Decision — record and close out the session's stale canvas files (2026-09-05 18:33)
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, infra, timeline]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Decision — close out the stale canvas files

**What.** While klerik's build ran in the background, the session used the wait to tidy: "Klerik is writing the SOUL now. Meanwhile, record and close out the session's canvas files, which have been stale:" ^[raw/inbox/2026-09-05.md] The canvas files are the coordinating session's own scratch/plan artifacts, not klerik's — they had fallen behind the actual state of the fleet.

**Why it is filed under klerik.** It marks the working pattern of that hour: long klerik runs are treated as background jobs, and the foreground uses the gap for housekeeping and gap-hunting ("While klerik builds, the next gap: …" 18:20 ^[raw/inbox/2026-09-05.md]). See [[topics-wiki/klerik/wiki/concepts/topic-agent-all-pass|Topic-agent --all pass]] for the other background job running in the same window. The line also documents the *state of belief* at 18:33 — that klerik was mid-SOUL — which the 18:42 result contradicted ([[topics-wiki/klerik/wiki/entities/senter-wiki-bot-spawn|senter-wiki-bot spawn]]). Lesson for the `skills-capabilities/background-job-liveness-check` skill: "is writing X now" needs a liveness/mtime check, not inference from elapsed time.

**Status.** Which canvas files and whether they were closed is not in this inbox. Low importance for klerik; recorded for completeness.
