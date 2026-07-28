# GitHub Copilot repository instructions

## Project context

Football Simulation is building an authoritative, deterministic and performance-oriented football simulation. Phase 1 is a headless Contact Lab with two simplified body proxies and one ball. The repository does not yet contain runtime implementation.

Read:

1. `docs/PROJECT-OVERVIEW.md`
2. `docs/PUBLIC-ROADMAP.md`
3. `docs/DEVELOPER-JOURNEY.md`
4. `docs/QUALITY-GATES.md`
5. the related public Issue

## Non-negotiable architecture

- The kernel owns canonical competitive state.
- Rendering, animation, engines and ML may consume or represent state but do not decide contact, possession, ball trajectory, rules or results.
- Time, input and randomness are explicit and controlled.
- Public interoperability uses a small stable C ABI.
- Optimization requires a reproducible baseline.
- Shared CI timing is not an absolute reference-hardware budget.
- Future-phase capability is prohibited unless the active public contract authorizes it.

## Work protocol

- Work only from a `READY`, bounded Issue with acceptance criteria.
- Keep one Issue, one short branch and one principal PR.
- State what changed and what did not change.
- Identify the applicable gate profile.
- Add or update tests required by the Issue.
- Run commands before reporting their results.
- Never fabricate benchmarks, evidence or capability claims.
- Preserve DCO signoff, licensing and public/private boundaries.
- Do not add assets, datasets, identities, brands, trained models or weights.

## Review and completion

- Copilot output requires the same CI and human review as human output.
- Copilot review is advisory and does not approve architecture or promotion.
- Merge means `IMPLEMENTED`; it does not automatically mean `VERIFIED` or `DEMONSTRATED`.
- Report residual risks, limitations and rollback.
