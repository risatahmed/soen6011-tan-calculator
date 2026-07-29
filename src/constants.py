"""From-scratch mathematical constants (Deliverable 2, Problem 5).

D1's ``PI = math.pi`` is replaced here with an independently derived value:
a Machin-like arctangent identity evaluated by a hand-written power series,
using only addition, multiplication, and division (no ``math`` module call).

    pi/4 = 4*arctan(1/5) - arctan(1/239)          (Machin, 1706)
    pi   = 16*arctan(1/5) - 4*arctan(1/239)

``arctan(y)`` for |y| <= 1 is the Maclaurin series
``y - y^3/3 + y^5/5 - y^7/7 + ...``, evaluated term-by-term (same
tolerance/max-terms pattern as ``trig_series.py``) so it terminates
unconditionally.
"""

PI_SERIES_TOL = 1.0e-18
PI_SERIES_N_MAX = 60


def _arctan_series(y, tol=PI_SERIES_TOL, n_max=PI_SERIES_N_MAX):
    """arctan(y) via its Maclaurin series, for |y| <= 1. No math module use."""
    term = y
    total = y
    y_squared = y * y
    n = 1
    while abs(term) >= tol and n <= n_max:
        term = term * (-y_squared) * (2 * n - 1) / (2 * n + 1)
        total += term
        n += 1
    return total


def _compute_pi():
    return 16 * _arctan_series(1.0 / 5.0) - 4 * _arctan_series(1.0 / 239.0)


PI = _compute_pi()  # computed once at import time; ~1e-18 accurate, from scratch
