# SOEN 6011 — F2 Tangent Function tan(x) — Deliverable 1 CASTROFF Prompts

**Purpose:** One CASTROFF-framework prompt per Deliverable 1 problem, to be used with a public LLM/GAI tool and documented per constraint **C-03** (prompt type, example prompt, and explanation/evaluation of output).

**Format used (matching the course example):** each prompt is written with a **TASK**, **RESTRICTIONS**, **OUTPUT FORMAT**, and **AUDIENCE** section, with the project-specific context embedded inside the TASK.

**Standing context to carry into every prompt (F2):**
- Function: **tan(x)**, the real tangent function, `tan(x) = sin(x) / cos(x)`.
- Angle unit: **radians** (default and stated assumption); a degrees option may be offered but the mathematics is in radians.
- Properties: period π (`tan(x + π) = tan(x)`); odd (`tan(−x) = −tan(x)`); range = all reals; **undefined at the poles** `x = π/2 + kπ` (k ∈ ℤ) where `cos(x) = 0`.
- Special values: `tan 0 = 0`, `tan(π/6) = 1/√3`, `tan(π/4) = 1`, `tan(π/3) = √3`.
- D1 delivers: persona → requirements (ISO/IEC/IEEE 29148) → two language-neutral algorithms → algorithm-selection + Python CLI prototype.

**Reminder:** for each problem, record the exact prompt used, the LLM output, and a short critical evaluation (accepted/rejected portions and why). Never paste output verbatim without verification and attribution.

---

## Problem 1 — Persona [20 marks]

**Prompt type:** Generative + decision-support (persona synthesis informed by a template-selection mind map).

```
TASK:

Help me create one primary user persona for a scientific-calculator application whose
single function computes the real tangent function tan(x) = sin(x) / cos(x), with the
angle x expressed in radians. The tangent function has period pi, is odd
(tan(-x) = -tan(x)), has range equal to all real numbers, and is undefined at the poles
x = pi/2 + k*pi (k an integer) where cos(x) = 0.

First, compare at least three established persona-template styles (for example
goal-directed, role-based, and lightweight/proto personas) and recommend which single
template is most suitable for documenting the user of a small scientific calculator.
Justify the recommendation against these criteria: relevance to a computation tool,
realism, conciseness, traceability to future requirements, and support for
accessibility considerations. Present the comparison as a mind-map-style outline
(central concept "Persona Template for Tangent Function Calculator", with branches for
each candidate, its advantages, disadvantages, and the final choice).

Then, using the recommended template, draft one realistic primary persona for a likely
user such as an engineering, physics, or surveying student or lab/research assistant who
occasionally needs trustworthy tan(x) values but does not want to write code or use a
full computer-algebra system. Include: character name, job title/role, experience level,
relevant skills, goals, education, typical tasks, working environment,
hardware/software platforms, and tangent-calculator-specific needs and pain points (for
example confusion between radians and degrees, uncertainty about what happens near 90
degrees / pi over 2, wanting quick trustworthy results, limited comfort with the command
line, and a need for accessible feedback). Add a short usage scenario showing how the
persona uses tan(x). Clearly separate what is evidence, what is reasonable synthesis, and
what is an explicit assumption.

RESTRICTIONS:

Do not invent statistics or claim the persona is a real interviewed person. Do not
include biographical details that have no effect on the design or requirements. Keep
every persona attribute traceable to a plausible design or requirement need — the
persona must be able to justify at least five later requirements. Do not prescribe any
implementation technology or algorithm. Avoid generic template boilerplate; keep the
persona specific to a tangent-function calculator user.

OUTPUT FORMAT:

Provide (1) the template-comparison mind-map outline with the final decision and
rationale, and (2) the persona as a structured persona card with clearly labelled
fields, followed by a bullet list of assumptions and a short (3-5 sentence) usage
scenario. Use headings so the two parts can be placed on separate slides.

AUDIENCE:

The audience includes the SOEN 6011 professor, teaching assistants, and graduate
software engineering students. The content must therefore be evidence-based, concise,
traceable, and focused on how the persona informs later requirements, not on
storytelling for its own sake.
```

---

## Problem 2 — Requirements (ISO/IEC/IEEE 29148) [30 marks]
*Note: Problem 2 must be informed by Problem 1.*

**Prompt type:** Generative + transformational (persona needs → verifiable requirements) with review.

