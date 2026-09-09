---
title: "mtplx-qwen38-27b endpoint"
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [model, tool]
sources: [raw/inbox/2026-09-07.md]
confidence: 0.7
---

# mtplx-qwen38-27b endpoint

A local model serving endpoint observed responding to health-check pings at `http://127.0.0.1:11613/v1/models` on 2026-09-07.

## Health check observations
Two background processes pinged the endpoint at 00:57 with sim scores 0.06 and 0.91:[^[raw/inbox/2026-09-07.md]]
```bash
sleep 120; curl -s -m 5 http://127.0.0.1:11613/v1/models 2>/dev/null | head -c 100 || echo "down"
```
Both returned the same response (truncated at 100 bytes):
```json
{"object":"list","data":[{"id":"mtplx-qwen38-27b-optimized-speed","object":"model","created":1788752
```

## Model ID
`mtplx-qwen38-27b-optimized-speed`

## Endpoint
`http://127.0.0.1:11613/v1/models`

## Second observed endpoint

^[raw/inbox/2026-09-07.md] At 10:42, a background process pinged `http://127.0.0.1:11622/v1/models` after a 180-second sleep. Output was empty/`down`-equivalent, so this may be another local model-serving target rather than a confirmed healthy endpoint.

## Related
- [[wiki/entities/ornith-mlx4b-artifacts|Ornith MLX-4B artifacts]]
- [[wiki/entities/ornith-dflash2-artifacts|Ornith DFlash2 artifacts]]
- [[wiki/concepts/watcher-status-noise|Watcher status noise]]
