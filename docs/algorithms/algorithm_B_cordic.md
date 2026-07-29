# Problem 3 — Algorithm B: CORDIC (Circular Mode, Rotation Mode)

Satisfies (traces to): ACC-01, VAL-03, VAL-04, REL-01 — same requirement set as Algorithm A, by a structurally different method (shift-and-add vector rotation instead of a power series). Pseudocode convention as in Algorithm A (Cormen et al. style).

## Inputs / outputs / constants

- **Input:** `x`, a real number (radians).
- **Output:** an approximation to `tan(x)`, or an exceptional signal (`RANGE-ERROR`, `POLE-ERROR`).
- **Constants (fixed before running, documented per DOC-01):**
  - `PI`, `X_MAX`, `EPSILON` — same meaning as in Algorithm A.
  - `A[0 .. N_MAX-1]` — a **precomputed table** of `A[i] = arctan(2^-i)`, computed once offline (not at run time, and not via a built-in `arctan` inside this algorithm — it is supplied as a constant table, consistent with the "no built-in trig" restriction).
  - `N_MAX` — fixed number of CORDIC iterations (guaranteed-termination safeguard; also fixes the achievable precision, since CORDIC gains roughly one bit of precision per iteration).
- **Preconditions:** same domain preconditions as Algorithm A; additionally, the reduced angle `r` (see below) must lie within CORDIC's convergence radius (`sum of all A[i] ≈ 1.7433` rad), which the `[-pi/4, pi/4]` reduction target satisfies with a wide margin.
- **Postconditions:** same postcondition shape as Algorithm A — a bounded relative-error approximation to `tan(x)`, or an exceptional signal.

## Subordinate functions / range reduction

CORDIC reuses the identical sign-and-quadrant reduction as Algorithm A (odd symmetry + reduction modulo `π/2`) to bring the working angle into `[-pi/4, pi/4]` before rotating, and the identical `tan(r + π/2) = -cos(r)/sin(r)` correction when `j = 1`. This reduction step is shared infrastructure, not part of what makes the two algorithms "different" — the difference is in how `sin(r)`/`cos(r)` themselves are produced.

```
TAN-BY-CORDIC(x, PI, X_MAX, EPSILON, A[0..N_MAX-1], N_MAX)
 1  if |x| > X_MAX
 2      signal RANGE-ERROR                          ▷ VAL-03
 3      return
 4  s ← 1
 5  if x < 0                                         ▷ odd symmetry
 6      x ← -x
 7      s ← -s
 8  k ← ROUND(x / (PI / 2))
 9  r ← x - k · (PI / 2)                              ▷ r ∈ [-π/4, π/4]
10  j ← k mod 2
11  (cosR, sinR) ← CORDIC-ROTATE(r, A, N_MAX)
12  if j = 0
13      num ← sinR
14      den ← cosR
15  else                                              ▷ tan(r + π/2) = -cos(r) / sin(r)
16      num ← -cosR
17      den ← sinR
18  if |den| < EPSILON
19      signal POLE-ERROR                            ▷ VAL-04
20      return
21  return s · (num / den)

CORDIC-ROTATE(r, A[0..N_MAX-1], N_MAX)
 1  vx ← 1                                           ▷ initial unit vector (unscaled)
 2  vy ← 0
 3  z ← r
 4  for i ← 0 to N_MAX - 1                            ▷ fixed iteration count: max-work safeguard
 5      if z ≥ 0
 6          d ← +1
 7      else
 8          d ← -1
 9      vx_next ← vx - d · vy · 2^(-i)                ▷ shift, not divide: 2^-i is a right-shift
10      vy_next ← vy + d · vx · 2^(-i)
11      z ← z - d · A[i]
12      vx ← vx_next
13      vy ← vy_next
14  K ← GAIN-CONSTANT(N_MAX)                          ▷ K = product of cos(A[i]) for i = 0..N_MAX-1, precomputed
15  return (vx / K, vy / K)                            ▷ (cos(r), sin(r))
```

*Optimization note (not required for correctness): because `tan(r) = sin(r)/cos(r) = (K · sin(r)) / (K · cos(r)) = vy / vx`, the gain constant `K` cancels exactly when only `tan` is needed — line 14/15's division by `K` can be skipped and `TAN-BY-CORDIC` may use `vy / vx` directly. `K` is still needed if `sin`/`cos` must be reported individually (out of scope here but relevant to a future extension).*

## Termination

