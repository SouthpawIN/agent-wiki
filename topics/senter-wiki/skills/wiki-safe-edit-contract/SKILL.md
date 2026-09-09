---
name: wiki-safe-edit-contract
description: Use when editing vault-live.html. Preserve boot bindings, row geometry, and dot centering.
version: 0.1.0
distilled: 2026-09-06 22:36
topic: senter-wiki
---
# wiki-safe-edit-contract
1. Before editing vault-live.html, identify last known-good state markers: `window.mdRender`, `--orbShift`, BRIEF.md references, and `.usage + .orbs` right-anchor selector. 2. Keep `.usage` → `.diffbadge` → `.tname` insertion order; `.rdiff` is fixed 44px between usage and dots. 3. After any edit, run `node --check` on the inline script and verify no `TEMP-` markers remain. 4. If recovery is needed, patch from the known-good snapshot rather than older backups that lack recent additions. 5. Boot-critical code must not reference bare `md` after it becomes `window.mdRender`.

## Evidence
> 'The file thrash stopped at: current page is structurally valid HTML/JS, but missing the good-state additions (`window.mdRender`, `--orbShift`, `BRIEF.md`, hover anchor handlers)'
> 'the editor module ended with `return {..., md, ...}` but `md` no longer exists under that name (it became `window.mdRender`, which doesn't bind a bare `md`). That one line threw at load and killed every line below it'
> 'I broke the row's right-anchor selector chain, which is what kept the dots flush-right and the usage strip pinned'
