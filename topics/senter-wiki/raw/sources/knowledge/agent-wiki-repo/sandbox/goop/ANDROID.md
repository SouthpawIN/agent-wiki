# ANDROID — Senter mobile surface

## Context

The Android surface is another front end for Senter Agent. It is not a separate agent. Its speech path is the unnamed STS auxiliary task of Senter.

## Side Button Mode

- A side-button invocation opens a compact input-bar overlay.
- The overlay supports voice/text input and a Senter response surface.
- The same icon is tap-to-send and double-tap-to-screenshot.
- The icon can be dragged upward to expand into the full chat view.

## Full Chat Canvas

The expanded view contains:

- input bar
- conversation canvas
- building-block sidebar
- drag-and-drop placement onto the center canvas
- morphable UI elements with sensible defaults

Initial building blocks:

- `SESSIONS.md`
- `CHAT.md`
- `SENTER.md`
- current topic context
- proposal queue
- Kanban status

## Phone Operations

Screenshots and phone operations are explicit capabilities of the Android client and must remain permission-gated. Senter Agent decides what should happen; Android enforces user/system permissions.

## Emergence

Android UI work is evidence for the Senter Agent process. Repeated operations should produce Skills; coherent skill clusters may produce an Agent proposal; stable workflows may produce Loop proposals. Do not hard-code the whole pipeline before the Markdown context and evidence justify it.

## Safety

The Android client never receives host credentials, Hermes session databases, or unrestricted shell access. It communicates with a controlled Senter endpoint and uses Android APIs/permissions for device operations.

## References

- Repository: `sandbox/hermes-android/`
- Senter language: `../SENTER.md`
- Senter runtime: `../../SENTER_AGENT.md`
