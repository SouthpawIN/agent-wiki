# Queue — agent-wiki / Senter

## [SKILLS]
- [x] turbofit-macos-setup — M1 Pro setup runbook; shipped in topics-wiki/turbofit/skills-capabilities/
- [x] vault GOOP structure — all 54 topics complete (janitor audit 2026-08-27)

## [AGENTS]
- [ ] fleet consolidation — senter + agent-wiki + klerik merging into ONE "Senter" repo (user directive 2026-08-29)

## [PLUGINS]
- [ ] obsidian-plugin — Hermes client inside Obsidian, GOOP mode default (held pending interface contract)
- [ ] speedometer-menu — TurboFit Check gauge redesign (B done, merged to feat/live-refit)
- [ ] expansion-option — conservative one-rung recovery default; jump-to-fit as option (shipped in plugin.js)

## [LOOPS]
- [ ] upstream-watch — periodic check of SouthpawIN/turbofit for macOS/Apple fixes
- [ ] senter-rebuild-watch — HP box recovery: user booting live USB → SSH-driven Omarchy install (2026-08-29)

## 2026-08-29 — SENTER RECOVERY + TURBOFIT FIX (log)
1. **senter Omarchy install — IN PROGRESS, PAUSED AT RECOVERY**: verified data absorb (68G on Mac, md5-logged), NIC gate passed (e1000e + igb in Omarchy 4.0.1 t2 initramfs), ISO SHA-verified. Pivot-to-tmpfs approach failed mid-chroot (box dropped off network — probable resource conflict: 6.2G ISO + 8G tmpfs + package cache on 90%-full disk). Disk state: new empty GPT written, NO filesystems — Ubuntu dead, nothing user-valuable lost (absorb verified first). RECOVERY: physical power-cycle → boot standard live USB (NOT Omarchy t2 kernel) → enable sshd → I drive partition/pacstrap/omarchy/bootloader/tailscale remotely. Milestone notes promised at each step.
2. **turbofit `Unknown provider 'turbofix'` on fresh Mac — FIXED upstream-ready**: root cause = apply_configuration/serve_tailnet wrote providers.turbofit only to default ~/.hermes/config.yaml, fresh profiles (turbosovth etc.) have their own config.yaml. Fix: _save_configuration_to_all_homes() fan-out + ensure_provider_registered() heal called from register() + serve_tailnet uses same fan-out. Commit 4cc6b06 on feat/live-refit. Verified: resolve_runtime_provider('turbofit') OK from both homes; gateway /v1/models returns auto/active:main/active:aux on M1 Pro. Push blocked on GitHub auth (PAT pending).
3. **Fleet note**: turbosovth (TurboFit support agent) holds sudo on senter and edited authorized_keys out-of-band during install — flagged; user should review whether that access is wanted. NOPASSWD sudoers.d/nopasswd exists on senter (remove post-install).
