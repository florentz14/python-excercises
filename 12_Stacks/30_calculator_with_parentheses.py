# -------------------------------------------------
# File Name: 30_calculator_with_parentheses.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Evaluate arithmetic expression with parentheses.
# -------------------------------------------------

"""
============================================================
  CALCULATOR WITH PARENTHESES - Python 3.14
  Evaluate expressions containing:
    - integers
    - +, -
    - parentheses ().

  Example:
    "1 + (2 - (3 + 4)) + 5" -> 1

  Technique:
    - One pass scan.
    - Use stack to save previous result/sign when entering '('.
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def calculate(expr: str) -> int:
    """Evaluate expression with +, -, and parentheses."""
    result = 0
    sign = 1
    number = 0
    stack: list[int] = []

    for ch in expr:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch in "+-":
            result += sign * number
            number = 0
            sign = 1 if ch == "+" else -1
        elif ch == "(":
            # Save current context and reset for inner expression.
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ")":
            result += sign * number
            number = 0
            prev_sign = stack.pop()
            prev_result = stack.pop()
            result = prev_result + prev_sign * result
        else:
            # Ignore spaces and unsupported separators.
            continue

    result += sign * number
    return result


def demo() -> None:
    title("CALCULATOR WITH PARENTHESES")

    tests = [
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("1 + (2 - (3 + 4)) + 5", 1),
        ("10 - (2 + 3) + (7 - (1 + 1))", 10),
    ]

    for expr, expected in tests:
        value = calculate(expr)
        print(f"\n  Expr    : {expr}")
        print(f"  Result  : {value}")
        print(f"  Expected: {expected}")
        print(f"  Match   : {value == expected}")


if __name__ == "__main__":
    demo()
