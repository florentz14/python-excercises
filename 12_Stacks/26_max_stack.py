# -------------------------------------------------
# File Name: 26_max_stack.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Max Stack with O(1) max retrieval.
# -------------------------------------------------

"""
============================================================
  MAX STACK - Python 3.14
  Stack with O(1) retrieval of current maximum.

  Supported operations:
    - push(x)
    - pop()
    - top()
    - get_max()

  Technique:
    - Keep a normal stack and a mirrored max stack.
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class MaxStack:
    """Stack that supports O(1) get_max()."""

    def __init__(self) -> None:
        self._stack: list[int] = []
        self._max_stack: list[int] = []

    def push(self, value: int) -> None:
        self._stack.append(value)
        if not self._max_stack:
            self._max_stack.append(value)
        else:
            self._max_stack.append(max(value, self._max_stack[-1]))

    def pop(self) -> int:
        if not self._stack:
            raise IndexError("Pop from empty stack.")
        self._max_stack.pop()
        return self._stack.pop()

    def top(self) -> int:
        if not self._stack:
            raise IndexError("Top from empty stack.")
        return self._stack[-1]

    def get_max(self) -> int:
        if not self._max_stack:
            raise IndexError("Max from empty stack.")
        return self._max_stack[-1]

    def is_empty(self) -> bool:
        return not self._stack

    def size(self) -> int:
        return len(self._stack)


def demo() -> None:
    title("MAX STACK - O(1) max retrieval")
    ms = MaxStack()

    for value in [2, 1, 5, 3, 7, 6]:
        ms.push(value)
        print(f"  push({value}) -> top={ms.top()}, max={ms.get_max()}")

    print("\n  Pop sequence:")
    while not ms.is_empty():
        popped = ms.pop()
        if not ms.is_empty():
            print(f"  pop() -> {popped}, new max={ms.get_max()}")
        else:
            print(f"  pop() -> {popped}, stack is now empty")


if __name__ == "__main__":
    demo()
