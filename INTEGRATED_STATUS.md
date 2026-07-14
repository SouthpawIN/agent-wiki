# Senter Agent Integrated Status

This is the verification map for the complete Senter Agent system. It deliberately separates contracts, implementation, and exercised behavior.

## Components

| Component | Artifact | Status | Verification |
|---|---|---|---|
| Unified Wiki | `~/.hermes/wiki/` | implemented | schema/index/log present |
| Senter runtime | `senter_agent/` | implemented | Python test suite |
| GOOP planner | `senter_agent/planner.py` | implemented, constrained | scoped source scan |
| Herm TUI | `sandbox/herm-sovth/` | implemented | typecheck, tests, build, startup smoke |
| Herm Petdex metadata | sidebar + `pet.info.meta` | implemented | Sidebar test |
| Petdex frame rendering | Hermes `pet.cells` backend + Herm `Petdex.tsx` | implemented | Sidebar test + full Herm suite |
| Android UX | `sandbox/android-surface/` | prototype implemented | browser interaction test |
| Android native client | `sandbox/hermes-android/` | prebuilt APK only | no source rebuild claimed |
| Android bridge | `sandbox/goop/android_bridge.py` | approval-gated implementation | contract/unit tests; live device blocked |
| STS | `sandbox/goop/STS_CONFIG.json` | specified | whole-flow validator |
| Eikon | Herm bundled/custom Eikon | implemented | avatar mapping tests/build |

## Known blockers

- No Android device/emulator is currently connected to ADB.
- The native Android checkout has no Gradle source tree.
- The owl reference HTML expected by `validate_owl_source.py` is absent from the checked-out workspace.
- Live Android device/emulator testing remains blocked until ADB has a connected target.

## Commands

```bash
PYTHONPATH=. pytest -q
SENTER_GOOP_SOURCES='sandbox/goop,sandbox/goop/profiles' python3 -m senter_agent.cli . --json --status
python3 sandbox/goop/validate_whole_flow.py sandbox/goop
python3 sandbox/goop/validate_android_surface.py sandbox/hermes-android/ANDROID_SURFACE.json
python3 sandbox/goop/validate_android_bridge.py sandbox/hermes-android/ANDROID_BRIDGE.json
cd sandbox/herm-sovth && bunx tsc --noEmit && bun test && bun run build
```

## User test surfaces

### Android prototype

```bash
python3 -m http.server 8765 --directory sandbox/android-surface
```

Open `http://127.0.0.1:8765` and test compact input, send, expand, drag/drop blocks, and screenshot-status behavior.

### Herm TUI

```bash
cd sandbox/herm-sovth
HERMES_HOME="$PWD/../hermes-home" bun run src/index.tsx
```

Test the three-eyed Eikon, state transitions, GOOP Wiki sidebar, and active Petdex metadata if Petdex is enabled in the disposable Hermes profile.
