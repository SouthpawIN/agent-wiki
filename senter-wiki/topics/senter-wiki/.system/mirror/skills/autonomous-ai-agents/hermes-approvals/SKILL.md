---
name: hermes-approvals
description: "Use when debugging or auditing Hermes approval flows."
version: 1.0.0
author: Anser (fleet)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, approval, gateway, security, debugging, audit, senter-bridge, plugins]
    related_skills: [hermes-agent]
---

# Hermes Approval & Gateway-Decision Subsystem

How to understand and debug "why didn't this action prompt the user?" / "why did
this prompt surface (or not) on my gateway surface?" in Hermes. This is the deep
architecture map — line numbers are point-in-time (verified against v0.20.6) and
MUST be re-checked against the live source (`~/.hermes/hermes-agent/tools/approval.py`,
`tools/file_tools.py`, `cli.py`) before you assert them. The map is the durable part.

## The one fact that explains most confusion: there are TWO separate gates

1. **`_run_approval_gate`** (`tools/approval.py`) — the shared decision core for
   `check_dangerous_command` (dangerous shell patterns) AND plugin `pre_tool_call`
   escalation. Honors, in order: yolo → session allowlist → **single-query
   short-circuit** → **cron short-circuit** → gateway notify branch → CLI panel.
2. **`_request_protected_instruction_approval`** (`tools/file_tools.py`) — writes to
   protected instruction files (SOUL.md, AGENTS.md, CLAUDE.md, .cursorrules,
   project `.hermes/config.yaml`). Deliberately does **NOT** route through
   `_run_approval_gate`: it reads `_gateway_notify_cbs` directly and calls
   `_await_gateway_decision` directly, so it asks EVERY time, with no
   session/permanent/yolo bypass. Fail-closed when no human channel exists.

**Debugging consequence:** an asymmetry where "protected-file writes prompt but
dangerous commands don't" is the expected default shape of a bug, because the two
gates short-circuit on different conditions. If only one kind is missing, trace
which gate that action uses first.

## Gate precedence (`_run_approval_gate`), in order

1. `--yolo` / session yolo → approved.
2. `is_approved(session_key, pattern_key)` → approved (session/permanent allowlist).
3. **single-query short-circuit**: if `_is_single_query_approval_context()` is True,
   force `is_cli = is_gateway = False`, then branch on `approvals.single_query_mode`
   (default `deny` → BLOCKED, no prompt; `approve` → auto-approve). This runs
   **BEFORE** the gateway/notify branch, so a single-query process never reaches a
   notify callback even if one is registered.
4. cron short-circuit: `_is_cron_approval_context()` → `approvals.cron_mode`
   (default `deny`).
5. gateway branch: if a `notify_cb` is registered for the session key
   (`_gateway_notify_cbs`), `_await_gateway_decision(...)` blocks for
   `approvals.timeout` (default 300s).
6. CLI panel (`prompt_dangerous_approval`) if an interactive callback exists.
7. else submit_pending / fail-closed.

## Context detection gotchas

- `_is_single_query_approval_context()` reads
  `gateway.session_context.get_session_env("HERMES_SINGLE_QUERY_SESSION")`, which
  falls back to `os.getenv` because that var is **NOT** in `session_context._VAR_MAP`.
  It is process-global only. Consequence: a plugin that pops it at *plugin-load
  time* is defeated if `cli.py` re-sets it later — see the env-var-ordering pitfall.
- `_is_gateway_approval_context()` = True when `HERMES_GATEWAY_SESSION` env is set
  OR a session platform is bound, but returns False if cron context is set first
  (cron is never a gateway approval context).
- Session key binding: `cli.py` calls `set_current_session_key(session_id)` **per
  turn, AFTER plugin load**. A plugin calling `register_gateway_notify(key, cb)` at
  import time therefore binds the stale `"default"` key. The workaround is lazy
  re-registration on the first `pre_tool_call` (which runs inside the turn with the
  real key bound).
- `-q` (single query) binds a real session key; `-Q` (bot-mode DM delivery,
  `tools/bot_mode_dm.py`) spawns a subprocess that **never** binds a real key — its
  `get_current_session_key()` stays `"default"`/`""` for the whole run.

## Timing / resolution

- `_await_gateway_decision` enqueues an `_ApprovalEntry`, fires the
  `pre_approval_request` hook, calls `notify_cb`, then blocks on the entry's
  `threading.Event` for `_get_approval_timeout()` (config `approvals.timeout`,
  default 300s, clamped to `MAX_SAFE_TIMEOUT_S`). On timeout the entry is dropped
  (`_drop_entry`) and the caller sees `resolved=False`.
- `resolve_gateway_approval(session_key, choice, request_id=...)` pops the entry and
  sets `entry.event`. Returns **0 when nothing was pending** (e.g. the agent already
  timed out). A client that polls longer than the agent's window will get `resolved=0`
  back — a false-positive "resolved" if the caller only checks the HTTP 200.
- Coalescing: identical concurrent approvals (same command + pattern_keys) adopt the
  leader's decision; `once` does not coalesce, session/always/deny/timeout do.

## Audit methodology (what "audit the whole approval path" actually means)

For each process type in scope, trace the full path and record per-gate results:

1. Which process types reach the surface: `-q`, `-Q` (bot_mode_dm), cron, gateway,
   desktop, kanban worker (`hermes chat -q "work kanban task <id>"`). Note how each
   arms the surface (argv sniff vs env var) and which are unattended (kanban, cron).
2. Both gates, separately: dangerous-command AND protected-file. They diverge (see
   above) — do NOT assume one implies the other.
3. Timing: gate-hit → card latency; does the agent's `approvals.timeout` expire before
   the human sees it; does the surface recover a card created while closed (pending
   backlog fetch on connect).
4. Redundancy: does anything else (gateway `/approve`, desktop prompt, another
   surface) race the decision and double-resolve? Headless `-q`/`-Q` arm only one
   surface in practice; interactive surfaces use their own notify path.

Evidence sources (read these, don't guess): `~/.hermes/senter-bridge/events.jsonl`
(approval phases: `request`/`pending`/`decided`/`response`), `pending/<id>.json` +
`pending/<id>.decision` files, and the `bridge/surface-armed` lines. A `decided`
event carries a `resolved:N` field — `0` means the agent had already timed out.

## Pitfalls

- **Env-var-ordering pitfall (the big one).** A plugin that sets/unsets an approval
  env var at import time is racing code that sets it later in `cli.py`. Verified:
  `cli.py` sets `os.environ["HERMES_SINGLE_QUERY_SESSION"]="1"` in the
  single-query handler **after** plugins load, so a plugin's load-time `pop()` is a
  no-op and single-query mode re-engages. Fix in the plugin's `pre_tool_call` hook
  (runs after the CLI has set its state), not at import.
- **"pop is sufficient" is a trap.** Because the var is process-global and re-set
  later, removing it once at load time does nothing. Always re-verify the var's value
  at the actual gate-hit moment.
- **False "approved" receipt.** A client that shows "approved" based only on a
  successful POST will mislabel a `resolved=0` (agent timed out) decision. Always
  thread the `resolved` field through to the UI state.
- **Don't key multi-bot routing on `session_key`** for `-Q` cards — it's `"default"`
  for every `-Q` run. Key on the request id.

See `references/senter-bridge-approval-integration.md` for the fleet-local
senter-bridge plugin/server specifics and the concrete findings from the first audit.
