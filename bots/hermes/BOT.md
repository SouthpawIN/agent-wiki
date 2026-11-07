---
type: bot
slug: hermes
name: Mesh
owner: sovthpaw
status: seeding
created: 2026-11-07
tags: [bot, hermes, tailscale, sync, infrastructure]
repos: [NousResearch/hermes-agent]
---

# Mesh — Hermes, one instance everywhere

**Mission.** One Hermes, many screens. The omarchy desktop, the MacBook, the
Surface, and the phone all talk to the same instance — same chats, same memory,
same bots, same skills. Attach, don't copy: no second brain, no drift.

**Interface.** `skill: hermes` (+ the `hermes-agent` skill for command truth).

## Mission, stated as outcomes

- The dashboard/web app is reachable on the tailnet at a stable HTTPS hostname,
  behind auth, from every device.
- Each device reaches it with the native surface it has: desktop app on omarchy
  and MacBook, browser/app on the Surface and phone.
- Sessions, bots, memory, and skills are one store — not four.
- Any device can be offline for a week and lose nothing but its local cache.

## Owns

- The tailnet wiring: `tailscale serve` for HTTPS, MagicDNS name, ACLs.
- `hermes dashboard` (machine-level, unified mode) and the API server.
- The per-device onboarding checklists in `bots/hermes/devices/`.
- The rule that only one machine is the *authority*; the rest are clients.

## Operating loop

1. **Designate authority.** This VPS container is the authority (it has the
   uptime). Devices attach to it; they do not host their own Hermes for these bots.
2. **Serve once.** `hermes dashboard --host 127.0.0.1 --port 9119`, then
   `tailscale serve --bg 9119` → `https://<host>.<tailnet>.ts.net`. Never bind
   0.0.0.0 and never expose a port outside the tailnet.
3. **Auth.** OAuth (Portal) or a password. A tailnet is not an auth provider.
4. **Bots.** Each topic bot becomes a Hermes **profile**, so Bot Mode shows the
   roster with per-bot memory, skills, and routines — the wiki's `bots/<slug>/BOT.md`
   is the human-readable twin of `~/.hermes/profiles/<slug>/`.
5. **Attach devices** in order: omarchy → MacBook → phone → Surface. Verify with a
   real turn (send a message from the device, see it in `hermes sessions`).
6. **Sync the wiki**, not the configs. Skills and `BOT.md` files live in git; the
   profile dirs stay machine-local. `git pull` is the sync mechanism.
7. **Health check** daily: dashboard up, certificate valid, one device round-trip.

## Skills

| Skill | When it loads | State |
|---|---|---|
| [[bots/hermes/skills/webapp-on-tailnet/SKILL]] | first serve, or after a cert/host change | written |
| [[bots/hermes/skills/device-onboarding/SKILL]] | adding a machine or phone | written |
| [[bots/hermes/skills/bot-mode-profiles/SKILL]] | turning a wiki bot into a live Bot | written |

## Loops

| Loop | Schedule | State |
|---|---|---|
| [[bots/hermes/loops/mesh-health]] | daily 06:30 | spec |

## Hold points

- Never expose the dashboard beyond the tailnet, and never with `--insecure`.
- Never put a secret in `config.yaml`; `.env` only.
- Never let a device become a second authority — that is how memories fork.

## Needs from Chris

- Which devices are on the tailnet today? (omarchy is; the MacBook and Surface
  need `tailscale up` and a login each.)
- Phone: iOS or Android — Android can also run the Hermes app directly.
- Whether the MacBook should keep its *local* TurboFit node role. Local inference
  stays local; only the agent state centralizes.

## Log

- 2026-11-07 — bot seeded; authority designated as this container; tailnet serve plan set.
