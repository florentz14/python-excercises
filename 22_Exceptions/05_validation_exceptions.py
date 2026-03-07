# ------------------------------------------------------------
# File: 05_validation_exceptions.py
# Chapter: Exceptions - Input Validation
#
# Purpose:
#   Validate user input using exceptions. Raise ValueError with
#   clear messages when input is invalid.
#
# Author: Florentino Baez (adapted)
# ------------------------------------------------------------


def parse_positive_int(value: str) -> int:
    """Convert string to positive integer. Raises ValueError if invalid."""
    num = int(value)
    if num <= 0:
        raise ValueError(f"Expected positive integer, got {num}")
    return num


def parse_percentage(value: str) -> float:
    """Convert string to percentage (0-100). Raises ValueError if invalid."""
    num = float(value)
    if not 0 <= num <= 100:
        raise ValueError(f"Percentage must be 0-100, got {num}")
    return num


def parse_email(value: str) -> str:
    """Basic email validation. Raises ValueError if invalid format."""
    value = value.strip()
    if "@" not in value or "." not in value.split("@")[-1]:
        raise ValueError(f"Invalid email format: {value!r}")
    return value


def safe_parse_positive_int(value: str) -> int | None:
    """Try to parse positive int. Returns None on error."""
    try:
        return parse_positive_int(value)
    except ValueError as e:
        print(f"Validation error: {e}")
        return None


def safe_parse_percentage(value: str) -> float | None:
    """Try to parse percentage. Returns None on error."""
    try:
        return parse_percentage(value)
    except ValueError as e:
        print(f"Validation error: {e}")
        return None


def safe_parse_email(value: str) -> str | None:
    """Try to parse email. Returns None on error."""
    try:
        return parse_email(value)
    except ValueError as e:
        print(f"Validation error: {e}")
        return None


# -----------------------------------------------------------------------------
# Main - Run examples
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 55)
    print("1. parse_positive_int")
    print("=" * 55)
    for val in ("42", "-1", "0", "abc"):
        result = safe_parse_positive_int(val)
        if result is not None:
            print(f"  '{val}' -> {result}")

    print("\n" + "=" * 55)
    print("2. parse_percentage")
    print("=" * 55)
    for val in ("75.5", "100", "150", "x"):
        result = safe_parse_percentage(val)
        if result is not None:
            print(f"  '{val}' -> {result}")

    print("\n" + "=" * 55)
    print("3. parse_email")
    print("=" * 55)
    for val in ("user@example.com", "invalid", "no-at-sign.com"):
        result = safe_parse_email(val)
        if result is not None:
            print(f"  '{val}' -> {result}")
