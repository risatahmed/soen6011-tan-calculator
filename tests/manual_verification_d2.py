#!/usr/bin/env python3
"""D2-P5.6 manual verification pass for the from-scratch numerical core.

Not the formal PyUnit/unittest suite (that is D3-P8.2); this is a
standalone, readable reference-value check run against a fixed commit and
captured as evidence (docs/verification_matrix_d2.md), per D2-P5.6:
"reference-value suite ... across special angles, general angles, negative
(symmetry), near-pole, and large-argument inputs ... invalid strings, empty,
at-pole, very large magnitudes."

Run with:  python3 -m tests.manual_verification_d2   (from repository root)

Reference values are the trusted table from docs/research_notes.md Section 4
(computed independently of the algorithm under test).
"""

import decimal

from src.exceptions import ConvergenceError, DomainError, NumericalRangeError
from src.tan_core import tan
from src.validation import parse_x

decimal.getcontext().prec = 30

# (label, x, expected tan(x) or None, expected exception or None)
# Expected values are an independent oracle (Python's math.tan, computed
# once and pasted here -- never the algorithm under test computing its own
# reference), matching D1's verification methodology.
CASES = [
    ("zero", 0.0, 0.0, None),
    ("special pi/6", 0.5235987755982988, 0.5773502691896256, None),
    ("special pi/4", 0.7853981633974483, 0.9999999999999999, None),
    ("special pi/3", 1.0471975511965976, 1.7320508075688767, None),
    ("negative (odd symmetry) -pi/4", -0.7853981633974483, -0.9999999999999999, None),
    ("small positive 0.1", 0.1, 0.10033467208545054, None),
    ("beyond one period pi+pi/4", 3.9269908169872414, 0.9999999999999997, None),
    ("large argument 1000", 1000.0, 1.4703241557027187, None),
    ("near pole pi/2 - 1e-6", 1.5707953267948966, 1000000.0000207009, None),
    ("negative pole-adjacent -pi/2 + 1e-6", -1.5707953267948966, -1000000.0000207009, None),
    ("at pole exactly pi/2", 1.5707963267948966, None, DomainError),
    ("out of range 1e10", 1.0e10, None, NumericalRangeError),
    ("out of range -1e10", -1.0e10, None, NumericalRangeError),
]

RELATIVE_TOLERANCE = 1.0e-9  # ACC-01


def relative_error(actual, expected):
    if expected == 0:
        return abs(actual)
    return abs((actual - expected) / expected)


def run():
    results = []
    for label, x, expected, expected_exc in CASES:
        try:
            actual = tan(x)
        except (DomainError, NumericalRangeError, ConvergenceError) as exc:
            if expected_exc is not None and isinstance(exc, expected_exc):
                results.append((label, x, "raised " + type(exc).__name__, "PASS", None))
            else:
                results.append((label, x, f"unexpected {type(exc).__name__}: {exc}", "FAIL", None))
            continue

        if expected_exc is not None:
            results.append((label, x, f"got {actual!r}, expected {expected_exc.__name__}", "FAIL", None))
            continue

        err = relative_error(actual, expected)
        verdict = "PASS" if err <= RELATIVE_TOLERANCE else "FAIL"
        results.append((label, x, actual, verdict, err))

    # Input-validation cases (parse_x), not numeric-core cases.
    for label, raw in [("invalid non-numeric", "abc"), ("invalid empty", "")]:
        try:
            parse_x(raw)
            results.append((label, raw, "did not raise", "FAIL", None))
        except ValueError as exc:
            results.append((label, raw, f"raised ValueError: {exc}", "PASS", None))

    print(f"{'Case':38} {'x / input':>24}  {'Result':>40}  {'RelErr':>10}  Verdict")
    print("-" * 130)
    n_pass = 0
    for label, x, actual, verdict, err in results:
        err_str = f"{err:.2e}" if isinstance(err, float) else ""
        x_str = f"{x!r}" if not isinstance(x, str) else x
        print(f"{label:38} {x_str:>24}  {str(actual):>40}  {err_str:>10}  {verdict}")
        n_pass += verdict == "PASS"
    print("-" * 130)
    print(f"{n_pass}/{len(results)} cases passed.")
    return n_pass == len(results)


if __name__ == "__main__":
    import sys

    sys.exit(0 if run() else 1)
