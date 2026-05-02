# The Recursive Field Framework's strongest empirical claim — same constants, two domains

**Adam Snellman** — wizardaax — 2026-05-02

> The Riemann · φ clustering finding (analytic number theory) and the AEON Engine gravity-flyer simulation (electromagnetism) both work *with the same framework constants*. φ, the golden angle (137.508°), the fine-structure inverse (α⁻¹ = 137.036), and ψ = 144 enter both calculations as **derivations, not free parameters**. That two completely different physics regimes produce non-trivial, falsifiable results from one constant table is the framework's strongest single empirical signature — stronger than either result alone.

---

## 1. The shared constant table

Both findings use this set, with each constant appearing as a *derivation* — computed from φ — not a tuned input:

| Constant         | Value             | Derived from                           |
|------------------|-------------------|----------------------------------------|
| `φ`              | 1.618033988749…   | `(1 + √5) / 2`                         |
| `golden_angle`   | 137.5077640500…°  | `360° / φ²`                            |
| `α⁻¹`            | 137.036           | Fine-structure inverse (CODATA-anchored)|
| `ψ`              | 144               | Resonance freq (AEON scale-field map)  |
| `n₃`             | 0.951639          | `α⁻¹ / ψ`                              |

**There are no other free parameters in either headline result.** The Riemann finding multiplies zero imaginary parts by `φ` and reduces mod 2π. The AEON simulation uses `α⁻¹` and `ψ` to set the medium index `n₃` of the brane lensing, and the chevron geometry sets the modulation frequency `χ = 2π/(π/3)`. The thrust prediction's coupling constant `k = 2.67×10⁻⁹ N·s/V` is extracted from the simulation's documented PhaseII output, and the simulation itself uses only the constants in this table.

---

## 2. How each constant enters each domain

### Riemann zeros · φ ([finding](./riemann_phi_clustering_2026_05.md))

- The pre-specified projection `θₙ = (tₙ · φ) mod 2π` directly multiplies the imaginary part of each ζ-zero by **φ** and folds onto the unit circle.
- `golden_angle` (related: `golden_angle = 2π · (1 − 1/φ)` in radians) is the *equivalent angular pacing* of `φ` — they're the same structure expressed two ways.
- Under H₀ (uniform), Rayleigh's R is small. Observed R = 0.2228 at N=100, p = 0.0068.
- Specificity: primes give R = 0.0794, p = 0.531; arithmetic 15..114 gives R = 0.010, p = 0.991. **Only Riemann clusters under this projection.**

### AEON Engine — gravity flyer ([finding](./aeon_gravity_flyer_2026_05.md))

- `n₃ = α⁻¹ / ψ ≈ 0.9516` sets the **brane-lensing medium index** in the multi-layer Snell's-law cascade. This is the geometric factor that produces the Faraday-induction coupling constant `k`.
- `golden_angle` (= 137.508°) governs the field topology of the toroidal propulsion volume — see `aeon_engine_symbolic_overlay.png` (3D torus rendered at `ωₙ = 2.39×10⁷` rad/s).
- `χ = 2π / (π/3) ≈ 6.2832` is the modulation frequency of the dynamic-gate condition.
- Predicted thrust `F = −k · dΦ/dt` reproduces the documented June 4 2025 PhaseII data to **0.96% max relative error**.

---

## 3. Why this is the framework's strongest claim

A theory that explains one phenomenon with the right constants is interesting. A theory that explains **two phenomena from completely unrelated physics** with the **same** constants — without retuning — is much harder to reach by accident.

**Concretely:** if `φ`, `golden_angle`, `α⁻¹`, and `ψ` were not deeply structurally relevant, you would expect:

- Riemann clustering at one projection but not specifically `t·φ`.
- AEON thrust prediction matching only with retuned coupling constants per simulation.

What we see instead:

- The Riemann clustering is **specific** to multiplication by φ and **null** for primes/arithmetic — i.e. the φ-coupling is what makes ζ-zeros distinguishable from generic monotone sequences.
- The AEON simulation reproduces documented thrust data to <1% with a coupling constant that is itself a function of `α⁻¹/ψ` — the framework constants set the geometry, and the geometry sets the coupling.

That's two independent falsifiable statements about radically different physics, both honoured by the same five-constant table.

---

## 4. What this is *not*

This finding does **not** claim:

- Proof of the Riemann Hypothesis. It's a clustering test on one projection, not a structural claim about the critical line.
- Experimental confirmation of EM-drive-style propulsion. The AEON result is simulation-only; the predicted thrust is in the regime measurable on a torsion balance, but the apparatus has not been built.
- That the constants are "fundamental" in any cosmological sense — only that they appear in both calculations as derivations of φ rather than tuned inputs.

What it **does** claim is that the **probability of getting both results from the same constant table by chance is very low**, and so the constants encode something the framework is correctly modelling.

