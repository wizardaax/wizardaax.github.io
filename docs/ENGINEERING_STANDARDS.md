# Engineering Standards

This document defines the engineering standards for `wizardaax/wizardaax.github.io`.

## Governance profile: **Light**

This is a personal static-site repository. Full heavy-CI pipelines (e.g. Python test suites, Docker builds) are out of scope unless the codebase changes materially.

---

## Applicable standard

| Standard | Version | Profile |
|----------|---------|---------|
| [aeon-standards](https://github.com/wizardaax/aeon-standards) | `v1` | `light` |

aeon-standards governs:
- Security scanning (secret detection, dependency auditing)
- HTML/asset validation for GitHub Pages sites
- Branch protection rules
- Pull-request workflow conventions

---

## Required CI checks

Every pull request targeting `main` must pass:

| Check name | Workflow file | Purpose |
|-----------|--------------|---------|
| `Security / Security Scan (shared)` | `.github/workflows/aeon-security.yml` | Secret scan + shared security rules via aeon-standards@v1 |
| `Pages Sanity / validate` | `.github/workflows/pages-sanity.yml` | HTML validation + broken internal-link check |

Python CI (`aeon-python-ci.yml`) is dormant and only activates when `.py` source files are present.

---

## Branch protection (light mode)

`main` branch settings (auto-enforced by `.github/workflows/branch-protection.yml`):
- **Require a pull request before merging**
- **Required approvals:** 1
- **Required status checks:**
  - `Security / Security Scan (shared)`
  - `Pages Sanity / validate`
- **Dismiss stale reviews on new push:** yes
- **Allow force pushes:** no
- **Allow deletions:** no

> **Note:** Auto-enforcement requires a repository secret named `BRANCH_PROTECTION_TOKEN`
> containing a fine-grained PAT (or classic PAT with `repo` scope).
> `GITHUB_TOKEN` cannot modify branch protection rules.

---

## Technology stack

| Layer | Technology |
|-------|-----------|
| Frontend | Static HTML5 + CSS (no framework, no build step) |
| Assets | PNG simulation outputs in `sim_outputs/` |
| Hosting | GitHub Pages (branch: `main`, root: `/`) |
| CI/CD | GitHub Actions |

---

## Adding Python scripts

If Python simulation scripts are added to this repository in the future, `.github/workflows/aeon-python-ci.yml` activates automatically (it is path-filtered to trigger only on `.py` and Python project config files).

---

## Dependency management

This site has **no runtime dependencies** (no `package.json`, no `requirements.txt`).

CI tooling dependencies (e.g. `html5validator`) are pinned in the workflow files and installed ephemerally during workflow runs.

---

## AI agent instructions

Autonomous AI coding agents (GitHub Copilot, Copilot Workspace, or compatible
systems) operating on this repository follow the **AEON Engineering App**
protocol defined in [`.github/copilot-instructions.md`](../.github/copilot-instructions.md).

Key protocol requirements:
- Every task follows a **PLAN → EXECUTE → VERIFY → REPORT** cycle.
- Reports must include exact files modified, PR links, and CI check results.
- Destructive or high-risk actions require explicit human approval before
  proceeding.
- Tool names are never hardcoded; the agent adapts to available tools.

---

## File organisation

```
.
├── index.html                          # Entry point served by GitHub Pages
├── sim_outputs/                        # Simulation output images (PNG)
├── docs/
│   ├── ENGINEERING_STANDARDS.md       # This file
│   └── HEALTH_DASHBOARD.md             # Live CI / governance status
├── .github/
│   ├── copilot-instructions.md         # AEON Engineering App orchestrator prompt
│   └── workflows/
│       ├── aeon-security.yml           # aeon-standards@v1 security scan
│       ├── aeon-python-ci.yml          # aeon-standards@v1 Python CI (dormant)
│       ├── branch-protection.yml       # auto-enforce branch protection
│       └── pages-sanity.yml            # HTML validation + link check
├── README.md
└── SECURITY.md
```

---

## Change process

1. Open a pull request against `main`.
2. Ensure all required CI checks pass.
3. Obtain at least 1 approval.
4. Squash-merge or rebase-merge.

For security issues, follow the process in [`../SECURITY.md`](../SECURITY.md).
