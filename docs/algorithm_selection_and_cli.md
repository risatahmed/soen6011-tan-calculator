# Problem 4 — Algorithm Selection + Python CLI (Step 5)

## Part 1 — Selection mind map (summary)

See `docs/mindmaps/algorithm_selection_mindmap.png` (source: `.dot` file in the same folder). Central concept: "Algorithm for tan(x)". Criteria: accuracy; domain coverage/pole handling; numerical stability near +/- pi/2 and for large `|x|`; implementation effort; suitability for a from-scratch D2 reimplementation; performance; explainability to the persona.

| Criterion | Algorithm A (Maclaurin series) | Algorithm B (CORDIC) |
|---|---|---|
| Accuracy | Excellent — super-linear (factorial) convergence, ~10-15 terms for `1e-12` | Good — linear convergence, ~40 iterations for comparable precision |
| Pole handling | Guard on `\|cos(r)\|` after series evaluation | Guard on `\|sin(r)\|` after `N_MAX` rotations (same guard shape) |
| Stability (large `\|x\|`) | Limited by shared PI-reduction error | Same shared limitation (reduction step is common to both) |
| Implementation effort | **Low** — direct series recurrence, no precomputed table | Moderate — needs a precomputed `arctan(2^-i)` table |
| D2 from-scratch suitability | Needs from-scratch multiply/divide (already computes its own sin/cos) | **Strong fit** — only add/subtract/shift in the hot loop |
| Performance | Fewer iterations, each a real multiply+divide | More iterations, each a trivial shift+add |
| Explainability to persona (Maya) | **High** — "the same Taylor series from calculus" | Moderate — needs a vector-rotation mental model |

**Selection: Algorithm A (range reduction + Maclaurin series).** It is the simplest way to *faithfully implement an actual algorithm* today (not just call a library `tan`), it is the most explainable to the persona, and its implementation effort is lowest for this prototype. Algorithm B's main advantage — a multiplication-free hot loop — is a D2 concern (the "from scratch, no built-ins" constraint), not a D1 one, so it does not outweigh A's simplicity here. This selection will be revisited in Deliverable 2, where B's from-scratch suitability becomes directly relevant.

## Part 2 — Python CLI implementation

Source: [`src/cli.py`](../src/cli.py). Structure:

- **Compute layer** (`maclaurin_sin`, `maclaurin_cos`, `tan_by_series`) — pure functions, no I/O, independently callable/testable; implements Algorithm A exactly as specified in `docs/algorithms/algorithm_A_maclaurin.md`.
- **I/O layer** (`run_cli`, `parse_x`, `format_result`, `BANNER`) — all prompting, reading, and printing; depends on the compute layer but not vice versa (traces to the "compute independent of I/O" restriction).
- **Exceptions:** `OutOfRangeError` (VAL-03) and `NearPoleError` (VAL-04) are custom exception classes raised by the compute layer and caught individually in the I/O loop, each producing a distinct, helpful message (ERR-01) — never an unhandled traceback (ERR-02, REL-01).
- **Angle unit + domain hint:** stated up front in `BANNER` before the first prompt (USE-01, FR-02).
- **Precision:** results displayed to 10 significant figures via `format_result` (ACC-02), documented in the banner text itself (DOC-01).

### Which `math` calls will need from-scratch replacement in D2

This implementation already computes `sin`/`cos` itself via the Maclaurin series (Algorithm A) rather than calling `math.sin`/`math.cos` — those two calls do **not** appear anywhere in the compute path. The one remaining standard-library dependency is:

- **`PI = math.pi`** — a finite-precision constant. In D2 ("from scratch", no built-in library functions beyond arithmetic/I/O/UI), this must be replaced by an independently derived value of pi (e.g., a fixed literal decimal expansion, or a from-scratch convergent series such as a Machin-like arctan formula, computed without relying on `math.pi`).

No other `math` module calls are used in `tan_by_series`, `maclaurin_sin`, or `maclaurin_cos`.

### Sample runs

Full transcripts and rendered images are in `docs/screenshots/` (see `docs/screenshots/README.md` for the exact commands). Summary:

| Case | Input | Output | Matches reference? |
|---|---|---|---|
| Valid (special value) | `x = pi/4 = 0.7853981633974483` | `tan(0.7853981634) = 1` | Yes — `docs/research_notes.md` |
| Negative argument (odd symmetry) | `x = -pi/4` | `tan(-0.7853981634) = -1` | Yes |
| Boundary/near-pole | `x = pi/2 - 1e-9` | `Cannot compute tan(x): x is at or within tolerance of a pole ...` | Yes — correctly rejected, not a huge number |
| Invalid (non-numeric) | `x = "abc"` | `Invalid input: 'abc' is not a valid real number. ...` | N/A — expected rejection |
| Missing input | `x = ""` (empty line) | `Invalid input: No input received. ...` | N/A — expected rejection |
| Large argument (supported) | `x = 1000` | `tan(1000) = 1.470324156` | Yes — matches `math.tan(1000)` to displayed precision |
| Large argument (out of range) | `x = 1e10` | `Input out of range: \|x\| = 1e+10 exceeds the supported range \|x\| <= 10000 radians.` | N/A — expected rejection |

Command used: `python3 src/cli.py` (interactive), or `printf '<inputs>\n' | python3 src/cli.py` for scripted/repeatable runs as shown in `docs/screenshots/README.md`.
