# Hermes-native map for the four primitives (Anser interview 2026-09-04, all verified in source)
Spec: Context → Loops → Agents → Skills (agent-wiki README). Below: what Hermes already provides per lane, so Senter squeezes in instead of replicating.

**Chris is the hermit. Hermes Agent is the commander.**
Hermes discovers its own abilities via skills frontmatter, slash commands, profile config, and built-in tools. This wiki is the coordination layer on top, not a replacement for native ability routing. If Hermes can already do it with `hermes skills`, `hermes cron`, `hermes profile`, or `hermes kanban`, we use that. We only add: live multi-topic coordination, per-message filing, proactive pitching, and UI motion.

## Context (wiki-topics/)
- Storage: markdown vault — ours. Similarity: ours (TF-IDF; Hermes has no embeddings; `hermes journey --json` is a skills-capabilities/memories graph only).
- Locks: ours (Hermes never auto-summarises arbitrary files; `sessions pin`/`curator pin` are session/skill-only).
- Self-documentation: `on_session_finalize` hook → `hermes sessions export --format md --session-id <id>`; `hermes logs --session --since`. Distillation into log.md stays ours.
- Share: JSON-RPC `file.attach{path}` → `@file:` ref; `hermes chat --query-file`; `hermes project` binds a folder to a kanban board.

## Loops (triggers-loops/)
- `hermes cron` per profile (`cron/jobs.json`, `--deliver local`, `--script`, `--continuity`, `runs`, `incidents`, `output/{job}/{ts}.md`). No `--prompt-file` → `--script` shim cats `triggers-loops/*.md`.
- Task lifecycle + dispatch: `hermes kanban` (45 verbs; claim = SQLite CAS; heartbeat/reclaim/comment/complete/attach; `watch`). Replaces CLAIM v2 + queue.md-as-lock.
- Approvals: `hermes serve` `approval.pending/respond`; plugin `register_approval_transport`.
- `curator` = skills only; `journey/learning` = graph only — NOT loop homes (Anser's recap said otherwise; retracted).

## Agents (agents/)
- Registry: `hermes profile list|describe|show`; dashboard `GET /api/profiles`, `/api/profiles/{name}/soul`.
- Agent↔agent protocol if a bus is needed: A2A platform plugin (port 9900). `hermes send/peer/portal/monitoring/moa` are NOT a bus.
- Verification evidence: written by Hermes core (`agent/verification_evidence.py`) → `hermes verify --detect-only --json`; `agent.verify_on_stop` for builders.

## Skills (skills-capabilities/)
- `GET /api/skills?profile=X` → name/description/category/enabled/usage/provenance; `skills-capabilities/.usage.json` per profile (13 fields). No cross-profile aggregate → loop profiles.
- `hermes bundles` = slash aliasing, irrelevant.

## Bridge (the seam)
- Keep: `/post` (until kanban watch lands), `/write` (vault-allowlisted), `/events`.
- Replace: `/stt /tts /file /health` → dashboard `/api/audio/transcribe`, `/api/audio/speak`, `/api/files/read`, `/api/health` (9119). Check `/api/files/read` allowlist scope first.
- Replace: approval relay (above). Composer injection → `file.attach`.

## Order of work
1 approvals → 2 bridge routes → 3 kanban (biggest; rewrites every bot prompt) → 4 usage via sessions export → 5 scanner inputs via /api.
