# SOEN 6011 — F2 Tangent Function tan(x) — Task List

**Project:** A User-Centred, From-Scratch Scientific Calculator for the Tangent Function tan(x)
**Course:** SOEN 6011 (Software Engineering Processes), Section CC, Summer 2026
**Type:** Individual, medium-sized scientific software engineering project
**Language:** Python · **Deliverables:** D1, D2, D3

> **Working assumptions to confirm with the professor first:**
> 1. **Angle unit** — treat the input `x` as **radians** (the mathematical default) and state this explicitly; offer degrees only as a clearly-labelled option if time permits.
> 2. **Domain** — `tan(x)` is defined for all real `x` **except** the poles `x = π/2 + kπ` (k ∈ ℤ), where `cos(x) = 0`. Near these poles the value diverges to ±∞; the tool must detect and refuse (or clearly flag) inputs within a small tolerance of a pole rather than returning a meaningless huge number.
> 3. **Large arguments** — for very large `|x|`, argument reduction modulo π loses precision because π is irrational; state a supported input range (e.g. `|x| ≤ 10⁴` rad) beyond which accuracy is not guaranteed.

---

## D1 Logistics (set by the professor)

Order of students is by function **F1–F8**; **F2 is 2nd** for both feedback and presentation.

| Event | Date / Time | Medium | Format / Rules |
|---|---|---|---|
| **Flash Feedback** | Mon **2026-07-13**, 14:00–16:00 | Zoom | 5 min per student (1-min buffer), order F1–F8 |
| **Submission** | Wed **2026-07-15**, **12:00 (noon)** | Moodle | **Zip = Source Code + LaTeX + PDF** |
| **Presentation** | Wed **2026-07-15**, 19:45–22:45 | Zoom | Slide presentation, **7 min + 3 min Q/A** (1-min buffer), order F1–F8 |

- **Slides must use the LaTeX Beamer package** (not a generic deck); output LaTeX + PDF.
- Submission (noon) is **before** the presentation (evening) the same day — the artifact must be finished first.
- Deadlines are non-negotiable per the course outline; missed = 0.

---

## Global Constraints (apply to every problem)

- [ ] **C-01** All work individual (analysis, artifacts, code, presentation, demo).
- [ ] **C-02** Every formal deliverable typeset in **LaTeX**.
- [ ] **C-03** Every problem uses one or more public **LLM/GAI tools** with **CASTROFF**-based prompts — record prompt types, examples, and output explanation/evaluation.
- [ ] **C-04** Cite/reference all non-original work; avoid syntactic and semantic copying.
- [ ] **C-05** Every technical/process claim is evidence-based (source, experiment, requirement, or recorded decision).
- [ ] **C-06** Iterative consistency — later deliverables modify/extend earlier artifacts rather than silently contradicting them.
- [ ] **C-07** D1 & D2 → Zoom slides + demo; D3 → in-person poster + demo.

---

## Deliverable Dependency Chain

`Persona → Requirements → Two Algorithms → Algorithm Selection → CLI Prototype → From-Scratch GUI → Updated Requirements → Quality/Accessibility → Unit Tests`

- P2 informed by P1 · P3 informed by P2 · P4 informed by P3
- D2 modifies the D1 implementation and updates D1 requirements
- D3 modifies the D2 implementation and tests the resulting behavior

---

## Deliverable 1 (D1) — Persona, Requirements, Algorithms, CLI Prototype
*Presented with slides + Zoom demo.*

- [ ] **D1-00 — Set up workspace & evidence log** *(deps: none)*
  Local project dir + private Git repo; folders for LaTeX/slides/mind maps/notes/prompts/pseudocode/src/tests/screenshots; start decision log, GAI usage log, and `.bib` bibliography.
  *Done when:* every later artifact has a storage location; no source/AI contribution left undocumented.

- [ ] **D1-01 — Research the tangent function domain & use cases** *(deps: none)*
  Document `tan(x) = sin(x)/cos(x)`; period π; odd symmetry `tan(−x) = −tan(x)`; poles at `x = π/2 + kπ`; range = all reals; special values (`tan 0 = 0`, `tan(π/6) = 1/√3`, `tan(π/4) = 1`, `tan(π/3) = √3`). Identify applications (trigonometry/geometry, slope & angle-of-elevation, physics — projectile/optics/phase, signal processing, computer-graphics rotations, surveying/navigation). Collect authoritative references + trusted reference values. List numerical risks: **poles/asymptotes** (cos → 0), **argument-reduction error** for large `|x|`, slow series convergence near ±π/2, overflow near poles, catastrophic cancellation.
  *Done when:* domain and angle unit stated unambiguously; ≥2 realistic user contexts; reference values suitable for tests.

