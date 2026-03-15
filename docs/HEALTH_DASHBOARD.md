# Health Dashboard

Live status for `wizardaax/wizardaax.github.io`.

## CI checks

| Check | Workflow | Status |
|-------|----------|--------|
| Security Scan | `aeon-security.yml` | [![Security](https://github.com/wizardaax/wizardaax.github.io/actions/workflows/aeon-security.yml/badge.svg)](https://github.com/wizardaax/wizardaax.github.io/actions/workflows/aeon-security.yml) |
| Pages Sanity | `pages-sanity.yml` | [![Pages Sanity](https://github.com/wizardaax/wizardaax.github.io/actions/workflows/pages-sanity.yml/badge.svg)](https://github.com/wizardaax/wizardaax.github.io/actions/workflows/pages-sanity.yml) |
| Python CI | `aeon-python-ci.yml` | dormant – activates when `.py` files are added |

## Governance

| Item | Status |
|------|--------|
| Standard | [aeon-standards](https://github.com/wizardaax/aeon-standards) `v1` |
| Profile | `light` |
| Branch protection | auto-enforced via `branch-protection.yml` (requires `BRANCH_PROTECTION_TOKEN` secret) |
| Required approvals | 1 |

## Branch protection (main)

| Rule | Setting |
|------|---------|
| Required status checks | `Security / Security Scan (shared)`, `Pages Sanity / validate` |
| Require PR before merging | ✓ |
| Required approvals | 1 |
| Dismiss stale reviews | ✓ |
| Allow force pushes | ✗ |
| Allow deletions | ✗ |

## AI agent protocol

| Item | Status |
|------|--------|
| AEON Engineering App | active — see [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) |
| Execution cycle | PLAN → EXECUTE → VERIFY → REPORT |
| Hardcoded tool names | ✗ (adapts to available tools) |
| Stop conditions | ✓ (destructive / high-risk actions require approval) |
| Artifact reporting | ✓ (files, PRs, check results required in every report) |

See [`ENGINEERING_STANDARDS.md`](ENGINEERING_STANDARDS.md) for the full policy.
