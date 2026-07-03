# PatchHive Fixture Map

This repo is the shared PatchHive test target. Keep the fixtures small and explicit so product behavior can be checked without touching random public repos.

## Product Recipes

### SignalHive

- Use this repo as a low-noise seed target.
- Open issues with the `bug`, `maintenance`, `release-blocker`, and `dependency` labels provide backlog and triage signals.
- The deliberately simple Python files give TODO/FIXME and recurring bug patterns room to grow.

### ReviewBee

- Use open PRs in this repo.
- Add ordinary PR comments and review comments to create actionable and resolved review-thread fixtures.
- Keep at least one quiet PR with no review activity so ReviewBee can show the `quiet` state.

### TrustGate

- Use diffs touching `fixtures/trust_gate/`.
- Safe baseline file: `fixtures/trust_gate/policy_surface.py`.
- Risky test changes should touch `admin_override`, `shell=True`, webhook validation, or token handling.

### RepoMemory

- Merge small PRs with clear review comments, then scan this repo.
- Closed issues with clear outcomes should become durable memories or early-signal prompt-pack material.

### MergeKeeper

- Use open PRs in this repo for real mergeability, review, and check-state reads.
- `patchhive-ci.yml` gives deterministic PR checks.
- Add `fixtures/checks/force_fail.txt` on a PR branch to force a failing controlled check.
- Use `require approval = false` when you need a clean ready call without asking another account to approve.

### FlakeSting

- Run the `PatchHive Flake Simulation` workflow manually several times.
- Dispatch some runs with `outcome=pass` and some with `outcome=fail`.
- FlakeSting should detect fail/pass swings on the same workflow/job/step.

### DepTriage

- Create dependency PRs that touch only dependency manifests:
  - `requirements.txt`
  - `requirements-dev.txt`
  - `package.json`
- PR titles containing `chore(deps)` or `dependabot` are intentionally easy for DepTriage to classify.

### VulnTriage

- `patchhive-codeql.yml` scans `fixtures/security/`.
- `requirements.txt` and `package.json` intentionally include old packages that may produce Dependabot alerts once GitHub security features process the repo.
- If GitHub security feeds are unavailable, the product should say that clearly instead of pretending no vulnerabilities exist.

### RefactorScout

- Scan this repo or the `fixtures/refactor/` path.
- `fixtures/refactor/oversized_module.py` contains repeated literals and a deliberately long function.

### ReleaseSentry

- Use target version `v0.1.0` or a later fixture tag.
- `CHANGELOG.md` and `fixtures/release/release_manifest.json` are release-surface files.
- Issues with label `release-blocker` create a hold decision.

### RepoReaper

- Use the existing small bug issues.
- Keep this repo disposable: draft PRs and comments can be deleted after testing.
- RepoReaper should not open a PR when an issue already has an open linked PR.

## Fixture Principles

- Prefer tiny files and obvious expected behavior.
- Use labels and titles that make product detection deterministic.
- Do not make the sandbox look like production code.
- Keep comments and PR bodies clearly attributed to PatchHive when products write to GitHub.
