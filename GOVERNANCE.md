# Governance

- This public repository is authoritative for publicly released source code and its public documentation.
- The public GitHub Project is an operational roadmap. It does not approve architecture, evidence, capability or phase transitions.
- Changes use issues, short branches and pull requests. Direct pushes to `main` are prohibited.
- Architectural changes require a public rationale and reviewable acceptance criteria.
- Phase transitions require explicit maintainer approval and recorded evidence.
- Public code must remain buildable, testable and modifiable without access to private planning material.
- Only material intentionally reviewed for publication may enter this repository.
- Maintainers may reject changes that disclose confidential information, lack provenance or conflict with the active project phase.
- Pull requests require passing CI, one approval, CODEOWNER review and resolved conversations.
- Squash merge is the only normal merge method; the source branch is deleted after integration.
- `@ale468` is the initial CODEOWNER and maintainer.

## Delivery semantics

The public lifecycle is:

`PLANNED → READY → IN PROGRESS → IN REVIEW → IMPLEMENTED → VERIFIED → DEMONSTRATED`

Squash merge establishes `IMPLEMENTED`. Verification and demonstration require their applicable tests and reproducible evidence. Automatic Issue or Project transitions may reflect progress but do not replace maintainer acceptance.

Copilot and other coding agents are assistants. Their implementation and review output is subject to the same gates and human approval as human-authored work.

An administrative bypass is permitted only to restore security, availability or repository integrity. It requires a retrospective issue documenting cause, diff, validation, rollback and prevention. Convenience or lack of a reviewer is not an emergency.

Release signing and maintainer succession will be documented before the first software release.