- [ ] **D1-P1.1 — Identify candidate persona templates** *(deps: D1-01)*
  Review persona template styles; list candidate fields; exclude irrelevant biographical detail; define evaluation criteria (relevance, realism, conciseness, traceability, accessibility support).
  *Done when:* ≥3 plausible templates compared; criteria stated before choosing.

- [ ] **D1-P1.2 — Persona-template selection mind map** *(deps: D1-P1.1)*
  Central concept "Persona Template for Tangent Function Calculator"; branches for alternatives/criteria/pros/cons/final choice; don't rely on colour alone; record why rejected; export hi-res image + keep editable source.
  *Done when:* map visibly compares alternatives; choice follows criteria not preference; readable in LaTeX/slides.

- [ ] **D1-P1.3 — Develop the primary persona** *(deps: D1-P1.2)* — **Problem 1 [20 marks]**
  Realistic role (e.g. an engineering, physics, or surveying student / lab assistant who needs quick trustworthy `tan(x)` values); mandatory fields (name, role, experience, skills, goals) + context-sensitive optional fields; tangent-specific needs/pain points (confusion over radians vs degrees, what happens near 90°/π-2, trusting results near asymptotes); distinguish evidence vs synthesis vs assumptions; add a short usage scenario.
  *Done when:* every detail relevant to design/requirements; ≥5 requirements traceable to persona goals/pains.

- [ ] **D1-P2.1 — Choose a requirements style (ISO/IEC/IEEE 29148)** *(deps: D1-P1.3)*
  Select one style; define ID scheme (FR-01, VAL-01, ACC-01, PERF-01, ERR-01); requirement record template (ID, statement, rationale/source, priority, verification method, trace to persona); keep assumptions separate.
  *Done when:* style applied consistently; every requirement uniquely identifiable and testable.

- [ ] **D1-P2.2 — Elicit & write the initial requirements** *(deps: D1-P2.1)* — **Problem 2 [30 marks]**
  Functional (accept `x`; state/choose angle unit; compute `tan(x)`; display; clear/retry; exit); domain/validation (non-numeric, missing, inputs at/near a pole `π/2 + kπ`, extreme magnitudes); accuracy (measurable tolerance + reference method, e.g. relative error vs trusted values); usability; reliability; portability; documentation. Assign priorities + verification methods.
  *Done when:* every requirement has a unique ID, avoids vague terms, has a planned verification method; no algorithm prescribed unless necessary.

- [ ] **D1-P2.3 — Review requirements for quality & consistency** *(deps: D1-P2.2)*
  Check necessity/correctness/unambiguity/completeness/singularity/feasibility/verifiability; confirm domain and angle unit match assumptions; resolve accuracy vs speed vs from-scratch conflicts; use a GAI reviewer then independently verify; revise traceability.
  *Done when:* no known contradiction; all high-priority persona needs represented; baseline frozen + versioned for D1.

- [ ] **D1-P3.1 — Select two genuinely different algorithm candidates** *(deps: D1-P2.3)*
  **A:** range reduction to a small interval (e.g. [−π/4, π/4]) + **Maclaurin/Taylor series** for `sin(x)` and `cos(x)`, then `tan = sin/cos`. **B:** **CORDIC** (shift-and-add rotations using a precomputed `arctan(2⁻ⁱ)` table) producing `sin` and `cos` simultaneously, then `tan = sin/cos` — *(alt B: Lentz-evaluated **continued fraction** `tan(x) = x/(1 − x²/(3 − x²/(5 − …)))`)*. Confirm they are meaningfully different; note subordinate ops (range reduction, factorial/power, division), convergence controls, pole handling, complexity, risks. No Python syntax.
  *Done when:* both expressible independently of Python; both plausible for the domain; differences substantial.

