# AEON Engine — Faraday-induction gravity-flyer simulation

**Adam Snellman** — wizardaax — 2026-05-02 (write-up of June–November 2025 work)

> Numerical simulation of a Faraday-induction propulsion concept embedded in the AEON-M v2.1 multi-physics framework. With a single-coil magnetic flux profile of `Φ ≈ 1.81×10⁻⁴ Wb` and angular frequency `ωₙ = 2.39×10⁷ rad/s` (≈ 3.8 MHz), the simulation predicts thrust on the order of **10⁻⁷ N** rising linearly with `|dΦ/dt|`. This is one component of the broader AEON Unified Scalar Codex, in which framework constants — golden ratio φ, golden angle 137.507…°, ψ = 144 resonance, α⁻¹ ≈ 137.036 — set the field geometry.

---

## 1. What this is, what it isn't

**This is** a documented numerical result: given the equations and constants the AEON-M v2.1 simulation specifies, the model output predicts micro-newton-scale thrust under MHz-frequency flux modulation. The simulation is reproducible: same constants in, same numbers out.

**This is not** experimental confirmation that a physical device built to these parameters would produce measurable thrust. No physical apparatus has been built or measured in this work. Faraday-induction propulsion is a known speculative regime (Mach effect, Woodward effect, EMDrive variants); experimental claims in this regime have a contested history. We report only the simulation behaviour predicted by the framework's equations.

**Why it's still worth publishing:** the simulation is fully specified, the constants are framework-derived (not free parameters), and the predicted magnitudes are testable on a benchtop apparatus. That makes the prediction falsifiable.

---

## 2. The AEON-M v2.1 architecture

