# -------------------------------------------------
# File Name: 23_design_hit_counter.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Hit Counter design using queue and timestamps.
# -------------------------------------------------

from collections import deque

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


class HitCounter:
    """Count hits in the past 5 minutes (300 seconds)."""

    def __init__(self) -> None:
        self._q = deque()

    def _evict_old(self, timestamp: int) -> None:
        while self._q and self._q[0] <= timestamp - 300:
            self._q.popleft()

    def hit(self, timestamp: int) -> None:
        self._q.append(timestamp)
        self._evict_old(timestamp)

    def get_hits(self, timestamp: int) -> int:
        self._evict_old(timestamp)
        return len(self._q)


def demo() -> None:
    title("DESIGN HIT COUNTER")
    hc = HitCounter()
    events = [1, 2, 3, 300, 301, 600]
    for t in events:
        hc.hit(t)
        print(f"  hit({t}) -> hits_now={hc.get_hits(t)}")
    print(f"  get_hits(602) -> {hc.get_hits(602)}")


if __name__ == "__main__":
    demo()
