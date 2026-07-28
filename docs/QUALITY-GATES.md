# Quality gates

A gate is evidence that a change satisfies a protected contract. Gate profiles are change-sensitive: every contribution receives the smallest sufficient profile, and touching another protected surface adds that surface's profile.

## Gate profiles

| Profile | Applies when | Required proof |
|---|---|---|
| `DOCS` | Documentation, governance or templates change | links, traceability, status, public-boundary scan and honest capability language |
| `KERNEL` | Authoritative runtime code changes | builds, tests, warnings policy, state invariants and production/instrumentation separation |
| `DETERMINISM` | Time, randomness, state or simulation order changes | controlled seed, replay and identical accepted hashes |
| `ABI` | Public C ABI changes | exported surface, ownership, versioning and compatibility evidence |
| `COLLISION_REALISM` | Contact, bodies or ball behavior changes | scenario invariants, no accepted tunneling or ghost contact, declared approximations |
| `PERFORMANCE` | Cost, layout, allocation or optimization changes | reproducible baseline, distribution, environment and rollback |
| `ML_FUTURE` | ML is authorized in a future phase | lineage, latency, constraints, temporal/OOD evaluation and classical fallback |
| `PUBLICATION` | New public material or dependency enters | rights, provenance, secret/private-reference scan and independent usability |

## Gates that apply to every pull request

- related public Issue and active phase;
- scoped change and declared non-scope;
- DCO signoff;
- repository validation;
- applicable tests;
- no unsupported capability or performance claim;
- no confidential or prohibited material;
- human approval under repository governance.

## Phase 1 technical gates

Once runtime code is introduced by an accepted Issue, Phase 1 requires:

- MSVC build and Linux/Clang correction build;
- unit and scenario tests;
- repeated replay with identical final hash under the accepted determinism scope;
- zero dynamic allocation during the simulation tick;
- no ghost contact or ball tunneling in accepted scenarios;
- production and diagnostic targets separated;
- benchmark metadata sufficient to reproduce the initial baseline.

The concrete commands belong to the implementation specification and CI added with the first code. This document does not pretend those checks already exist.

## Realism gate

In Phase 1, realism means authoritative and physical coherence, not photorealistic output. A change states:

- the observable phenomenon;
- the declared model and approximation;
- the causal result expected;
- invariants that may not regress;
- the test scenario and evidence.

Biomechanical and visual realism gates activate only in their authorized phases.

## Human acceptance

CI can reject a change, but it does not accept architecture or promote a phase. Copilot may report findings but does not satisfy required human approval. A maintainer records exceptions and promotion decisions.
