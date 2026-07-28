# Project overview

## North Star

Football Simulation aims to become an authoritative 11v11 football simulation that can eventually support broadcast-level visual realism without allowing rendering, animation or machine learning to decide competitive truth.

Realism and performance guide technical decisions:

- authoritative correctness comes before appearance;
- physical and biomechanical claims require observable evidence;
- optimization requires a reproducible baseline;
- visual systems may represent authoritative state but may not contradict it.

## Current capability

Phase 1 — Deterministic Contact Lab is active.

The repository currently contains the public open-source foundation, contribution rules and repository validation. It does not yet contain a game, simulation kernel, physics implementation, renderer, animation, machine-learning model, athlete identity, asset or dataset.

The first executable objective is deliberately small:

```text
two simplified body proxies
+ one spherical ball
+ explicit authoritative state
+ fixed-step deterministic execution
+ replay and state hashing
+ reproducible tests and performance baseline
```

The first ready implementation unit is [FNS-CORE-001](https://github.com/ale468/football-simulation/issues/3).

## Architecture in plain language

The kernel owns the truth:

- positions and velocities;
- contacts and impulses;
- ball trajectory;
- controlled time and randomness;
- replayable state.

Future clients, engines, renderers, animation and ML consume that truth through explicit boundaries. They do not become its owner.

## Phase 1 limits

Allowed:

- C++20, CMake and Ninja;
- a headless library and tests;
- explicit world, two-body and ball state;
- fixed tick, seed, replay and canonical hash;
- minimal rigid-body contact and ball collision;
- a small stable C ABI;
- telemetry and a reproducible benchmark.

Not allowed yet:

- graphics, animation, audio, user interface or game engine integration;
- tactical AI, networking, full officiating or 22 players;
- neural rendering, ML, real athletes, external assets or datasets;
- an arbitrary absolute performance budget before the first baseline.

## Where to go next

- [Public roadmap](PUBLIC-ROADMAP.md)
- [Developer journey](DEVELOPER-JOURNEY.md)
- [Quality gates](QUALITY-GATES.md)
- [Performance gates](PERFORMANCE-GATES.md)
- [Evidence guide](EVIDENCE-GUIDE.md)
- [Public GitHub Project](https://github.com/users/ale468/projects/2)
- [Português](pt-BR/README.md)
