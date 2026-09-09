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
