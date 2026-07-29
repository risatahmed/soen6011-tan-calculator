# D2-P5.4 — Tkinter GUI Wireframe

Designed before coding, per D2-P5.4. Targets persona Maya Chen's needs:
explicit angle-unit statement (need 1), a visible domain hint before
disaster near a pole (need 2), a documented precision (need 3), and
non-cryptic errors shown near context (need 5).

## ASCII wireframe

```
+---------------------------------------------------------------+
|  tan(x) Calculator  -- Deliverable 2                    [ - X ]|
+---------------------------------------------------------------+
|                                                                 |
|  x :  [_______________________]   Unit: (o) radians ( ) degrees|
|                                                                 |
|  Domain hint: |x| <= 10000; rejected within 1e-06 of a pole    |
|  (x = pi/2 + k*pi). Enter is expected in the selected unit.    |
|                                                                 |
|       [ Calculate (Enter) ]      [ Clear (Esc) ]               |
|                                                                 |
|  Result:  tan(0.7853981634) = 1.000000000                      |
|                                                                 |
|  Status:  (blank when OK; error text appears here, e.g.        |
|            "Error: x is at/near an asymptote (pi/2 + k*pi).    |
|             Try a value further from that point.")             |
|                                                                 |
+---------------------------------------------------------------+
```

## Controls

| Control | Type | Notes |
|---|---|---|
| `x` field | `ttk.Entry`, labelled "x in radians" / "x in degrees" (label text updates with unit) | Default keyboard focus on launch; meaningful label, not a placeholder-only hint (avoids "recall over recognition" pitfall) |
| Angle-unit selector | `ttk.Radiobutton` pair (radians / degrees) | Explicit, always-visible choice (persona need 1); radians is the default-selected option, matching D1/D2 assumption; changing it does not clear the entered value |
| Calculate button | `ttk.Button`, also bound to `<Return>`/`<KP_Enter>` on the whole window | Primary action; keyboard-reachable without a mouse |
| Clear button | `ttk.Button`, also bound to `<Escape>` | Resets entry, result, and status to a predictable empty state (does not change the unit selection) |
| Domain-hint label | Static `ttk.Label`, always visible above the buttons | States range + pole tolerance + expected unit before any error can occur (USE-01), so the user is warned proactively, not just reactively |
| Result label | `ttk.Label`, updated only on success | Shows `tan(<formatted x>) = <formatted result>` to the documented significant figures |
| Status/error label | `ttk.Label`, text + a leading "Error:" / "OK" word (never colour alone) | Errors are specific per exception type (`DomainError` -> near-pole message; `NumericalRangeError` -> range message; `ValueError`/parse -> invalid-input message; `ConvergenceError` -> convergence message), shown in place, next to the field that caused them |

## Interaction rules

1. **Keyboard navigation:** natural `Tab` order is field -> unit radio group -> Calculate -> Clear; all controls reachable and operable without a mouse (anticipates D3-P7.7 accessibility work).
2. **Default focus:** the `x` entry field receives focus when the window opens.
3. **Enter-to-calculate / Esc-to-clear:** bound at the window level so focus does not need to be on a specific button.
4. **Resizable layout:** widgets are placed with `grid` and column/row `weight` so the window can be resized without clipping text (D2-P5.4 "resizable layout").
5. **Errors never rely on colour alone:** status text always includes a word ("Error"/"OK") plus the specific explanation; colour (if used) is a secondary reinforcement, not the only signal (anticipates D3 accessibility).
6. **No unhandled traceback:** every exception raised by `src.tan_core.tan`/`src.validation` is caught in the GUI's Calculate handler and turned into a status message; the numerical core itself is never modified to know about Tkinter (keeps `tan_core.py` GUI-independent, D2-P5.5 "core still invocable independently").

**Done when:** a first-time user can infer the required action from labels alone (no external instructions needed), and the layout supports exactly the persona's workflow without extra/unused controls (e.g. no unnecessary menu bar, no unrelated calculator functions).