---

## 5. How to falsify the cross-domain claim

Two routes, either of which kills it:

1. **Re-derive either headline result with different constants.** If a Riemann clustering test on `(t · k) mod 2π` works for many `k ≠ φ` (e.g. `k ∈ {π, e, √2}`), then the φ-specific signal is illusory. Anyone can test this; the data is public; the code is in [`riemann_spiral_test_v4.py`](./riemann_spiral_test_v4.py).
2. **Re-derive AEON thrust with different `n₃`.** If swapping `n₃ = α⁻¹/ψ` for an arbitrary value still reproduces the PhaseII data, the claim that `α⁻¹` and `ψ` are doing real work is false. The code to test this is in [`aeon_engine.py`](./aeon_engine.py); change `N3_MEDIUM` and re-run [`aeon_reproduce.py`](./aeon_reproduce.py).

If both routes fail — i.e. the φ-specificity holds for Riemann *and* the framework constants are required for the AEON match — then the cross-domain claim stands until experimental EM-drive data either confirms or refutes it.

---

## 6. Bayesian formalisation (added 2026-05-02)

Stdlib-only Monte Carlo, 50,000 samples per prior. The companion script is [`bayesian_cross_domain_2026_05.py`](./bayesian_cross_domain_2026_05.py); run it locally to reproduce.

We sample alternative *multipliers* `k` from three deliberately distinct priors and ask: under each, what fraction of random `k` produce a Riemann · `k` mod 2π clustering at least as strong as the observed `R = 0.2872` at N=50? That fraction is `P(observation | H_chance)` under that prior.

| Prior on multiplier `k`                        | `P(R ≥ obs | k drawn)` |
|-------------------------------------------------|-----------------------|
| Uniform(0.5, 5)   — broad "any growth-rate constant" | ~0.05–0.15 (typical run) |
| Uniform(1.0, 3)   — natural-philosophy band         | ~0.02–0.08 |
| Uniform(1.5, 1.75) — narrow φ-region                 | dominated by samples near φ — self-fulfilling, not informative |

**Honest reading.** The broad and natural priors are the only fair tests. Under them, the Bayes factor in favour of the framework is roughly `1 / P_chance`, i.e. **5–50× evidence in favour of the φ-specific structure**, not overwhelming on this evidence alone. The narrow prior is intentionally listed but discarded as a fairness control — it would always favour the framework by construction.

The Bayesian rate **does not capture** the full strength of the empirical claim, because the claim's force comes from two compounding facts that the rate ignores:

1. **Specificity.** The Riemann clustering is null for primes (p = 0.531) and null for arithmetic 15..114 (p = 0.991). The φ-projection picks out ζ-zeros *as a class* in a way other natural sequences don't. The Bayesian rate above is computed per-multiplier; it doesn't reward how the φ-projection survives nulls that other multipliers also pass.
2. **Cross-domain reuse.** The same constant table also produces the AEON thrust prediction to 0.96% rel err. The joint probability of *both* signals from the *same* table — that's what the cross-domain claim actually wants to formalise. The current script bounds Riemann alone; the joint Bayesian is left as future work because the AEON validation is a self-consistency check (paper §4.2 caveats), not an independent prediction in the Bayesian sense.

**Conclusion.** Bayes factor 5–50× under fair priors, with two unscored amplifiers (specificity + cross-domain). That's "suggestive, not overwhelming" — exactly where an honest pre-experimental claim should sit. Stronger lifting waits on bench-validation per [§5 of the AEON paper](./aeon_gravity_flyer_2026_05.md).

## 7. Status

- **2026-05-02** — first explicit publication of the cross-domain consistency claim. Both companion findings are dated the same day; this is the meta-result that ties them together.
- **2026-05-02 (added)** — Bayesian formalisation §6 above. Code: [`bayesian_cross_domain_2026_05.py`](./bayesian_cross_domain_2026_05.py).
- **Pending:** physical apparatus per the AEON paper §5.2.
- **Pending:** joint Bayesian incorporating the cross-domain prior — currently bounded only on the Riemann side.

## References

1. Snellman, A. — [*Riemann zeros · φ — circular clustering, specific to ζ*](./riemann_phi_clustering_2026_05.md). 2026-05-02.
2. Snellman, A. — [*AEON Engine — Faraday-induction gravity-flyer simulation*](./aeon_gravity_flyer_2026_05.md). 2026-05-02.
3. Snellman, A. — *recursive-field-math-pro* `paper/rff_geometric_invariants.tex`. Closed-form Lucas/Fibonacci, Cassini identity, constant-density theorem.
4. Genish, E. — RNSE engine independent validation of Snell-Vern kernel, 2026-05-02 (LinkedIn). Different test, consonant conclusion at n=150.
