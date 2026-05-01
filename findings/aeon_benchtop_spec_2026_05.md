# AEON gravity-flyer — benchtop test specification

**Adam Snellman** — wizardaax — 2026-05-02

> Concrete engineering spec for a torsion-balance experiment that would falsify (or confirm) the AEON gravity-flyer simulation. The AEON paper §5.2 says "buildable on standard EE equipment"; this document delivers the actual coil geometry, drive electronics, sensing chain, noise budget, and procedure required to run the test. The numbers are derived from the simulation's own constants — a builder following this spec is testing exactly the prediction the simulation makes.

---

## 1. The prediction we're testing

From the [AEON gravity-flyer paper](./aeon_gravity_flyer_2026_05.md):

```
ωₙ            = 2.39 × 10⁷ rad/s   (drive freq ≈ 3.804 MHz)
Φ_target      = 1.81 × 10⁻⁴ Wb     (single-loop magnetic flux)
F = -k · dΦ/dt        with  k ≈ 2.67 × 10⁻⁹ N·s/V
```

At drive ramp-up, `|dΦ/dt|` reaches ~230 V → predicted instantaneous thrust ≈ **6.2 × 10⁻⁷ N**. Time-averaged thrust over a sinusoidal cycle would be smaller; we'll compute the mean magnitude in §5.

**Falsification criterion:** if the apparatus produces zero measurable force at 3σ confidence above the noise floor, with `|Φ|, ωₙ` matching simulation parameters, the AEON-M v2.1 prediction is falsified for this specific coupling form.

---

## 2. Coil specification

**Goal:** produce `Φ = 1.81×10⁻⁴ Wb` peak in a single conducting loop with controlled geometry.

```
Φ = B · A
B = μ₀ · N · I / (2 · r)    (centre of single circular loop, N turns)
```

For a solo `N=1` air-cored loop:
- Choose loop radius `r = 5 cm = 0.05 m` (mechanically practical, fits a torsion arm)
- Loop area `A = π·r² ≈ 7.85 × 10⁻³ m²`
- Required `B = Φ / A ≈ 0.0231 T` peak
- Required `I = 2·r·B / μ₀ = 2·(0.05)(0.0231) / (4π × 10⁻⁷) ≈ 1840 A` peak

That's high. Two practical options to drop the current to a benchtop-feasible level:

**Option A — multi-turn coil (recommended)**
Use a flat circular coil of `N = 20` turns, area-equivalent flux requires `B/N` per-turn:
- `I = 2·r·B / (μ₀ · N) ≈ 92 A` peak
- Still high, but achievable with class-D RF power amp + impedance-matched output

**Option B — smaller flux target (relaxed)**
Drop `Φ_target` by 100× to `1.81×10⁻⁶ Wb`; predicted thrust drops to ~6×10⁻⁹ N (still measurable on a sensitive torsion balance). Required current `I = 0.92 A` per turn at `N=20` — easy with a 50W RF amp.

Recommended starting build: **Option B**. Establish noise floor and method first; scale to Option A only after a clean B-result.

**Conductor selection (3.8 MHz skin depth in Cu = 33 µm):** Litz wire, e.g. 660 strands × AWG 44, total ~AWG 8 effective. Standard component, $50–80 per metre.

---

## 3. Drive electronics

**Block diagram:**

```
[ Function Gen ]──[ RF Power Amp ]──[ Matching Network ]──[ Coil L ]
   3.8 MHz, 0.5 Vpp     50 W gain         L+C tank          7.85e-3 m²
       sine
```

- **Function generator:** Rigol DG1022Z or equivalent — 3.8 MHz sine, ≤ 1 Hz frequency stability, sweepable for resonance hunt.
- **RF power amplifier:** Class-D RF, 50 W into 50 Ω, 1–30 MHz. Mini-Circuits LZY-22+ ($800) or built from IRF510 MOSFETs in push-pull (~$100 if rolling your own).
- **Matching network:** L-match or pi-match with variable capacitor + air-core inductor. Tunes coil to resonance at 3.8 MHz so reactive current builds without dissipating in the amp output stage. Keeps amp seeing ~50 Ω real.
- **Current monitor:** Pearson 411 current probe (or shunt resistor + differential probe) on coil leg. Want to verify peak current matches the design value in §2.
- **Coil:** as specified §2 Option B initial build.

