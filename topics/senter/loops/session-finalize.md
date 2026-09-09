# Loop: session-finalize (owner: senter · hook)
Every finished session appends its distilled changelog to the topic's `log.md`/`session.md` automatically.

## Native home (verified 2026-09-04)
`on_session_finalize` hook (plugin or shell; `lifecycle.py:49/63`, payload `{session_id, platform, reason}`) → pull `hermes sessions export --format md --session-id <id>`.

## Replaces
"the agent must remember" — the per-turn canvas contract done by hand.

## Cadence
Per session end. Hook payload carries no transcript; the hook pulls it. Distillation (raw md → one-liners) stays custom or an LLM cron step.

## Status
[QUEUED] WRAP. First: `hermes sessions export --format md --dry-run`.
