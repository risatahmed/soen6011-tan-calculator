"""Pure, from-scratch tan(x) numerical core (Deliverable 2, Problem 5).

`tan(x, tolerance, max_terms)` is the single entry point required by the D2
architecture note: it has no I/O, no GUI dependency, and can be imported and
tested on its own (D2-P5.2 "testable without launching GUI").

Pipeline: validate range (VAL-03) -> apply odd symmetry tan(-x) = -tan(x) ->
reduce modulo pi/2 using the from-scratch PI (constants.py) -> evaluate
sin/cos of the reduced angle via the from-scratch series (trig_series.py) ->
recombine per quadrant -> guard the division against a near-zero denominator
(VAL-04). No `math.sin`/`math.cos`/`math.tan` is called anywhere in this
path.
"""

from src.constants import PI
from src.exceptions import DomainError, NumericalRangeError
from src.trig_series import SERIES_N_MAX, SERIES_TOL, maclaurin_cos, maclaurin_sin

X_MAX = 1.0e4          # VAL-03: largest supported |x|, in radians
POLE_EPSILON = 1.0e-6  # VAL-04: |denominator| below this is treated as "at/near a pole"


def tan(x, tolerance=SERIES_TOL, max_terms=SERIES_N_MAX, x_max=X_MAX, pole_epsilon=POLE_EPSILON):
    """Compute tan(x), x in radians, entirely from scratch.

    Raises NumericalRangeError if |x| > x_max (VAL-03).
    Raises DomainError if x is at/within pole_epsilon of a pole x = pi/2 + k*pi (VAL-04).
    Raises ConvergenceError (propagated from trig_series) if a series fails
    to converge within max_terms (REL-01 safeguard).
    """
    if abs(x) > x_max:
        raise NumericalRangeError(
            f"|x| = {abs(x):.6g} exceeds the supported range |x| <= {x_max:g} radians."
        )

    sign = 1.0
    reduced_x = x
    if reduced_x < 0:
        reduced_x = -reduced_x
        sign = -1.0  # tan(-x) = -tan(x): odd symmetry (shrinks the argument's sign, not magnitude)

    k = round(reduced_x / (PI / 2))       # nearest multiple of pi/2
    r = reduced_x - k * (PI / 2)          # r in [-pi/4, pi/4]; also exploits period pi via k's parity
    quadrant_flip = (k % 2) == 1

    sin_r = maclaurin_sin(r, tolerance, max_terms)
    cos_r = maclaurin_cos(r, tolerance, max_terms)

    if quadrant_flip:                     # tan(r + pi/2) = -cos(r) / sin(r)
        numerator, denominator = -cos_r, sin_r
    else:
        numerator, denominator = sin_r, cos_r

    if abs(denominator) < pole_epsilon:
        raise DomainError(
            "x is at or within tolerance of a pole (x = pi/2 + k*pi), "
            "where cos(x) is approximately zero and tan(x) is undefined."
        )

    return sign * (numerator / denominator)
