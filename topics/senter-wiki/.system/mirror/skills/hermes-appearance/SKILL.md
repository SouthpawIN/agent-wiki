---
name: hermes-appearance
description: "Use when customizing Hermes pets, bot avatars, or themes."
version: 1.0.0
author: Dogeman curator
license: MIT
metadata:
  hermes:
    tags: [hermes, pets, avatar, petdex, appearance, theme, skin]
    homepage: https://github.com/NousResearch/hermes-agent
    related_skills: [hermes-agent]
---

# Hermes Appearance — Pets, Avatars & Theming

Make Hermes *look* like your crew. Pets are animated mascots (`display.pet`), avatars are the 160×160 bot icons (`assets/avatar.png`), skins/themes recolor every surface. This skill keeps them in sync.

## Quick Routing

| Goal | Do |
|---|---|
| Change / sync bot icon to pet (e.g. 123MikeyD → Dogeman) | See `references/pet-avatar-sync.md` — extract frame from `spritesheet.webp` |
| Run a multi-bot pet parade (Dogeman + TurboSovth + Teknium, etc.) | See `references/pet-parade.md` — per-profile pets, one pet per window, 3-window parade + Teknium builder pattern |
| Browse / install / scale pets | `hermes pets list`, `install <slug> --select`, `scale 0.75`, `doctor` — see `hermes-agent` references/petdex.md |
| Theme / skin tweak | `hermes skin set <key> <hex>` on active skin; `hermes config set display.skin <name>` |
| Diagnose pet not showing | `hermes pets doctor` — checks installed + enabled + Pillow + terminal graphics |

## Avatar vs Pet — Don't Confuse

- **Pet** = animated sprite sheet in `<HERMES_HOME>/pets/<slug>/spritesheet.webp`, controlled by `display.pet.slug`/`enabled`/`scale`. Reacts to agent state (idle/run/error).
- **Avatar** = static 160×160 PNG at `<HERMES_HOME>/assets/avatar.png` (global) and `profiles/<profile>/assets/avatar.png` (per-profile override). Shown as bot icon in chat/desktop.
- Setting a pet does **not** change the avatar automatically. Syncing is a manual extract → resize → replace step (this skill).

## Profile-Aware Paths

Resolve home via `$HERMES_HOME` (or `~/.hermes` / `~/.hermes/profiles/<name>` when a profile is active). Avatars are profile-scoped:
- Active profile `dogeman` uses `~/.hermes/profiles/dogeman/assets/avatar.png` if it exists, else falls back to global `~/.hermes/assets/avatar.png`.
- Replacing only the global file won't affect a profile with its own override — replace the profile one for "this bot's icon".

## References

- `references/pet-avatar-sync.md` — full pet spritesheet → 160×160 avatar workflow (123MikeyD pattern, grid detection, trim/center, backup, reload)
- `references/pet-parade.md` — multi-profile pet pack: per-profile install, one-pet-per-window invariant, 3-window parade, Teknium Hermes-Agent builder profile, per-profile avatars

## Pitfalls

- Use the Hermes venv python (`~/.hermes/hermes-agent/venv/bin/python`) for Pillow — system `python3` on macOS often lacks PIL.
- Always backup `assets/avatar.png` before overwrite; replacement is silent.
- Avatar is cached at launch — `View → Reload` or restart desktop to see change.
- Sprite dirs are lowercase (`123mikeyd`) even when displayName is cased (`123MikeyD`).
