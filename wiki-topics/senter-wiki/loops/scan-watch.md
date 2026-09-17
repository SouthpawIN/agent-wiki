# Loop: scan-watch (owner: senter · custom, KEEP)
Watches the vault + `~/.hermes/profiles/*` and rewrites `.system-live.json` on every change; the page re-renders from it.

## Why custom (verified 2026-09-04, Anser turn 3)
Hermes has NO filesystem hooks: all 37 `VALID_HOOKS` are lifecycle/tool/LLM/kanban/gateway events. Nothing fires on `wiki-topics/` edits.

## Shrink its inputs instead
bots[] → `GET /api/profiles` (`web_routers/profiles.py:634`); skills[] → `GET /api/skills?profile=X` + `skills-capabilities/.usage.json`. The `wiki-topics/` walk stays ours.

## Cadence
FSEvents via watchdog; launchd `com.senter.scanwatch`; 20 s poll fallback.

## Status
KEEP-CUSTOM (watcher) · [QUEUED] swap bots-profiles/skills sources to the dashboard API.
