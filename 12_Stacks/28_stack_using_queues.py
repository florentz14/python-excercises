# -------------------------------------------------
# File Name: 28_stack_using_queues.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Implement stack using queues.
# -------------------------------------------------

"""
============================================================
  STACK USING QUEUES - Python 3.14
  Implement LIFO stack behavior using queue primitives.

  This file implements:
    A) One-queue approach
       - push: O(n), pop/top: O(1)
    B) Two-queue approach
       - push: O(1), pop/top: O(n)
============================================================
"""

from collections import deque

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class StackUsingOneQueue:
    """Rotate queue on push so newest element stays at front."""

    def __init__(self) -> None:
        self._q = deque()

    def push(self, x: int) -> None:
        self._q.append(x)
        # Rotate previous elements behind the new one.
        for _ in range(len(self._q) - 1):
            self._q.append(self._q.popleft())

    def pop(self) -> int:
        if not self._q:
            raise IndexError("Pop from empty stack.")
        return self._q.popleft()

    def top(self) -> int:
        if not self._q:
            raise IndexError("Top from empty stack.")
        return self._q[0]

    def is_empty(self) -> bool:
        return not self._q


class StackUsingTwoQueues:
    """Keep push cheap, do transfer work during pop/top."""

    def __init__(self) -> None:
        self._q1 = deque()
        self._q2 = deque()

    def push(self, x: int) -> None:
        self._q1.append(x)

    def _move_until_last(self) -> None:
        while len(self._q1) > 1:
            self._q2.append(self._q1.popleft())

    def pop(self) -> int:
        if not self._q1:
            raise IndexError("Pop from empty stack.")
        self._move_until_last()
        value = self._q1.popleft()
        self._q1, self._q2 = self._q2, self._q1
        return value

    def top(self) -> int:
        if not self._q1:
            raise IndexError("Top from empty stack.")
        self._move_until_last()
        value = self._q1.popleft()
        self._q2.append(value)
        self._q1, self._q2 = self._q2, self._q1
        return value

    def is_empty(self) -> bool:
        return not self._q1


def demo_one_queue() -> None:
    title("A) STACK USING ONE QUEUE")
    st = StackUsingOneQueue()
    for x in [10, 20, 30]:
        st.push(x)
        print(f"  push({x})")
    print(f"  top() -> {st.top()}")
    print(f"  pop() -> {st.pop()}")
    print(f"  pop() -> {st.pop()}")
    print(f"  top() -> {st.top()}")


def demo_two_queues() -> None:
    title("B) STACK USING TWO QUEUES")
    st = StackUsingTwoQueues()
    for x in [100, 200, 300]:
        st.push(x)
        print(f"  push({x})")
    print(f"  top() -> {st.top()}")
    print(f"  pop() -> {st.pop()}")
    print(f"  pop() -> {st.pop()}")
    print(f"  top() -> {st.top()}")


if __name__ == "__main__":
    demo_one_queue()
    demo_two_queues()