`CORDIC-ROTATE`'s `for` loop runs exactly `N_MAX` times — a fixed, input-independent iteration count, so it terminates unconditionally (a stronger and simpler guarantee than Algorithm A's tolerance-or-max-terms `while` loop). `TAN-BY-CORDIC` itself is straight-line with two guarded exceptional exits, terminating given `CORDIC-ROTATE` terminates.

## Complexity

`CORDIC-ROTATE` performs exactly `N_MAX` iterations, each with **only additions/subtractions and a binary shift** (`2^-i`) — no multiplication or division inside the loop, unlike Algorithm A's series terms which require a real multiplication and division per term. Overall cost is `O(N_MAX)` shift-add operations. Because CORDIC converges linearly (approximately one bit of precision per iteration, verified below), matching Algorithm A's `1e-12`-relative-error target requires roughly `N_MAX ≈ 40` iterations here, versus roughly `10–15` terms for Algorithm A — more iterations, but each one is arithmetically far cheaper.

## Known numerical weaknesses

1. **Linear convergence rate.** Each iteration gains roughly one bit of accuracy; reaching a target precision requires a fixed, comparatively large `N_MAX`, unlike Algorithm A's faster (factorial-denominator) convergence per term.
2. **Finite angle-table length.** `A[0..N_MAX-1]` is precomputed to fixed precision; if the table itself is not precise enough (or too short), the ultimate achievable accuracy is capped regardless of `N_MAX` — a different but analogous limitation to Algorithm A's finite-precision `PI` constant.
3. **Shared range-reduction risk.** Because CORDIC reuses Algorithm A's reduction step, it inherits the same argument-reduction error growth for large `|x|` and the same near-pole precision loss just outside the `EPSILON` band (both discussed under Algorithm A).

## Worked trace — `tan(pi/4) = 1`

Reduction (identical mechanism to Algorithm A): `x = pi/4`, `s = 1`, `k = ROUND(0.5) = 0` (round-half-to-even), `r = pi/4 ≈ 0.7853981634`, `j = 0`.

`CORDIC-ROTATE(r, A, N_MAX)`, starting from `(vx, vy, z) = (1, 0, 0.7853981634)`:

| i | d | vx | vy | z | vy/vx |
|---|---|---|---|---|---|
| 0 | +1 | 1.0000000 | 1.0000000 | 0.0000000 | 1.0000000 |
| 1 | +1 | 0.5000000 | 1.5000000 | -0.4636476 | 3.0000000 |
| 2 | -1 | 0.8750000 | 1.3750000 | -0.2186689 | 1.5714286 |
| 3 | -1 | 1.0468750 | 1.2656250 | -0.0943140 | 1.2089552 |
| 4 | -1 | 1.1259766 | 1.2001953 | -0.0318951 | 1.0659150 |
| 5 | -1 | 1.1634827 | 1.1650085 | -0.0006553 | 1.0013115 |
| 6 | -1 | 1.1816859 | 1.1468291 | 0.0149684 | 0.9705025 |
| 7 | +1 | 1.1727263 | 1.1560610 | 0.0071561 | 0.9857893 |
| ... | | | | | (continues) |
| 9 | | | | | 0.9974099 |
| 19 | | | | | 0.9999967 |
| 29 | | | | | 0.9999999993 |
| 39 | | | | | 1.0000000000 |

(Table values obtained by direct hand/tool computation of the recurrence above — `A[i] = arctan(2^-i)` — to confirm the pseudocode is correct, not by calling a built-in `tan`.)

At `i = 0`, `j = 0`, so `num = vy = 1.1560610` (using `i=7` row for illustration) is not yet the final answer — the ratio `vy/vx` is read only after the full `N_MAX` iterations. By `i = 39`, `vy/vx = 1.000000000000`, matching the reference value `tan(pi/4) = 1`. This also demonstrates the linear-convergence weakness directly: after only 7 of 40 iterations the ratio is still `0.986`, three orders of magnitude short of the final precision, whereas Algorithm A's series reached 6-digit accuracy after only 4 terms.

## Confirmation: A and B are genuinely different

Algorithm A is **analytic/series-based**: it evaluates two independent truncated power series and forms their ratio, with real multiplication and division at every term, and a convergence rate governed by factorial growth in the denominator. Algorithm B is **iterative/geometric**: it rotates a vector step-by-step using only additions, subtractions, and power-of-two shifts, drawing on a precomputed constant table, with a fixed iteration count and linear convergence. They differ in their core arithmetic primitives, their convergence-rate class, their termination mechanism (tolerance-or-cap vs. fixed count), and their suitability for a future from-scratch, multiplication-free implementation (Algorithm B) versus one that still needs general multiplication/division (Algorithm A). These are not superficial variants of the same idea.
