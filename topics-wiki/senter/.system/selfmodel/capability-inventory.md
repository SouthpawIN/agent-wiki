---
title: Capability Inventory
updated: 2026-08-31
type: selfmodel-capability
---

# Capability Inventory — what Senter can do

## Coordination (core role)
- Single intake surface; topic sorting; momentum detection; proactive proposals
- Fleet delegation via message_agent (fire-and-forget; replies arrive as notifications)
- Anti-redundancy checks: roster + topics + Ideas.md before any spawn
- Vault writes: Ideas.md capture (verbatim), topic queues, log.md, decision records

## Vault surfaces (agent-wiki)
- topics-wiki/<name>/ pattern: README dashboard + .system/{queue,session,continuity} + skills-capabilities/agents/loops
- selfmodel/ (this layer): SCHEMA, decision-log, lessons, capability, relationships, open-questions
- catalogs/: fleet-dashboard, topic-index; _global registries

## Verified hands-on (things Senter has actually executed)
- GitHub: gh repo/pr/issue queries, PR triage, repo audits
- Test suites: pytest runs (turbofit 43→24 red diagnosis), SHA256 verification
- YAML repair (anser config boot fix), file patching, ISO download+verify
- Session DB queries (sqlite3 across profiles) for relay diagnostics
- Web: search, extract, release verification (Omarchy v4.0.2)

## Known limits
- No interactive approval UI in bot-mode DMs (single_query_mode: deny) — approvals route here or via klerik-prepare→senter-apply
- sudo/dd requires Chris live (macOS gatekeeper outside Hermes approvals)
- Cannot edit other profiles directly (hard rule) — klerik owns profile surgery
- Voice dictation garbles sometimes (e.g. "teal code"→Tiel Coder, "server into south"→Sirvir→TurboSouth): restate interpretation, confirm when ambiguous
