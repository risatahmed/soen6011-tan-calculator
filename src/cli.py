#!/usr/bin/env python3
"""Textual scientific-calculator interface for tan(x) -- Deliverable 2.

Run with:  python3 -m src.cli   (from the repository root)

D1's version computed sin/cos itself but still imported PI from the
`math` module. This D2 version imports the shared from-scratch core
(src/tan_core.py, src/constants.py) instead, so no prohibited direct
trig call (`math.tan`/`math.sin`/`math.cos`) and no `math.pi` remain
anywhere in the compute path. See docs/from_scratch_boundary.md.

I/O (this module) stays separate from computation (src/tan_core.py) so the
core can be imported and tested without a terminal.
"""

import sys

from src.exceptions import ConvergenceError, DomainError, NumericalRangeError
from src.tan_core import X_MAX
from src.tan_core import tan as tan_core
from src.validation import UNIT_DEGREES, UNIT_RADIANS, parse_x, to_radians

DISPLAY_SIG_FIGS = 10  # ACC-02 / DOC-01: displayed precision

BANNER = (
    "tan(x) calculator (Deliverable 2 -- from-scratch core, Tkinter GUI also available via 'python3 -m src.gui')\n"
    "  - Enter x as a real number.\n"
    "  - Default angle unit is RADIANS; prefix with 'd:' to enter degrees (e.g. 'd:45').\n"
    f"  - Supported range: |x| <= {X_MAX:g} radians (after unit conversion).\n"
    "  - Values at or within tolerance of a pole (x = pi/2 + k*pi) are rejected\n"
    "    with an explanation rather than returning a huge/meaningless number.\n"
    f"  - Results are displayed to {DISPLAY_SIG_FIGS} significant figures.\n"
    "  - Type 'quit' or 'exit' to leave.\n"
)


def format_result(value):
    return f"{value:.{DISPLAY_SIG_FIGS}g}"


def parse_x_and_unit(raw_text):
    """Split an optional 'd:' degrees prefix, then parse the numeric part.

    Returns (value_in_original_unit, unit). Raises ValueError on bad input.
    """
    text = raw_text.strip()
    if text.lower().startswith("d:"):
        return parse_x(text[2:]), UNIT_DEGREES
    return parse_x(text), UNIT_RADIANS


def run_cli(input_stream=sys.stdin, output_stream=sys.stdout):
    """Main interactive loop. Streams are parameterized for testability."""
    print(BANNER, file=output_stream)
    while True:
        print("Enter x (radians, or 'd:<value>' for degrees), or 'quit' to exit:", file=output_stream, end=" ")
        raw = input_stream.readline()
        if raw == "":  # EOF (e.g. piped input exhausted)
            print("\nEnd of input. Exiting.", file=output_stream)
            break

        stripped = raw.strip()
        if stripped.lower() in ("quit", "exit", "q"):
            print("Goodbye.", file=output_stream)
            break

        try:
            value, unit = parse_x_and_unit(raw)
            x = to_radians(value, unit)
        except ValueError as exc:
            print(f"Invalid input: {exc}", file=output_stream)
            continue

        try:
            result = tan_core(x)
        except NumericalRangeError as exc:
            print(f"Input out of range: {exc}", file=output_stream)
            continue
        except DomainError as exc:
            print(f"Cannot compute tan(x): {exc}", file=output_stream)
            continue
        except ConvergenceError as exc:
            print(f"Could not compute a converged result: {exc}", file=output_stream)
            continue

        print(f"tan({format_result(x)}) = {format_result(result)}", file=output_stream)


if __name__ == "__main__":
    run_cli()
