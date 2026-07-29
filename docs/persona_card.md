# Problem 1 — Persona (Deliverable 1)

## Part 1 — Template-selection mind map (summary)

See `docs/mindmaps/persona_template_mindmap.png` (source: `docs/mindmaps/persona_template_mindmap.dot`) for the full mind map. Summary of the comparison:

| Template | Advantages | Disadvantages | Verdict |
|---|---|---|---|
| **Goal-directed** (Cooper) | Strong tie to user goals; drives requirement traceability; filters out irrelevant biography | Requires a clear goal/task analysis up front | **SELECTED** |
| Role-based | Good fit when a system serves many distinct job functions | Overkill for a single-function calculator; adds ceremony without added traceability | Rejected |
| Lightweight / proto-persona | Fast to produce, low overhead | Thin on evidence; weak traceability; risks generic boilerplate | Rejected |

**Decision:** the **goal-directed template** is used, evaluated against: relevance to a computation tool, realism, conciseness, traceability to future requirements, and support for accessibility considerations. It wins because a one-function calculator's design is entirely driven by *what the user is trying to accomplish* with `tan(x)`, and every field in the template must earn its place by tracing to a later requirement — exactly what a role-based or proto-persona template does not enforce.

---

## Part 2 — Persona card

| Field | Value |
|---|---|
| **Name** | Maya Chen |
| **Role / job title** | M.A.Sc. student, Mechanical Engineering; part-time research assistant in an undergraduate optics teaching lab |
| **Experience level** | Comfortable with algebra, trigonometry, and basic scripting (has used spreadsheets and MATLAB in coursework); not a professional software developer |
| **Relevant skills** | Reading angle/triangle problems from lab manuals; unit conversion between degrees and radians; sanity-checking numeric results against known special angles (e.g. 30°/45°/60°) |
| **Goals** | Get a trustworthy `tan(x)` value quickly during a lab session without opening a full CAS (e.g. MATLAB/Mathematica) just for one number; avoid silently wrong answers from a radians/degrees mix-up |
| **Education** | B.Eng. (Mechanical), currently in an M.A.Sc. program |
| **Typical tasks** | Computing the angle of a refracted beam or an incline's slope; checking a hand-derived formula against a quick numeric evaluation; occasionally probing behaviour very close to 90 degrees when a setup is nearly vertical |
| **Working environment** | Shared teaching lab and personal laptop; sometimes SSH'd into a lab machine over a slow connection; prefers a lightweight terminal tool over launching a heavyweight IDE or CAS |
| **Hardware/software platforms** | Laptop (Windows or macOS) with a terminal available; occasional lab desktop with only a bare Python install, no GUI toolkits guaranteed |
| **Tangent-specific needs** | (1) A clear statement of whether the input is expected in radians or degrees, since her lab manuals mix both; (2) confidence that a value near 90 degrees / `pi/2` won't silently return a nonsensical huge number; (3) a documented precision/accuracy so she can decide if the result is good enough for a lab report; (4) a way to double-check a familiar special value (e.g. `tan(45°) = 1`) to build trust in a new tool; (5) clear, non-cryptic error messages when she mistypes or enters something out of range |
| **Pain points** | Confusion between radians and degrees leading to silently wrong answers; not knowing what happens if her angle lands very close to an asymptote; distrust of "black box" results with no way to sanity-check; limited patience for command-line tools that crash with a raw Python traceback instead of a helpful message; needing quick answers without booting a full computer-algebra system |

### Assumptions (explicitly separated from evidence)

- **Evidence:** the tangent function's mathematical properties (period, poles, special values) used to justify the pain points are drawn from Step 1 research notes (`docs/research_notes.md`), not invented.
- **Reasonable synthesis:** Maya's specific role (mechanical engineering + optics lab) is a plausible, illustrative composite of the kind of user in the task list ("engineering, physics, or surveying student or lab/research assistant"), not a real interviewed individual.
- **Explicit assumptions:**
  - Maya is not a professional programmer and should not need to read source code to trust the tool.
  - She has access to a terminal but not necessarily a GUI environment (consistent with D1's textual-interface constraint).
  - Her lab materials sometimes express angles in degrees, motivating an explicit radians-is-the-default statement (not a silent assumption) even though D1 computes in radians only.
  - No claim is made that Maya represents the only possible user — she is the *primary* persona used to drive requirements prioritization.

### Usage scenario

Maya is checking the exit angle of a light beam in a refraction experiment. Her lab manual gives the angle as `50.5` degrees, and she needs `tan` of the equivalent radian value to finish a slope calculation for her report. She opens the calculator in her terminal, and it clearly tells her that the input `x` must be in radians and reminds her of the valid domain before she types anything. She converts `50.5` degrees to radians herself (`~0.8814` rad), enters it, and gets a numeric result with a stated precision — plus, out of curiosity, she also tries an angle suspiciously close to `pi/2` and is relieved to see a clear "near an undefined point" message instead of a giant meaningless number.

### Persona-to-requirement traceability (gate check: >= 5 needs traced)

| Persona need / pain point | Traces to (planned requirement category) |
|---|---|
| 1. Confusion between radians and degrees | FR (state/confirm angle unit) |
| 2. Fear of silent huge numbers near 90 degrees / pi/2 | VAL (near-pole detection) + ERR (helpful message) |
| 3. Wants a documented precision to judge lab-report suitability | ACC (accuracy tolerance) + DOC (documented precision) |
| 4. Wants to sanity-check against a known special value | ACC (verification against reference values) |
| 5. Limited patience for cryptic tracebacks on typos | ERR (helpful error messages, no unhandled crash) |
| 6. No full CAS available / prefers lightweight terminal tool | USE (textual interface, runs from terminal) |
| 7. Occasionally works on a bare lab machine | REL / PERF (no heavyweight dependencies, runs standalone) |

Seven traceable needs identified, exceeding the >=5 gate for Step 2.
