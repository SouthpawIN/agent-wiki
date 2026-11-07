---
name: device-onboarding
description: Attach a new device to the single Hermes authority.
version: 1.0.0
author: Mesh
license: MIT
metadata:
  hermes:
    tags: [hermes, devices, tailscale, macos, windows, android]
---

# Device onboarding

One authority (this VPS), everything else attaches. Order matters: network first,
then app, then verify with a real turn.

## Procedure

1. **Network** — install Tailscale, `tailscale up`, confirm the device appears in
   `tailscale status` and resolves the authority's MagicDNS name.
2. **Reach the web app** — open `https://<host>.<tailnet>.ts.net`, log in, send one
   message. If this fails, stop; do not install anything else yet.
3. **Desktop app** (macOS / Windows / Linux) — install Hermes, point it at the
   remote backend URL rather than starting a local agent. `hermes -p <bot> chat`
   against the remote should show the *same* sessions as the web app.
4. **Phone** — web app in the browser, then "Add to Home Screen" for an app-like
   surface. Android may also run the Hermes app; if it does, still point it at the
   authority, don't let it create a local profile.
5. **Verify sameness**, all three ways:
   - a message sent on the phone appears in `hermes sessions` on the authority;
   - a skill created on the desktop is listed on the phone;
   - a bot's Bot Chat has the same history on both.
6. **Local-only carve-outs** — if the device also runs local inference (TurboFit
   on the MacBook), keep the model local and the *agent state* remote. Document it
   in `devices/<name>.md` so nobody "fixes" it later by centralizing the model.
7. **Write `devices/<name>.md`**: OS, tailnet name, surface used, date verified,
   and the one command that re-opens it.

## Anti-patterns

- Two authorities. Memory forks immediately and silently.
- Copying `~/.hermes` between machines "to sync". That is how you get four brains.
- Exposing the dashboard on the LAN to avoid Tailscale. The tailnet is the point.