```
TASK:

Help me express the requirements for a scientific-calculator application that computes
the real tangent function tan(x) = sin(x) / cos(x), with x in radians, using a
requirement statement style and quality guidelines consistent with the ISO/IEC/IEEE
29148 standard. The requirements must be informed by the following persona and its goals
and pain points: [PASTE THE FINALISED PROBLEM 1 PERSONA, GOALS, AND PAIN POINTS HERE].

Produce a requirements specification that:
- Uses a single consistent statement style and a unique identifier scheme grouped by
  category, for example FR-01 (functional), VAL-01 (input validation/domain),
  ACC-01 (accuracy/numerical), USE-01 (usability), REL-01 (reliability),
  PERF-01 (performance), ERR-01 (error handling), DOC-01 (documentation).
- Records, for each requirement: identifier, statement, rationale/source (including the
  persona need it traces to), priority, and planned verification method (test,
  inspection, analysis, or demonstration).
- Covers accepting x, selecting/stating the angle unit, computing tan(x), displaying the
  result with a stated precision, clearing/retrying, and exiting; rejecting non-numeric,
  missing, and extreme-magnitude inputs, and detecting inputs at or near a pole
  (x = pi/2 + k*pi, where cos(x) approaches 0) with a helpful message rather than a huge
  or infinite number; a measurable accuracy tolerance with a defined reference method
  (for example relative error against trusted reference values); and understandable
  output.
- Lists all explicit project assumptions separately from the requirements (for example
  angle unit is radians; the supported input range for x; behaviour near poles).

Then review the draft for the 29148 quality characteristics (necessary, unambiguous,
complete, singular, feasible, verifiable, consistent) and report any requirement that
fails a characteristic, with a suggested correction.

RESTRICTIONS:

Do not prescribe a specific algorithm, library, or programming language inside a
requirement (algorithm selection happens later). Avoid vague terms such as "fast",
"user-friendly", or "accurate" unless they are quantified and measurable. Every
requirement must be singular (one testable statement) and independently verifiable. Do
not introduce requirements that the persona cannot justify. Do not copy standard text
verbatim; paraphrase and attribute.

OUTPUT FORMAT:

Provide the requirements as a table with columns: ID, Statement, Rationale/Source
(persona trace), Priority, Verification Method. Follow it with a separate "Assumptions"
list and a separate "Requirements review findings" table (ID, characteristic at risk,
issue, suggested fix). Use a layout that can be reproduced in LaTeX.

AUDIENCE:

The audience includes the SOEN 6011 professor, teaching assistants, and graduate
software engineering students. The requirements must therefore be standard-aligned,
uniquely identifiable, testable, and clearly traceable to the persona.
```

---

## Problem 3 — Two Algorithms in Pseudocode [20 marks]
*Note: Problem 3 must be informed by Problem 2.*

**Prompt type:** Generative + comparative (two independent, language-neutral algorithms in established pseudocode).

```
TASK:

Help me specify two genuinely different, language-independent algorithms for computing
the real tangent function tan(x) = sin(x) / cos(x), with x in radians, each written in an
established pseudocode convention (for example the style used in Cormen et al. / typical
algorithms-textbook pseudocode). The two algorithms must satisfy the following
requirements: [PASTE THE RELEVANT PROBLEM 2 REQUIREMENT IDS AND STATEMENTS HERE,
especially accuracy tolerance, angle unit, near-pole handling, and reliability].

Algorithm A (power series): first perform argument reduction using the period pi and the
odd symmetry to bring x into a small interval such as [-pi/4, pi/4], tracking the sign
and quadrant; then compute sin(x) and cos(x) with their Maclaurin/Taylor series
(sin(x) = sum of (-1)^n * x^(2n+1) / (2n+1)! ; cos(x) = sum of (-1)^n * x^(2n) / (2n)!),
stopping when the next term is below the tolerance or a maximum number of terms is
reached; finally return sin/cos, guarding against a near-zero cosine (a pole).

Algorithm B (CORDIC): use the CORDIC rotation method in circular mode with a precomputed
table of arctan(2^-i) angles and the CORDIC gain constant K, using only additions,
subtractions, and binary shifts to rotate a unit vector by the (reduced) angle x,
producing cos(x) and sin(x) simultaneously; then return sin/cos. (As an alternative
Algorithm B, you may instead specify the continued-fraction expansion
tan(x) = x / (1 - x^2 / (3 - x^2 / (5 - x^2 / (7 - ...)))) evaluated with Lentz's
algorithm.) State clearly which alternative you use.

For each algorithm, define: inputs, outputs, preconditions, postconditions, constants
and tolerance, input validation and exceptional termination (including detection of
inputs at or near a pole), the core computation steps, the convergence/stopping
condition, and a maximum-work (iteration/term) safeguard. State the computational
complexity and known numerical weaknesses (for example accuracy near +/- pi/2, and
argument-reduction error for large |x|). Include a short worked trace for a simple value
such as tan(pi/4) = 1 or tan(0) = 0. Confirm explicitly that the two algorithms are
substantially different, not superficial variants.

RESTRICTIONS:

Do not use Python or any real programming-language syntax; the pseudocode must be
language-neutral. Every loop or recursion must have a guaranteed termination condition or
a maximum-work safeguard. Do not assume access to a built-in tangent, sine, or cosine
function inside the algorithms — any subordinate function (sin, cos, power, factorial,
argument reduction) must be named and treated as separately definable. Do not present
the two algorithms as interchangeable; make their trade-offs explicit. Keep each step
traceable to a requirement where relevant.

OUTPUT FORMAT:

Provide two clearly separated pseudocode listings (Algorithm A, Algorithm B), each
followed by: a preconditions/postconditions note, a complexity-and-limitations note, and
a worked trace. End with a short "How A and B differ" comparison table (dimension,
Algorithm A, Algorithm B). Use monospaced/verbatim-friendly formatting suitable for a
LaTeX listing.

AUDIENCE:

The audience includes the SOEN 6011 professor, teaching assistants, and graduate
software engineering students. The pseudocode must therefore be rigorous, unambiguous,
independently implementable, and genuinely comparative rather than a single approach
written twice.
```

