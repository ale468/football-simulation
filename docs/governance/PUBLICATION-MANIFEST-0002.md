# Publication manifest 0002 — Public developer journey

- Public issue: [#4](https://github.com/ale468/football-simulation/issues/4)
- Public pull request: [#6](https://github.com/ale468/football-simulation/pull/6)
- Base commit: `3635a029c77082454df6f37d56f4f3b58f8b530a`
- Source category: newly authored public documentation, templates, agent instructions and validation
- Runtime impact: none
- Initial branch commit: `50384d0d8015d87f5b6657b5ed8d73c25be566e8`

## Purpose

Provide an independent English and Portuguese developer journey from project discovery to demonstrated capability. Define quality, realism, performance and evidence gates without publishing runtime code or confidential planning material.

## Allowlist

- `README.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `GOVERNANCE.md`
- `.github/copilot-instructions.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/**`
- `docs/PROJECT-OVERVIEW.md`
- `docs/DEVELOPER-JOURNEY.md`
- `docs/QUALITY-GATES.md`
- `docs/PERFORMANCE-GATES.md`
- `docs/EVIDENCE-GUIDE.md`
- `docs/PUBLIC-ROADMAP.md`
- `docs/pt-BR/**`
- `docs/governance/PUBLICATION-MANIFEST-0002.md`
- `tools/repository-validation/**`

## Required checks

- repository validator tests;
- public repository validation;
- Markdown relative-link validation;
- DCO signoff for every PR commit;
- private-boundary and personal-path scan;
- no unsupported capability, benchmark or performance-budget claim;
- no runtime, physics, rendering, ML, asset or dataset implementation.

## Independence and rights

This batch is written for public use under the repository's `AGPL-3.0-only` terms. It contains no private prompts, internal evidence, confidential deliberations, credentials, personal paths or externally licensed assets. Public contributors can understand and use it without access to any private planning system.

## Known limitations

- GitHub Project view and workflow configuration may require GitHub UI operations where no supported API exists.
- Absolute performance gating remains manual until the first reproducible reference-hardware baseline and an accepted automation strategy exist.
- Documentation defines future runtime gates but does not claim those checks already execute.

## Rollback

Revert the public pull request. Project metadata can be corrected independently without changing runtime because this batch introduces no runtime content.