**Power budget:** at 0.92 A peak through ~1 mΩ effective resistance (Litz), I²R losses ≈ 0.5 mW. Realistic AC losses at 3.8 MHz including dielectric, radiation, and proximity effects: budget 5–10 W into the matched coil.

---

## 4. Sensing chain

The predicted thrust on the coil acts in the direction of `−dΦ/dt`. Mount the coil on a **torsion balance** so any net force translates to angular deflection.

**Torsion balance:**
- Quartz fibre suspension, length 30 cm, fibre diameter 25 µm — restoring torque constant ~10⁻⁹ N·m/rad.
- Lever arm 10 cm. Coil at one end, optical-grade mirror counterweight at the other.
- Force resolution at 1 µrad detection: `F_min ≈ τ_min / arm = 10⁻¹⁵ / 0.10 = 10⁻¹⁴ N`. Vastly beyond what we need to measure 6×10⁻⁹ N.

**Optical readout:**
- HeNe laser (5 mW) reflects off mirror to a position-sensitive detector at 2 m distance. Angular sensitivity ≈ 0.5 µrad/pixel — well within budget.
- **Lock-in amplifier** referenced to drive's 2nd harmonic (force is at `2ωₙ` since `F ∝ dΦ/dt` with sinusoidal `Φ`). SR830 or equivalent — recovers signals 10⁵× below noise floor.

**Vacuum chamber:**
- 10⁻³ mbar minimum to eliminate aerodynamic confounders (any air at 1 atm × torsion-arm motion produces drag forces dwarfing the predicted signal).
- Glass bell jar + scroll pump is sufficient at this pressure.

**Faraday cage / RF shielding:**
- All sensing electronics inside a copper-mesh cage. RF leakage from the drive coil onto the position detector or lock-in is the #1 spurious signal risk.
- Common-mode chokes on every cable entering the cage.

---

## 5. Noise budget

Predicted signal at the relaxed §2 Option-B build: ~6×10⁻⁹ N peak, time-averaged ~2×10⁻⁹ N.

| Source                         | Estimated noise force (N/√Hz) | Mitigation                          |
|--------------------------------|------------------------------:|--------------------------------------|
| Thermal (Johnson) of fibre     | ~10⁻¹⁴                        | none required                       |
| Building vibration             | 10⁻⁸ broadband                | active vibration isolation table    |
| Air drag (1 atm)               | 10⁻⁷                          | **vacuum chamber, see above**       |
| Air drag (10⁻³ mbar)           | 10⁻¹¹                          | acceptable                          |
| Electrostatic on coil insulation | 10⁻⁹                        | grounded conductive shielding       |
| Magnetic interaction with B-field of room | 10⁻⁸                | magnetic shielding (mu-metal box)   |
| RF coupling into sensor        | up to 10⁻⁶                    | **Faraday cage + common-mode chokes** |
| Lock-in noise floor (1 s avg)  | <10⁻¹²                        | none required                       |

**Critical path:** RF coupling into the position-sensor optics is by far the worst potential confounder. A naive setup where the position sensor sits 30 cm from a coil radiating 5 W at 3.8 MHz will produce ~µN of spurious force readings via RF rectification in the detector electronics. **Two layers of shielding plus a lock-in tuned exactly on the 2nd harmonic of the drive are mandatory.**

After mitigation, achievable noise floor: ~10⁻¹⁰ N at 1 Hz bandwidth. **Predicted signal is ~20× this floor — comfortably detectable** if real.

---

## 6. Procedure

