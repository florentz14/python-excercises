# -------------------------------------------------
# File Name: 27_frequency_stack.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Frequency stack (pop most frequent, recency tie-break).
# -------------------------------------------------

"""
============================================================
  FREQUENCY STACK - Python 3.14
  Pop returns:
    1) highest frequency value
    2) if tie, most recently pushed among them

  Operations:
    - push(x)
    - pop()

  Typical complexity:
    - push: O(1)
    - pop : O(1)
============================================================
"""

from collections import defaultdict

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class FrequencyStack:
    """Stack-like structure by frequency and recency."""

    def __init__(self) -> None:
        self._freq = defaultdict(int)      # value -> frequency
        self._group = defaultdict(list)    # frequency -> values stack
        self._max_freq = 0

    def push(self, value: int) -> None:
        f = self._freq[value] + 1
        self._freq[value] = f
        self._group[f].append(value)
        if f > self._max_freq:
            self._max_freq = f

    def pop(self) -> int:
        if self._max_freq == 0:
            raise IndexError("Pop from empty FrequencyStack.")
        value = self._group[self._max_freq].pop()
        self._freq[value] -= 1
        if not self._group[self._max_freq]:
            self._max_freq -= 1
        return value

    def is_empty(self) -> bool:
        return self._max_freq == 0


def demo() -> None:
    title("FREQUENCY STACK - Frequency + recency behavior")
    fs = FrequencyStack()

    pushes = [5, 7, 5, 7, 4, 5]
    print(f"  Push sequence: {pushes}")
    for x in pushes:
        fs.push(x)
        print(f"  push({x})")

    print("\n  Pop sequence (expected: 5, 7, 5, 4, 7, 5):")
    while not fs.is_empty():
        print(f"  pop() -> {fs.pop()}")


if __name__ == "__main__":
    demo()
