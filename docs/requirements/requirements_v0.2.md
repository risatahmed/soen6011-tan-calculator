# Problem 7 — Requirements Update, Baseline v0.2 (Deliverable 2)

Supersedes `requirements_v0.1.md` (frozen, retained for history per C-06 --
"iterative consistency"). This baseline incorporates evidence from the D2
implementation (`src/`), GUI (`src/gui.py`), and verification pass
(`docs/verification_matrix_d2.md`). Every changed requirement below states
what changed, why, and whether it was discovered through implementation.

## Changelog against v0.1

| ID | Change type | What changed | Discovered via |
|---|---|---|---|
| FR-02 | Revised | Now states the angle unit is stated **and selectable** (radians default, degrees optional), not radians-only. | Implementation (D-08): degrees mode added since "time permitted." |
| FR-07 *(new)* | Added | The system shall provide a labelled degrees input mode as a non-default alternative to radians. | Implementation (D-08). |
| USE-02 | Revised | "Textual interface" broadened to "at least one interface (textual and/or graphical)"; a new USE-03 covers the GUI specifically. | D2-P5.5: Tkinter GUI added alongside the retained CLI. |
| USE-03 *(new)* | Added | The system shall provide a Tkinter graphical interface with labelled controls, keyboard navigation, and errors shown in place (not by colour alone). | D2-P5.4/5.5 implementation + wireframe. |
| DEP-01 *(new)* | Added | The system's core computation (`src/tan_core.py`, `src/trig_series.py`, `src/constants.py`) shall not call `math.sin`, `math.cos`, `math.tan`, or `math.pi`, or any equivalent library trigonometric function. | D2-P5.1/5.2/5.3 "from-scratch" constraint; verified by `docs/from_scratch_boundary.md`. |
| ERR-03 *(new)* | Added | The system shall raise one of three documented exception types (`NumericalRangeError`, `DomainError`, `ConvergenceError`) for the corresponding failure condition, distinct from a generic `Exception`/`ValueError`, in both the CLI and GUI. | D2-P5.2 architecture: replaces D1's ad hoc `OutOfRangeError`/`NearPoleError` naming with the D2 architecture-note names, and adds `ConvergenceError` (not present in D1). |
| ACC-01 | Revised (tightened evidence, not the numeric bound) | Bound unchanged (`<= 1e-9` relative error), but now explicitly flagged as **tight, not comfortable** near the pole-tolerance boundary. | D2-P5.6 verification: the near-pole cases measured `3.83e-10`, the closest margin of any passing case (`docs/verification_matrix_d2.md`). |
| REL-03 *(new)* | Added | Neither `src/cli.py` nor `src/gui.py` shall present a raw Python traceback to the user for any of: invalid input, empty input, at/near-pole input, out-of-range input, or non-convergence. | D2-P5.5/5.6: GUI adds a fifth failure mode (`ConvergenceError`) beyond D1's two, all of which must stay caught. |
| DOC-02 *(new)* | Added | The from-scratch dependency boundary (what is/is not permitted, and why) shall be documented and kept current. | D2-P5.1 (`docs/from_scratch_boundary.md`). |

No v0.1 requirement was deleted; VAL-01 through VAL-04, FR-01/03/04/05/06,
ACC-02, USE-01, REL-01/02, ERR-01/02, and DOC-01 are carried forward
**unchanged** into v0.2 and remain in force (all still hold under the D2
implementation, confirmed by `docs/verification_matrix_d2.md`).

## Full requirements table (v0.2)

