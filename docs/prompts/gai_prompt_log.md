# GAI / Prompt Log — F2 tan(x), Deliverable 1

Per constraint **C-03**: every problem records the GAI tool, prompt type, exact CASTROFF prompt, an output summary, a critical evaluation (accepted / rejected / corrected, and why), how the output was verified, and attribution of any non-original content.

**GAI tool used for all entries below:** Claude Code (Claude, Anthropic), Sonnet 5 model (`claude-sonnet-5`), accessed 2026-07-15. The CASTROFF prompts below are the exact prompts defined in `SOEN_6011_F2_D1_Prompts.md`, submitted to the tool as-is (with prior-problem content pasted in where the prompt calls for it).

---

## Problem 1 — Persona

- **Prompt type:** Generative + decision-support (persona synthesis informed by a template-selection mind map).
- **Exact prompt:** see "Problem 1" in `SOEN_6011_F2_D1_Prompts.md` (submitted verbatim, no prior content to paste in since P1 has no dependency).
- **Output summary:** A three-way comparison of persona template styles (goal-directed, role-based, lightweight/proto-persona) rendered as a mind map, ending in a recommendation of the **goal-directed template**; then a full persona card for "Maya Chen," a mechanical-engineering master's student and part-time optics-lab research assistant, plus a 4-sentence usage scenario.
- **Critical evaluation:**
  - *Accepted:* the goal-directed template choice (it best supports traceability to requirements, which is the D1 priority); the core persona fields (role, experience, skills, goals, pain points); the tan-specific pain points (rad/deg confusion, distrust of results near pi/2, wanting a quick sanity check against a known value).
  - *Rejected/trimmed:* an initial draft included unnecessary biography (hobbies, hometown) with no traceability to requirements — removed per the "no irrelevant biographical detail" restriction in the prompt.
  - *Corrected:* tightened the usage scenario from 6 sentences to 4-5 to match the OUTPUT FORMAT constraint.
- **Verification:** Checked each persona need/pain point maps to at least one plausible D1 requirement category (FR/VAL/ACC/USE/ERR) before finalizing — 7 traceable needs identified, exceeding the ≥5 gate in Step 2.
- **Attribution:** Persona-template taxonomy (goal-directed / role-based / proto-persona) follows standard HCI literature (Cooper's goal-directed design; Pruitt & Adlin's persona lifecycle); paraphrased, not copied. Cited in `docs/references.bib` as `cooper2007` and `pruitt2006`.

---

## Problem 2 — Requirements (ISO/IEC/IEEE 29148)

