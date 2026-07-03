# Security Fixtures

This directory intentionally contains unsafe patterns for PatchHive security testing.

Expected products:

- VulnTriage should rank GitHub code scanning or dependency alerts when GitHub exposes them.
- TrustGate should treat diffs that expand this surface as risky.
- RepoReaper should avoid drive-by changes here unless the issue is narrow and clearly scoped.