---

## Problem 4 — Algorithm Selection + Python CLI Implementation [30 marks]
*Note: Problem 4 must be informed by Problem 3.*

**Prompt type:** Decision-support (algorithm-selection mind map) + generative (Python implementation with a textual UI).

```
TASK:

Help me with two connected steps for a scientific-calculator application that computes
the real tangent function tan(x) = sin(x) / cos(x), with x in radians.

Step 1 - Selection: Use a mind-map-style comparison to decide which of the two
algorithms below to implement first. [PASTE THE TWO PROBLEM 3 ALGORITHMS OR THEIR
SUMMARIES HERE]. Central concept "Algorithm for tan(x)". Compare the candidates against:
accuracy, domain coverage and pole handling, numerical stability (near +/- pi/2 and for
large |x|), implementation effort, suitability for a later from-scratch reimplementation
(no built-in sin/cos/tan), performance, and explainability to the persona. Record
positive and negative evidence for each criterion, state which algorithm is selected, and
explain why the other is rejected for this stage.

Step 2 - Implementation: Produce a Python 3 command-line program that implements the
selected algorithm with a textual user interface for input and output. It must: separate
input/output code from the computation logic; prompt for x with its meaning, the angle
unit (radians), and a valid-domain hint; convert and validate the input; detect inputs
at or near a pole and report them helpfully instead of returning an enormous number;
compute tan(x) using the selected algorithm; display the result with a documented number
format and precision; and catch expected invalid-input and numerical-failure cases,
showing helpful messages instead of crashing. Add comments or docstrings only where they
explain intent or a non-obvious numerical decision (such as argument reduction or the
near-pole guard). Provide sample successful and unsuccessful runs.

RESTRICTIONS:

The selection must follow from the stated criteria, not from personal preference, and
must be consistent with the Problem 2 requirements while anticipating the Deliverable 2
"from scratch" constraint (no built-in tan, sin, cos, or pi in the final version). The
program must run from a terminal without depending on any IDE. Invalid inputs
(non-numeric, empty, extremely large) and inputs at or near a pole must never produce an
unhandled traceback. Do not present unsupported cases as correct. Keep the computation
core callable independently of the input/output code. This D1 prototype may use Python's
standard math facilities, but note which calls (sin, cos, pi) would need a from-scratch
replacement in Deliverable 2.

OUTPUT FORMAT:

Provide (1) the algorithm-selection mind-map outline with the decision and rationale,
(2) the complete, runnable Python source code in a single code block, and (3) a short
list of sample runs (valid case such as tan(pi/4), a boundary/near-pole case, a negative
argument showing odd symmetry, and an invalid case with its message) plus the exact
command used to run the program.

AUDIENCE:

The audience includes the SOEN 6011 professor, teaching assistants, and graduate
software engineering students. The output must therefore be evidence-based in its
selection, clean and readable in its code, robust against invalid and near-pole input,
and runnable outside an IDE.
```

---

## GAI Documentation Reminder (per prompt, for the report)

For each of the four prompts above, record in the report / GAI evidence log:
- **GAI tool used** (name and version/date).
- **Prompt type** (as labelled above).
- **Exact prompt** (the CASTROFF text actually submitted, including any pasted prior-problem content).
- **Output summary** and a **critical evaluation**: which parts were accepted, which were rejected or corrected, and why.
- **Verification**: how the output was independently checked (reference values, standard, requirement, or manual reasoning).
- **Attribution**: any non-original content cited appropriately.
