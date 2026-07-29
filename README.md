# A User-Centred, From-Scratch Scientific Calculator for tan(x)

**Public repository:** https://github.com/risatahmed/soen6011-tan-calculator

SOEN 6011 (Software Engineering Processes), Section CC, Summer 2026 --
individual project (F2: tangent function). Deliverable 2 (D2): from-scratch
numerical core, Tkinter GUI, and an updated requirements baseline built on
top of the Deliverable 1 (D1) persona/requirements/algorithms/CLI.

## What this is

A calculator for the real tangent function `tan(x) = sin(x)/cos(x)`, `x`
in radians by default (degrees optional). It:

- computes `sin`/`cos` itself via a from-scratch Maclaurin series (no
  `math.sin`/`math.cos`/`math.tan`);
- derives its own value of `pi` from scratch via a Machin-like arctangent
  series (no `math.pi`) -- see `docs/from_scratch_boundary.md`;
- detects and rejects inputs at/near a pole (`x = pi/2 + k*pi`) instead of
  returning a meaningless huge number;
- bounds the supported argument range (`|x| <= 1e4` radians) and says so
  rather than silently degrading;
- is available as both a terminal CLI and a Tkinter GUI, sharing the same
  numerical core.

See `docs/persona_card.md` for the target user (Maya Chen) and
`docs/requirements/requirements_v0.2.md` for the current requirements
baseline.

## Known limitations (stated up front, not discovered by surprise)

- Supported range is `|x| <= 1e4` radians; accuracy is not guaranteed
  beyond that (argument reduction modulo a finite-precision `pi`
  accumulates error proportional to `|x|`).
- Near the pole-tolerance boundary, measured relative error approaches
  (but does not exceed) the `1e-9` requirement ceiling -- see
  `docs/verification_matrix_d2.md`, "Observation."
- No performance/timing requirement is verified (deliberately out of
  scope; not part of the persona's stated pain points).
- The formal PyUnit/`unittest` suite is a Deliverable 3 deliverable
  (Problem 8); D2's verification is `tests/manual_verification_d2.py`, a
  standalone reference-value script, not the graded unit-test suite.

## Requirements

- Python 3.9+ (developed/tested on Python 3.13). No third-party packages.
- Tkinter (bundled with the standard python.org macOS/Windows installers;
  on some Linux distributions install it separately, e.g.
  `sudo apt install python3-tk`).

## Running

From the repository root (the directory containing `src/`):

```bash
python3 -m src.cli     # terminal interface
python3 -m src.gui     # Tkinter graphical interface
```

(Module (`-m`) invocation is used, not `python3 src/cli.py` directly,
because the modules import each other as `src.<name>` -- running as `-m`
guarantees the repository root is on `sys.path` regardless of your current
directory.)

## Usage examples

**CLI** (radians by default; prefix a value with `d:` for degrees):

```
$ python3 -m src.cli
tan(x) calculator (Deliverable 2 -- from-scratch core, Tkinter GUI also available via 'python3 -m src.gui')
  ...
Enter x (radians, or 'd:<value>' for degrees), or 'quit' to exit: 0.7853981633974483
tan(0.7853981634) = 1
Enter x (radians, or 'd:<value>' for degrees), or 'quit' to exit: d:45
tan(0.7853981634) = 1
Enter x (radians, or 'd:<value>' for degrees), or 'quit' to exit: 1.5707963267948966
Cannot compute tan(x): x is at or within tolerance of a pole (x = pi/2 + k*pi), where cos(x) is approximately zero and tan(x) is undefined.
```

Full transcript: `docs/screenshots/d2_cli_session.txt`.

**GUI:**

| State | Screenshot |
|---|---|
| Valid input (`x = pi/4`) | `docs/screenshots/d2_gui_valid_pi4.png` |
| Degrees mode (`x = 45`) | `docs/screenshots/d2_gui_degrees_45.png` |
| Near-pole error | `docs/screenshots/d2_gui_near_pole.png` |
| Out-of-range error | `docs/screenshots/d2_gui_out_of_range.png` |
| Invalid text error | `docs/screenshots/d2_gui_invalid_text.png` |

## Error messages / troubleshooting

| Message contains... | Cause | What to do |
|---|---|---|
| "is not a valid real number" | Non-numeric input (VAL-01) | Re-enter a real number, e.g. `0.785` or `-1.2`. |
| "No input received" | Empty input (VAL-02) | Enter a value before pressing Calculate/Enter. |
| "exceeds the supported range" | `\|x\| > 1e4` radians after unit conversion (VAL-03) | Use a smaller-magnitude `x`; accuracy is not guaranteed beyond this bound. |
| "at or within tolerance of a pole" / "at/near an asymptote" | `x` within `1e-6` of `pi/2 + k*pi` (VAL-04) | `tan(x)` is undefined there; choose an `x` further from the pole. |
| "did not converge" | Internal series safeguard triggered (should not occur for `\|x\| <= 1e4`; report as a defect if seen) | File an issue with the exact `x` value. |

## Repository structure

```
D1/                              (working directory name; project spans D1-D3)
├── README.md                    (this file)
├── src/
│   ├── constants.py              from-scratch PI (Machin-like arctan series)
│   ├── exceptions.py             DomainError, NumericalRangeError, ConvergenceError
│   ├── trig_series.py            from-scratch sin/cos (Maclaurin series)
│   ├── tan_core.py                pure tan(x, tolerance, max_terms)
│   ├── validation.py             input parsing + degrees/radians conversion
│   ├── cli.py                    terminal interface
│   └── gui.py                    Tkinter interface
├── tests/
│   └── manual_verification_d2.py D2 reference-value verification pass
├── docs/
│   ├── persona_card.md, research_notes.md, references.bib     (D1)
│   ├── requirements/requirements_v0.1.md, requirements_v0.2.md
│   ├── algorithms/                                              (D1)
│   ├── mindmaps/                                                (D1)
│   ├── decisions/decision_log.md
│   ├── prompts/gai_prompt_log.md
│   ├── from_scratch_boundary.md   (D2)
│   ├── gui_wireframe.md           (D2)
│   ├── verification_matrix.md     (D1) / verification_matrix_d2.md (D2)
│   └── screenshots/
└── deliverables/
    ├── D1/report.tex, slides.tex (+ PDFs)
    └── D2/report.tex, slides.tex (+ PDFs)
```

## Version & authorship

Risat Ahmed, Student ID 40294116, SOEN 6011 Section CC, Concordia
University, Summer 2026. Deliverable 2 build. Semantic versioning is
formally adopted in Deliverable 3 (D3-P7.5); informally, this is the
"D2 GUI" milestone referenced there as `0.2.0`.

## GAI usage

Every problem in this deliverable used a public GAI tool (Claude Code,
Claude/Anthropic, Sonnet 5) with a documented prompt, output evaluation,
and verification method, per constraint C-03. Full log:
`docs/prompts/gai_prompt_log.md`. Decisions and their rationale:
`docs/decisions/decision_log.md`.
