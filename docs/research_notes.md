# Step 1 — Research Notes: the Tangent Function tan(x)

## 1. Definition and core properties

- **Definition:** `tan(x) = sin(x) / cos(x)`, for real `x`.
- **Domain:** all real numbers except the poles `x = pi/2 + k*pi` (k an integer), where `cos(x) = 0`.
- **Range:** all real numbers (unlike `sin`/`cos`, which are bounded to `[-1, 1]`).
- **Period:** `pi` (not `2*pi` like sine/cosine) — `tan(x + pi) = tan(x)`.
- **Symmetry:** odd — `tan(-x) = -tan(x)`.
- **Monotonicity:** strictly increasing on each open interval between consecutive poles, e.g. on `(-pi/2, pi/2)`.
- **Poles/asymptotes:** vertical asymptotes at every `x = pi/2 + k*pi`; `tan(x) -> +infinity` as `x -> (pi/2)^-` and `tan(x) -> -infinity` as `x -> (pi/2)^+` (and symmetric behaviour at every other pole).
- **Zeros:** `tan(x) = 0` exactly at `x = k*pi`.

## 2. Special values (used as the reference/verification anchors)

| x (radians) | exact tan(x) | decimal (15 sig. figs) |
|---|---|---|
| 0 | 0 | 0.000000000000000 |
| pi/6 | 1/sqrt(3) = sqrt(3)/3 | 0.577350269189626 |
| pi/4 | 1 | 1.000000000000000 |
| pi/3 | sqrt(3) | 1.732050807568877 |

These four are the standard "unit circle" special angles and form the backbone of both the reference-value table (Section 4) and the worked traces used in Problem 3 (Step 4).

## 3. Applications (why a persona would want this function)

- **Trigonometry / geometry:** relating an angle to the ratio of opposite/adjacent sides in a right triangle; computing unknown side lengths or angles.
- **Slope and angle of elevation/depression:** `slope = tan(theta)` for a line making angle `theta` with the horizontal — used in civil engineering, road/ramp grading, and surveying.
- **Physics:** projectile motion (range and trajectory equations involve `tan(launch angle)`); optics (refraction and lens equations); AC circuit phase angle (`tan(phi) = X/R`).
- **Signal processing:** phase relationships, filter design.
- **Computer graphics:** field-of-view and perspective-projection matrices commonly use `tan(fov/2)`.
- **Surveying / navigation:** triangulation calculations that recover distances from angle measurements.

## 4. Reference-value table (trusted values for later verification)

This table is the "ground truth" the CLI/tests will be checked against in Step 6 (verification matrix) and D2/D3. Values computed to 15 significant figures using exact/high-precision identities, not the algorithms under test.

| Case | x (radians) | Expected tan(x) | Notes |
|---|---|---|---|
| Zero | `0` | `0.000000000000000` | exact zero, sanity check |
| Special: pi/6 | `0.5235987755982988` | `0.577350269189626` | `1/sqrt(3)` |
| Special: pi/4 | `0.7853981633974483` | `1.000000000000000` | exact `1`; primary worked-trace case |
| Special: pi/3 | `1.0471975511965976` | `1.732050807568877` | `sqrt(3)` |
| Negative argument (odd symmetry) | `-0.7853981633974483` (`-pi/4`) | `-1.000000000000000` | must equal `-tan(pi/4)`; verifies odd symmetry |
| Small positive | `0.1` | `0.100334672085451` | near-zero regime, tests cancellation-free behaviour |
| Near pole (approaching from below) | `1.5707963267948966 - 1e-6` (`pi/2 - 1e-6`) | `999999.999999...` (~`1.0e6`) | value grows without bound; used to validate the near-pole guard triggers *before* returning a huge number |
| Beyond one period | `pi + pi/4` = `3.9269908169872414` | `1.000000000000000` | tests period-`pi` reduction: should equal `tan(pi/4)` |
| Large argument | `1000.0` | `1.470324155702719` (via high-precision reduction of `1000 mod pi`) | tests argument-reduction accuracy at magnitude far from the origin |
| Negative pole-adjacent | `-1.5707963267948966 + 1e-6` (`-pi/2 + 1e-6`) | `-999999.999999...` (~`-1.0e6`) | mirrors the near-pole case under odd symmetry |

*(Large-argument and near-pole rows are recomputed with a high-precision reference, e.g. Python's `decimal`/`mpmath` at D2/D3 time, since D1's own algorithms are exactly what is being verified against them — using `math.tan` from D1's prototype as ground truth would be circular.)*

## 5. Numerical risks identified

1. **Poles / asymptotes.** As `x` approaches `pi/2 + k*pi`, `cos(x) -> 0`, so `sin(x)/cos(x)` blows up; naive division returns an enormous or infinite/`NaN` value instead of a meaningful error. Any implementation must detect `|cos(x)|` below a tolerance and refuse/flag rather than divide.
2. **Argument-reduction error for large `|x|`.** Because `pi` is irrational, reducing a large `x` modulo `pi` (or `2*pi`) using a *finite-precision* approximation of `pi` accumulates error proportional to `|x|`; the larger the argument, the less trustworthy the reduced angle, and therefore the less trustworthy the result. This bounds the practically supported input range.
3. **Slow series convergence near +/- pi/2.** Any power-series approach to `sin`/`cos` (Algorithm A) needs the reduced angle to be small (e.g., within `[-pi/4, pi/4]`) for fast convergence; angles reduced close to the interval boundary near a pole still leave `cos(x)` small, so the *division* remains ill-conditioned even if the series itself converges fine.
4. **Overflow near poles.** A very small `cos(x)` in the denominator can produce a floating-point overflow or a value at the edge of representable range, rather than a clean error.
5. **Catastrophic cancellation.** When accumulating alternating-sign series terms (Maclaurin series for `sin`/`cos`), or when angle-reduction subtracts a large multiple of `pi` from a large `x`, the subtraction of nearly-equal large numbers can cancel significant digits, degrading precision even before the series is summed.

## 6. Sources

Special values, identities, and the pole/period structure follow standard trigonometric references (see `docs/references.bib`: `abramowitz1964`, `nist_dlmf`). Numerical-risk analysis (argument reduction, cancellation, convergence) follows standard floating-point/numerical-methods treatment (`muller2016`).
