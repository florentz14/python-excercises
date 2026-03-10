# -------------------------------------------------
# File Name: 32_basic_calculator_ii.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Basic Calculator II using stack.
# -------------------------------------------------

"""
============================================================
  BASIC CALCULATOR II - Python 3.14
  Evaluate arithmetic strings containing:
    - non-negative integers
    - +, -, *, /
    - spaces
  without parentheses.

  Example:
    "3+2*2" -> 7
    " 3/2 " -> 1

  Technique:
    - Stack stores signed terms.
    - Apply * and / immediately to stack top.
    - Sum stack at the end.
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def calculate(expression: str) -> int:
    """Evaluate expression in O(n) time."""
    stack: list[int] = []
    num = 0
    op = "+"

    for i, ch in enumerate(expression + "+"):
        if ch.isdigit():
            num = num * 10 + int(ch)
            continue

        if ch == " ":
            continue

        # Apply previous operator.
        if op == "+":
            stack.append(num)
        elif op == "-":
            stack.append(-num)
        elif op == "*":
            stack[-1] = stack[-1] * num
        elif op == "/":
            # Truncate toward zero.
            stack[-1] = int(stack[-1] / num)

        op = ch
        num = 0

    return sum(stack)


def demo() -> None:
    title("BASIC CALCULATOR II - Stack evaluation")

    tests = [
        ("3+2*2", 7),
        (" 3/2 ", 1),
        (" 3+5 / 2 ", 5),
        ("14-3/2", 13),
        ("100+20*3-10/2", 155),
    ]

    for expr, expected in tests:
        value = calculate(expr)
        print(f"\n  Expr    : {expr}")
        print(f"  Result  : {value}")
        print(f"  Expected: {expected}")
        print(f"  Match   : {value == expected}")


if __name__ == "__main__":
    demo()
