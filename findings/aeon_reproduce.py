"""
One-shot reproducibility script for the AEON gravity-flyer paper.

Downloads not required beyond `aeon_engine.py` in the same directory.
Runs the canonical AEON-M v2.1 simulation, asserts the result matches
the documented June 4 2025 PhaseII PDF data to <1% relative error,
and prints a single-line PASS / FAIL verdict.

Usage:
    python aeon_reproduce.py

Stdlib only — no pip install required. Tested on Python 3.10+.
"""

from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

try:
    import aeon_engine  # type: ignore[import-not-found]
except ImportError as e:
    print(f"FAIL: cannot import aeon_engine.py — make sure it's in the same dir as this script. ({e})")
    raise SystemExit(2)


def main() -> int:
    summary = aeon_engine.aeon_summary()
    val = summary["validation"]

    print("=" * 70)
    print("AEON Engine v2.1 — reproducibility check")
    print("=" * 70)
    print(f"  ωₙ           = {summary['constants']['omega_n']:.4e} rad/s")
    print(f"  drive freq   = {summary['constants']['drive_freq_hz']/1e6:.3f} MHz")
    print(f"  n₃ medium    = {summary['constants']['n3_medium']:.6f}  (= α⁻¹/ψ)")
    print(f"  coupling k   = {summary['constants']['coupling_k']:.4e} N·s/V")
    print()
    print("Thrust series (computed → ref from PhaseII PDF, June 4 2025):")
    for i, s in enumerate(summary["thrust_series"]):
        ref = aeon_engine.PHASEII_DATA[i] if i < len(aeon_engine.PHASEII_DATA) else None
        if ref:
            print(f"  t={s['t']:.2e}s  dΦ/dt={s['dphi_dt']:7.2f}V  "
                  f"F={s['thrust']:+.3e} N  (ref {ref[3]:+.3e} N)")
    print()
    print(f"Validation: matched={val['matched']}  max_rel_err={val['max_rel_err']*100:.2f}%")
    print()
    if val["matched"] and val["max_rel_err"] < 0.01:
        print("PASS — AEON Engine v2.1 reproduces documented PhaseII data to <1% rel error.")
        return 0
    print(f"FAIL — max relative error {val['max_rel_err']*100:.2f}% exceeds 1% threshold.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
