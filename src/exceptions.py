"""Custom exceptions for the from-scratch tan(x) numerical core (D2, Problem 5)."""


class NumericalRangeError(Exception):
    """Raised when |x| exceeds the supported argument range (VAL-03)."""


class DomainError(Exception):
    """Raised when x is at or within tolerance of a pole x = pi/2 + k*pi (VAL-04)."""


class ConvergenceError(Exception):
    """Raised when a series fails to reach its tolerance within max_terms (REL-01)."""
