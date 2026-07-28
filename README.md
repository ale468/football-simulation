# Football Simulation

Authoritative public source-code and contribution repository for an open-source football simulation.

[Português](docs/pt-BR/README.md) · [Project overview](docs/PROJECT-OVERVIEW.md) · [Public roadmap](docs/PUBLIC-ROADMAP.md) · [Developer journey](docs/DEVELOPER-JOURNEY.md) · [GitHub Project](https://github.com/users/ale468/projects/2)

## Status

**Phase 1 — Deterministic Contact Lab is active.**

The repository currently provides its open-source foundation, governance and validation. No game, simulation kernel, physics implementation, renderer, animation, ML model, athlete identity, asset or dataset has been published yet.

The first authorized executable is a headless deterministic Contact Lab with two simplified body proxies and one spherical ball. It will establish replay, state hashing, collision evidence and a reproducible performance baseline before graphics, animation or ML.

Start with:

- [what the project is and is not](docs/PROJECT-OVERVIEW.md);
- [how a contribution progresses](docs/DEVELOPER-JOURNEY.md);
- [which gates apply](docs/QUALITY-GATES.md);
- [how performance is measured](docs/PERFORMANCE-GATES.md);
- [what counts as evidence](docs/EVIDENCE-GUIDE.md);
- [ready public work](https://github.com/users/ale468/projects/2).

The first ready implementation Issue is [FNS-CORE-001 — Bootstrap the deterministic headless kernel state](https://github.com/ale468/football-simulation/issues/3).

## Engineering direction

Realism and performance guide decisions:

1. authoritative-state correctness;
2. reproducibility and explainability;
3. observable physical coherence;
4. measured latency and throughput;
5. biomechanical plausibility;
6. visual fidelity.

A lower layer may not falsify a higher layer. Rendering, animation and ML never decide authoritative contact, possession, ball trajectory, rules or competitive results.

## Developer lifecycle

```text
PLANNED → READY → IN PROGRESS → IN REVIEW
→ IMPLEMENTED → VERIFIED → DEMONSTRATED
```

Issues define bounded work. PRs present changes and evidence. CI applies machine-verifiable gates. Copilot may assist implementation and review, but human maintainers accept decisions and promotion. A merged PR is not automatically a demonstrated capability.

## License

Source code and documentation in this repository are licensed under the [GNU Affero General Public License v3.0 only](LICENSE), SPDX identifier `AGPL-3.0-only`, unless a file explicitly states otherwise.

The license permits use, study, modification and redistribution under its terms. Modified versions made available to users over a network must offer corresponding source as required by the AGPL.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), the [public contribution contract](docs/governance/PUBLIC-CONTRIBUTION-CONTRACT.md), the [Realism–Performance contract](docs/governance/REALISM-PERFORMANCE-CONTRACT.md), the [Code of Conduct](CODE_OF_CONDUCT.md) and [SECURITY.md](SECURITY.md).

Every code commit requires a DCO 1.1 signoff. External assets, datasets, identities, brands, trained models and model weights are not currently accepted.