- [ ] **D1-P3.2 — Pseudocode for Algorithm A** *(deps: D1-P3.1)* — **Problem 3 (part) [20 marks]**
  Inputs/outputs/pre/postconditions/constants/tolerance; validation + exceptional termination near poles; range-reduction step (reduce modulo π, track quadrant/sign); Maclaurin series for sin & cos with term-based stopping + max terms; division with near-zero-cos guard; complexity note; worked trace (e.g. `tan(π/4) = 1`).
  *Done when:* uses an established convention consistently; every branch terminates or has a max-work safeguard; links to requirements.

- [ ] **D1-P3.3 — Pseudocode for Algorithm B** *(deps: D1-P3.1)* — **Problem 3 (part)**
  Inputs/outputs/pre/postconditions/subordinate functions; CORDIC rotation loop with precomputed angle table + gain constant `K` (or continued-fraction recurrence via Lentz); iteration/convergence + max-iteration rules; known weaknesses (near ±π/2, large arguments, table length vs precision); worked trace linked to requirements.
  *Done when:* same quality standard as A; independently implementable from the pseudocode.

- [ ] **D1-P4.1 — Algorithm-selection mind map** *(deps: D1-P3.2, D1-P3.3)*
  Central concept "Algorithm for tan(x)"; compare on accuracy, domain coverage & pole handling, numerical stability, effort, from-scratch suitability, performance, maintainability, explainability to persona; record positive/negative evidence; state selection + why the other is rejected; export readable image.
  *Done when:* selection follows criteria; trade-offs + rejected alternative visible; consistent with D1 requirements and anticipates D2 constraints.

- [ ] **D1-P4.2 — Implement the D1 textual-interface prototype** *(deps: D1-P4.1)* — **Problem 4 [30 marks]**
  Separate I/O from computation; prompt for `x` with meaning + angle-unit + valid-domain hint; convert/validate; compute with selected algorithm; display with documented format/precision; catch invalid input + near-pole/numerical failures with helpful messages; comments only where they explain intent.
  *Done when:* runs outside an IDE from a terminal; known reference cases within tolerance; invalid/near-pole inputs never crash unhandled.

- [ ] **D1-P4.3 — Verify & demonstrate the D1 prototype** *(deps: D1-P4.2)*
  Verification matrix (requirement ID → demo case); run normal/boundary/invalid/near-pole/negative(odd-symmetry)/large-argument cases; compare against trusted references; record limitations honestly; prepare a repeatable live demo script.
  *Done when:* every mandatory D1 behavior demonstrated within allotted time; nothing unsupported presented as correct.

- [ ] **D1-REP — Assemble the D1 LaTeX report & slides** *(deps: all D1 tasks)*
  Coherent LaTeX with per-problem sections; persona + mind-map figures with captions; requirements table, assumptions, traceability, two pseudocode listings, decision rationale, implementation summary; per-problem GAI (tool, prompt type, CASTROFF example, output explanation, critical evaluation); one citation style; concise Beamer slides; rehearse Zoom audio/video/screen-share/terminal + fallback screenshots.
  *Done when:* all four problems visibly answered; all mandatory constraints addressed; slides/demo tell the same story as report and code.

---

## Deliverable 2 (D2) — From-Scratch Implementation, Tkinter GUI, VCS, Updated Requirements
*Presented with slides + Zoom demo.*

- [ ] **D2-P5.1 — Interpret & freeze the from-scratch boundary** *(deps: D1-P4.2)*
  List every built-in/stdlib/third-party function used; classify each as input/output/arithmetic/UI/exception vs **prohibited mathematical support**; identify subordinate functions needing manual implementation (`sin`, `cos`, the π constant, argument reduction modulo π, factorial, power/`x^n`, and for CORDIC the `arctan` table + gain); ask the professor where ambiguous; record final interpretation as an assumption + README note.
  *Done when:* no prohibited direct trig call remains (no `math.tan`/`math.sin`/`math.cos`); every retained dependency justified.

- [ ] **D2-P5.2 — Design the from-scratch numerical architecture** *(deps: D2-P5.1)*
  Pure core `tan(x, tolerance, max_terms)`; components for range reduction, sin/cos series (or CORDIC), near-pole detection, error estimation; custom exceptions (`DomainError` for at/near a pole, `ConvergenceError`, `NumericalRangeError` for out-of-supported-range arguments); config constants (π to sufficient digits, tolerance, max iterations — no magic numbers).
  *Done when:* each component has one responsibility; testable without launching GUI; termination + failure behavior defined.

