# -------------------------------------------------
# File Name: 24_time_needed_to_buy_tickets.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Queue simulation for ticket buying time.
# -------------------------------------------------

from collections import deque

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def time_required_to_buy(tickets: list[int], k: int) -> int:
    """Return total time for person k to finish buying tickets."""
    q = deque((i, t) for i, t in enumerate(tickets))
    elapsed = 0

    while q:
        idx, remaining = q.popleft()
        remaining -= 1
        elapsed += 1
        if remaining > 0:
            q.append((idx, remaining))
        elif idx == k:
            return elapsed

    return elapsed


def demo() -> None:
    title("TIME NEEDED TO BUY TICKETS")
    tests = [
        ([2, 3, 2], 2),
        ([5, 1, 1, 1], 0),
        ([1, 1, 1], 1),
    ]
    for tickets, k in tests:
        result = time_required_to_buy(tickets, k)
        print(f"  tickets={tickets}, k={k} -> time={result}")


if __name__ == "__main__":
    demo()
