---
name: proposal-apply-proof
description: Use when marking any approved proposal (bot, loop, research, skill) as applied/LIVE. The status flag is written only from a verification result — never from the apply command having been issued.
version: 0.1.0
distilled: 2026-09-05 18:21
topic: klerik
---
# proposal-apply-proof
Rule: status LIVE / card running is set ONLY after the proof command for the artifact type returns the artifact; apply failure → status: FAILED (apply) + error verbatim + BLOCKED, never LIVE next to FAILED. Proof table: bot → `hermes -p <name> -q` emits bridge/loaded; loop → `hermes -p <owner> cron list` shows the job and first tick logs to .system/session.md; research → query page has a dated answer and .md.proposed is gone; skill → file exists AND a bot loads it. Steps: read proposal → apply (loops: SHORT cron prompt pointing at the loop file, never inline paragraphs — inline got mangled and FAILED 2026-09-05) → run proof, capture real output → only then flip status, append ## Applied with proof, log session.md, POST DONE before→after→proof. Pitfalls: on disk ≠ connected (rule 8); paladin 'spawned' twice before it existed and klerik-queue-drain was LIVE with zero cron jobs — same bug; file tools only, batch protected writes (rule 14); no workarounds around a failed gate (rule 7). Written to topics/klerik/skills/proposal-apply-proof/SKILL.md.

## Evidence
> Now the pending proposals — approve the ones that are clearly what Chris described, and prove the apply path with one real approval.
> Approving a bot card still just renames the file; the actual `hermes profile create` via klerik is the next wire.
