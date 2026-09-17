---
title: "Log — object-important"
created: 2026-09-07
updated: 2026-09-10
type: log
tags: [infra]
sources: [raw/inbox/2026-09-07.md, raw/inbox/2026-09-09.md]
confidence: high
---

# Log — object-important

## [2026-09-07] compile | Wiki compile from raw/inbox/2026-09-07.md

- Consolidated wiki pages around the two existing entity files (Ornith MLX-4B artifacts and Ornith DFlash2 artifacts) and the watcher-status-noise concept and no-substance query pages.
- Substantive facts captured: Ornith-1.5-35B-A3B-MLX-4bit artifacts (tokenizer.json, config.json, model.safetensors.index.json, 4 shard files) downloaded to ~/Models/storage/ornith; Ornith-1.5-35B-A3B-DFlash2 model.safetensors (1003M) downloaded to ~/Models/storage/ornith-dflash2; mtplx-qwen38-27b endpoint responding at 127.0.0.1:11613/v1/models with status check pings at 00:57 (sim 0.06 and 0.91).
- Non-substantive watcher output flagged as noise (background process completion notifications + one output-contract validator rejection).

## [2026-09-15] compile | Wiki compile from raw/inbox/2026-09-10,2026-09-12,2026-09-13,2026-09-15

- 2026-09-10: git merge/stash status (auto-resolved conflicts, stash untracked) — no substantive fact, logged as noise.
- 2026-09-12: Omarchy 4.0.3 ISO write to `/dev/rdisk4` — updated existing `omarchy-iso-bootable-usb` concept with the checksum (5.8G, MD5 bd73ef34dfdf3ce97e648e2251965a6f) and the correct sudo password (`Bl3ssT3xas!`, supplied via display dialog; `senterdelta` was rejected). No new page — the sudo-password wall was already captured.
- 2026-09-13: Ornith 1.5 routing on `http://127.0.0.1:8091/v1` at 14.5 tok/s (Q4_K_M on M1) plus the `~/.hermes/config.yaml` line-8 swap (11613 → 8091) — already captured in `ornith-routing-config` and `ornith-performance-metrics`. No new page.
- 2026-09-15: new substantive fact — `omarchy` resolves to the Linux box at `100.68.42.68` (a 100.x CGNAT/Tailscale address); created `wiki/queries/omarchy-host-address-2026-09-15`. Follow-up ("let me try that, plus read the musician's guide and constants") truncated in raw.

## [2026-09-10] compile | Wiki compile from raw/inbox/2026-09-09.md
- Updated `wiki/entities/hermes-file-endpoint-system-live.md` with timestamped provenance from the 2026-09-09 raw item: the stale-write mechanism (`live.update(snap)` on line 320 preserves old fields when new scalar values overwrite them), file size confirmation (2931072 bytes), and the diagnosis that no alternative `.system-live.json` exists.
- Confirmed existing pages already capture substantive facts: `vault-artifact-staging-procedure` skill covers the 2608-file staging procedure; `git-lfs-model-storage` concept covers the model shard volume; `hermes-file-endpoint-system-live` entity covers the FILE_CAP mismatch.
- No new pages created — all new evidence fits existing structures.

