# Loop: approval-relay (owner: senter · hermes serve)
Relays every pending Hermes approval into the wiki feed as a yellow-bordered card and returns Chris's decision.

## Native home (verified 2026-09-04, Anser turn 5)
`hermes serve` JSON-RPC `approval.pending` / `approval.respond` (`tui_gateway/methods_prompt.py:1104/1154`), or the plugin API
`register_approval_transport(name, present_fn)` (`hermes_cli/plugins.py:423`) selected by `security.approval.transport`.

## Replaces
senter-bridge `pending/*.json` + `.decision` file polling (`~/.hermes/plugins/senter-bridge/server.py`). Root cause of its fragility: it never used the sanctioned transport API.

## Cadence
Event-driven (no cron). Requires `hermes serve` running — the desktop app spawns it.

## Status
[QUEUED] — first replacement to do (smallest blast radius). First command: `hermes serve --status`.
