# D2-P5.1 — From-Scratch Boundary: Dependency Inventory

Per the D2 constraint ("no prohibited direct trig call... every retained
dependency justified"), this document lists every standard-library /
built-in dependency touched by `src/`, classifies it, and states the final
interpretation of the from-scratch boundary.

## Interpretation adopted

**Prohibited:** any function that itself computes trigonometric,
exponential, logarithmic, or other transcendental "mathematical support"
directly (e.g. `math.sin`, `math.cos`, `math.tan`, `math.atan`, `math.pi`,
`cmath.*`, any third-party numerics library replicating these).

**Permitted (not "mathematical support" in the prohibited sense):**
elementary arithmetic operators (`+ - * / %`), comparison operators,
`abs()`, `round()` (banker's-rounding to nearest integer — not a
trigonometric or transcendental computation), Python control flow
(`while`/`for`/`if`), I/O (`print`, `input`, `sys.stdin`), string/number
parsing (`float()`, `str.strip()`), and the Tkinter GUI toolkit (UI
rendering, not mathematical computation). This interpretation was recorded
as **decision D-06** (`docs/decisions/decision_log.md`) and follows the
task list's own examples of the boundary (`sin`, `cos`, the `pi` constant,
argument reduction modulo `pi`, factorial, power/`x^n` are named as
needing manual implementation; ordinary arithmetic is not on that list).

## Dependency inventory

| Symbol | Where used | Classification | Disposition |
|---|---|---|---|
| `math.sin`, `math.cos`, `math.tan` | *(D1 cli.py never called these — verified absent)* | Prohibited mathematical support | **Not used anywhere in D2.** |
| `math.pi` | D1 `src/cli.py` line 17 (`PI = math.pi`) | Prohibited mathematical support (transcendental constant from a library) | **Replaced.** `src/constants.py` now derives `PI` from a Machin-like arctangent identity (`pi = 16*arctan(1/5) - 4*arctan(1/239)`), with `arctan` itself evaluated by a hand-written Maclaurin series using only `+ - * /`. No `import math` remains in `src/constants.py`, `src/trig_series.py`, `src/tan_core.py`, or `src/validation.py`. |
| `math.atan` | Not used | Prohibited mathematical support | Not needed — `arctan` for the Machin formula is implemented from scratch in `src/constants.py::_arctan_series`. |
| Maclaurin series for `sin`, `cos` | `src/trig_series.py` | Subordinate function — manually implemented, not a library call | Retained; this *is* the from-scratch implementation (unchanged in algorithmic structure from D1, which already avoided `math.sin`/`math.cos`). |
| Range reduction modulo `pi/2` | `src/tan_core.py` | Subordinate function | Manually implemented using the from-scratch `PI` and arithmetic only. |
| `round()` | `src/tan_core.py` (nearest multiple of `pi/2`) | Built-in numeric rounding, not trigonometric | Permitted — rounds to nearest integer, no trigonometric/transcendental computation involved. |
| `abs()` | throughout `src/` | Built-in arithmetic (absolute value) | Permitted. |
| `float()`, `str.strip()` | `src/validation.py` | I/O / text parsing | Permitted — input conversion, not mathematical computation. |
| `sys.stdin`/`sys.stdout` | `src/cli.py` | I/O | Permitted. |
| `tkinter` (`Tk`, `ttk`, widgets, `StringVar`, event bindings) | `src/gui.py` | UI toolkit | Permitted — renders and collects input/output; performs no trigonometric computation itself. All numeric work is delegated to `src/tan_core.py`. |
| `factorial`/`x**n` (power) | Not used directly | N/A | Algorithm A's series is evaluated by an incremental term recurrence (`term = term * (-(r*r)) / ((2n)(2n+1))`, etc.), which never calls `math.factorial` or the `**` power operator — the recurrence itself avoids needing them, per the D1 pseudocode. |

## Verification

```
$ grep -rn "math\." src/ | grep -v "^Binary"
(no output — confirmed no math module symbol is referenced anywhere in src/)
$ grep -rn "^import math\|^from math" src/
(no output)
```

**Done when:** no prohibited direct trig call remains (`math.tan`/`math.sin`/`math.cos`/`math.pi` all absent from `src/`), confirmed above; every retained standard-library/toolkit dependency is justified in the table.
