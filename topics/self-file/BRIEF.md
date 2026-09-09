# self-file — BRIEF

## Scope
This topic tracks Chris's personal data files, local model-serving setup, and the raw→wiki compilation loop around his self-hosted inference notes.

## Anti-scope
Do not rewrite raw items, touch other topics' wikis, or silently spawn bots without a pitch.

## Lens
Treat every raw line as Chris's actual evidence; prefer contested truth over smoothed prose.

## Preferences
Keep decisions as separate pages; quote Chris verbatim when possible; do not rewrite `<!-- chris -->` lines.

## Learned
- Ornith port mapping remains contested between `11620` and `11622`; MTPLX still anchors `11613`; port churn through Colibri download and ornith restarts is now explicit in `local-servers-2026-09-07`.
- Colibri is now recorded as a separate ruling: incompatible with standard `mlx_lm`; Bonsai MLX is the next named alternative but has no viability result yet.
- A repeatable compatibility-check procedure is emerging: probe candidate backend against `mlx_lm server` endpoints before switching Hermes config.
