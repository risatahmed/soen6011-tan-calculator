# Problem 3 — Algorithm A: Range Reduction + Maclaurin Series

Satisfies (traces to): ACC-01 (accuracy tolerance vs. reference values), VAL-03 (range check), VAL-04 (pole detection), REL-01 (no unhandled failure). Pseudocode convention follows the Cormen et al. (*Introduction to Algorithms*) style: `Procedure(args)`, 1-indexed numbered lines, `▷` for inline comments, `signal` for exceptional termination.

## Inputs / outputs / constants

- **Input:** `x`, a real number (radians).
- **Output:** an approximation to `tan(x)`, or an exceptional signal (`RANGE-ERROR`, `POLE-ERROR`).
- **Constants (fixed before running, documented per DOC-01):**
  - `PI` — a fixed finite-precision approximation of the constant π.
  - `X_MAX` — largest supported `|x|` (VAL-03; provisionally `1e4`, see decision log D-03).
  - `EPSILON` — pole-proximity tolerance (VAL-04); an accepted `x` is rejected as a pole if the reduced denominator's magnitude falls below `EPSILON`.
  - `TOL` — per-term series stopping tolerance (drives ACC-01).
  - `N_MAX` — maximum number of series terms (guaranteed-termination safeguard).
- **Preconditions:** `PI`, `EPSILON`, `TOL`, `N_MAX`, `X_MAX` are fixed positive constants set so that ACC-01's relative-error bound is achievable.
- **Postconditions:** if `|x| <= X_MAX` and `x` is not within `EPSILON` of a pole, returns `r` with `|r - tan(x)| / |tan(x)| <= TOL`-derived bound; otherwise signals `RANGE-ERROR` or `POLE-ERROR` and returns no numeric value.

## Subordinate functions

`MACLAURIN-SIN` and `MACLAURIN-COS` are treated as separately defined subordinate procedures (no built-in `sin`/`cos`/`tan` is assumed), per the Problem 3 restriction.

```
TAN-BY-SERIES(x, PI, X_MAX, EPSILON, TOL, N_MAX)
 1  if |x| > X_MAX
 2      signal RANGE-ERROR                          ▷ VAL-03
 3      return
 4  s ← 1
 5  if x < 0                                         ▷ odd symmetry: tan(-x) = -tan(x)
 6      x ← -x
 7      s ← -s
 8  k ← ROUND(x / (PI / 2))                          ▷ nearest multiple of π/2; round-half-to-even
 9  r ← x - k · (PI / 2)                              ▷ r ∈ [-π/4, π/4]
10  j ← k mod 2
11  sinR ← MACLAURIN-SIN(r, TOL, N_MAX)
12  cosR ← MACLAURIN-COS(r, TOL, N_MAX)
13  if j = 0
14      num ← sinR
15      den ← cosR
16  else                                              ▷ tan(r + π/2) = -cos(r) / sin(r)
17      num ← -cosR
18      den ← sinR
19  if |den| < EPSILON
20      signal POLE-ERROR                            ▷ VAL-04
21      return
22  return s · (num / den)

MACLAURIN-SIN(r, TOL, N_MAX)
 1  term ← r
 2  sum ← r
 3  n ← 1
 4  while |term| ≥ TOL and n ≤ N_MAX                 ▷ max-work safeguard: n ≤ N_MAX
 5      term ← term · (-(r · r)) / ((2n) · (2n + 1))
 6      sum ← sum + term
 7      n ← n + 1
 8  return sum

MACLAURIN-COS(r, TOL, N_MAX)
 1  term ← 1
 2  sum ← 1
 3  n ← 1
 4  while |term| ≥ TOL and n ≤ N_MAX                 ▷ max-work safeguard: n ≤ N_MAX
 5      term ← term · (-(r · r)) / ((2n - 1) · (2n))
 6      sum ← sum + term
 7      n ← n + 1
 8  return sum
```

