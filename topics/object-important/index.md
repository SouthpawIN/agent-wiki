# object-important — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-16 | Total pages: 14

## Entities
- [[topics/object-important/wiki/entities/dirk-qwen38-27b-mlx-artifacts|Dirk-Qwen3.8-27B-MLX-oQ4e artifacts]] — Artifacts downloaded for the MLX oQ4e variant of Qwen3.8 27B on 2026-09-07.
- [[topics/object-important/wiki/entities/hermes-file-endpoint-system-live|Hermes /file endpoint and system-live.json]] — A local Hermes server's file-serving route and the capacity limit that prevents it from serving a larger live-state artifact.
- [[topics/object-important/wiki/entities/mtplx-qwen38-27b-endpoint|mtplx-qwen38-27b endpoint]] — A local model serving endpoint observed responding to health-check pings at `http://127.0.0.1:11613/v1/models` on 2026-09-07.
- [[topics/object-important/wiki/entities/ornith-dflash2-artifacts|Ornith DFlash2 artifacts]] — Artifacts downloaded for the DFlash2 variant of Ornith 1.5.
- [[topics/object-important/wiki/entities/ornith-mlx4b-artifacts|Ornith 1.5 model artifacts]] — Artifacts downloaded into `~/Models/storage/ornith` and `~/Models/storage/ornith-dflash2` on 2026-09-07.

## Concepts
- [[topics/object-important/wiki/concepts/git-lfs-model-storage|git-lfs model storage strategy]] — `raw/inbox/2026-09-09.md` contains a Hermes background session on staging model artifacts for version control. The key substantive observation is that `.system-
- [[topics/object-important/wiki/concepts/omarchy-iso-bootable-usb|Omarchy 4.0.3 bootable-USB write]] — On 2026-09-12 Chris downloaded the **Omarchy 4.0.3** ISO (a minimal, Arch-based Linux distro) and wrote it to a USB stick to make it bootable, using `sudo dd`. 
- [[topics/object-important/wiki/concepts/ornith-performance-metrics|Ornith performance metrics]] — Observed throughput numbers for Ornith 1.5 local variants, captured across local-inference runs on 2026-09-07 and 2026-09-13.
- [[topics/object-important/wiki/concepts/ornith-routing-config|Ornith 1.5 routing config (8091)]] — On 2026-09-13 Hermes reported that Ornith 1.5 is now alive and routing on a **new local endpoint at `http://127.0.0.1:8091/v1`**, serving 14.5 tok/s on an M1 wi
- [[topics/object-important/wiki/concepts/watcher-status-noise|Watcher status noise]] — Status-only watcher filings can dominate a topic without adding substance.

## Decisions


## Comparisons


## Queries
- [[topics/object-important/wiki/queries/file-endpoint-cap-question-2026-09-08|2026-09-08: FILE_CAP size mismatch on Hermes /file endpoint]] — ^[raw/inbox/2026-09-08.md] Does the server serve `.system-live.json` via the `/file` endpoint?
- [[topics/object-important/wiki/queries/no-topic-substance-2026-09-07|2026-09-07: no actionable object-important substance in raw/inbox]] — The only raw item is `raw/inbox/2026-09-07.md`. It contains repeated background-process completions for local-model status checks and artifact downloads under `
- [[topics/object-important/wiki/queries/omarchy-host-address-2026-09-15|Omarchy host address (100.68.42.68)]] — A single-line observation from 2026-09-15 about where the Omarchy machine actually lives.
- [[topics/object-important/wiki/queries/tiel-coder-misrouted-2026-09-07|2026-09-07: Tiel-Coder download already belongs in turbofit]] — `raw/inbox/2026-09-07.md` contains `peculiar-ragdoll/Tiel-Coder-35B-A3B-MLX-oQ4e` download output under `~/Models/storage/tiel-coder`, but `topics/turbofit/wiki

