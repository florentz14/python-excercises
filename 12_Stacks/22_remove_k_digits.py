# -------------------------------------------------
# File Name: 22_remove_k_digits.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Remove K Digits problem using greedy stack.
# -------------------------------------------------

"""
============================================================
  REMOVE K DIGITS - Python 3.14
  Given a non-negative integer as a string and integer k,
  remove k digits so the resulting number is the smallest
  possible.

  Example:
    num = "1432219", k = 3  -> "1219"

  Technique:
    - Greedy + monotonic increasing stack.
    - While current digit is smaller than stack top, pop.
    - O(n) time, O(n) space.
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def remove_k_digits(num: str, k: int) -> str:
    """Return the smallest possible number after removing k digits."""
    if k >= len(num):
        return "0"

    stack: list[str] = []

    for digit in num:
        # Pop larger previous digits to keep number lexicographically small.
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # If removals remain, remove from the end (largest suffix impact).
    while k > 0 and stack:
        stack.pop()
        k -= 1

    # Strip leading zeros; fallback to zero.
    result = "".join(stack).lstrip("0")
    return result if result else "0"


def demo() -> None:
    title("REMOVE K DIGITS - Greedy stack demo")

    tests = [
        ("1432219", 3, "1219"),
        ("10200", 1, "200"),
        ("10", 2, "0"),
        ("100200", 1, "200"),
        ("123456", 3, "123"),
        ("765028321", 5, None),
    ]

    for num, k, expected in tests:
        result = remove_k_digits(num, k)
        print(f"\n  num={num!r}, k={k}")
        print(f"  result  : {result}")
        if expected is not None:
            print(f"  expected: {expected}")
            print(f"  match   : {result == expected}")


if __name__ == "__main__":
    demo()
