# PETDEX.md — presentation-only mascot contract

Petdex is a presentation adapter for Hermes surfaces. It may show activity states,
but never grants execution permission and never changes the Senter approval boundary.

## Selection

- Hermes-native commands: `hermes pets list`, `hermes pets install <slug> --select`,
  `hermes pets doctor`.
- The active mascot is profile-scoped under `<HERMES_HOME>/pets/`.
- Senter's owl Eikon remains the authoritative identity; Petdex is an optional
  activity indicator and must fall back to the static owl when unavailable.

## Whole-flow mapping

| Flow state | Petdex state |
|---|---|
| idle | idle |
| thinking/listening/working | run |
| speaking | done |
| error | error |

## Safety

Petdex is display-only. It cannot invoke ADB, shell, host tools, STS capture, or
speech playback. Missing gallery/network/terminal graphics support must degrade
gracefully to the static Herm/Eikon asset.

## Verification

Use `hermes pets doctor` only in a disposable profile. Do not install, select, or
modify a live Hermes profile without explicit approval.

Source: the Hermes-native `petdex` skill, not a duplicated mascot implementation.