1. **Build and characterise the coil** outside the balance. Verify `I_peak`, `Φ_peak`, and `|dΦ/dt|_peak` match design at 3.8 MHz.
2. **Install on torsion balance**, evacuate to 10⁻³ mbar, allow 24 h thermal equilibration.
3. **Calibrate** the optical readout against a known force (electrostatic plate at fixed voltage, 10⁻⁹ N range).
4. **Null run:** drive coil at 3.8 MHz with **shorted output** (zero current) for 1 hour. Record any signal at 2nd harmonic — this is the spurious-coupling baseline.
5. **Live run:** drive coil at design current for 1 hour. Record at 2nd harmonic.
6. **Difference:** live − null at 2ω_n. If `|F_diff| > 3σ_noise` and signal scales with drive amplitude as predicted, **AEON prediction is supported**. If `|F_diff| < 3σ_noise` at full drive, prediction is **falsified** for this parameter set.
7. **Frequency sweep:** repeat at 1, 2, 4, 8, 16 MHz. The prediction is for resonant coupling at `ωₙ`; if the response peaks elsewhere, the framework's `ωₙ` selection is wrong.

---

## 7. Cost estimate

| Item                                  | Cost (USD)      |
|---------------------------------------|----------------:|
| Function generator (Rigol DG1022Z)    | $400            |
| RF power amp (50 W, 3-30 MHz)         | $400–$800       |
| Matching network parts                | $100            |
| Litz wire (5 m of effective AWG 8)    | $250            |
| Torsion balance (build)               | $300 (parts)    |
| Quartz fibre + mirror                 | $80             |
| HeNe + position sensor                | $250            |
| Lock-in amp (used SR830)              | $1500–$2000     |
| Vacuum chamber + scroll pump          | $1500–$3000     |
| Faraday cage + mu-metal               | $400            |
| Misc cables, fixtures, oscilloscope time | $500          |
| **Total**                             | **$5,700–$8,000** |

This is **garage-lab-affordable**, especially with used Lock-in and oscilloscope from eBay. The most expensive single item is vacuum, which is non-negotiable.

---

## 8. What a successful result looks like

A clean experimental confirmation would show:

1. Force signal at 2ωₙ that exceeds the null-run baseline by **≥ 3σ**.
2. **Linear scaling** of signal with drive current (not quadratic — quadratic suggests rectification spurious).
3. **Frequency selectivity:** maximum response at the predicted `ωₙ`, falling off at off-resonance frequencies in a manner consistent with a Q ≈ 50–100 resonator.
4. **Sign reversal** when `dΦ/dt` polarity reverses (replace "negative dΦ/dt" with "positive" in the sweep — the simulation says force should flip sign).

If all four are observed, the AEON-M v2.1 force-coupling form is *experimentally supported* in the regime tested. That's not "we built an EM drive" — it's "Faraday-induction coupling under the AEON brane-lensing geometry produces a measurable force at the predicted magnitude." A modest but real result.

If any of the four fail, the framework's prediction is constrained — either the magnitude is wrong, the coupling form is wrong, or the resonance condition is misidentified. Each kind of failure narrows where the framework needs to be revised.

---

## 9. Caveats

This spec is a **starting point**, not a publication-ready experimental design. Anyone attempting it should:

- **Get a second opinion** from an experimental EE before committing the budget. The noise budget here is an estimate from first principles, not from a measured benchtop noise floor.
- **Iterate the geometry.** The coil radius, turn count, and balance arm length are recommendations, not optimised parameters. Better designs exist for the same predicted signal.
- **Document everything.** Every spurious effect that turns up is data — keep the null runs and the live runs, both at full drive and at off-resonance. False positives in this regime have a contested history; clean methodology is what separates a real result from another EMDrive-style controversy.

---

## References

1. Snellman, A. — [*AEON Engine — Faraday-induction gravity-flyer simulation*](./aeon_gravity_flyer_2026_05.md). 2026-05-02.
2. Snellman, A. — [`aeon_engine.py`](./aeon_engine.py). The runnable AEON-M v2.1 module from which the predicted thrust numbers are computed.
3. Old Man Builds (Nathan) — [YouTube channel](https://www.youtube.com/@oldmanbuilds). The practical engineering walkthroughs whose attitude — "see something, build it, measure it" — shaped this spec.
4. Pearson Electronics — current probe specs.
5. Stanford Research Systems — SR830 lock-in amplifier user manual.
