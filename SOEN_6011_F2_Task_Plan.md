# SOEN 6011 — F2 Tangent Function tan(x) — Project Task Plan

**Course:** SOEN 6011 (Software Engineering Processes), Section CC, Summer 2026
**Assigned function:** **F2 — tan(x)** (transcendental tangent function)
**Type:** Individual · **Language:** Python · **Deliverables:** D1, D2, D3

This is the high-level plan. Full task breakdown is in [SOEN_6011_F2_Task_List.md](SOEN_6011_F2_Task_List.md);
D1 working order is in [SOEN_6011_F2_D1_Execution_Steps.md](SOEN_6011_F2_D1_Execution_Steps.md);
the D1 GAI prompts are in [SOEN_6011_F2_D1_Prompts.md](SOEN_6011_F2_D1_Prompts.md).

---

## 1. The function

`tan(x) = sin(x) / cos(x)` — a transcendental, periodic function.

| Property | Value |
|---|---|
| Period | π (`tan(x + π) = tan(x)`) |
| Symmetry | Odd (`tan(−x) = −tan(x)`) |
| Range | All real numbers |
| Undefined at (poles) | `x = π/2 + kπ`, k ∈ ℤ (where `cos(x) = 0`) |
| Special values | `tan 0 = 0`, `tan(π/6) = 1/√3`, `tan(π/4) = 1`, `tan(π/3) = √3` |

**Key assumptions to confirm with the professor:** angle unit = **radians**; refuse/flag inputs at or near a pole; declare a supported range for large `|x|` (argument reduction loses precision).

---

## 2. Deliverables at a glance

| Deliverable | Focus | Key problems (marks) | Presentation |
|---|---|---|---|
| **D1** | Persona · Requirements · Two algorithms · CLI prototype | P1 [20], P2 [30], P3 [20], P4 [30] | Zoom slides + demo |
| **D2** | From-scratch implementation · Tkinter GUI · public VCS · updated requirements | P5 [60], P6 [20], P7 [20] | Zoom slides + demo |
| **D3** | Style · quality tools (Flake8/pdb/Pylint) · SemVer · accessibility (UIDP) · unit tests | P7 [70], P8 [30] | In-person poster + demo |

*Note:* the project description labels a "Problem 7" in both D2 (20) and D3 (70) — confirm the numbering with the professor.

---

## 3. Chosen technical approach

**Two candidate algorithms (D1-P3), genuinely different:**

- **Algorithm A — Power series.** Argument-reduce `x` into `[−π/4, π/4]` using period π + odd symmetry, then evaluate the Maclaurin series for `sin(x)` and `cos(x)` and return `sin/cos`. Simple, transparent, easy to reason about accuracy; needs a near-zero-cosine guard.
- **Algorithm B — CORDIC** (shift-and-add rotations with a precomputed `arctan(2⁻ⁱ)` table), producing `sin` and `cos` together; return `sin/cos`. *(Alternative B: Lentz-evaluated continued fraction for `tan(x)`.)* Hardware-friendly, multiplication-free, fundamentally different family.

**From-scratch boundary (D2):** replace `math.tan`, `math.sin`, `math.cos`, and `math.pi` with manual implementations — a π constant, argument reduction modulo π, factorial/power, and the series (or CORDIC) — keeping only input/output/arithmetic/UI/exception facilities.

---

## 4. Dependency chain

`Persona → Requirements → Two Algorithms → Selection → CLI → From-scratch GUI → Updated Requirements → Quality/Accessibility → Unit Tests`

P2 ← P1 · P3 ← P2 · P4 ← P3 · D2 modifies D1 · D3 modifies D2.

---

## 5. D1 critical path & schedule (submission Wed 2026-07-15, 12:00 noon)

1. Setup + research (function facts, reference-value table, risk list)
2. **P1** persona (+ template mind map)
3. **P2** requirements (ISO/IEC/IEEE 29148, unique IDs, assumptions)
4. **P3** two pseudocode algorithms (+ comparison)
5. **P4** selection mind map + Python CLI (+ sample runs)
6. Verify (verification matrix incl. near-pole & negative-argument cases)
7. LaTeX report → Beamer slides → demo prep → zip & submit

**Submission artifact:** `zip = Source Code + LaTeX (.tex) + PDF`. Present the same day on Zoom (F2 = 2nd in order), 7 min + 3 min Q/A.

---

## 6. Top risks

| Risk | Mitigation |
|---|---|
| Radians-vs-degrees ambiguity | Default radians, labelled unit selector, documented assumption |
| Input at/near a pole `π/2 + kπ` | Detect `|cos x| < ε` → `DomainError` with a helpful message |
| Argument-reduction error for large `|x|` | Bound the supported range; reduce with sufficient π precision; document honestly |
| "From-scratch" violation in D2 | Implement sin/cos + π manually; keep a dependency inventory |
| Evidence/version drift | One release-candidate commit for all screenshots; consistency review before each submission |

---

## 7. Standing constraints (every problem)

Individual work · LaTeX typeset · public GAI tools with CASTROFF prompts documented · cite all non-original work · evidence-based claims · iterative consistency across deliverables.
