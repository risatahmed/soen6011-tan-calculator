"""Input parsing and angle-unit conversion (Deliverable 2).

Kept separate from tan_core.py so the numerical core stays pure and the I/O
layers (cli.py, gui.py) share one validation implementation.
"""

from src.constants import PI

UNIT_RADIANS = "rad"
UNIT_DEGREES = "deg"


def parse_x(raw_text):
    """Parse user input into a float, or raise ValueError with a helpful message."""
    text = raw_text.strip()
    if text == "":
        raise ValueError("No input received. Please enter a numeric value for x.")
    try:
        return float(text)
    except ValueError:
        raise ValueError(
            f"'{raw_text.strip()}' is not a valid real number. "
            "Please enter something like 0.7853981634 or -1.2."
        )


def to_radians(x, unit):
    """Convert x to radians given unit in {UNIT_RADIANS, UNIT_DEGREES}.

    Uses the from-scratch PI (constants.py); no math.radians/math.pi call.
    """
    if unit == UNIT_DEGREES:
        return x * PI / 180.0
    if unit == UNIT_RADIANS:
        return x
    raise ValueError(f"Unknown angle unit {unit!r}; expected {UNIT_RADIANS!r} or {UNIT_DEGREES!r}.")
