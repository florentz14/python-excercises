# -------------------------------------------------
# File Name: 22_first_unique_character_stream.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: First unique character in a stream.
# -------------------------------------------------

from collections import Counter, deque

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class FirstUniqueStream:
    """Track first non-repeating character in a stream."""

    def __init__(self) -> None:
        self._freq = Counter()
        self._q = deque()

    def add(self, ch: str) -> None:
        self._freq[ch] += 1
        self._q.append(ch)
        while self._q and self._freq[self._q[0]] > 1:
            self._q.popleft()

    def first_unique(self) -> str:
        return self._q[0] if self._q else "#"


def demo() -> None:
    title("FIRST UNIQUE CHARACTER IN STREAM")
    stream = "aabcbdbe"
    tracker = FirstUniqueStream()
    print(f"  Stream: {stream}")
    for ch in stream:
        tracker.add(ch)
        print(f"  add('{ch}') -> first_unique='{tracker.first_unique()}'")


if __name__ == "__main__":
    demo()
