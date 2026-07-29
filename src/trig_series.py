"""From-scratch sin/cos for a small reduced angle (Deliverable 2, Problem 5).

Implements Algorithm A (docs/algorithms/algorithm_A_maclaurin.md) exactly:
Maclaurin series evaluated term-by-term, with a tolerance-or-max-terms
stopping rule. No `math.sin`/`math.cos`/`math.tan` call appears anywhere in
this module or in tan_core.py — only +, -, *, / and abs().

Each function is testable in isolation (no GUI, no I/O), per D2-P5.2.
"""

from src.exceptions import ConvergenceError

SERIES_TOL = 1.0e-12
SERIES_N_MAX = 100


def maclaurin_sin(r, tol=SERIES_TOL, n_max=SERIES_N_MAX):
    """sin(r) via Maclaurin series. Assumes |r| <= pi/4 for fast convergence.

    Raises ConvergenceError if the per-term tolerance is not reached within
    n_max terms (REL-01 safeguard; not expected for |r| <= pi/4 in practice).
    """
    term = r
    total = r
    n = 1
    while abs(term) >= tol:
        if n > n_max:
            raise ConvergenceError(
                f"sin series did not converge to tol={tol:g} within "
                f"{n_max} terms (r={r!r})."
            )
        term = term * (-(r * r)) / ((2 * n) * (2 * n + 1))
        total += term
        n += 1
    return total


def maclaurin_cos(r, tol=SERIES_TOL, n_max=SERIES_N_MAX):
    """cos(r) via Maclaurin series. Assumes |r| <= pi/4 for fast convergence.

    Raises ConvergenceError if the per-term tolerance is not reached within
    n_max terms (REL-01 safeguard; not expected for |r| <= pi/4 in practice).
    """
    term = 1.0
    total = 1.0
    n = 1
    while abs(term) >= tol:
        if n > n_max:
            raise ConvergenceError(
                f"cos series did not converge to tol={tol:g} within "
                f"{n_max} terms (r={r!r})."
            )
        term = term * (-(r * r)) / ((2 * n - 1) * (2 * n))
        total += term
        n += 1
    return total
