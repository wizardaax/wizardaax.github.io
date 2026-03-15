# wizardaax.github.io

Personal GitHub Pages site — **Recursive Field Framework** visualisation hub.

## Purpose

This site presents simulation outputs and research artefacts from the Recursive Field Framework project, including:

- Riemann spiral fields
- Recursive field mathematics
- Codex entropy pump diagrams
- Snell–Vern drive matrix renders
- Glyph phase engine outputs
- SCE-88 architecture diagrams

Live at: **[https://wizardaax.github.io](https://wizardaax.github.io)**

---

## Deploy model

Deployment is handled automatically by **GitHub Pages** on every push to `main`.

| Branch | Environment | URL |
|--------|-------------|-----|
| `main` | Production | https://wizardaax.github.io |

No build step is required — the site is pure static HTML served directly by GitHub Pages.

---

## Local preview

Clone the repo and open the site in a browser:

```bash
git clone https://github.com/wizardaax/wizardaax.github.io.git
cd wizardaax.github.io

# Option 1 – Python (no install required)
python3 -m http.server 8080
# → open http://localhost:8080

# Option 2 – Node.js (npx, no global install required)
npx serve .
# → open the URL shown in terminal
```

---

## Repository layout

```
.
├── index.html            # Main page
├── sim_outputs/          # Simulation output images (PNG)
├── docs/
│   └── ENGINEERING_STANDARDS.md
├── .github/
│   └── workflows/
│       ├── aeon-security.yml   # Shared security scan
│       └── pages-sanity.yml    # HTML link / validation check
├── README.md
└── SECURITY.md
```

---

## Governance

Security and CI policies follow the **aeon-standards v1** light governance profile.
See [`docs/ENGINEERING_STANDARDS.md`](docs/ENGINEERING_STANDARDS.md) and [`SECURITY.md`](SECURITY.md).
