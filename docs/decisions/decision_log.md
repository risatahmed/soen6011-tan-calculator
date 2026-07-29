# Decision Log — F2 tan(x), Deliverable 1

Running log of non-trivial decisions made during D1, with rationale. Newest entries at the bottom.

| # | Date | Decision | Rationale | Alternatives considered | Status |
|---|------|----------|-----------|--------------------------|--------|
| D-01 | 2026-07-15 | Angle unit for `x` is **radians** by default; degrees may be offered later only as a clearly-labelled convenience option, never as the internal representation. | Matches the mathematical definition of `tan`, avoids silent conversion bugs, and is the working assumption stated in the task list. | Degrees-first UI with internal conversion. | **Provisional — pending professor confirmation (Step 0 action item, see below).** |
| D-02 | 2026-07-15 | Near-pole policy: treat any `x` with `|cos(x)|` below a small tolerance `epsilon` (or `x` within `epsilon` of `pi/2 + k*pi`) as an error condition to be reported helpfully, not computed. | Prevents returning meaningless huge/`inf` values; matches ERR/VAL requirement direction in the task list. | Silently returning `inf`/`-inf`; clamping to a max magnitude. | **Provisional — pending professor confirmation.** |
| D-03 | 2026-07-15 | Supported large-argument range: `|x| <= 1e4` radians; beyond that, accuracy is not guaranteed and the tool should say so rather than silently degrade. | Argument reduction modulo pi accumulates error because pi is irrational and only representable to finite precision; stated explicitly per task list guidance. | Unbounded input range with no accuracy disclaimer. | **Provisional — pending professor confirmation.** |
| D-04 | 2026-07-15 | Scope of "Steps 0-4" (this session) = Setup, Research, Persona (Problem 1), Requirements (Problem 2), Two Algorithms (Problem 3). Problem 4 (algorithm-selection mind map + Python CLI) is Step 5 and is **out of scope** for this pass. | Matches the execution-steps numbering in `SOEN_6011_F2_D1_Execution_Steps.md`, where Step 4 = Problem 3 and Step 5 = Problem 4. | Interpreting "steps 0-4" as covering all four problems. | Adopted |
| D-05 | 2026-07-15 | Algorithm B (Problem 3) is **CORDIC** (circular-mode rotation), not the Lentz continued-fraction alternative. | CORDIC is structurally the most different from the Maclaurin-series Algorithm A (additions/shifts vs. power series), is explicitly requested first in the prompt, and generalizes better to the D2 from-scratch constraint (no built-in `sin`/`cos`). | Lentz-evaluated continued fraction for `tan(x)` directly. | Adopted |

## Open action items (Step 0, professor confirmation — user to complete)
The following must be confirmed with the professor before D1 is frozen (per Step 0 of the execution steps). D-01/D-02/D-03 above are working assumptions used to keep progress moving and must be revisited if the professor's answer differs:
1. Angle unit = radians (confirm no degrees requirement).
2. Near-pole handling policy (tolerance value, error vs. warning).
3. Supported large-argument range (is `|x| <= 1e4` acceptable, or a different bound expected).
4. D2/D3 "Problem 7" numbering — the project description reuses "Problem 7" for both D2 (requirements update, 20 marks) and D3 (from-scratch polish, 70 marks); confirm how these should be cited/labelled to avoid confusion in later deliverables.