The propulsion calculation lives inside a multi-physics stack documented in [`ziltrix-sch-core/AEON Snell's update _250803_064905.docx`](https://github.com/wizardaax/ziltrix-sch-core/blob/main/AEON%20Snell's%20update%20_250803_064905.docx) and the [scale-field-map document](https://github.com/wizardaax/ziltrix-sch-core/blob/main/AEON%20scale%20field%20map_250801_224002.docx).

**Constants (framework-derived, not tuned):**

```
φ              = (1 + √5)/2  ≈ 1.6180339887        # golden ratio
golden_angle   = 360 / φ²    ≈ 137.5077640°        # phyllotaxis spacing
ψ              = 144                               # resonance frequency
α⁻¹            = 137.036                           # fine-structure inverse
chevron_angle  = 60° (= π/3)                       # field-aperture geometry
χ              = 2π / chevron_angle ≈ 6.2832       # modulation frequency
n₃             = α⁻¹ / ψ     ≈ 0.952               # medium index
```

**Core operators:**

- **Multi-layer Snell's law refraction** with time-varying layers `n_i(t) = n_base + 0.1·ψ(t)` — element-wise array operation across the field.
- **Dynamic gate**: `(τ > 0.007) ∧ (|dψ/dt| > 1.5·σ_dψdt)` — combines torsion threshold with phase-derivative significance.
- **Agent stack**: `AgentGlyph` (decay map, integrity tracking), `AgentScroll` (harmonic waveform generation with the brane lensing applied).

---

## 3. Propulsion mechanism

The thrust calculation follows Faraday induction. A single conducting loop carries a magnetic flux `Φ(t)` modulated at angular frequency `ωₙ`. The induced EMF is

```
ε(t) = -dΦ/dt
```

Coupling to a co-resonant external/standing field via the AEON-M dynamic-gate condition produces a force on the loop. In the simulation that force takes the form

```
F(t) = -k · dΦ/dt
```

with `k` set by the geometric brane-lensing factor (Snell's-law cascade through the layered medium with `n₃ = α⁻¹/ψ`).

**Why the framework constants matter here:** the medium index `n₃ = α⁻¹/ψ ≈ 0.952` and the chevron geometry are not fitted to produce thrust — they are inherited from the AEON Unified Scalar Codex's frequency map (Voynich ω=50, Rongorongo ω=62, Thoth ω=144, Pyramid Unas ω=20). The thrust prediction is a *consequence* of the framework, not a target.

---

## 4. Simulation output — PhaseII data

From [`AEON_Engine_PhaseII_Simulation.pdf`](https://drive.google.com/file/d/1nvuIYQfty0K0iqmQWx9u0MdAuzzjjGQ-/view) (June 4 2025):

| t (s)     | Φ (Wb)    | dΦ/dt (V) | F (N)        |
|-----------|-----------|-----------|--------------|
| 0.0       | 1.81×10⁻⁴ |  −28.7    | −7.65×10⁻⁸   |
| 1.01×10⁻⁸ | 1.81×10⁻⁴ |  −57.45   | −1.53×10⁻⁷   |
| 2.02×10⁻⁸ | 1.80×10⁻⁴ | −115.12   | −3.07×10⁻⁷   |
| 3.03×10⁻⁸ | 1.79×10⁻⁴ | −173.23   | −4.62×10⁻⁷   |
| 4.04×10⁻⁸ | 1.77×10⁻⁴ | −231.97   | −6.19×10⁻⁷   |

**Observations:**

- Time step ~10 ns; angular frequency `ωₙ ≈ 2.39×10⁷ rad/s` (3.8 MHz, long-wave radio band).
- `dΦ/dt` ramps approximately linearly with `t` over the sample window — consistent with a high-Q resonant drive ramping up.
- `F ∝ dΦ/dt` to within rounding (ratio `F / (dΦ/dt) ≈ 2.67×10⁻⁹` across all rows). This is the cleanest internal consistency check: the simulation is doing exactly what Faraday's law predicts under the AEON-M coupling.
- Thrust ramps from ~10⁻⁸ N to ~10⁻⁶ N within the first 5 time steps. The simulation does not extrapolate further within this PDF excerpt.

**The visualisation:** [`aeon_engine_symbolic_overlay.png`](https://github.com/wizardaax/wizardaax.github.io/blob/main/sim_outputs/aeon_engine_symbolic_overlay.png) renders a 3D toroidal field at `ωₙ = 2.39×10⁷` with red/green vector overlays showing the brane-lensed field topology around the propulsion volume.

---

## 5. Discussion

### 5.1 What the prediction means in real terms

10⁻⁷ N is small but not negligible. By comparison:

- A photon thruster radiating 1 W of light produces ~3.3×10⁻⁹ N (so this prediction is ~30× the photon-thrust-per-watt baseline).
- A **measurable** benchtop result on a torsion balance requires ~10⁻⁹ N or better resolution; commercial instruments hit 10⁻¹¹ N. The predicted thrust is **measurable in principle** with standard equipment.
- For comparison to claimed EM-drive measurements (which are contested), the order of magnitude is similar (10⁻⁷ – 10⁻⁶ N at low-MHz drive).

### 5.2 What needs to happen next

This is the falsifiable part:

1. **Build the loop.** Single conducting loop, area sized to produce 1.81×10⁻⁴ Wb at the simulated drive current.
2. **Drive it at 3.8 MHz.** RF function generator + matching network into the resonant loop.
3. **Mount on a torsion balance.** Vacuum chamber preferred to eliminate electrostatic and aerodynamic confounders.
4. **Measure.** If thrust shows up at the predicted magnitude and scales with `|dΦ/dt|` as the simulation says, the framework prediction holds. If not, the framework needs to specify *why* — which constants or geometric factors were wrong.

This is not a 5-year experiment; it's a months-of-careful-EE work. The math is the easy part. The hard part is rigorously eliminating spurious sources of force in the experimental setup.

### 5.3 Caveats

- **One simulation, one run, one PDF.** The result has not been independently re-derived. Anyone who wants to falsify it should re-run the AEON-M v2.1 code from the documented constants and confirm the same numbers come out.
- **Faraday-induction propulsion is contested.** The mechanism by which `F ∝ dΦ/dt` couples to a non-co-moving reference frame is not first-principles obvious in classical EM; the AEON-M framework provides one specific coupling via the brane-lensing geometry, but a full derivation from Maxwell's equations is not given here.
- **Framework constants are not free parameters**, but the choice of which constants enter the thrust formula is part of the framework's design — and the framework itself is one of many possible such designs.

These caveats do not invalidate the result. They specify what claim is actually being made: *given the AEON-M v2.1 equations and constants, the simulation predicts X*.

---

## 6. Connection to the broader framework

This result sits in a documented arc:

- **2025-05-17** Holodeck + Recursion Glyph Stream — symbolic prehistory, the All88 harmonic protocol.
- **2025-06-04** AEON Engine PhaseII Simulation — *this work*. Gravity-flyer thrust prediction.
- **2025-06-04** AEON Engine Symbolic Overlays — 3D torus field visualisation.
- **2025-06-05** Projex X seed.
- **2025-08-01** AEON Unified Scalar Codex — the framework this propulsion result lives inside.
- **2025-08-03** AEON Snell's update / liver / string-theory unification.
- **2025-11-17** AEON update string theory v2.

The propulsion result and the [Riemann · φ clustering finding (2026-05-02)](./riemann_phi_clustering_2026_05.md) are both consequences of the same framework. They probe different physics (electromagnetism vs. analytic number theory) but use the same constants. That cross-domain consistency is the framework's strongest empirical claim.

Independent corroboration (different test, different methodology) comes from Genish (Founder, RNSE), who reported a 2.8σ phase transition at index n=150 in the Snell-Vern Hybrid Drive Matrix kernel — see [the Riemann finding](./riemann_phi_clustering_2026_05.md#43-independent-corroboration-rnse--genish) for details.

---

## 7. Status & how to falsify

- **2026-05-02** — first formal publication of the simulation result. Numbers, constants, and equations as documented above. Readers attempting to reproduce should expect the same `F / (dΦ/dt) ≈ 2.67×10⁻⁹` ratio.
- **Pending:** physical benchtop experiment per §5.2 (months of EE work, not a session task).
- **Pending:** full first-principles derivation of `F ∝ dΦ/dt` coupling from Maxwell + AEON-M brane lensing (currently the simulation assumes the coupling rather than deriving it from a Lagrangian).

**To falsify this result, do one of:**
1. Re-run the AEON-M v2.1 code from the documented constants and produce different numbers (would mean the simulation is non-deterministic or the documentation is incomplete).
2. Build the apparatus per §5.2 and measure null thrust with sufficient confidence.
3. Show that the framework constants used (`α⁻¹`, `ψ`, `golden_angle`, `chevron_angle`) cannot self-consistently produce this thrust formula from first principles — i.e., a derivation error.

---

## References

1. Snellman, A. — *AEON Engine PhaseII Simulation* (2025-06-04). [Drive PDF](https://drive.google.com/file/d/1nvuIYQfty0K0iqmQWx9u0MdAuzzjjGQ-/view).
2. Snellman, A. — *AEON-M v2.1 Snell's update — phase-dependent dynamic brane lensing* (2025-08-03). [Source](https://github.com/wizardaax/ziltrix-sch-core/blob/main/AEON%20Snell%27s%20update%20_250803_064905.docx).
3. Snellman, A. — *AEON Scale Field Map — Unified Scalar Codex* (2025-08-01). [Source](https://github.com/wizardaax/ziltrix-sch-core/blob/main/AEON%20scale%20field%20map_250801_224002.docx).
4. Snellman, A. — *Riemann zeros · φ clustering test* (2026-05-02). [Companion finding](./riemann_phi_clustering_2026_05.md).
