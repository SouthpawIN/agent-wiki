# Critical gaps — TurboFit self-install promises (audit 2026-08-27)

## Fixed right now
- gateway healthy
- provider wired into Hermes config
- plugin enabled (was already in config)
- skill installed (was already present)

## Open gaps (ranked)
1. CRITICAL: controller+gateway not installed as launchd services — TurboFit is NOT automatic; it only runs when manually invoked. install-controller-service must run (it's Linux-systemd-shaped, needs a macOS launchd translation).
2. shell rc not wired (install.sh step never run)
3. PROMISE GAP: 'fresh install should self-configure' — scripts/install.sh only wires shell rc + assumes skill exists; it does NOT: (a) clone repo, (b) create venv, (c) build native runtime, (d) download models, (e) set auto selection, (f) start gateway, (g) add Hermes provider block. On macOS there is also no launchd service installer (only systemd). These steps are what we did by hand today — they must become one command.

## What 'automatic' must mean (acceptance)
One command on a fresh Mac (no repo, no venv, no models) ends with:
1. deps checked/installed (python3.10+, cmake)
2. repo cloned + venv + runtime built (metal)
3. models downloaded (Fit-List group for this machine)
4. `set auto` written, gateway+controller running as launchd services (survive reboot)
5. Hermes config.yaml provider block added, plugin enabled, skill linked
6. `/turbofit status` answers in a fresh Hermes session
Current state: steps 2-5 done manually today; nothing survives reboot except files.

## Gaps vs the 2026-10-18 scope (audit 2026-10-18)
Ranked against the new universal scope (see ROADMAP.md):
1. README lineup ≠ live `references/model-catalog.json` — aspirational models/numbers ("slop"). Align to real catalog.
2. **One combined fit list** — no GPU-dedicated (dense) vs unified (MoE) split. `turbofit_list.py` + profiles.
3. **No engine registration** — engines are a fixed set; TurboFit must be able to add inference engines, not just models.
4. **No benchmark publication surface** — `external-benchmarks.md` is discovery-only (all candidates show `-`); users can't see best model+engine per tier.
5. **SALT-core not integrated** — fork is a dry-run public export; needs a qualification gate before it's a real engine.
6. **Cross-OS debt** — 10 environmental test failures (Linux/Windows); self-install promise still hand-run.
7. **Tailscale** — solidify auto-config on install + reliable discovery/federation.
