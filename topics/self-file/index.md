# self-file — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-08 | Total pages: 12

## Entities
- [[topics/self-file/wiki/entities/colibri|Colibri]] — A local inference target evaluated on 2026-09-07 and ruled out for standard `mlx_lm` because it requires custom Maple MLX code. Hermes recorded, "Colibri requir
- [[topics/self-file/wiki/entities/hermes|Hermes]] — The AI agent framework Chris uses, which surfaced the 2026-09-07 server-testing intent and reported the background process exit for the ornith server. ^[raw/inb
- [[topics/self-file/wiki/entities/mltplx-server|MTPLX server]] — A local inference server observed on `127.0.0.1:11613`. On 2026-09-07 Hermes noted, "The server on 11613 is MTPLX." ^[raw/inbox/2026-09-07.md]
- [[topics/self-file/wiki/entities/ornith-server|ornith server — mlx_lm local instance]] — Local `mlx_lm` server instance serving the `ornith` model from `/tmp/mlx-lm-deepgrove`, bound to `127.0.0.1` with a contested port. Chris said at 2026-09-07 14:

## Concepts
- [[topics/self-file/wiki/concepts/local-model-serving|local model serving]] — Running LLM inference locally on Chris's machine, rather than via remote API. On 2026-09-07 Chris said, "I have good info on the current setup. Let me test both
- [[topics/self-file/wiki/concepts/server-compatibility-constraints|server compatibility constraints]] — Constraints that determine whether a local inference target can actually run on Chris's existing `mlx_lm` setup, as opposed to requiring a different server fram

## Decisions
- [[topics/self-file/wiki/decisions/colibri-ruling-2026-09-07|Colibri ruling — 2026-09-07]] — On 2026-09-07, after downloading and attempting to use Colibri, Hermes decided it was not compatible with standard `mlx_lm` and switched back to ornith. Hermes 
- [[topics/self-file/wiki/decisions/server-exploration-2026-09-07|Server exploration note — 2026-09-07]] — On 2026-09-07 Chris said he had good info on the current setup and intended to test both existing servers and explore other options. ^[raw/inbox/2026-09-07.md] 
- [[topics/self-file/wiki/decisions/token-desync-2026-09-08|Token desync — 2026-09-08 server restart]] — On 2026-09-08, after both local servers came back up, Hermes found the `/token` endpoint returning a stale value different from the newly written token file. Th

## Comparisons
- [[topics/self-file/wiki/comparisons/local-servers-2026-09-07|Local servers — 2026-09-07]] — | Server | Port evidence | Status notes | Source |

## Queries
- [[topics/self-file/wiki/queries/bonsai-mlx-viability|Bonsai MLX viability]] — After Colibri was ruled out for standard `mlx_lm`, Hermes said, "Let me start Bonsai MLX and get things working." ^[raw/inbox/2026-09-07.md] On 2026-09-08, Herm
- [[topics/self-file/wiki/queries/mlx-lm-large-prompt-kill-causes|What triggers SIGKILL in mlx_lm server during long prompt processing: cache limits, memory pressure, or timeout?]] — Chris hit a hard kill after 40k tokens on the ornith `mlx_lm` server; knowing the cause informs whether to tune cache, add swap, or switch servers.