## Termination

`TAN-BY-SERIES` has no loops of its own — it is straight-line code with two guarded exceptional exits, so it terminates unconditionally given that its two subordinate calls terminate. `MACLAURIN-SIN`/`MACLAURIN-COS` each terminate because their `while` loop is bounded by `n ≤ N_MAX` regardless of whether the tolerance condition is ever met — the max-work safeguard guarantees termination even if `TOL` is set unrealistically small.

## Complexity

Each `MACLAURIN-*` call performs `O(N_MAX)` arithmetic operations (multiplications, additions), where `N_MAX` is a fixed constant chosen once for the target precision — in practice `~10–15` terms suffice for a `1e-12` relative-error target at `|r| <= pi/4`, since the series' factorial-growing denominator gives super-linear (better than linear) convergence per term. `TAN-BY-SERIES` itself is `O(1)` beyond the two series calls, so overall cost is `O(N_MAX)`, independent of `|x|` after reduction.

## Known numerical weaknesses

1. **Argument-reduction error for large `|x|`.** `PI` is a finite-precision approximation; subtracting `k · (PI/2)` from `x` amplifies the representation error of `PI` proportionally to `k` (and hence to `|x|`), degrading `r`'s accuracy — and therefore the final result — as `|x|` grows (this is the concrete mechanism behind the VAL-03 range limit).
2. **Catastrophic cancellation.** For large `x`, `x` and `k · (PI/2)` are both large and nearly equal, so their subtraction (line 9) can cancel significant digits before the series is even evaluated.
3. **Near-pole precision loss just outside the guard band.** Just outside the `EPSILON` threshold, `den` is small but not rejected, so the division on line 22 is ill-conditioned and amplifies any upstream rounding error in `sinR`/`cosR`.

## Worked trace — `tan(pi/4) = 1`

Let `x = pi/4 ≈ 0.7853981634`, well within `X_MAX`, not near a pole.

1. Line 1: `|x| = 0.7854 <= X_MAX` — no range error.
2. Lines 4–7: `x > 0`, so `s = 1`, `x` unchanged.
3. Line 8: `k = ROUND((pi/4) / (pi/2)) = ROUND(0.5)`. Using round-half-to-even, `ROUND(0.5) = 0`, so `k = 0`.
4. Line 9: `r = x - 0 · (pi/2) = pi/4 ≈ 0.7853981634`.
5. Line 10: `j = 0 mod 2 = 0`.
6. `MACLAURIN-SIN(r, ...)`: `term_0 = r = 0.7853981634`, `sum = 0.7853981634`.
   - `n=1`: `term_1 = term_0 · (-(r²))/(2·3) = 0.7853981634 · (-0.6168503) / 6 ≈ -0.0807504`; `sum ≈ 0.7046478`.
   - `n=2`: `term_2 = term_1 · (-(r²))/(4·5) ≈ 0.0024917`; `sum ≈ 0.7071395`.
   - `n=3`: `term_3 ≈ -0.0000368`; `sum ≈ 0.7071027`.
   - `n=4`: `term_4 ≈ 0.00000031`; `sum ≈ 0.70710678` — converging to `sin(pi/4) ≈ 0.70710678`; loop continues until `|term| < TOL` (a few more terms for `TOL = 1e-12`).
7. `MACLAURIN-COS(r, ...)` converges analogously to `cos(pi/4) ≈ 0.70710678` (same magnitude by symmetry of the special angle).
8. Line 13: `j = 0`, so `num = sinR ≈ 0.70710678`, `den = cosR ≈ 0.70710678`.
9. Line 19: `|den| = 0.7071 >= EPSILON` — no pole signalled.
10. Line 22: return `s · (num/den) = 1 · (0.70710678 / 0.70710678) = 1`.

Result: `TAN-BY-SERIES(pi/4) = 1`, matching the reference value in `docs/research_notes.md`.
