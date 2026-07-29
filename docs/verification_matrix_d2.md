# D2-P5.6 — Verification Matrix (Numerical Core + GUI)

Run against commit-time source with `python3 -m tests.manual_verification_d2`
(full script: `tests/manual_verification_d2.py`; not the formal PyUnit suite,
which is D3-P8.2). Reference values are Python's `math.tan` computed
independently and pasted as literals -- never the from-scratch algorithm
verifying itself. Relative-error tolerance is `1e-9` per requirement ACC-01.

## Numerical core results (15/15 pass)

| Case | x | Result | Relative error | Requirement(s) | Verdict |
|---|---|---|---|---|---|
| Zero | `0.0` | `0.0` | `0.00e+00` | FR-03, ACC-01 | Pass |
| Special pi/6 | `0.5235987755982988` | `0.577350269189625` | `1.15e-15` | ACC-01 | Pass |
| Special pi/4 | `0.7853981633974483` | `1.0000000000000013` | `1.44e-15` | ACC-01 | Pass |
| Special pi/3 | `1.0471975511965976` | `1.7320508075688776` | `5.13e-16` | ACC-01 | Pass |
| Negative (odd symmetry) | `-0.7853981633974483` | `-1.0000000000000013` | `1.44e-15` | ACC-01, odd symmetry | Pass |
| Small positive | `0.1` | `0.10033467208545055` | `1.38e-16` | ACC-01 | Pass |
| Beyond one period (`pi+pi/4`) | `3.9269908169872414` | `0.9999999999999996` | `1.11e-16` | ACC-01, period pi | Pass |
| Large argument | `1000.0` | `1.4703241557018916` | `5.63e-13` | ACC-01, VAL-03 | Pass |
| Near pole (+) | `1.5707953267948966` (`pi/2 - 1e-6`) | `999999.999637844` | `3.83e-10` | ACC-01 | Pass |
| Near pole (-) | `-1.5707953267948966` | `-999999.999637844` | `3.83e-10` | ACC-01, odd symmetry | Pass |
| At pole exactly | `1.5707963267948966` (`pi/2`) | raised `DomainError` | n/a | VAL-04, ERR-01/02, REL-01 | Pass (rejected as designed) |
| Out of range | `1.0e10` | raised `NumericalRangeError` | n/a | VAL-03, ERR-01/02, REL-01 | Pass (rejected as designed) |
| Out of range (negative) | `-1.0e10` | raised `NumericalRangeError` | n/a | VAL-03, ERR-01/02, REL-01 | Pass (rejected as designed) |
| Invalid non-numeric | `"abc"` | raised `ValueError` | n/a | VAL-01, ERR-01, REL-01 | Pass (rejected as designed) |
| Invalid empty | `""` | raised `ValueError` | n/a | VAL-02, ERR-01, REL-01 | Pass (rejected as designed) |

**Observation:** the near-pole cases (`3.83e-10`) sit closest to the `1e-9`
tolerance ceiling of any passing case, confirming the D1 prediction that
precision degrades near the guard-band boundary (`docs/algorithms/algorithm_A_maclaurin.md`,
"known numerical weaknesses" #3). Still within tolerance, but the margin is
worth documenting rather than hiding (D2-P7.1 revisits ACC-01 accordingly).

## CLI evidence (`docs/screenshots/`)

| File | Case |
|---|---|
| `d2_cli_session.txt` | Full scripted session: valid, degrees prefix, invalid, empty, near-pole, out-of-range, quit |

## GUI evidence (`docs/screenshots/`)

| File | Case | Requirement(s) |
|---|---|---|
| `d2_gui_initial.png` | Startup state, default focus on `x` field, radians selected | D2-P5.4 default focus, USE-01 |
| `d2_gui_valid_pi4.png` | `x = pi/4` radians -> `tan = 1` | FR-03/04, ACC-01 |
| `d2_gui_degrees_45.png` | Degrees unit selected, `x = 45` -> label updates to "x (degrees)", `tan = 1` | FR-02, degree-conversion (D2 extension) |
| `d2_gui_near_pole.png` | `x = pi/2` -> red "Error: x is at/near an asymptote..." message, no traceback | VAL-04, ERR-01/02, REL-01 |
| `d2_gui_out_of_range.png` | `x = 1e10` -> "Error: input out of range..." | VAL-03, ERR-01/02, REL-01 |
| `d2_gui_invalid_text.png` | `x = "abc"` -> "Error: 'abc' is not a valid real number..." | VAL-01, ERR-01, REL-01 |

**Done when (D2-P5.6):** critical defects resolved (none found -- all 15
numerical cases and all captured GUI states pass on first implementation);
known limitation documented (near-pole relative error approaches, but does
not exceed, the `1e-9` ceiling); behavior ready to drive the D2-P7.1
requirement update.
