---
title: "git-lfs model storage strategy"
created: 2026-09-09
updated: 2026-09-09
type: concept
tags: [infra, tool, decision, model]
sources: [raw/inbox/2026-09-09.md]
confidence: medium
---

# git-lfs model storage strategy

`raw/inbox/2026-09-09.md` contains a Hermes background session on staging model artifacts for version control. The key substantive observation is that `.system-live.json` is **generated** and excluded from staging, while downloaded model shards (`safetensors` files under `~/Models/storage/`) accumulate as large untracked binaries that would require git-lfs if committed.

## Staged file volume

^[[raw/inbox/2026-09-09.md]] The background session reported **2608 staged files** plus additional untracked model artifacts before the cut-off.

## Staging procedure

^[[raw/inbox/2026-09-09.md]] The session followed a repeatable sequence: set up git user config, stage important files while excluding `.system-live.json` because it is generated, then make a commit so updates can work.

## Untracked model artifacts

^[[raw/inbox/2026-09-09.md]] After staging 2608 files, some untracked files remained; the session treated these as additional model artifacts rather than source files.

## Generated artifact exclusion

^[[raw/inbox/2026-09-09.md]] The instruction "Stage the important files (excluding .system-live.json which is generated)" indicates that live-state JSON is regenerated at runtime and intentionally kept out of the model-artifact staging set.

## Implied git-lfs need

^[[raw/inbox/2026-09-09.md]] A comment about the server possibly needing git-lfs because `.system-live.json` was "too large" (2.8MB) extends to the much larger `safetensors` shard files, which are routinely hundreds of megabytes each — see [[topics/object-important/wiki/entities/ornith-mlx4b-artifacts|Ornith 1.5 model artifacts]] and [[topics/object-important/wiki/entities/dirk-qwen38-27b-mlx-artifacts|Dirk-Qwen3.8-27B-MLX-oQ4e artifacts]] for shard sizes from earlier passes.

## Related

- [[topics/object-important/wiki/entities/hermes-file-endpoint-system-live|Hermes /file endpoint and system-live.json]]
- [[topics/object-important/wiki/concepts/watcher-status-noise|Watcher status noise]]
