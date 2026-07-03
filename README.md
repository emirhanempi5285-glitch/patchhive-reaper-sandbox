# PatchHive Test Sandbox

This repository is intentionally small, controlled, and slightly broken.

It exists so PatchHive products can safely test:

- GitHub issue and PR discovery
- MergeKeeper readiness decisions
- ReviewBee review/comment ingestion
- TrustGate diff risk checks
- RepoMemory prompt packs and durable history
- FlakeSting workflow history scans
- DepTriage dependency PR ranking
- VulnTriage security-feed handling
- RefactorScout local and GitHub repo scans
- ReleaseSentry release readiness checks
- managed issue comments
- held/no-patch explanations
- draft pull request creation
- PatchHive attribution

The code is deliberately simple Python so automated patches are easy to inspect.

See [PATCHHIVE_FIXTURES.md](PATCHHIVE_FIXTURES.md) for the fixture map and suggested test recipes.