- [ ] **D2-P5.3 — Implement the from-scratch tan computation** *(deps: D2-P5.2)* — **Problem 5 (core) [60 marks]**
  Implement subordinate numerical procedures manually (π constant, range reduction, sin/cos series or CORDIC rotations, division); explicit loops/recursion + arithmetic (no prohibited trig shortcuts); tolerance + max-work safeguards; use odd symmetry `tan(−x) = −tan(x)` and period π to shrink the argument; return structured success or raise documented exceptions (keep GUI messages out of the numerical core); compare incrementally against references.
  *Done when:* all target cases meet the revised accuracy goal; terminates on difficult inputs (near poles, large `|x|`); no direct library trig used unless explicitly permitted/justified.

- [ ] **D2-P5.4 — Design the Tkinter GUI** *(deps: D1-P1.3, D2-P5.2)*
  Wireframe before coding (title, `x` field, angle-unit selector (rad/deg), Calculate, Clear, result area, help/domain hint, status/error area); meaningful labels ("x in radians"); keyboard navigation, default focus, Enter-to-calculate, Esc/clear; resizable layout; errors (e.g. "input is at/near an asymptote") shown near context and not by colour alone.
  *Done when:* a first-time user can infer the required action; layout supports the persona and avoids unnecessary controls.

- [ ] **D2-P5.5 — Implement & integrate the Tkinter GUI** *(deps: D2-P5.3, D2-P5.4)* — **Problem 5 (GUI)**
  Main window + widgets in Tkinter; connect Calculate to parsing/validation/core/formatting; Clear/Reset to a predictable clean state; catch domain(near-pole)/conversion/convergence/range errors separately; helpful messages (what happened + how to fix); starts with a normal Python command, no IDE dependency.
  *Done when:* GUI starts/closes cleanly; all expected errors handled without a traceback shown to the user; core still invocable independently.

- [ ] **D2-P5.6 — Verify D2 numerical & GUI behavior** *(deps: D2-P5.5)*
  Reference-value suite across special angles, general angles, negative (symmetry), near-pole, and large-argument inputs; test invalid strings, empty, at-pole, very large magnitudes, non-convergence; measure/estimate runtime; ensure formatting doesn't imply more precision than achieved; log every defect + resolution.
  *Done when:* critical defects resolved; known limitations documented; behavior ready to drive the requirement update.

- [ ] **D2-P6.1 — Create & publish the public repository** *(deps: D2-P5.3)* — **Problem 6 (part) [20 marks]**
  Clear repo name; appropriate `.gitignore` (no temp files/secrets/IDE settings); logical structure (source/docs/screenshots/tests); publish to GitHub or another public host; verify the public URL in a logged-out/private session.
  *Done when:* repo publicly accessible; a fresh clone can locate and run the program via documented steps.

- [ ] **D2-P6.2 — Create a high-quality commit history** *(deps: D2-P6.1)* — **Problem 6 (part)** *(continuous)*
  Cohesive commits (not one bulk upload); imperative, specific subjects ("Add range reduction modulo pi"); explain motivation/trade-offs in bodies; separate refactor/behavior/docs/screenshots; review history for accidental files + misleading messages.
  *Done when:* history shows the project evolution; each commit has a clear purpose and doesn't mix unrelated work.

- [ ] **D2-P6.3 — Write the repository README** *(deps: D2-P5.5, D2-P6.1)*
  Project purpose + tan definition; supported domain/angle unit/assumptions/algorithm/known limitations (poles, large arguments); Python/Tkinter prerequisites + exact run command; usage examples + screenshots; error messages + troubleshooting; repo structure, version, authorship, licence (if any), attribution; testing instructions (or reserve for D3).
  *Done when:* a new user can run the program using only the README; claims match the actual implementation.