| ID | Statement | Rationale / Source | Priority | Verification Method |
|---|---|---|---|---|
| FR-01 | Accept a real-valued angle `x` entered by the user as text input. | Unchanged from v0.1. | Must | Test |
| FR-02 | State, before requesting `x`, that the default unit is radians, and how to select degrees instead. | Revised (D-08). | Must | Demonstration |
| FR-03 | For any `x` accepted under VAL-01--04 (after unit conversion), compute `tan(x) = sin(x)/cos(x)`. | Unchanged. | Must | Test |
| FR-04 | Display the computed `tan(x)` result as text. | Unchanged. | Must | Demonstration |
| FR-05 | Allow the user to submit a new value of `x` in the same session without restarting. | Unchanged. | Should | Test |
| FR-06 | Allow the user to exit through an explicit, documented command (CLI) or window close (GUI). | Unchanged (widened to cover GUI). | Must | Demonstration |
| FR-07 | Provide a labelled, non-default degrees input mode alongside the radians default. | New (D-08). | Should | Test |
| VAL-01 | Reject non-numeric input for `x`; identify it as non-numeric. | Unchanged. | Must | Test |
| VAL-02 | Reject empty (missing) input for `x`; identify it as missing. | Unchanged. | Must | Test |
| VAL-03 | Reject input whose `|x|` (after unit conversion) exceeds `1e4` radians; report as out of supported range. | Unchanged. | Must | Test |
| VAL-04 | Detect `x` within `1e-6` of a pole (`x = pi/2 + k*pi`) and treat as invalid rather than returning a numeric value. | Unchanged. | Must | Test |
| ACC-01 | For accepted `x` outside the pole-tolerance band and within range, compute `tan(x)` with relative error `<= 1e-9` vs. trusted references. Margin is tightest near the pole-tolerance boundary (measured `~3.83e-10`); not to be weakened without new evidence. | Revised evidence (still Must). | Must | Test (`docs/verification_matrix_d2.md`) |
| ACC-02 | Display the result to 10 significant figures. | Unchanged. | Should | Inspection |
| USE-01 | State the valid domain and angle unit before requesting `x`, in both interfaces. | Unchanged (widened to cover GUI). | Must | Demonstration |
| USE-02 | Provide at least one interface (textual and/or graphical) usable without a full IDE. | Revised (was CLI-only). | Must | Demonstration |
| USE-03 | Provide a Tkinter GUI with labelled controls, a sensible keyboard tab order, Enter-to-calculate/Esc-to-clear, and errors shown in place without relying on colour alone. | New. | Must | Demonstration |
| REL-01 | For every input, valid or invalid, return control to the user without an unhandled crash. | Unchanged. | Must | Test |
| REL-02 | Run from a terminal without depending on any specific IDE (`python3 -m src.cli` / `python3 -m src.gui`). | Unchanged. | Must | Demonstration |
| REL-03 | Neither interface shall present a raw traceback for any of the five documented failure modes (invalid, empty, near-pole, out-of-range, non-convergence). | New. | Must | Test |
| DEP-01 | The numerical core (`src/tan_core.py`, `src/trig_series.py`, `src/constants.py`) shall not call `math.sin`/`math.cos`/`math.tan`/`math.pi` or an equivalent library trig function. | New (D2 from-scratch constraint). | Must | Inspection (`docs/from_scratch_boundary.md`) |
| ERR-01 | On rejection under any VAL requirement, display a message naming the specific violated condition. | Unchanged. | Must | Test |
| ERR-02 | Never propagate an unhandled Python exception for an expected invalid-input, near-pole, or non-convergence case. | Revised (added non-convergence). | Must | Test |
| ERR-03 | Raise one of `NumericalRangeError`, `DomainError`, `ConvergenceError` for its corresponding condition, distinct from a bare `Exception`. | New. | Must | Test |
| DOC-01 | Document the assumed angle unit(s), supported range, near-pole tolerance, and displayed precision. | Unchanged. | Should | Inspection |
| DOC-02 | Document the from-scratch dependency boundary (permitted vs. prohibited) and keep it current with `src/`. | New. | Should | Inspection |

## Assumptions carried forward / revised

1. Radians remain the **default** angle unit; degrees is an explicit, labelled, non-default option (revises v0.1 assumption 1, which excluded degrees entirely).
2. Near-pole tolerance remains `1e-6`, unchanged and now exercised by `docs/verification_matrix_d2.md` (v0.1 assumption 2 is no longer "to be fixed" -- it is fixed and evidenced).
3. Supported range remains `|x| <= 1e4` radians (v0.1 assumption 3, unchanged; still provisional pending professor confirmation per the decision log).
4. No requirement in this baseline prescribes CORDIC vs. Maclaurin; Algorithm A was retained for D2 as an implementation decision (D-06), not a requirement.
5. "Numeric" input interpretation (v0.1 assumption 5) is unchanged; the optional `d:` degrees prefix (CLI) is parsed before, not instead of, that numeric check.

## Baseline

Frozen as **Requirements Baseline v0.2** for Deliverable 2. D3 (Problem 8, unit tests) must trace every Must-priority requirement above to at least one automated test case.
