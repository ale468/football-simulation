# Evidence guide

Evidence connects a claim to a reproducible observation. It is not a manually written assertion that a gate “passed.”

## Minimum manifest

Every material evidence record identifies:

- evidence ID;
- Issue, feature and phase;
- commit;
- date and responsible person;
- operating system, hardware and configuration;
- exact command or procedure;
- input, seed and scenario;
- raw result and artifact hashes when applicable;
- interpretation;
- limitations;
- applicable gate profile.

## Evidence types

- test report;
- replay and canonical hash;
- simulation log or telemetry export;
- benchmark;
- ABI report;
- sanitizer or static-analysis report;
- video or image for visual claims;
- comparison report;
- model or dataset evaluation in future authorized phases;
- publication manifest.

## What evidence does not prove

- A screenshot does not prove determinism.
- A video does not prove authoritative contact.
- One FPS value does not prove a performance distribution.
- A merged PR does not prove the capability works.
- A Copilot statement does not prove that a command ran.
- Shared CI timing does not establish a reference-hardware budget.

## Lifecycle

- `IMPLEMENTED`: the approved change is on `main`.
- `VERIFIED`: accepted tests and criteria pass on the integrated state.
- `DEMONSTRATED`: reproducible evidence supports the capability claim.

Evidence may be corrected by a new version; published historical evidence is not silently rewritten.
