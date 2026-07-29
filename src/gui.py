#!/usr/bin/env python3
"""Tkinter GUI for tan(x) -- Deliverable 2, Problem 5 (GUI).

Run with:  python3 -m src.gui   (from the repository root)

Wireframe: docs/gui_wireframe.md. All numeric work is delegated to
src/tan_core.py + src/validation.py; this module only wires widgets to
those pure functions and turns exceptions into status messages -- the
core stays importable/testable without launching a window (D2-P5.5).
"""

import tkinter as tk
from tkinter import ttk

from src.exceptions import ConvergenceError, DomainError, NumericalRangeError
from src.tan_core import POLE_EPSILON, X_MAX
from src.tan_core import tan as tan_core
from src.validation import UNIT_DEGREES, UNIT_RADIANS, parse_x, to_radians

DISPLAY_SIG_FIGS = 10

DOMAIN_HINT = (
    f"Domain hint: |x| <= {X_MAX:g}; rejected within {POLE_EPSILON:g} of a pole "
    "(x = pi/2 + k*pi). Enter x in the selected unit."
)


def format_number(value):
    return f"{value:.{DISPLAY_SIG_FIGS}g}"


class TanCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("tan(x) Calculator -- Deliverable 2")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.unit_var = tk.StringVar(value=UNIT_RADIANS)
        self.x_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Result: (none yet)")
        self.status_var = tk.StringVar(value="OK: enter a value and press Calculate.")
        self.label_var = tk.StringVar(value="x (radians):")

        self._build_widgets()
        self._bind_keys()
        self.x_entry.focus_set()

    def _build_widgets(self):
        frame = ttk.Frame(self.root, padding=12)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, textvariable=self.label_var).grid(row=0, column=0, sticky="w")
        self.x_entry = ttk.Entry(frame, width=28)
        self.x_entry.grid(row=0, column=1, sticky="ew", padx=(6, 12))

        unit_frame = ttk.Frame(frame)
        unit_frame.grid(row=0, column=2, sticky="w")
        ttk.Label(unit_frame, text="Unit:").grid(row=0, column=0, padx=(0, 4))
        ttk.Radiobutton(
            unit_frame, text="radians", value=UNIT_RADIANS, variable=self.unit_var,
            command=self._update_unit_label,
        ).grid(row=0, column=1)
        ttk.Radiobutton(
            unit_frame, text="degrees", value=UNIT_DEGREES, variable=self.unit_var,
            command=self._update_unit_label,
        ).grid(row=0, column=2)

        hint_label = ttk.Label(frame, text=DOMAIN_HINT, wraplength=460, foreground="#444444")
        hint_label.grid(row=1, column=0, columnspan=3, sticky="w", pady=(8, 8))

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=2, column=0, columnspan=3, sticky="w")
        self.calc_button = ttk.Button(button_frame, text="Calculate (Enter)", command=self.on_calculate)
        self.calc_button.grid(row=0, column=0, padx=(0, 8))
        self.clear_button = ttk.Button(button_frame, text="Clear (Esc)", command=self.on_clear)
        self.clear_button.grid(row=0, column=1)

        result_label = ttk.Label(frame, textvariable=self.result_var, font=("TkDefaultFont", 11, "bold"))
        result_label.grid(row=3, column=0, columnspan=3, sticky="w", pady=(12, 4))

        status_label = ttk.Label(frame, textvariable=self.status_var, wraplength=460)
        status_label.grid(row=4, column=0, columnspan=3, sticky="w")
        self.status_label = status_label

    def _bind_keys(self):
        self.root.bind("<Return>", lambda event: self.on_calculate())
        self.root.bind("<KP_Enter>", lambda event: self.on_calculate())
        self.root.bind("<Escape>", lambda event: self.on_clear())

    def _update_unit_label(self):
        unit = self.unit_var.get()
        self.label_var.set("x (radians):" if unit == UNIT_RADIANS else "x (degrees):")

    def _set_status(self, ok, message):
        prefix = "OK" if ok else "Error"
        self.status_var.set(f"{prefix}: {message}")
        self.status_label.configure(foreground="#1a7a1a" if ok else "#a11")

    def on_calculate(self):
        raw = self.x_entry.get()
        try:
            value = parse_x(raw)
        except ValueError as exc:
            self._set_status(False, str(exc))
            return

        unit = self.unit_var.get()
        x = to_radians(value, unit)

        try:
            result = tan_core(x)
        except NumericalRangeError as exc:
            self._set_status(False, f"input out of range -- {exc}")
            return
        except DomainError as exc:
            self._set_status(False, f"x is at/near an asymptote (pi/2 + k*pi) -- {exc}")
            return
        except ConvergenceError as exc:
            self._set_status(False, f"could not compute a converged result -- {exc}")
            return

        self.result_var.set(f"Result: tan({format_number(x)}) = {format_number(result)}")
        self._set_status(True, "calculation succeeded.")

    def on_clear(self):
        self.x_entry.delete(0, tk.END)
        self.result_var.set("Result: (none yet)")
        self._set_status(True, "cleared. enter a value and press Calculate.")
        self.x_entry.focus_set()


def main():
    root = tk.Tk()
    TanCalculatorApp(root)
    root.lift()
    root.attributes("-topmost", True)
    root.after_idle(root.attributes, "-topmost", False)
    root.focus_force()
    root.mainloop()


if __name__ == "__main__":
    main()
