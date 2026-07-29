# Step 6 — Verification Matrix (D1-P4.3)

Each row ties a requirement (`docs/requirements/requirements_v0.1.md`) to a concrete demo case run against `src/cli.py`, compared to the trusted reference in `docs/research_notes.md` (Section 4) or an independent `math.tan`/`math.atan` check (never the CLI's own output used as its own reference). All raw transcripts are in `docs/screenshots/`.

| Requirement ID | Demo case | Input `x` | Reference value | CLI result | Verdict |
|---|---|---|---|---|---|
| FR-01, FR-03, FR-04, ACC-01 | Valid special value | `pi/4 = 0.7853981633974483` | `tan(pi/4) = 1.000000000` | `tan(0.7853981634) = 1` | **Pass** |
| FR-03, ACC-01, VAL-04 (odd-symmetry / negative argument) | Negative argument | `-pi/4 = -0.7853981633974483` | `tan(-pi/4) = -1.000000000` | `tan(-0.7853981634) = -1` | **Pass** — confirms `tan(-x) = -tan(x)` |
| ACC-01 | Special value | `pi/6 = 0.5235987755982988` | `0.5773502692` | `tan(0.5235987756) = 0.5773502692` | **Pass** |
| ACC-01 | Special value | `pi/3 = 1.0471975511965976` | `1.732050808` | `tan(1.047197551) = 1.732050808` | **Pass** |
| VAL-04, ERR-01, ERR-02, REL-01 (near-pole, positive side) | Boundary/near-pole | `pi/2 - 1e-9 = 1.5707963257948965` | undefined (pole); `math.tan` returns `~1.06e9`, a meaningless-for-users huge number | `Cannot compute tan(x): x is at or within tolerance of a pole ...` | **Pass** — rejected helpfully instead of returning a huge number |
| VAL-04, ERR-01, ERR-02, REL-01 (near-pole, negative side) | Boundary/near-pole | `-pi/2 = -1.5707963267948965` | undefined (pole) | `Cannot compute tan(x): x is at or within tolerance of a pole ...` | **Pass** |
| VAL-01, ERR-01, REL-01 | Invalid (non-numeric) | `"abc"` | n/a — must be rejected | `Invalid input: 'abc' is not a valid real number. ...` | **Pass** — no traceback |
| VAL-02, ERR-01, REL-01 | Invalid (missing) | `""` (empty line) | n/a — must be rejected | `Invalid input: No input received. ...` | **Pass** |
| ACC-01, VAL-03 (large but supported) | Large argument | `1000` | `1.470324156` (`math.tan(1000) = 1.4703241557...`) | `tan(1000) = 1.470324156` | **Pass** — matches to all 10 displayed significant figures |
| VAL-03, ERR-01, REL-01 (out of range) | Invalid (extreme magnitude) | `1e10` | n/a — must be rejected, exceeds `X_MAX = 1e4` | `Input out of range: \|x\| = 1e+10 exceeds the supported range \|x\| <= 10000 radians.` | **Pass** |
| FR-05, FR-06, USE-01, USE-02, REL-02 | Session behaviour | multiple values then `quit`; also EOF without `quit` | must accept repeated input and exit cleanly either way | Multiple computations accepted in one run; both `quit` and raw EOF exit without a crash (see `docs/screenshots/` transcripts and the ad hoc EOF test) | **Pass** |
| DOC-01, ACC-02 | Documentation/precision | n/a | precision and domain must be stated up front | Banner states radians-only, `\|x\| <= 1e4`, near-pole rejection policy, and "10 significant figures" before the first prompt | **Pass** |

## Known limitations (honest disclosure)

1. **Large-argument accuracy degrades gradually, not sharply, as `|x|` grows.** `X_MAX = 1e4` is a documented cutoff, but accuracy already begins degrading below that limit because `PI = math.pi` is only a finite-precision approximation of `pi`; the reduction `x - k*(pi/2)` accumulates more absolute error as `k` grows. This D1 prototype does not yet quantify *where between 0 and 1e4* the relative-error bound in ACC-01 stops holding — that characterization is deferred to D2/D3 testing with a higher-precision reference (e.g. `mpmath`/`decimal`).
2. **Near-pole tolerance (`POLE_EPSILON = 1e-6`) is a provisional constant**, not yet confirmed with the professor (decision log D-02). A different tolerance would shift the boundary between "rejected as near-pole" and "computed as a large-but-finite value."
3. **`X_MAX = 1e4` is likewise provisional** (decision log D-03), pending professor confirmation, not derived from a rigorous error-propagation bound.
4. **No performance/timing requirement was verified** — a `PERF` category was considered during the Problem 2 quality review and deliberately deferred (see `docs/requirements/requirements_v0.1.md`, review findings), so no timing measurements are reported here.
5. **The reference values used for verification above 4 decimal places rely on Python's `math.tan`**, which is itself a finite-precision floating-point implementation, not an arbitrary-precision oracle. This is adequate for the `1e-9`–`1e-10` relative-error target in this deliverable but would need a higher-precision reference (e.g. `mpmath`) if tolerance requirements tighten in D2/D3.
