import math


class Calculator:
    """Arithmetic operations: basic + modulus, power, sqrt, floor division, percentage, absolute value."""

    # ── Binary operations (require a and b) ──────────────────────────────────

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def modulus(self, a: float, b: float) -> float:
        """Remainder of a ÷ b."""
        if b == 0:
            raise ValueError("Modulus by zero is not allowed.")
        return a % b

    def power(self, a: float, b: float) -> float:
        """a raised to the power b."""
        return a ** b

    def floor_divide(self, a: float, b: float) -> float:
        """Integer (floor) division of a ÷ b."""
        if b == 0:
            raise ValueError("Floor division by zero is not allowed.")
        return a // b

    def percentage(self, a: float, b: float) -> float:
        """a percent of b  →  (a / 100) × b."""
        return (a / 100) * b

    # ── Unary operations (require only a) ────────────────────────────────────

    def sqrt(self, a: float) -> float:
        """Square root of a."""
        if a < 0:
            raise ValueError("Square root of a negative number is not defined.")
        return math.sqrt(a)

    def absolute(self, a: float) -> float:
        """Absolute value of a."""
        return abs(a)
