# Sample CLI Runs — Problem 4 (Step 5)

This is a headless development environment with no interactive GUI terminal available, so a literal OS-level screenshot could not be captured. Instead, each `.txt` file is a **verbatim transcript** of `python3 src/cli.py` run with piped input (the exact command is given below each case), and each matching `.png` is that transcript rendered in a terminal-styled image for use in the report/slides. The `.txt` is the source of truth; the `.png` is a presentation copy of the same text.

| File | Command | Cases covered |
|---|---|---|
| `run1_valid_and_odd_symmetry.{txt,png}` | `printf '0.7853981633974483\n-0.7853981633974483\n0.5235987755982988\n1.0471975511965976\nquit\n' \| python3 src/cli.py` | Valid special values (`pi/4`, `pi/6`, `pi/3`) and a negative argument demonstrating odd symmetry (`tan(-pi/4) = -tan(pi/4)`) |
| `run2_invalid_and_missing.{txt,png}` | `printf 'abc\n\nquit\n' \| python3 src/cli.py` | Non-numeric input (`abc`) and missing/empty input, each with a helpful message, no crash |
| `run3_near_pole.{txt,png}` | `printf '1.5707963257948965\n-1.5707963267948965\nquit\n' \| python3 src/cli.py` | Near-pole input on both sides (`pi/2 - 1e-9` and `-pi/2`), rejected with an explanation instead of a huge number |
| `run4_large_argument.{txt,png}` | `printf '1000\n1e10\nquit\n' \| python3 src/cli.py` | Large-but-supported argument (`x = 1000`, within `|x| <= 1e4`) and an out-of-range argument (`x = 1e10`) |

All four runs were also cross-checked against the reference-value table in `docs/research_notes.md` (Section 4) and confirmed via `python3 -c "import math; ..."` — see the verification matrix in `docs/verification_matrix.md`.
