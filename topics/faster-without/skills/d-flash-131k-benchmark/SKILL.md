---
name: d-flash-131k-benchmark
description: Use when benchmarking D-flash variants for the 27B model at 131K context.
version: 0.1.0
distilled: 2026-09-07 04:26
topic: faster-without
---
# d-flash-131k-benchmark
1. Confirm both Unleashed and Unleashed+DFlash2 servers are running at 131K context.
2. Warm up each server before measurement.
3. Run head-to-head speed test on both servers.
4. Record tok/s for 1000 tokens and note any errors.
5. Append results to topics/faster-without/log.md with timestamps.

Pitfalls: do not change server configs; if a server is unreachable, log the failure and stop.

## Evidence
> Unleashed + DFlash2 is up at 131K! Let me warm up, then test speed.
> Unleashed is up. Let me run the head-to-head comparison now.
> Good, I can see both servers are running. Let me test performance on both existing servers.
