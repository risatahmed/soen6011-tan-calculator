# Problem 2 — Requirements (ISO/IEC/IEEE 29148), Baseline v0.1

Informed by the Problem 1 persona (`docs/persona_card.md`, Maya Chen). Requirement statements follow a single consistent style: "The system shall &lt;testable behaviour&gt;." Each requirement has a unique ID grouped by category, a rationale traced to a persona need, a priority, and a verification method.

**ID scheme:** `FR` functional · `VAL` input validation/domain · `ACC` accuracy/numerical · `USE` usability · `REL` reliability · `PERF` performance · `ERR` error handling · `DOC` documentation.

**Priority scale:** Must (baseline-blocking) / Should (important, not blocking) / Could (nice-to-have).

## Requirements table

| ID | Statement | Rationale / Source (persona trace) | Priority | Verification Method |
|---|---|---|---|---|
| FR-01 | The system shall accept a real-valued angle `x` entered by the user as text input. | Persona need 6: no full CAS available, needs a simple entry point. | Must | Test |
| FR-02 | The system shall state, before requesting `x`, that the accepted value is interpreted in radians. | Persona need 1: radians/degrees confusion. | Must | Demonstration |
| FR-03 | For any `x` accepted under VAL-01 through VAL-04, the system shall compute `tan(x) = sin(x)/cos(x)`. | Core function purpose. | Must | Test |
| FR-04 | The system shall display the computed `tan(x)` result as text to the user. | Persona need 6: quick trustworthy result without a CAS. | Must | Demonstration |
| FR-05 | The system shall allow the user to submit a new value of `x` in the same session without restarting the program. | Persona goal: get a value quickly during a lab session, likely more than once. | Should | Test |
| FR-06 | The system shall allow the user to exit the program through an explicit, documented command. | Basic usability of any interactive CLI. | Must | Demonstration |
| VAL-01 | The system shall reject non-numeric input for `x` and re-prompt with a message identifying the input as non-numeric. | Persona need 5: no cryptic crash on typos. | Must | Test |
| VAL-02 | The system shall reject empty (missing) input for `x` and re-prompt with a message identifying the input as missing. | Persona need 5. | Must | Test |
| VAL-03 | The system shall reject input for `x` whose absolute value exceeds a documented maximum supported magnitude (`|x| <= 1e4` radians, per D-03 in the decision log) and report that the input is outside the supported range, rather than returning an unreliable result. | Numerical risk: argument-reduction error grows with `|x|` (research notes, Section 5.2). | Must | Test |
| VAL-04 | The system shall detect input `x` within a documented tolerance of a pole (`x = pi/2 + k*pi`, `k` an integer) and treat it as an invalid computation rather than returning a numeric value. | Persona need 2: fear of silent huge/meaningless numbers near 90 degrees. | Must | Test |
| ACC-01 | For any accepted `x` outside the near-pole tolerance band (VAL-04) and within the supported range (VAL-03), the system shall compute `tan(x)` with a relative error no greater than `1e-9` when compared against the trusted reference values in `docs/research_notes.md`, Section 4. | Persona need 3: wants a documented precision to judge lab-report suitability. | Must | Test (against reference-value table) |
| ACC-02 | The system shall display the computed result rounded to a documented, fixed number of significant digits (10 significant figures). | Persona need 3. | Should | Inspection |
| USE-01 | The system shall present the valid input domain (supported range, pole exclusion) and the expected angle unit to the user before requesting `x`. | Persona needs 1 and 2. | Must | Demonstration |
| USE-02 | The system shall provide a textual (command-line) interface that requires no graphical environment. | Persona need: sometimes on a bare lab machine without GUI toolkits; matches D1's textual-UI constraint. | Must | Demonstration |
| REL-01 | For every input, valid or invalid, the system shall return control to the user without an unhandled program crash. | Persona need 5; project constraint (no unhandled traceback). | Must | Test |
| REL-02 | The system shall run from a terminal without depending on any specific IDE to execute. | Persona need: works on a shared/bare lab machine. | Must | Demonstration |
| ERR-01 | When input is rejected under any VAL requirement, the system shall display a message that identifies which specific condition was violated (non-numeric, missing, out-of-range, or near-pole). | Persona need 5: helpful, non-generic error messages. | Must | Test |
| ERR-02 | The system shall not propagate an unhandled Python exception to the user's terminal for any expected invalid-input or near-pole case. | Same as ERR-01; project constraint. | Must | Test |
| DOC-01 | The system's accompanying documentation shall state the assumed angle unit, the supported argument range, the near-pole tolerance, and the displayed result precision. | Persona need 3; supports trust and lab-report use. | Should | Inspection |

## Assumptions (kept separate from requirements)

1. Angle unit for `x` is radians; no degrees-mode requirement is included in this baseline (see decision log D-01 — pending professor confirmation).
2. The near-pole tolerance value itself (the exact `epsilon` in VAL-04) is an implementation-time constant to be fixed and documented in D1-Problem 4/DOC-01, not prescribed numerically here (see decision log D-02).
3. Supported input range is `|x| <= 1e4` radians (decision log D-03); this is a documented limitation, not a claim of unbounded validity.
4. No requirement in this baseline prescribes a specific algorithm, library, or programming language; algorithm selection is deferred to Problem 3/4.
5. "Numeric" input (VAL-01) is interpreted as any input Python's standard numeric parsing accepts for a floating-point real number (e.g., `1.2`, `-0.5`, `1e3`); complex numbers and non-real notations are out of scope.

## Requirements review findings (29148 quality pass)

The draft below shows three requirements that failed a 29148 quality characteristic during review, and how each was corrected before being placed in the table above.

| ID (draft) | Characteristic at risk | Issue | Suggested fix (adopted in table above) |
|---|---|---|---|
| ACC-01 (draft) | **Verifiable / Unambiguous** — original text: *"The system shall compute tan(x) quickly and accurately."* | "Quickly" and "accurately" are unquantified, subjective terms; cannot be tested pass/fail. | Rewritten as a quantified relative-error bound against a named reference (adopted as **ACC-01**); the performance aspect was split out separately (see PERF note below). |
| FR-03 (draft) | **Feasible / does not prescribe implementation** — original text: *"The system shall compute tan(x) using a Taylor series expansion of sin and cos."* | Prescribes a specific algorithm inside a Problem-2 requirement, which the prompt explicitly disallows (algorithm choice belongs to Problem 3/4) and would make the requirement infeasible to keep stable if the algorithm changes later. | Rewritten to state only *what* is computed (`tan(x) = sin(x)/cos(x)`), not *how* (adopted as **FR-03**). |
| VAL-03/VAL-04 (draft) | **Singular** — original text: *"The system shall reject out-of-range and near-pole inputs."* | Bundles two independently testable conditions (range vs. pole-proximity) into one statement, so a test could pass one condition and fail the other while the requirement as a whole is ambiguous to mark. | Split into two separate, independently verifiable requirements: **VAL-03** (range) and **VAL-04** (pole proximity). |

No requirement in the finalized table above was found to violate **necessary**, **complete**, or **consistent** during this pass; a note was made that a dedicated **PERF** requirement (response-time bound) was considered but held back from this v0.1 baseline as **Could**-priority pending confirmation that response time is a graded concern for this project (not part of the persona's stated pain points, which are about correctness and trust, not speed).

## Baseline

Frozen as **Requirements Baseline v0.1** for Deliverable 1. Future changes (e.g., in D2/Problem 7) must be recorded as a new version with a changelog against this baseline, per constraint C-06 (iterative consistency).
