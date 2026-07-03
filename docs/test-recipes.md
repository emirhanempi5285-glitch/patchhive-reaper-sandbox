# PatchHive Test Recipes

## MergeKeeper

Use any open PR in this repo. For a clean local decision, disable approval-required in the UI. For a failing check fixture, create a PR that adds `fixtures/checks/force_fail.txt`.

## FlakeSting

Run the `PatchHive Flake Simulation` workflow by hand:

```text
pass, fail, pass, fail, pass
```

Then scan `coe0718/patchhive-reaper-sandbox` with FlakeSting.

## ReleaseSentry

Use:

```text
Repo: coe0718/patchhive-reaper-sandbox
Branch: main
Target version: v0.1.0
Target tag: v0.1.0
Changelog: CHANGELOG.md
Blocker labels: release-blocker
```

Open `release-blocker` issues should create a hold call.

## DepTriage

Create dependency-only PRs touching `requirements.txt`, `requirements-dev.txt`, or `package.json`. Titles should start with `chore(deps):`.

## VulnTriage

Run after CodeQL and Dependabot have had time to process the repository. If alerts are not available, the expected result is an explicit permission or feed-availability message.
