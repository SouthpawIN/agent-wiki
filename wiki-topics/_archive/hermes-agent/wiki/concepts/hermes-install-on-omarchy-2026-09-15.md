---
title: "Hermes Install Broken-Fixed on Omarchy — 2026-09-15"
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [tool, infra, pain, timeline]
sources: ["raw/inbox/2026-09-15.md"]
confidence: medium
---

# Hermes Install Broken-Fixed on Omarchy — 2026-09-15

On `2026-09-15`, the Hermes CLI on Chris's **Omarchy** machine was found broken and then repaired. The root cause was a root-owned virtualenv blocking the real user (`sovthpaw`) from running the `sovthpaw`-owned source.^[raw/inbox/2026-09-15.md]

## The failure
- `2026-09-15 09:27` — Hermes: "The venv was created by `root` but the hermes-agent source is owned by `sovthpaw`. When you try to run as yourself, you get 'Permission denied' because the venv is root-owned."^[raw/inbox/2026-09-15.md]

## The fix
- `2026-09-15 09:31` — Hermes: "**Hermes CLI is fixed on Omarchy** — the venv had been created by `root`, making the python binary inaccessible to your user. I removed it, recreated it as `sovthpaw` with Python 3.13 (via uv), and symlinked the binary to `~/.local/bin/hermes`. `hermes --version` now works."^[raw/inbox/2026-09-15.md]
- Status summary reported:
  - SSH access via Tailscale: `tailscale ssh root@omarchy` works.
  - Hermes CLI: working — `Hermes Agent v0.21.0`.
  - Desktop package: installed — `hermes-desktop 2026.8.31-3`.
- `2026-09-15 10:04` — a later operation was interrupted; the fix itself, however, stood.^[raw/inbox/2026-09-15.md]

## Root cause (for future passes)
A root-created venv shadowing a `sovthpaw`-owned checkout. The durable lesson: ensure the Hermes venv is owned by the login user before running, or recreate it under that user (uv + Python 3.13) and symlink into `~/.local/bin`.

## Notes / scope
- The physical/Tailscale recovery (needing keyboard/monitor access, SSH key setup) is infrastructure and leans toward the `senter` topic; the hermes-agent-relevant part here is the broken-venv ownership fix and the version pin. See [[wiki-topics/hermes-agent/wiki/entities/session-20260915-262k-81tok|262K / 81.2 tok/s Milestone — 2026-09-15]] for the same session's later model work.

## Related
- [[wiki-topics/hermes-agent/wiki/concepts/active-model-provider-churn|Active Model / Provider Churn]]
- [[wiki-topics/hermes-agent/wiki/decisions/stable-context-lock-2026-09-07|Stable Context Lock — 2026-09-07]]
