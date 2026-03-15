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

---

## Branch protection (light mode)

`main` branch settings:
- **Require a pull request before merging**
- **Required approvals:** 1
- **Required status checks:**
  - `Security / Security Scan (shared)`
  - `Pages Sanity / validate`
- **Dismiss stale reviews on new push:** recommended

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

If Python simulation scripts are added to this repository in the future, enable `.github/workflows/aeon-python-ci.yml` following the aeon-standards@v1 Python CI template.

---

## Dependency management

This site has **no runtime dependencies** (no `package.json`, no `requirements.txt`).

CI tooling dependencies (e.g. `html5validator`) are pinned in the workflow files and installed ephemerally during workflow runs.

---

## File organisation

```
.
├── index.html                     # Entry point served by GitHub Pages
├── sim_outputs/                   # Simulation output images (PNG)
├── docs/
│   └── ENGINEERING_STANDARDS.md  # This file
├── .github/
│   └── workflows/
│       ├── aeon-security.yml      # aeon-standards@v1 security scan
│       └── pages-sanity.yml       # HTML validation + link check
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
