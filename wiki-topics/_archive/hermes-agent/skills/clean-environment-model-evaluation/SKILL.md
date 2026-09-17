---
name: clean-environment-model-evaluation
description: Use when evaluating a model in a live Hermes session. Behavior: enforce a clean test environment, use streamed tok/s measurement, verify active provider health before diagnosing failures.
version: 0.1.0
distilled: 2026-09-07 05:58
topic: hermes-agent
---
# clean-environment-model-evaluation
## Clean-environment evaluation protocol

1. Before any model evaluation run, remove Maple and delete any uncensored model variants; Chris treats this as mandatory, not optional.
2. Verify the active provider/server pid is healthy before treating an OOM or failure as a model or hardware issue; stale wrong-flag processes can misdiagnose the host.
3. Measure tok/s with streamed metrics that separate prompt processing time from generation time; raw non-streamed numbers are not accurate for comparison.
4. Use a realistic compression workload such as big-essay summarization as the benchmark.
5. Capture the session id and explicit similarity delta when the user checks whether the model works.
6. On M1 32GB hosts, treat 65K context as the stable operating point for 27B-class models; 131K OOMs at 10K+ prompts.

## Evidence
> Chris: 'I would really rather you be testing this 27B with as clean of a hard drive as you can... in fact delete that if it's still here I don't want to confused.'
> Hermes: 'The failed process was just a stale attempt with the wrong flag — the active server (pid 60316) is up and has been running for 33+ minutes.'
> Hermes: 'I need to improve the script with streaming to separate prompt processing from generation time for accurate tok/s.'
