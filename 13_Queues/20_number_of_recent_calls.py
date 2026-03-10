# -------------------------------------------------
# File Name: 20_number_of_recent_calls.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Number of Recent Calls using queue window.
# -------------------------------------------------

from collections import deque

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class RecentCounter:
    """Count calls in the last 3000 milliseconds."""

    def __init__(self) -> None:
        self._q = deque()

    def ping(self, t: int) -> int:
        self._q.append(t)
        while self._q and self._q[0] < t - 3000:
            self._q.popleft()
        return len(self._q)


def demo() -> None:
    title("NUMBER OF RECENT CALLS")
    rc = RecentCounter()
    calls = [1, 100, 3001, 3002, 7000, 7001]
    for t in calls:
        print(f"  ping({t}) -> {rc.ping(t)}")


if __name__ == "__main__":
    demo()
