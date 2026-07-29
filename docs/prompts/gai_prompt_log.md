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
