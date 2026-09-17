# self-file — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-15 | Total pages: 17

## Entities
- [[topics/self-file/wiki/entities/colibri|Colibri]] — A local inference target evaluated on 2026-09-07 and ruled out for standard `mlx_lm` because it requires custom Maple MLX code. Hermes recorded, "Colibri requir
- [[topics/self-file/wiki/entities/hermes|Hermes]] — The AI agent framework Chris uses. On 2026-09-07 it surfaced the server-testing intent and reported the background process exit for the ornith server. ^[raw/inb
- [[topics/self-file/wiki/entities/mltplx-server|MTPLX server]] — A local inference server observed on `127.0.0.1:11613`. On 2026-09-07 Hermes noted, "The server on 11613 is MTPLX." ^[raw/inbox/2026-09-07.md]
- [[topics/self-file/wiki/entities/ornith-server|ornith server — mlx_lm local instance]] — Local `mlx_lm` server instance serving the `ornith` model from `/tmp/mlx-lm-deepgrove`, bound to `127.0.0.1` with a contested port. Chris said at 2026-09-07 14:

## Concepts
- [[topics/self-file/wiki/concepts/local-model-serving|local model serving]] — Running LLM inference locally on Chris's machine, rather than via remote API. On 2026-09-07 Chris said, "I have good info on the current setup. Let me test both
- [[topics/self-file/wiki/concepts/remote-host-inference-discovery|remote-host inference discovery]] — The practice of locating and bringing up a local-inference server on a remote compute box in Chris's setup — a machine Chris calls the "HP" (with a related `oma
- [[topics/self-file/wiki/concepts/remote-inference-stack-2026-09-15|Remote inference stack — 2026-09-15]] — A remote inference deployment Chris's setup converged on by 2026-09-15, distinct from the earlier local-loopback ornith server. The stack, as reported by Hermes
- [[topics/self-file/wiki/concepts/scan-json-schema|scan-topics.py JSON schema — skills field]] — A `skills` field schema mismatch surfaced in the raw→wiki compilation loop on 2026-09-09. The scan's PRINT output reported `skills=0` (an integer count) while t
- [[topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]] — Constraints that determine whether a local inference target can actually run on Chris's existing `mlx_lm` setup, as opposed to requiring a different server fram

## Decisions
- [[topics/self-file/wiki/decisions/colibri-ruling-2026-09-07|Colibri ruling — 2026-09-07]] — On 2026-09-07, after downloading and attempting to use Colibri, Hermes decided it was not compatible with standard `mlx_lm` and switched back to ornith. Hermes 
- [[topics/self-file/wiki/decisions/remote-stack-converged-2026-09-15|Remote inference stack converged — 2026-09-15]] — On 2026-09-15 Hermes reported the remote inference stack healthy after a session of GPU-memory kills and restarts: "nginx is up on 8080, model server healthy on
- [[topics/self-file/wiki/decisions/server-exploration-2026-09-07|Server exploration note — 2026-09-07]] — On 2026-09-07 Chris said he had good info on the current setup and intended to test both existing servers and explore other options. ^[raw/inbox/2026-09-07.md] 
- [[topics/self-file/wiki/decisions/token-desync-2026-09-08|Token desync — 2026-09-08 server restart]] — On 2026-09-08, after both local servers came back up, Hermes found the `/token` endpoint returning a stale value different from the newly written token file. Th
- [[topics/self-file/wiki/decisions/watch-process-overwrite-2026-09-09|Watch process data-overwrite restart — 2026-09-09]] — On 2026-09-09, Hermes observed that a running watch process was overwriting files with old data, creating a stale-data consistency issue in the raw→wiki compila

## Comparisons
- [[topics/self-file/wiki/comparisons/local-servers-2026-09-07|Local servers — 2026-09-07]] — | Server | Port evidence | Status notes | Source |

## Queries
- [[topics/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]] — After Colibri was ruled out for standard `mlx_lm`, Hermes said, "Let me start Bonsai MLX and get things working." ^[raw/inbox/2026-09-07.md] On 2026-09-08, Herm
- [[topics/self-file/wiki/queries/mlx-lm-large-prompt-kill-causes|What triggers SIGKILL in mlx_lm server during long prompt processing: cache limits, memory pressure, or timeout?]] — Chris hit a hard kill after 40k tokens on the ornith `mlx_lm` server; knowing the cause informs whether to tune cache, add swap, or switch servers.

