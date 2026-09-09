# EIKON.md — Senter owl integration contract

## Authority

The embedded owl player is the accepted animation reference and source artifact:

- `owl-player-embedded.html`
- embedded identifier: `owl-animated-24fps`
- source states: `idle`, `thinking`, `speaking`
- source frame rate: 24 fps
- source grid: 192×96

Do not redesign the owl or generate replacement animation art as part of frontend integration.

## Herm State Mapping

The Herm avatar driver has six runtime states. The accepted mapping is:

| Herm state | Source animation |
|---|---|
| `idle` | `idle` |
| `thinking` | `thinking` |
| `speaking` | `speaking` |
| `listening` | `thinking` |
| `working` | `thinking` |
| `error` | `speaking` |

The source animations are reused as-is. Missing Herm states are aliases, not new clips.

## Integration Boundary

The browser player and the Herm `.eikon` format are different representations. The browser player must remain available for visual verification. A production `.eikon` conversion is a separate, reproducible preprocessing step and must not silently alter the selected animations.

Until that converter is verified at real Herm TUI scale, Herm may use its existing baked fallback while the owl integration is tested independently.

## Acceptance Checks

- All six Herm states resolve through the mapping above.
- No new animation states are authored.
- The source player can be opened and inspected offline.
- Any conversion records source hash, dimensions, frame count, and mapping.
- Malformed source data fails closed rather than producing a partial identity asset.
