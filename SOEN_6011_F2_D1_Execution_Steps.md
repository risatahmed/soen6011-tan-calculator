# SOEN 6011 — F2 Tangent Function tan(x) — D1 Execution Steps (do one at a time)

**Deadline:** Submit to Moodle **Wed 2026-07-15, 12:00 noon** — zip = **Source Code + LaTeX + PDF**.
**Present:** Zoom same day 19:45–22:45 — Beamer slides, 7 min + 3 min Q/A (F2 presents 2nd).
**Rule:** each step is finished only when its artifact is saved **and** its GAI/decision use is logged (C-03).

References: prompts in [SOEN_6011_F2_D1_Prompts.md](SOEN_6011_F2_D1_Prompts.md) · full detail in [SOEN_6011_F2_Task_List.md](SOEN_6011_F2_Task_List.md).

---

## Step 0 — Setup (once)
- [ ] Create the folder layout: `src/`, `docs/{requirements,algorithms,mindmaps,screenshots,prompts,decisions}/`, `deliverables/{D1,D2,D3}/`, `tests/`.
- [ ] Start three running logs: **decision log** (`docs/decisions/decision_log.md`), **GAI/prompt log** (`docs/prompts/gai_prompt_log.md`), **bibliography** (`docs/references.bib`).
- [ ] Init a local git repo on `main`; make the first commit (`git commit -m "Scaffold project structure and evidence logs"`).
- [ ] **You:** confirm with professor — **angle unit = radians**; the near-pole handling policy; the supported large-argument range; and the D2/D3 "Problem 7" numbering.

## Step 1 — Research (feeds everything)
- [ ] Write short notes: `tan = sin/cos`, period π, odd symmetry, poles at `π/2 + kπ`, range = ℝ, special values (`tan 0 = 0`, `tan(π/6)=1/√3`, `tan(π/4)=1`, `tan(π/3)=√3`), applications.
- [ ] Build a small **reference-value table** (trusted `tan(x)` values, incl. a near-pole and a negative-argument case) for later verification.
- [ ] List numerical risks: poles/asymptotes, argument-reduction error for large `|x|`, slow convergence near ±π/2, overflow, cancellation.
- **Output:** research notes + reference table in `docs/`.

## Step 2 — Problem 1: Persona [20]
- [ ] Run the **P1 prompt** → get template comparison + persona draft.
- [ ] Build the **template-selection mind map**; export a hi-res image to `docs/mindmaps/`.
- [ ] Finalize the **persona card** (name, role, experience, skills, goals, environment, needs, pain points) + usage scenario — emphasise tan-specific pains (rad vs deg confusion, behaviour near 90°/π-2).
- [ ] Log the P1 prompt + your evaluation.
- **Output:** persona mind map image + persona card. **Gate:** ≥5 needs/pains you can trace to requirements.

## Step 3 — Problem 2: Requirements (ISO/IEC/IEEE 29148) [30]
- [ ] Run the **P2 prompt** (paste the finalized persona).
- [ ] Produce the requirements table: ID · statement · rationale/persona-trace · priority · verification method.
- [ ] Write the **assumptions** list separately (angle unit = radians; domain excludes poles; supported argument range).
- [ ] Do the quality review pass; fix flagged requirements; freeze as baseline v0.1.
- [ ] Log the P2 prompt + evaluation.
- **Output:** requirements table + assumptions + traceability. **Gate:** every requirement unique, testable, traceable.

## Step 4 — Problem 3: Two Algorithms [20]
- [ ] Run the **P3 prompt** (paste relevant requirement IDs).
- [ ] Write **Algorithm A** pseudocode (range reduction + Maclaurin series for sin & cos, then divide) + worked trace (`tan(π/4)=1`).
- [ ] Write **Algorithm B** pseudocode (CORDIC rotations, or Lentz continued fraction) + worked trace.
- [ ] Add the "How A and B differ" comparison.
- [ ] Log the P3 prompt + evaluation.
- **Output:** two pseudocode listings (language-neutral) + comparison. **Gate:** genuinely different; each terminates.

## Step 5 — Problem 4: Selection + Python CLI [30]
- [ ] Run the **P4 prompt** (paste both algorithms).
- [ ] Build the **algorithm-selection mind map**; export image to `docs/mindmaps/`.
- [ ] Write the Python CLI (`src/cli.py`): I/O separated from compute, angle-unit + domain hint, validation, near-pole guard, helpful errors, documented precision.
- [ ] Run valid / boundary / invalid / near-pole / negative / large-argument cases; save terminal screenshots to `docs/screenshots/`.
- [ ] Note which `math` calls (`sin`, `cos`, `pi`) will need from-scratch replacement in D2.
- [ ] Log the P4 prompt + evaluation.
- **Output:** selection mind map + runnable `cli.py` + sample runs. **Gate:** runs from terminal, no unhandled crash.

## Step 6 — Verify D1 (P4.3)
- [ ] Build a verification matrix: requirement ID → demo case → result vs reference.
- [ ] Include a near-pole case and a negative-argument (odd-symmetry) case explicitly.
- [ ] Record honest known limitations (large arguments, near-pole precision).
- **Output:** verification matrix + known-limitations list.

## Step 7 — LaTeX Report (D1-REP)
- [ ] Assemble report in LaTeX: sections for P1–P4, figures (persona + both mind maps), requirements table, both pseudocode listings, decision rationale, implementation summary.
- [ ] For each problem, include GAI tool, prompt type, CASTROFF prompt example, output explanation, critical evaluation.
- [ ] Add references in one consistent citation style.
- **Output:** `report.tex` → `report.pdf`.

## Step 8 — Beamer Slides (D1-REP)
- [ ] Create the Beamer deck (`\documentclass{beamer}`): title → outline → persona → requirements → algorithms → selection → CLI/demo → GAI evidence → limitations → references.
- [ ] Keep slides to ~7 min; slides explain **decisions**, not the full report.
- [ ] Compile to PDF.
- **Output:** `slides.tex` → `slides.pdf`.

## Step 9 — Demo prep
- [ ] Write a timed demo script; pre-open terminal + files; capture fallback screenshots in case live run fails.
- [ ] Include a near-pole input in the demo to show graceful error handling.

## Step 10 — Package & submit (before noon)
- [ ] Consistency check: version, angle unit, domain, tolerance, algorithm name, requirements, screenshots all agree across report/slides/code.
- [ ] Build the **zip = source code + LaTeX (.tex) + PDF(s)**.
- [ ] Submit on Moodle. Back up a copy offline + remote.

---

### Suggested order if time is tight
Research → P1 → P2 → P3 → P4 (code) → verify → report → slides → package.
P2 needs P1, P3 needs P2, P4 needs P3 — so they **cannot** be parallelized out of order. Report and slides can be drafted in parallel once P1–P4 exist.
