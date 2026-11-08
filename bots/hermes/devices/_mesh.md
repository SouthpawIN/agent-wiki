---
type: mesh
title: The mesh
updated: 2026-11-08
authority: hermes-vps
tags: [hermes, tailscale, mesh, devices]
---

# The mesh

One authority, every device attached. This file is the record of what is actually
wired, verified, and how to re-verify it.

## Authority

| Field | Value |
|---|---|
| Authority host | `hermes-vps` (100.110.215.46), tailnet `tail6ff78b.ts.net` |
| Web app (dashboard) | **https://hermes-vps.tail6ff78b.ts.net:8443/** |
| Local dashboard port | 9119 (platform-managed; loopback) |
| Auth | Nous OAuth (`/auth/login?provider=nous`) — the tailnet is transport, not auth |
| TurboFit gateway | https://hermes-vps.tail6ff78b.ts.net/ → 127.0.0.1:8091 (pre-existing) |
| Verified | 2026-11-08 — HTTP/2 302 → `/auth/login?provider=nous`, `server: uvicorn` |

## Serve configuration

```bash
tailscale serve --bg --https=8443 9119     # dashboard, root path, own port
tailscale serve status                     # both proxies listed
```

The dashboard is served on its **own HTTPS port** rather than a subpath, because
the app expects to live at `/`. Port 443 was already proxying the TurboFit
gateway, so 8443 keeps both alive.

## Devices on the tailnet

| Device | Tailscale IP | OS | Seen | Role |
|---|---|---|---|---|
| hermes-vps | 100.110.215.46 | linux | online | **authority** |
| omarchy | 100.68.42.68 | linux | online | client + local TurboFit node |
| chriss-s10 | 100.93.96.90 | android | online | client (browser / add-to-home-screen) |
| christophers-macbook-pro | 100.81.37.77 | macOS | offline (5 m ago) | client + local TurboFit node |
| surface-duo-2 | 100.79.15.54 | android | offline (4 d) | client |

## Bot profiles

Nine profiles exist on the authority, one per bot, each with its `SOUL.md` rendered
from its `BOT.md` and its `bot-<slug>` skill installed.

| Wiki bot | Profile name | Callsign |
|---|---|---|
| bot-wiki | `bot-wiki` | Klerik |
| youtube | `youtube` | Cutroom |
| pocketshop | `pocketshop` | Binder |
| turbofit | `turbofit` | TurboSouth |
| kart-racer | `kart-racer` | Apex |
| ai-daw | `ai-daw` | Riff |
| anser | `anser` | Anser |
| **hermes** | **`mesh`** | Mesh |
| ssi | `ssi` | Beacon |

`hermes` is reserved by Hermes itself, so the profile is named `mesh`; the wiki
slug stays `hermes`.

```bash
hermes profile list              # ten profiles: default + the nine bots
hermes -p youtube chat           # opens the same agent the wiki describes
python tools/publish_profiles.py . ~/.hermes   # re-render after any BOT.md edit
```

## Onboarding a device

1. Confirm it is on the tailnet: `tailscale status` shows it, and it resolves
   `hermes-vps.tail6ff78b.ts.net`.
2. Open **https://hermes-vps.tail6ff78b.ts.net:8443/** and sign in with the Nous
   account. Send one message.
3. Desktop app: point it at the remote backend URL instead of starting a local
   agent. `hermes -p <bot> chat` must show the same sessions as the web app.
4. Phone: open the URL, then Add to Home Screen for an app-like surface. Do not
   let the phone create a local profile — that forks memory.
5. Verify sameness three ways: a message sent on the device appears in the
   authority's sessions; a skill created on desktop is listed on the phone; one
   bot's chat history matches on both.
6. Record the device in this file with the date verified.

## Container limitation (this authority)

`hermes-vps` runs tailscaled in **userspace mode** (no TUN, no root). Consequences:

- MagicDNS is not installed system-wide, so `curl https://…ts.net` from inside the
  container fails. Verify through the SOCKS proxy instead:
  `curl -sI --proxy socks5h://localhost:1055 https://hermes-vps.tail6ff78b.ts.net:8443/`
- `tailscale ssh` and direct 100.x connections are unreliable from here. Real
  devices (omarchy, MacBook, phone) have proper TUN and reach the URL directly.
- If the container restarts, tailscaled must be started again:
  `/opt/data/bin/tailscaled --tun=userspace-networking --state=/opt/data/state/tailscale/tailscaled.state --socket=/opt/data/state/tailscale/tailscaled.sock --socks5-server=localhost:1055 &`
  then `tailscale serve --bg --https=8443 9119`. Serve config persists in state.

## What is NOT done

- The MacBook, Surface Duo 2, and phone have not **signed in** to the instance yet.
  The profiles exist here; each device needs one login at
  https://hermes-vps.tail6ff78b.ts.net:8443/ to see them in Bot Mode.
