# Security Policy

## Scope

This repository hosts a **static GitHub Pages site** (HTML + PNG assets).
There is no server-side code, no user authentication, and no data storage.

| In scope | Out of scope |
|----------|--------------|
| Content injection / XSS in the served HTML | Infrastructure outside this repo |
| Malicious workflow / supply-chain changes to `.github/` | Third-party CDNs or external links |
| Sensitive data accidentally committed | GitHub Pages platform itself |

---

## Supported versions

Only the content currently deployed from the `main` branch is supported.

---

## Reporting a vulnerability

**Please do not open a public GitHub issue for security vulnerabilities.**

To report a security concern:

1. Navigate to the **[Security tab → Report a vulnerability](https://github.com/wizardaax/wizardaax.github.io/security/advisories/new)** (GitHub private advisory).
2. Provide a clear description of the issue, steps to reproduce, and potential impact.
3. You will receive an acknowledgement within **5 business days**.

Alternatively, you can reach the maintainer via the contact information on the GitHub profile: [https://github.com/wizardaax](https://github.com/wizardaax).

---

## Response process

| Step | Target timeline |
|------|----------------|
| Acknowledgement | 5 business days |
| Initial assessment | 10 business days |
| Fix or public disclosure decision | 30 business days |

---

## Security controls

- **Automated security scanning** runs on every push and pull request via `.github/workflows/aeon-security.yml` (aeon-standards@v1).
- **HTML validation** runs on every push via `.github/workflows/pages-sanity.yml`.
- Branch protection requires passing security checks before merging to `main`.
