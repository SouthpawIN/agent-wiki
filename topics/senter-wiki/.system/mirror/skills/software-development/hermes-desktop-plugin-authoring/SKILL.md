---
name: hermes-desktop-plugin-authoring
description: "Write + verify Hermes desktop plugins with no build step."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, desktop, plugins, electron, sdk, verification, statusbar, keybinds]
    related_skills: [hermes-agent, inspecting-hermes-desktop-dom]
---

# Authoring Hermes desktop plugins

## When to Use

- Adding a UI element to the Hermes desktop app: a statusbar chip, a pane, a
  ⌘K command, a keybind, a route, or a transcript directive.
- A plugin you wrote fails to load, renders blank, or shows an error toast.
- You need to drive gateway RPCs from a desktop UI control.

Skip when the request is a theme/skin (that is `hermes skin set` + the skins
reference) or a TUI widget (different contract, different directory).

The bundled `hermes-agent` skill carries the API surface reference at
`references/desktop-plugins.md` (areas, `ctx.register`, pane placement,
`ctx.os`, `ctx.rest`) — load that skill for the contract. **This skill covers
what that reference does not: how to VERIFY a plugin before claiming it
works.**

## The core hazard: no build step

The plugin file is loaded **uncompiled** — source → bare-specifier rewrite →
blob `import()`. There is no typechecker, no linter, no bundler between you and
the renderer. Consequences that decide how you must work:

- A misspelled or unimported identifier is a **runtime `ReferenceError` at
  render**, not a build error. It fails when the user looks at it.
- JSX syntax does not parse. Use `jsx()` / `jsxs()` from `react/jsx-runtime`.
- Only three specifiers resolve: `@hermes/plugin-sdk`, `react`,
  `react/jsx-runtime`. Anything else throws at import.
- `node --check` proves only SYNTAX. It cannot see a bad import name. Passing
  it is not evidence the plugin works.

So: **verify every identifier against the real SDK source before writing.**

## Procedure

1. Pick a kebab-case `id`; the folder name MUST equal it.
   `$HERMES_HOME/desktop-plugins/<id>/plugin.js`
2. Find the RPCs/state you need in the real source, not from memory:
   - Gateway RPC names: `grep -n '^@method(' tui_gateway/server.py`
   - Read the handler body before calling it — params and their semantics
     matter (see the `persist` pitfall below).
   - `host.state` atoms: `apps/desktop/src/sdk/index.ts` (`export const host`).
3. Write the file.
4. **Verify identifiers** (see next section). Do this BEFORE reporting success.
5. `node --input-type=module --check < plugin.js` for syntax.
6. The app watches the directory and hot-loads within a few seconds. Fallback:
   ⌘K → **Reload desktop plugins**.

## Verification ladder

Climb it as far as the environment allows, then state plainly where you stopped.

**Rung 1 — every import resolves.** The loader rewrites `@hermes/plugin-sdk` to
a shim blob that re-exports live members enumerated with `Object.keys`, so a
name absent from the SDK is simply undefined at runtime. Check each imported
name against `apps/desktop/src/sdk/index.ts`, allowing for all the export
shapes (`export const X`, `export { X }`, `Y as X`, `export * as X`):

```python
# execute_code — batch-check instead of eyeballing a long import list
imported = ["host", "Tip", "cn", "icons", "useValue", "usePluginI18n"]
sdk = read_file(".../apps/desktop/src/sdk/index.ts", limit=2000)["content"]
sdk = "\n".join(l.split("|",1)[1] if "|" in l else l for l in sdk.splitlines())
pats = [r"export\s+const\s+{n}\b", r"export\s+\*\s+as\s+{n}\b", r"\bas\s+{n}\b",
        r"export\s*{{[^}}]*\b{n}\b[^}}]*}}", r"export\s+function\s+{n}\b"]
missing = [n for n in imported
           if not any(re.search(p.format(n=n), sdk, re.S) for p in pats)]
```

**Rung 2 — every asset name exists.** Some props take a free-form string and
fail silently. See the Codicon pitfall.

**Rung 3 — syntax.** `node --input-type=module --check < plugin.js`.

**Rung 4 — live DOM.** Only on dev-server runs (see
`inspecting-hermes-desktop-dom`). **Packaged builds expose no CDP port** —
`apps/desktop/electron/dev-cdp.ts` closes it for packaged builds with no
env override. Do not relaunch the user's app to get a port; you would destroy
their session. Stop at rung 3 and say so.

## Pitfalls

- **`Codicon` accepts ANY string.** It renders
  `<i class="codicon codicon-{name}">` with no validation — a wrong name is an
  invisible blank square, not an error. Confirm against the bundled font:
  `grep -n 'codicon-<name>' node_modules/@vscode/codicons/dist/codicon.css`.
  (`mute`, `unmute`, `mic`, `mic-filled` are real.)
- **Read an RPC handler before calling it.** Params carry semantics you cannot
  guess. Canonical example: `wake.stop` / `wake.start` accept `persist` —
  `persist: true` **writes `wake_word.enabled` to config.yaml**. A temporary
  runtime action must pass `persist: false` or it silently clobbers a
  persistent user setting.
- **Restore only what you tore down.** For any mute/pause/suspend toggle,
  snapshot what was actually running, then restore exactly that. Blindly
  re-enabling everything turns a toggle into a settings change.
- **Serialize async toggles.** Keep a module-level in-flight promise and
  early-return while it is pending; a double-clicked chip otherwise interleaves
  teardown with re-arm and leaves a device half-owned.
- **Runtime-only vs persisted state.** A "right now" gesture (mute, pause)
  should live in a plain `atom`, NOT `ctx.storage` — persisting it leaves the
  user silently muted after a restart.
- **Handlers read state imperatively** (`$atom.get()`), never from a render
  closure, or rapid events see stale values.
- **Never hardcode colors.** Theme vars only: `var(--ui-text-tertiary)`,
  `var(--ui-accent)`, `var(--chrome-action-hover)`.
- **Two on-disk doors, different defaults.** `desktop-plugins/<id>/plugin.js`
  loads enabled. `plugins/<id>/desktop/plugin.js` (the unified agent-plugin
  half) is **opt-in** — it inventories in Settings → Plugins but stays off
  until toggled. Check that toggle before debugging a "not appearing" report.

## Reporting honestly

A plugin is not "working" because the file was written. Say which rungs you
climbed and which you could not. Distinguish:

- verified (imports resolve, asset names exist, syntax passes), from
- expected (hot-load, chip renders) — with the ⌘K reload fallback offered.

If you fixed a root cause alongside the plugin, lead with the root cause and
cite the evidence (a log line count, a config key). The plugin is often the
workaround; the config gate is often the fix.

## Working with the user

When the user says "just install the plugin" / "just do X", they are cutting
off investigation. Stop researching breadth-first, ship the artifact, and fold
any remaining findings into the final report as a short offer ("want me to also
…?"). Do not narrate further exploration first.

## Supporting files

- `templates/toggle-plugin.js` — copyable device/state toggle plugin:
  statusbar chip + ⌘K row + rebindable keybind driving one serialized async
  action, with snapshot-then-restore. Start here for any toggle.
- `references/voice-and-mic-subsystem.md` — the voice/wake/barge-in RPC and
  config map, and the server-vs-client barge-in split.