- [ ] **D2-P7.1 — Update requirements based on D2 evidence** *(deps: D2-P5.6)* — **Problem 7 [20 marks]**
  Compare every D1 requirement with actual D2 behavior; add/revise for Tkinter, allowed dependencies, exception handling, helpful messages, near-pole handling, convergence limits, performance, supported argument range; retire obsolete requirements with rationale (don't delete history); assign a new baseline/version + update traceability; record which changes were discovered through implementation.
  *Done when:* every changed requirement has a rationale; spec accurately describes the D2 product; no feature presented as required unless added to baseline.

- [ ] **D2-REP — Assemble D2 LaTeX report, slides & Zoom demo** *(deps: all D2 tasks)*
  Explain from-scratch interpretation + subordinate functions (sin/cos, range reduction, π); architecture + numerical safeguards (pole detection, argument-reduction limits); GUI screenshots + helpful-error examples; public repo URL, README evidence, selected high-quality commits; requirement change log + updated baseline; per-problem CASTROFF prompts + critical GAI evaluation; live demo (launch from terminal, valid + near-pole + invalid cases, open the public repo).
  *Done when:* all D2 mandatory statements addressed; demo runs without an IDE; repository and report versions synchronized.

---

## Deliverable 3 (D3) — Style, Quality Tools, Debugging, Versioning, Accessibility, Unit Tests
*Presented with an in-person poster + demonstration.*

- [ ] **D3-P7.1 — Refactor to an established Python style** *(deps: D2-P5.5)* — **Problem 7 [70 marks] (part)**
  Adopt PEP 8 (or another justified style); review naming/line length/whitespace/imports/function size/docstrings/constants/module boundaries; remove dead + duplicate code without changing behavior; keep numerical formulas readable + explain non-obvious stability choices (range reduction, near-pole guard); re-run verification cases after each batch.
  *Done when:* behavior unchanged except intentional fixes; source understandable without the IDE.

- [ ] **D3-P7.2 — Run Flake8 & resolve style findings** *(deps: D3-P7.1)*
  Install/configure Flake8 reproducibly; run from project root with exact command recorded; resolve legitimate findings, justify any exclusions; capture readable **snapshots** (command, files checked, final result); add the command to README/dev docs.
  *Done when:* final output has no unexplained violations; screenshots match the submitted version.

- [ ] **D3-P7.3 — Use a debugger & document a real debugging session** *(deps: D3-P7.1)*
  Pick a meaningful defect/edge case (near-pole behaviour, argument-reduction accuracy, sign after quadrant reduction); set a breakpoint with `pdb`; inspect variables + step through control flow; correct + rerun; capture **snapshots** of debugger commands + useful state (no clutter / personal info).
  *Done when:* evidence shows actual investigation; the resolved case added to regression/unit tests where appropriate.

- [ ] **D3-P7.4 — Run Pylint & address static-analysis findings** *(deps: D3-P7.1)*
  Run Pylint on all modules; classify messages (defect / maintainability / convention / acceptable false positive); fix high-severity + relevant maintainability findings; only narrowly justified suppressions; capture **snapshots** + record final score/output.
  *Done when:* no high-severity finding left unexplained; screenshots match the final source version.

- [ ] **D3-P7.5 — Apply Semantic Versioning** *(deps: D2-P6.1)*
  Define what version numbers represent; assign versions to major states (e.g. 0.1.0 D1 CLI, 0.2.0 D2 GUI, 1.0.0 final D3 if stable); patch = backward-compatible fixes, minor = added compatible features; add a version constant/metadata + show in GUI/About; create Git tags + concise release notes.
  *Done when:* version consistent in code, repo tag, README, and poster; increments match the documented policy.

- [ ] **D3-P7.6 — Select applicable UIDP via a mind map** *(deps: D2-P5.4)*
  Collect candidate principles from course + HCI sources; branches for applicable / partially applicable / not applicable; evaluate visibility, feedback, consistency, error prevention, user control, simplicity, mapping, affordance, recognition-over-recall, tolerance; for each selected principle name the affected widget/interaction (e.g. angle-unit selector = error prevention); for each rejected principle explain why it's outside a small calculator's context.
  *Done when:* the mind map is a decision artifact (not just a list); every selected principle produces observable design evidence.

- [ ] **D3-P7.7 — Improve GUI accessibility** *(deps: D3-P7.6)*
  Clear textual labels on all controls; logical keyboard tab order + keyboard activation for primary actions; never communicate state/errors by colour alone; readable font sizes, spacing, strong contrast; visible focus, avoid unnecessary motion; specific/polite/corrective error messages; test resizing + (where possible) high-DPI/screen-reader behavior; document Tkinter platform limitations honestly.
  *Done when:* primary workflow usable without a mouse; labels/messages understandable without colour; no obvious clipping at normal scaling.

- [ ] **D3-P7.8 — Capture final quality evidence & freeze release candidate** *(deps: D3-P7.2 → D3-P7.7)*
  Run Flake8, Pylint, the debugger example, and manual GUI checks on the **same commit**; save commands + outputs with timestamps/commit hash; update README, screenshots, version, changelog; create a release-candidate tag only after all evidence is synchronized.
  *Done when:* all screenshots/claims point to the same source revision; the application runs from a fresh clone.

- [ ] **D3-P8.1 — Design the unit-test strategy** *(deps: D2-P7.1)* — **Problem 8 [30 marks] (part)**
  Map test categories to updated requirement IDs; define equivalence classes + boundary values for `x`; include known identities (odd symmetry `tan(−x) = −tan(x)`, period `tan(x+π) = tan(x)`, special angles `tan 0 = 0`, `tan(π/4) = 1`, `tan(π/3) = √3`); include invalid inputs, at/near-pole inputs, large-argument limits, simulated convergence failures; define numeric comparison tolerance (no exact equality for approximations); separate core unit tests from GUI/manual tests.
  *Done when:* every critical requirement has ≥1 planned test; tolerance justified + consistent with the algorithm.

- [ ] **D3-P8.2 — Implement unit tests (PyUnit / unittest)** *(deps: D3-P8.1)* — **Problem 8 (part)**
  Deterministic tests for normal + boundary inputs; `assertAlmostEqual` or an explicit relative/absolute error helper; test validation + expected exception classes (near-pole → `DomainError`); test subordinate numerical functions (sin, cos, range reduction) independently; add regression tests for defects found via pdb/Pylint; setup/teardown only where it improves clarity.
  *Done when:* tests run with a standard command; failure messages identify the case clearly; no dependency on GUI interaction or an IDE.

- [ ] **D3-P8.3 — Run, review & document the test suite** *(deps: D3-P8.2)*
  Run the full suite from a clean environment; record #tests/passes/failures/execution time; investigate every failure (don't weaken tolerances without justification); optionally manage cases in Jira but keep repo evidence authoritative; capture readable output for poster/report; update the README testing section.
  *Done when:* all mandatory tests pass; no test disabled without explanation; the tested commit is the release-candidate commit.

- [ ] **D3-REP — Create the D3 poster & in-person demonstration package** *(deps: all D3 tasks)*
  Structure the poster around problem/process/user/requirements/algorithm/architecture/GUI/quality tools/accessibility/tests/version/results; readable figures + minimal dense prose; include UIDP mind map, final GUI, selected Flake8/pdb/Pylint evidence, test summary; show traceability persona → tests; include public repo URL + final semantic version; retain CASTROFF prompts + critical GAI evaluation in submission materials; prepare an in-person demo (run the release tag, normal + near-pole + error cases, run the unit tests); carry offline backups of code/screenshots/poster/reference outputs.
  *Done when:* poster readable at presentation distance; demo uses the same tagged version the poster describes; all mandatory D3 evidence visible and credible.

---

## Cross-Deliverable Project Management (continuous)

- [ ] **X-01** Maintain traceability continuously — links among persona, requirements, algorithm steps, code modules, GUI controls, and tests after every meaningful change.
- [ ] **X-02** Maintain a decision log — alternatives, criteria, decision, rationale, date, affected artifacts (include rejected options).
- [ ] **X-03** Maintain a GAI evidence log — per problem: CASTROFF prompt components, prompt type, example, output summary, verification, final use/non-use decision.
- [ ] **X-04** Maintain bibliography & attribution — capture source metadata immediately; distinguish quotations/paraphrases/ideas/images/formulas/tool docs.
- [ ] **X-05** Baseline each deliverable — tag/archive the exact report, code, slides/poster, and evidence used per presentation.
- [ ] **X-06** Run consistency reviews before submission — compare version, domain, angle unit, tolerance, algorithm name, requirements, screenshots, repository, and claims across artifacts.
- [ ] **X-07** Rehearse demonstrations — timed script, known inputs, offline fallback, clean terminal, pre-opened files; avoid improvising unsupported cases.
- [ ] **X-08** Back up work — ≥1 remote repo copy + ≥1 separate offline/exported copy of reports, mind maps, screenshots, presentations.

---

## Suggested Repository Structure

```
tangent-function-calculator/
├── README.md
├── CHANGELOG.md
├── LICENSE                 # only if a licence is selected
├── src/
│   ├── tan_core.py         # pure tan(x): range reduction + sin/cos series or CORDIC
│   ├── trig_series.py      # from-scratch sin/cos (D2)
│   ├── validation.py
│   ├── exceptions.py
│   ├── cli.py              # D1 baseline or retained reference
│   └── gui.py
├── tests/
│   ├── test_tan_core.py
│   ├── test_trig_series.py
│   ├── test_validation.py
│   └── test_regressions.py
├── docs/
│   ├── requirements/
│   ├── algorithms/
│   ├── mindmaps/
│   ├── screenshots/
│   ├── prompts/
│   └── decisions/
├── deliverables/
│   ├── D1/
│   ├── D2/
│   └── D3/
└── pyproject.toml or tool configuration files
```

---

## Master Completion Checklists

**Before D1 submission**
- [ ] Persona-template mind map completed and readable
- [ ] Persona includes relevant goals, skills, needs, environment, pain points
- [ ] Requirements use unique IDs and explicit assumptions (angle unit + domain)
- [ ] Requirements trace to persona and have verification methods
- [ ] Two independent language-neutral algorithms provided (series vs CORDIC/continued fraction)
- [ ] Algorithm-selection mind map justifies the final choice
- [ ] Python CLI works from terminal
- [ ] D1 LaTeX, citations, GAI evidence, slides, and demo are synchronized

**Before D2 submission**
- [ ] From-scratch boundary is documented (no `math.tan`/`sin`/`cos`)
- [ ] Mathematical core no longer uses prohibited functions
- [ ] Tkinter GUI works without an IDE
- [ ] Exceptions are handled and messages are helpful (near-pole message)
- [ ] Public repository URL works
- [ ] Commit history is incremental and meaningful
- [ ] README permits a fresh user to run the application
- [ ] Requirements are updated with change rationale
- [ ] D2 LaTeX, slides, GAI evidence, repository, and demo are synchronized

**Before D3 submission**
- [ ] Code conforms to selected style
- [ ] Flake8 evidence is captured
- [ ] Real pdb debugging evidence is captured
- [ ] Pylint findings are addressed or justified
- [ ] Semantic version is consistent everywhere
- [ ] UIDP mind map identifies applicable and non-applicable principles
- [ ] Accessibility improvements are implemented and tested
- [ ] Unit tests cover requirements, identities, boundaries, and errors
- [ ] All tests pass on the final tagged commit
- [ ] Poster, repository, final version, GAI evidence, and demo are synchronized

---

## Key Risks & Mitigations

| Risk | Impact | Early warning | Mitigation |
|---|---|---|---|
| Angle unit ambiguity (rad vs deg) | Wrong results, rejected requirements | Users expect degrees; math default is radians | State radians as default; add a clearly-labelled unit selector; document the assumption |
| Input at/near a pole `π/2 + kπ` | Divide-by-near-zero, meaningless huge output | `tan(1.5707963)` returns an enormous number | Detect `|cos(x)| < ε`; raise `DomainError` with a helpful message instead of returning ∞ |
| Argument-reduction error for large `|x|` | Large inaccuracy silently returned | `tan(10000)` disagrees with references | Bound supported range; reduce with sufficient π precision; document the limit honestly |
| Slow/loss of precision near ±π/2 | Accuracy target missed | Series needs many terms near the edge | Reduce to [−π/4, π/4]; use `cot` complement where appropriate; cap max terms |
| "From scratch" violation | Major D2 compliance issue | Use of `math.tan`/`sin`/`cos`/`math.pi` | Implement sin/cos + π constant manually; maintain dependency inventory; clarify with professor |
| Tolerance chosen after seeing results | Weak, non-evidence-based requirement | Tests pass only after broadening tolerance | Define tolerance + reference methodology before final testing |
| GUI tightly coupled to math core | Testing/maintenance difficulty | Cannot test without launching window | Keep pure core functions + thin event handlers |
| Screenshots from different code versions | Evidence inconsistency | Tool output doesn't match repository | Capture evidence from one release-candidate commit + record hash |
| GAI documentation omitted | Mandatory constraint not met | Prompt history scattered across chats | Maintain per-problem prompt/evaluation log from the start |
| Late bulk Git commits | Weak process evidence | Most work remains uncommitted | Commit each cohesive task throughout development |

---

*Open item to clarify with the professor no later than the second lecture:* the project description labels a problem "Problem 7" in both D2 and D3 with different mark totals (20 vs 70) — confirm the intended numbering/weighting.
