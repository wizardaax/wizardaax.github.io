"""
Riemann v4 — controls for the log(t)·φ "miracle" finding.

Hypothesis: log(t)·φ at N=100 R=0.67, p<10⁻⁵, looks like a paper-grade signal.
But log(14.13) to log(236.5) spans only 2.82 → ·φ → 4.57 rad < 2π.
The values can't wrap the circle — they're trivially clustered.

If ANY monotone sequence with similar log-range produces the same R, the
finding is a range artifact, NOT specific to Riemann.

This script settles it.
"""

from __future__ import annotations

import math
import random

PHI = (1.0 + math.sqrt(5.0)) / 2.0
TWO_PI = 2.0 * math.pi

RIEMANN_ZEROS_100 = [
    14.134725141734, 21.022039638771, 25.010857580145, 30.424876125859, 32.935061587739,
    37.586178158826, 40.918719012147, 43.327073280914, 48.005150881167, 49.773832477672,
    52.970321477714, 56.446247697063, 59.347044002602, 60.831778524609, 65.112544048081,
    67.079810529494, 69.546401711173, 72.067157674481, 75.704690699083, 77.144840068874,
    79.337375020249, 82.910380854086, 84.735492980517, 87.425274613125, 88.809111207634,
    92.491899270558, 94.651344040519, 95.870634228245, 98.831194218193, 101.317851005731,
    103.725538040259, 105.446623052026, 107.168611184276, 111.029535543031, 111.874659177002,
    114.320220915452, 116.226680320857, 118.790782866263, 121.370125002420, 122.946829293552,
    124.256818554371, 127.516683879596, 129.578704199956, 131.087688531600, 133.497737203000,
    134.756509753400, 138.116042055000, 139.736208952000, 141.123707404000, 143.111845808600,
    146.000982486800, 147.422765342500, 150.053520420800, 150.925257612400, 153.024693811000,
    156.112909294500, 157.597591817400, 158.849988171500, 161.188964137800, 163.030709686900,
    165.537069188100, 167.184439978200, 169.094515415700, 169.911976479300, 173.411536519800,
    174.754191523200, 176.441434297500, 178.377407776100, 179.916484020100, 182.207078484100,
    184.874467848400, 185.598783678300, 187.228922583900, 189.416158656100, 192.026656360700,
    193.079726603700, 195.265396679800, 196.876481841000, 198.015309676000, 201.264751945000,
    202.493594514100, 204.189671803300, 205.394697201700, 207.906258887800, 209.576509716900,
    211.690862595000, 213.347919360100, 214.547044783200, 216.169538508900, 219.067596349200,
    220.714918840200, 221.430705554800, 224.007000254000, 224.983324670500, 227.421444279600,
    229.337413307700, 231.250188700000, 231.987235253000, 233.693404178000, 236.524229666500,
]

PRIMES_100 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
              101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,
              193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,
              293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,
              409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,
              521,523,541]


def rayleigh(angles):
    n = len(angles)
    if n == 0: return 0.0, 0.0
    cx = sum(math.cos(a) for a in angles)/n
    cy = sum(math.sin(a) for a in angles)/n
    R = math.hypot(cx, cy)
    return R, n*R*R


def emp_p(z, n, n_shuf=5000, seed=42):
    rng = random.Random(seed)
    nulls = []
    for _ in range(n_shuf):
        sample = [rng.uniform(0, TWO_PI) for _ in range(n)]
        _, zz = rayleigh(sample)
        nulls.append(zz)
    return sum(1 for x in nulls if x >= z)/n_shuf


def proj_log_phi(seq):
    return [(math.log(t) * PHI) % TWO_PI for t in seq]


def proj_t_phi(seq):
    return [(t * PHI) % TWO_PI for t in seq]


def report(label, seq):
    angles = proj_log_phi(seq)
    R, z = rayleigh(angles)
    p = emp_p(z, len(seq))
    log_min = min(math.log(t) for t in seq)
    log_max = max(math.log(t) for t in seq)
    log_span = log_max - log_min
    arc_span_rad = log_span * PHI
    print(f"  {label:<28}  R={R:.4f}  p={p:.5f}  log_span={log_span:.3f}  arc_span={arc_span_rad:.3f} rad ({math.degrees(arc_span_rad):.1f}°)")
    return R, p


def main():
    print("=" * 80)
    print("CONTROLS FOR log(t)·φ FINDING — IS IT REAL OR A RANGE ARTIFACT?")
    print("=" * 80)
    print(f"  φ = {PHI:.15f}, 2π = {TWO_PI:.6f}")
    print()
    print("If signal is REAL: only Riemann shows it.")
    print("If signal is ARTIFACT: any monotone sequence with similar log-range shows it.")
    print()
    print("─" * 80)
    print("TEST: log(t)·φ mod 2π,  N=100, on each sequence:")
    print("─" * 80)

    arith = [float(i) for i in range(15, 115)]      # similar magnitude to zeros
    arith_lin = [float(i*100) for i in range(1, 101)]  # 100..10000
    geom = [10.0 * (1.05 ** i) for i in range(100)]   # geometric growth

    rR, rP = report("Riemann zeros (N=100)", RIEMANN_ZEROS_100)
    pR, pP = report("Primes (N=100)", [float(p) for p in PRIMES_100])
    aR, aP = report("Arithmetic 15..114", arith)
    a2R, a2P = report("Arithmetic 100..10000", arith_lin)
    gR, gP = report("Geometric 10·1.05^i", geom)

    print()
    print("─" * 80)
    print("VERDICT")
    print("─" * 80)
    if pP < 0.05 or aP < 0.05:
        print("  ✗ Controls (primes/arithmetic) ALSO show the signal.")
        print("  → log(t)·φ is a RANGE ARTIFACT, not specific to Riemann zeros.")
        print("  → log(t) for any 100-element sequence in this magnitude has narrow span,")
        print("    so multiplied by φ doesn't wrap the circle, producing fake clustering.")
    elif rP < 0.001 and pP > 0.05 and aP > 0.05:
        print("  ✓ Riemann clusters; controls do NOT.")
        print("  → log(t)·φ signal IS specific to Riemann zeros — real finding.")
    else:
        print("  ? Mixed result; needs deeper analysis.")
    print()

    # Also test the headline t·φ result on the same controls
    print("─" * 80)
    print("CROSS-CHECK: original Test B (t·φ mod 2π, N=100):")
    print("─" * 80)
    for label, seq in [("Riemann", RIEMANN_ZEROS_100),
                       ("Primes",  [float(p) for p in PRIMES_100]),
                       ("Arithmetic 15..114", arith),
                       ("Arithmetic 100..10000", arith_lin)]:
        a = proj_t_phi(seq)
        R, z = rayleigh(a)
        p = emp_p(z, len(seq))
        sig = "**" if p < 0.01 else "*" if p < 0.05 else ""
        print(f"  {label:<26}  R={R:.4f}  p={p:.5f}  {sig}")


if __name__ == "__main__":
    main()
