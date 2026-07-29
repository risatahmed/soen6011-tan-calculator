#!/usr/bin/env python3
"""Textual scientific-calculator prototype for tan(x) — Deliverable 1, Problem 4.

Implements Algorithm A (Problem 3): range reduction modulo pi/2 + Maclaurin
series for sin and cos, then tan = sin / cos. Selected over Algorithm B
(CORDIC) per docs/mindmaps/algorithm_selection_mindmap.png.

Computation (this module's compute functions) is kept independent of I/O so
it can be imported and tested without a terminal.
"""

import math
import sys

# --- Constants (documented per requirement DOC-01) ----------------------

PI = math.pi          # finite-precision constant; from-scratch replacement needed in D2 (see NOTE below)
X_MAX = 1.0e4         # VAL-03: largest supported |x|, in radians
POLE_EPSILON = 1.0e-6 # VAL-04: |cos(reduced angle)| below this is treated as "at/near a pole"
SERIES_TOL = 1.0e-12  # per-term stopping tolerance driving ACC-01
SERIES_N_MAX = 100    # max-work safeguard for the series loops
DISPLAY_SIG_FIGS = 10 # ACC-02 / DOC-01: displayed precision

# NOTE for Deliverable 2 ("from scratch"): this module already computes
# sin/cos itself via Maclaurin series rather than calling math.sin/math.cos,
# so those two calls do not appear anywhere in the compute path below. The
# one remaining standard-library dependency is `PI = math.pi`, used as the
# finite-precision value of pi; D2 must replace it with an independently
# derived from-scratch constant (e.g. a fixed literal expansion or a
# Machin-like arctan series computed without math.pi).


class OutOfRangeError(Exception):
    """Raised when |x| exceeds the supported argument range (VAL-03)."""


class NearPoleError(Exception):
    """Raised when x is at or within tolerance of a pole x = pi/2 + k*pi (VAL-04)."""


# --- Compute layer (Algorithm A; no I/O) ---------------------------------

def maclaurin_sin(r, tol=SERIES_TOL, n_max=SERIES_N_MAX):
    """sin(r) via Maclaurin series, r assumed small (|r| <= pi/4)."""
    term = r
    total = r
    n = 1
    while abs(term) >= tol and n <= n_max:
        term = term * (-(r * r)) / ((2 * n) * (2 * n + 1))
        total += term
        n += 1
    return total


def maclaurin_cos(r, tol=SERIES_TOL, n_max=SERIES_N_MAX):
    """cos(r) via Maclaurin series, r assumed small (|r| <= pi/4)."""
    term = 1.0
    total = 1.0
    n = 1
    while abs(term) >= tol and n <= n_max:
        term = term * (-(r * r)) / ((2 * n - 1) * (2 * n))
        total += term
        n += 1
    return total


def tan_by_series(x):
    """Compute tan(x) via Algorithm A: range reduction + Maclaurin series.

    Raises OutOfRangeError if |x| > X_MAX (VAL-03).
    Raises NearPoleError if x is at/within tolerance of a pole x = pi/2 + k*pi (VAL-04).
    """
    if abs(x) > X_MAX:
        raise OutOfRangeError(
            f"|x| = {abs(x):.6g} exceeds the supported range |x| <= {X_MAX:g} radians."
        )

    sign = 1.0
    if x < 0:
        x = -x
        sign = -1.0  # tan(-x) = -tan(x): odd symmetry

    k = round(x / (PI / 2))          # nearest multiple of pi/2
    r = x - k * (PI / 2)             # r in [-pi/4, pi/4]
    quadrant_flip = (k % 2) == 1

    sin_r = maclaurin_sin(r)
    cos_r = maclaurin_cos(r)

    if quadrant_flip:                # tan(r + pi/2) = -cos(r) / sin(r)
        numerator, denominator = -cos_r, sin_r
    else:
        numerator, denominator = sin_r, cos_r

    if abs(denominator) < POLE_EPSILON:
        raise NearPoleError(
            "x is at or within tolerance of a pole (x = pi/2 + k*pi), "
            "where cos(x) is approximately zero and tan(x) is undefined."
        )

    return sign * (numerator / denominator)


# --- I/O layer (all user interaction lives here) -------------------------

BANNER = (
    "tan(x) calculator (Deliverable 1 prototype)\n"
    "  - Enter x as a real number, in RADIANS (not degrees).\n"
    f"  - Supported range: |x| <= {X_MAX:g} radians.\n"
    "  - Values at or within tolerance of a pole (x = pi/2 + k*pi) are rejected\n"
    "    with an explanation rather than returning a huge/meaningless number.\n"
    f"  - Results are displayed to {DISPLAY_SIG_FIGS} significant figures.\n"
    "  - Type 'quit' or 'exit' to leave.\n"
)


def format_result(value):
    return f"{value:.{DISPLAY_SIG_FIGS}g}"


def parse_x(raw_text):
    """Parse user input into a float, or raise ValueError with a helpful message."""
    text = raw_text.strip()
    if text == "":
        raise ValueError("No input received. Please enter a numeric value for x.")
    try:
        return float(text)
    except ValueError:
        raise ValueError(
            f"'{raw_text.strip()}' is not a valid real number. "
            "Please enter something like 0.7853981634 or -1.2."
        )


def run_cli(input_stream=sys.stdin, output_stream=sys.stdout):
    """Main interactive loop. Streams are parameterized for testability."""
    print(BANNER, file=output_stream)
    while True:
        print("Enter x (radians), or 'quit' to exit:", file=output_stream, end=" ")
        raw = input_stream.readline()
        if raw == "":  # EOF (e.g. piped input exhausted)
            print("\nEnd of input. Exiting.", file=output_stream)
            break

        stripped = raw.strip()
        if stripped.lower() in ("quit", "exit", "q"):
            print("Goodbye.", file=output_stream)
            break

        try:
            x = parse_x(raw)
        except ValueError as exc:
            print(f"Invalid input: {exc}", file=output_stream)
            continue

        try:
            result = tan_by_series(x)
        except OutOfRangeError as exc:
            print(f"Input out of range: {exc}", file=output_stream)
            continue
        except NearPoleError as exc:
            print(f"Cannot compute tan(x): {exc}", file=output_stream)
            continue

        print(f"tan({format_result(x)}) = {format_result(result)}", file=output_stream)


if __name__ == "__main__":
    run_cli()