- **Prompt type:** Generative + transformational (persona needs -> verifiable requirements) with review.
- **Exact prompt:** see "Problem 2" in `SOEN_6011_F2_D1_Prompts.md`, submitted with the finalized Problem 1 persona card (`docs/persona_card.md`) pasted into the `[PASTE ...]` placeholder.
- **Output summary:** A requirements table with IDs across FR/VAL/ACC/USE/REL/PERF/ERR/DOC categories, each with statement, persona-traced rationale, priority, and verification method; a separate assumptions list; and a 29148-quality review table flagging and correcting 3 draft requirements.
- **Critical evaluation:**
  - *Accepted:* the category/ID scheme; the accuracy requirement framed as measurable relative error vs. reference values (not the vague "accurate"); the near-pole detection requirement as VAL, not ERR (it's an input-domain condition, not a runtime failure).
  - *Rejected/corrected:* an early draft of the accuracy requirement said "the tool should be fast and accurate" — flagged in the review pass as violating the "no vague/unquantified terms" restriction and rewritten as a quantified relative-error bound (ACC-01).
  - *Rejected:* a draft requirement prescribing "use a Taylor series" was removed — algorithm choice is out of scope for Problem 2 per the prompt's restriction.
- **Verification:** Each requirement manually checked against the 29148 quality characteristics (necessary, unambiguous, complete, singular, feasible, verifiable, consistent); any requirement bundling two testable conditions was split into two IDs.
- **Attribution:** Requirement statement style and quality-characteristic checklist paraphrased from ISO/IEC/IEEE 29148:2018 guidance (not copied verbatim); cited as `iso29148` in `docs/references.bib`.

---

## Problem 3 — Two Algorithms in Pseudocode

- **Prompt type:** Generative + comparative (two independent, language-neutral algorithms in established pseudocode).
- **Exact prompt:** see "Problem 3" in `SOEN_6011_F2_D1_Prompts.md`, submitted with the relevant Problem 2 requirement IDs (ACC-01, VAL-02, VAL-03, REL-01) pasted into the placeholder.
- **Output summary:** Algorithm A (range reduction mod pi + Maclaurin series for sin/cos, then divide) and Algorithm B (CORDIC circular-mode rotation using a precomputed arctan(2^-i) table and gain constant K), each with pre/postconditions, complexity/limitations notes, and a worked trace for `tan(pi/4) = 1`; closed with an A-vs-B comparison table.
- **Critical evaluation:**
  - *Accepted:* both algorithms as structurally genuine alternatives (power-series/analytic vs. iterative rotation/shift-and-add); the explicit max-iteration/max-term safeguards on every loop; the near-zero-cosine guard in both.
  - *Rejected:* an initial CORDIC draft assumed a built-in `arctan` to generate the angle table at runtime — corrected to state the table is **precomputed offline/constants**, since the prompt disallows assuming built-in trig functions inside the algorithm.
  - *Corrected:* the Maclaurin worked trace initially stopped after 3 terms without checking the tolerance condition explicitly — rewritten to show the stopping test against the tolerance, not just a fixed term count.
- **Verification:** Hand-traced `tan(pi/4)` through both algorithms' pseudocode step-by-step and confirmed both converge to `1` (within stated tolerance); confirmed every loop has an explicit termination/max-work bound by inspection.
- **Attribution:** Maclaurin series formulas for sin/cos are standard mathematical identities (no attribution needed beyond a textbook reference). CORDIC's rotation/gain-constant formulation follows Volder's original method as commonly presented in numerical-methods textbooks; cited as `volder1959` and `muller2016` in `docs/references.bib`.

---

## Problem 4 — Algorithm Selection + Python CLI

- **Prompt type:** Decision-support (algorithm-selection mind map) + generative (Python implementation with a textual UI).
- **Exact prompt:** see "Problem 4" in `SOEN_6011_F2_D1_Prompts.md`, submitted with the two Problem 3 algorithms (`docs/algorithms/algorithm_A_maclaurin.md`, `docs/algorithms/algorithm_B_cordic.md`) pasted into the placeholder.
- **Output summary:** A criteria-weighted comparison (accuracy, pole handling, stability, implementation effort, D2 from-scratch suitability, performance, explainability) selecting **Algorithm A** for the D1 prototype; a Python CLI (`src/cli.py`) implementing Algorithm A with I/O separated from compute, custom `OutOfRangeError`/`NearPoleError` exceptions, and sample runs across valid/negative/near-pole/invalid/large-argument cases.
- **Critical evaluation:**
  - *Accepted:* selecting Algorithm A for D1 despite Algorithm B's stronger D2 fit — the prompt's own criteria (implementation effort, explainability) outweigh D2-suitability at this stage, and the decision log records this as revisitable in D2.
  - *Accepted:* the compute/I/O separation and the two named exception classes, since they map directly onto VAL-03/VAL-04/ERR-01/ERR-02.
  - *Corrected:* an initial draft of `tan_by_series` called `math.sin`/`math.cos` directly as a shortcut — rejected and rewritten to call the from-scratch `maclaurin_sin`/`maclaurin_cos` functions instead, since Problem 4 requires implementing *the selected algorithm*, not wrapping the library function; this also makes the D2 migration note accurate (only `math.pi` remains).
  - *Corrected:* the initial near-pole tolerance was left unset/arbitrary — fixed to a documented constant (`POLE_EPSILON = 1e-6`) consistent with VAL-04 and the decision log's provisional policy.
- **Verification:** Ran the CLI with piped input covering valid special values, a negative argument (odd symmetry), a near-pole case on both sides of a pole, non-numeric/missing input, and both a supported and an out-of-range large argument; every numeric result was cross-checked against `docs/research_notes.md` and `math.tan`/`math.atan` computed independently in a separate Python check (not via the CLI itself, to avoid circularity). No case produced an unhandled traceback.
- **Attribution:** No non-original code copied; the CLI is original code written for this project structured per the Problem 3 pseudocode already attributed above.

---

# GAI / Prompt Log — Deliverable 2

**GAI tool used for all D2 entries below:** Claude Code (Claude, Anthropic), Sonnet 5 model (`claude-sonnet-5`), accessed 2026-07-29.

## Problem 5 — From-Scratch Core + Tkinter GUI

- **Prompt type:** Generative + architectural (dependency-boundary analysis, from-scratch numerical core, GUI wireframe + implementation).
- **Prompt (paraphrased; interactive session, not a single CASTROFF block):** **Task** -- interpret and freeze the from-scratch boundary for a D1 CLI that already implements `sin`/`cos` manually but still imports `math.pi`; design and implement a pure `tan(x, tolerance, max_terms)` core with custom exceptions (`DomainError`, `ConvergenceError`, `NumericalRangeError`); design (wireframe first) and implement a Tkinter GUI wired to that core; verify against reference values. **Restrictions** -- no `math.sin`/`math.cos`/`math.tan`/`math.pi` anywhere in the compute path; core must stay importable/testable without launching the GUI; no unhandled traceback for any documented failure mode. **Output format** -- a dependency inventory doc, the core modules, a wireframe doc, `gui.py`, and a verification matrix. **Audience** -- same SOEN 6011 grading audience as D1; evidence-based, traceable to VAL/ACC/ERR/REL requirements.
- **Output summary:** `docs/from_scratch_boundary.md` (dependency inventory + `grep` verification that no `math.*` symbol remains); `src/constants.py` (from-scratch `PI` via a Machin-like arctangent series); `src/trig_series.py`/`src/tan_core.py` (refactor of D1's compute layer into a pure, importable core with three named exceptions); `docs/gui_wireframe.md`; `src/gui.py` (Tkinter GUI); `tests/manual_verification_d2.py` + `docs/verification_matrix_d2.md` (15/15 reference cases pass).
- **Critical evaluation:**
  - *Accepted:* deriving `PI` via Machin's formula (`16*arctan(1/5) - 4*arctan(1/239)`) rather than a hardcoded literal -- it is genuinely computed, not copy-pasted digits, and reuses the same tolerance/max-terms pattern already used for `sin`/`cos`.
  - *Accepted:* keeping Algorithm A (Maclaurin) instead of switching to CORDIC as D1's report had flagged -- see the reasoning captured as decision D-06 (`docs/decisions/decision_log.md`); this was a deliberate correction of the D1 report's forward-looking note after re-reading the actual from-scratch restriction (arithmetic is not prohibited, only library trig calls are).
  - *Rejected/corrected:* a first draft of `maclaurin_sin`/`maclaurin_cos` silently stopped at `n_max` without signalling anything (matching D1's behaviour) -- corrected to raise `ConvergenceError`, since the D2 architecture note explicitly names that exception and D1's silent-stop was identified as a REL-01 gap once GUI callers need to distinguish "no convergence" from "a computed value."
  - *Rejected:* an initial GUI draft put the near-pole/range/parse exception handling inside `src/tan_core.py` (formatting a user-facing string there) -- rejected and moved to `src/gui.py`/`src/cli.py` only, keeping the core GUI-independent per D2-P5.2's "keep GUI messages out of the numerical core."
- **Verification:** `grep -rn "math\." src/` and `grep -rn "^import math"` confirm zero matches outside docstring mentions (`docs/from_scratch_boundary.md`); `tests/manual_verification_d2.py` cross-checks 15 cases against an independently computed `math.tan` oracle (15/15 pass, worst-case relative error `3.83e-10` vs. the `1e-9` ACC-01 ceiling); the GUI was launched and driven through 5 states (valid, degrees, near-pole, out-of-range, invalid) and screenshotted (`docs/screenshots/d2_gui_*.png`) to confirm no traceback reaches the user.
- **Attribution:** Machin's arctangent identity for pi is a standard 1706 result (no attribution beyond a textbook/NIST DLMF reference, already in `docs/references.bib` as `nist_dlmf`); no other non-original code copied.

## Problem 6 — Repository, Commit History, README

- **Prompt type:** Process/generative (repository hygiene, README authored for a first-time cloner).
- **Prompt (paraphrased):** **Task** -- turn the working tree into a public-repo-ready project: a `.gitignore` appropriate for Python/LaTeX/macOS artifacts (already present from D1), a cohesive incremental commit history grouped by concern (core, GUI, docs, tests, requirements) rather than one bulk commit, and a root `README.md` a stranger could use to run the program with no other context. **Restrictions** -- no secrets/IDE-local files committed; commit subjects imperative and specific; README claims must match the actual `src/` behaviour (checked, not assumed). **Output format** -- `README.md` + a sequence of `git commit` operations. **Audience** -- same grading audience, plus a hypothetical fresh GitHub visitor.
- **Output summary:** `README.md` covering purpose, from-scratch scope, run commands (`python3 -m src.cli`, `python3 -m src.gui`), usage examples with screenshots, error/troubleshooting reference, repo structure, version/authorship, and a note that the formal PyUnit suite lands in D3; a curated multi-commit history (see `git log` at submission time).
- **Critical evaluation:**
  - *Accepted:* the `python3 -m src.cli`/`python3 -m src.gui` invocation form (module execution) over `python3 src/cli.py`, because the package uses absolute `from src...` imports internally (needed once `src/` grew past one file) and `-m` guarantees the repository root is on `sys.path` regardless of the caller's working directory.
  - *Corrected:* an early README draft claimed "no known limitations" for large arguments -- corrected to explicitly restate the `|x| <= 1e4` boundary and the near-pole precision-margin note from `docs/verification_matrix_d2.md`, since C-05 requires every claim to be evidence-based, not aspirational.
- **Verification:** Followed the README's own run commands from a clean shell (not an IDE) and confirmed both the CLI and GUI start; confirmed `git log --oneline` shows the intended per-concern grouping before submission.
- **Attribution:** No non-original content.

## Problem 7 — Updated Requirements (Baseline v0.2)

- **Prompt type:** Transformational (D1 requirements + D2 implementation evidence -> revised baseline) with an explicit changelog.
- **Prompt (paraphrased):** **Task** -- compare every v0.1 requirement against what `src/` and `docs/verification_matrix_d2.md` actually do; add/revise requirements for the GUI, the from-scratch dependency boundary, the three named exceptions, and the optional degrees mode; retire nothing without rationale; freeze as v0.2 with a changelog table showing what changed and why. **Restrictions** -- do not silently rewrite v0.1 (keep it on disk); every changed/added ID needs a one-line "discovered via" note distinguishing implementation-driven changes from planned ones. **Output format** -- changelog table + full v0.2 requirements table + revised assumptions. **Audience** -- same grading audience; must support a traceability review.
- **Output summary:** `docs/requirements/requirements_v0.2.md`, adding FR-07, USE-03, DEP-01, ERR-03, REL-03, DOC-02; revising FR-02, USE-02, ACC-01 (evidence, not the bound); carrying 13 v0.1 requirements forward unchanged.
- **Critical evaluation:**
  - *Accepted:* flagging ACC-01 as "tight, not comfortable" near the pole boundary rather than either silently widening the tolerance or hiding the `3.83e-10` measurement -- matches the D3-P8.1 warning against "weakening tolerances without justification," applied one deliverable early.
  - *Rejected:* a draft new requirement "the GUI shall be visually appealing" -- rejected as unquantified/unverifiable (same 29148 problem D1's review process already caught once); replaced with the concrete, testable USE-03 wording (labelled controls, tab order, Enter/Esc bindings, no colour-only errors).
- **Verification:** Re-ran `tests/manual_verification_d2.py` after freezing the wording to confirm ACC-01's stated bound is still met by the current source; cross-read every new/changed ID against the corresponding `src/` file and `docs/verification_matrix_d2.md` row before adopting it.
- **Attribution:** No non-original content; ID scheme and statement style continue D1's ISO/IEC/IEEE 29148-informed approach (`iso29148` in `docs/references.bib`).
