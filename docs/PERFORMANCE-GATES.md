# Performance gates

Performance is an architectural requirement, but a number without a reproducible environment is not a reliable gate.

## Current policy

The first reproducible Phase 1 benchmark establishes the baseline. No arbitrary absolute tick, latency, memory or throughput budget is claimed before that evidence exists.

The owner's reference computer is the initial reference-hardware surface. Shared GitHub-hosted runners prove build and correctness and may detect gross regressions; their variable workload does not define an absolute performance budget.

## Required benchmark record

Every accepted performance result records:

- commit and source tree state;
- compiler, version, flags and build profile;
- operating system and hardware;
- scenario, tick rate, seed and input;
- warm-up, repetitions and duration;
- median, p95 and p99;
- throughput;
- memory and allocation counts;
- dispersion and known noise;
- raw result location;
- interpretation, limitation and rollback.

## Gate levels

### Shared CI

Suitable for:

- build and functional correctness;
- benchmark smoke execution;
- format and output-schema validation;
- obvious order-of-magnitude regression detection.

Not suitable for:

- small absolute latency comparisons;
- reference-hardware budgets;
- unsupported “faster” claims from one run.

### Reference hardware

Suitable for:

- establishing and updating the approved baseline;
- evaluating material regression or improvement;
- setting future absolute budgets through an accepted decision;
- comparing data layout, solver or compiler changes.

Until a dedicated reference runner is automated, the reference-hardware gate is recorded evidence reviewed by a human.

## Performance change contract

A performance Issue and PR must state:

1. observed bottleneck and profile;
2. reproducible baseline;
3. proposed causal mechanism;
4. authoritative, determinism and realism invariants;
5. expected CPU, memory, allocation and latency impact;
6. acceptance threshold derived from evidence;
7. rollback or fallback.

An optimization that falsifies authoritative state, physical invariants or deterministic replay fails even when it is faster.
