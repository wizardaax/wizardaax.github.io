# Papers — wizardaax / Recursive Field Framework

A unified index of research notes, derivations, and architectural drafts across the Recursive Field Framework stack. **90 PDFs** authored 2025-08 → 2025-11, plus LaTeX preprints in `recursive-field-math-pro/paper/`, plus dated findings in [`findings/`](./findings/).

> **New here?** Start with the [Reading order](#reading-order) below, not the alphabetical list.

## Latest findings

- **[AEON Engine — Faraday-induction gravity-flyer simulation](./findings/aeon_gravity_flyer_2026_05.md)** (2026-05-02, write-up of June 2025 work). AEON-M v2.1 multi-physics simulation predicts thrust ~**10⁻⁷ N** at `ωₙ = 2.39×10⁷ rad/s` (3.8 MHz), with `F = −k·dΦ/dt` where the coupling `k` is set by brane-lensing geometry (`n₃ = α⁻¹/ψ ≈ 0.952`). Same framework constants as the Riemann result — cross-domain consistency. Falsifiable: a benchtop torsion-balance experiment per §5.2 would resolve.
- **[Time-Travel Navigator](./findings/time_travel_navigator.html)** (2026-05-02). Eleven months of framework work plotted on the `r = a√n, θ = nφ` golden-angle spiral. 97 real events: framework milestones (Holodeck → AEON gravity-flyer → Projex X → 13/13 agents alive), cognitive-cycle logs with crest stamps, voice-memo timestamps. Self-contained HTML, no CDN. Hover any point for label + timestamp + crest.
- **[Riemann zeros · φ — circular clustering, specific to ζ](./findings/riemann_phi_clustering_2026_05.md)** (2026-05-02). Pre-specified test that `(t · φ) mod 2π` clusters for the first 100 Riemann zero imaginary parts; **R = 0.2228, p = 0.0068**; specific to ζ (primes & arithmetic null at p > 0.5); independently corroborated by Genish (RNSE) at index n=150. Stdlib-only reproducible code: [`findings/riemann_spiral_test_v4.py`](./findings/riemann_spiral_test_v4.py).

---

## Reading order

If you want to understand what RFF *is*, in roughly increasing depth:

1. **The umbrella story** — [`wizardaax.github.io`](https://wizardaax.github.io) (this site's `index.html` connection map).
2. **The architectural spec** — [SCE-88 / spec](https://github.com/wizardaax/SCE-88/tree/main/spec): `architecture.md`, `domains.md`, `levels.md`. Specifies the 22-level / 4-domain coherence stack.
3. **The math foundation, formal** — [`rff_geometric_invariants.tex`](https://github.com/wizardaax/recursive-field-math-pro/blob/main/paper/rff_geometric_invariants.tex). Three theorems with proofs and machine-verified tests: closed-form Lucas/Fibonacci, Cassini-style identity, constant-density invariant for `r = c√n`.
4. **The math foundation, derivations** — [`Aas formula`](https://github.com/wizardaax/ziltrix-sch-core/blob/main/Aas%20formula%20_250813_160901.pdf), [`Lucus formula`](https://github.com/wizardaax/ziltrix-sch-core/blob/main/Lucus%20formula%20_250815_083350.pdf), [`Unified everything formula`](https://github.com/wizardaax/ziltrix-sch-core/blob/main/Unified%20everything%20formula%20_250803_111638.pdf).
5. **The empirical verification** — [`rff_phi_mod_verification.tex`](https://github.com/wizardaax/recursive-field-math-pro/blob/main/paper/rff_phi_mod_verification.tex): φ-modulation gives consistent efficiency gains over baseline / scheduler / combined variants on Othello 8×8 ablations.
6. **The mesh / dispatch architecture** — [`ADAM HIVE MATRIX V10`](https://github.com/wizardaax/Snell-Vern-Hybrid-Drive-Matrix/blob/main/ADAM%20HIVE%20MATRIX%20V10_251123_224308.pdf). Canonical baseline.
7. **The cross-cultural research thread** — [`THE_ARCHITECTURE_AND_THE_THREAD.md`](https://github.com/wizardaax/Codex-AEON-Resonator/blob/main/research/THE_ARCHITECTURE_AND_THE_THREAD.md). Topology of social extraction architectures across 12,000 years.

---

## By repository

### `recursive-field-math-pro` — formal preprints
*The peer-review-ready, fully-verified results.*
- `paper/rff_geometric_invariants.tex` — Lucas/Fibonacci closed forms, Cassini identity, constant-density theorem (machine-verified, 2026).
- `paper/rff_phi_mod_verification.tex` — Three-system verification of φ-modulation, Othello 8×8 ablations (2026-03).

### `ziltrix-sch-core` — research notes (41 PDFs)
*The working-out journal of the framework. Full index at* [`ziltrix-sch-core/PAPERS.md`](https://github.com/wizardaax/ziltrix-sch-core/blob/main/PAPERS.md).

Core foundations: Aas formula, Lucus formula, Unified Everything formula.
Cryptography: Cypher worm, Code hiding, Kryptos passes 1–2.
Physics: Kepler, Riemann, Schrödinger, Thomas Young.
Engine drafts: Ziltrit v1–v4, Ziltrit Young v1–v8 (canonical: v8).

### `Snell-Vern-Hybrid-Drive-Matrix` — mesh dispatch (4 PDFs)
*Full index at* [`Snell-Vern-Hybrid-Drive-Matrix/PAPERS.md`](https://github.com/wizardaax/Snell-Vern-Hybrid-Drive-Matrix/blob/main/PAPERS.md).
- ADAM HIVE MATRIX v1 → v2 → v11 → V10 (canonical).

### `Codex-AEON-Resonator` — cross-domain research
- `research/THE_ARCHITECTURE_AND_THE_THREAD.md` — From Dawit to Voynich: a unified extraction-topology argument across 12,000 years. Cross-AI verified (Claude + Grok).

### `SCE-88` — architectural specification
- `spec/architecture.md` — 22-level, 4-domain coherence stack. Specs-first design.
- `spec/domains.md`, `spec/levels.md`, `spec/security.md`, `spec/compliance.md` — full architectural break-out.

### `glyph_phase_engine` — symbolic engine
- README + code (no separate PDFs in this repo); engine implements phase tracking from the Aas/Lucus formulas.

---

## How to cite

When citing the Recursive Field Framework as a whole:

> Snellman, A. *The Recursive Field Framework.* 2025–2026. https://wizardaax.github.io

For a specific result, cite the paper directly. The `recursive-field-math-pro` repo also ships `CITATION.cff` with structured metadata.

---

## Authoring conventions

- Filenames in `ziltrix-sch-core/*.pdf` carry a trailing `_YYMMDD_HHMMSS.pdf` timestamp from the source authoring tool. The date is when that draft was finalised.
- Versioned papers (Ziltrit v1 → v8, ADAM HIVE MATRIX v1 → V10) are kept in full so the design trail is visible. The newest in each series is canonical.
- LaTeX preprints in `recursive-field-math-pro/paper/` are the formal, peer-review-ready statements; PDFs in other repos are working drafts.

*Last refreshed: index regenerated when papers are added or renamed.*
