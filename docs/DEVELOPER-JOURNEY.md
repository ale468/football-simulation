# Developer journey

This is the expected path from discovering the project to demonstrating a capability.

## 1. Discover

Read the [project overview](PROJECT-OVERVIEW.md), [roadmap](PUBLIC-ROADMAP.md), license and governance. Confirm the current capability and active phase before proposing implementation.

## 2. Find ready work

Open the [public Project](https://github.com/users/ale468/projects/2) and use the ready-work view. A ready Issue must contain:

- a bounded problem and outcome;
- phase, scope and non-scope;
- acceptance criteria;
- gate profile;
- realism, performance and authoritative-state impact;
- expected tests, evidence and rollback.

Do not implement a planned or blocked capability merely because it is interesting.

## 3. Claim and prepare

Ask for assignment or assign yourself when permitted. Use one short branch for one principal Issue and pull request. Confirm that no unresolved architectural decision is hidden inside the task.

Recommended branch forms:

```text
feat/FNS-CORE-001-description
fix/FNS-CORE-001-description
docs/FNS-GOV-001-description
test/FNS-TEST-001-description
experiment/FNS-ML-001-description
```

## 4. Implement

Follow the Issue, repository instructions and accepted contracts. Keep authoritative state independent from presentation. Do not add future-phase dependencies or unrelated refactors.

Copilot may be assigned to a ready, bounded Issue. Its pull request receives the same CI and human review as any other contribution.

## 5. Validate locally

Run every command required by the Issue and gate profile. Report only commands that actually ran and preserve raw results when evidence is required.

Before runtime code exists, the public validation commands are:

```bash
python -B tools/repository-validation/test_validate.py
python -B tools/repository-validation/validate.py
git diff --check
```

Phase 1 build and test commands will be added by the accepted bootstrap Issue, not invented in advance.

## 6. Open the pull request

Sign every commit under DCO 1.1:

```bash
git commit --signoff -m "type: concise description"
```

Complete the PR template, link the Issue, declare the gate profile and attach reproducible evidence. A performance claim needs a reproducible benchmark; a realism claim needs an observable phenomenon, model and evidence.

## 7. Pass review and gates

CI checks machine-verifiable requirements. Copilot review is advisory. A human maintainer remains responsible for approval, exceptions and architectural interpretation.

## 8. Integrate

The normal integration method is squash merge. The branch history becomes one intentional commit on `main`, and the work branch is deleted.

Merged means `IMPLEMENTED`. It does not automatically mean `VERIFIED` or `DEMONSTRATED`.

## 9. Verify and demonstrate

Verification connects the integrated result to accepted tests and criteria. Demonstration adds reproducible evidence sufficient for the capability claim. Only then may the Project and public documentation describe the capability as demonstrated.

## Lifecycle

```text
PLANNED
→ READY
→ IN PROGRESS
→ IN REVIEW
→ IMPLEMENTED
→ VERIFIED
→ DEMONSTRATED
```

`BLOCKED` identifies a declared dependency or unresolved decision. GitHub Project metadata reflects this lifecycle but does not approve it.

## Contribution boundary

Do not submit confidential information, private planning material, credentials, personal paths or third-party content without documented redistribution rights. Public contribution must remain understandable and executable from this repository alone.
