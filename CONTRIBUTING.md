# Contributing

Thank you for helping improve Football Simulation.

Start with the [project overview](docs/PROJECT-OVERVIEW.md), [developer journey](docs/DEVELOPER-JOURNEY.md) and [ready work in the public Project](https://github.com/users/ale468/projects/2). Portuguese guidance starts at [docs/pt-BR/README.md](docs/pt-BR/README.md).

## Workflow

1. Choose a `READY` Issue or open a proposal with problem, scope and expected evidence.
2. Confirm the active phase, gate profile and non-scope.
3. Create a short branch for that Issue.
4. Keep changes small and reviewable.
5. Add tests and reproducible evidence appropriate to the change.
6. Sign every commit with `git commit --signoff`.
7. Submit a pull request against `main`.
8. Address CI, human review and open conversations.
9. Do not claim `VERIFIED` or `DEMONSTRATED` merely because the PR merged.

Access to private planning material is not required to contribute. Do not submit confidential information, private prompts, credentials, personal data or material you are not entitled to license.

## Licensing contributions

Every code contribution intentionally submitted for inclusion is offered under `AGPL-3.0-only`, the same license used by this repository. Contributors retain their copyright and certify their right to submit through the [Developer Certificate of Origin 1.1](DCO).

The AGPL permits legitimate copies, modifications and forks when its conditions are followed. It does not grant rights in project names, logos, third-party assets or trademarks.

External assets, datasets, identities, brands, trained models and model weights are temporarily not accepted. Read the [public contribution contract](docs/governance/PUBLIC-CONTRIBUTION-CONTRACT.md).

## Realism and performance

Correct authoritative state takes priority over visual plausibility. Performance claims require a reproducible baseline and distribution, not a single FPS number. Read the [Realism–Performance contract](docs/governance/REALISM-PERFORMANCE-CONTRACT.md).

Every change declares its applicable [quality gate profile](docs/QUALITY-GATES.md). Performance work also follows [PERFORMANCE-GATES.md](docs/PERFORMANCE-GATES.md), and capability claims follow the [evidence guide](docs/EVIDENCE-GUIDE.md).

## Copilot and coding agents

Copilot may be assigned to a bounded `READY` Issue when its acceptance criteria, commands and non-scope are sufficient. Agent-generated pull requests receive the same CI and human review as any other contribution. Copilot does not approve its own work, accept architecture or promote phases.
