# -------------------------------------------------
# File Name: 33_remove_duplicate_letters.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Remove duplicate letters using monotonic stack.
# -------------------------------------------------

"""
============================================================
  REMOVE DUPLICATE LETTERS - Python 3.14
  Return the lexicographically smallest string that contains
  each distinct letter exactly once.

  Example:
    "bcabc" -> "abc"
    "cbacdcbc" -> "acdb"

  Technique:
    - Monotonic stack of characters.
    - Last-occurrence index map.
    - In-stack set to avoid duplicates.
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def remove_duplicate_letters(s: str) -> str:
    """Return smallest lexicographic unique-letter string."""
    last_index = {ch: i for i, ch in enumerate(s)}
    stack: list[str] = []
    in_stack: set[str] = set()

    for i, ch in enumerate(s):
        if ch in in_stack:
            continue

        # Keep stack increasing if popped char appears later again.
        while stack and ch < stack[-1] and last_index[stack[-1]] > i:
            removed = stack.pop()
            in_stack.remove(removed)

        stack.append(ch)
        in_stack.add(ch)

    return "".join(stack)


def demo() -> None:
    title("REMOVE DUPLICATE LETTERS - Monotonic stack")

    tests = [
        ("bcabc", "abc"),
        ("cbacdcbc", "acdb"),
        ("abacb", "abc"),
        ("bbcaac", "bac"),
        ("aaaa", "a"),
    ]

    for text, expected in tests:
        result = remove_duplicate_letters(text)
        print(f"\n  Input   : {text!r}")
        print(f"  Result  : {result!r}")
        print(f"  Expected: {expected!r}")
        print(f"  Match   : {result == expected}")


if __name__ == "__main__":
    demo()
