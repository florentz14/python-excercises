# -------------------------------------------------
# File Name: 21_dota2_senate_queue_simulation.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Dota2 Senate simulation using two queues.
# -------------------------------------------------

from collections import deque

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def predict_party_victory(senate: str) -> str:
    """Return winning party: 'Radiant' or 'Dire'."""
    n = len(senate)
    radiant = deque()
    dire = deque()

    for i, ch in enumerate(senate):
        if ch == "R":
            radiant.append(i)
        else:
            dire.append(i)

    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()
        if r < d:
            radiant.append(r + n)
        else:
            dire.append(d + n)

    return "Radiant" if radiant else "Dire"


def demo() -> None:
    title("DOTA2 SENATE - QUEUE SIMULATION")
    tests = ["RD", "RDD", "RRDDD", "DRRDRDR"]
    for s in tests:
        print(f"  {s} -> {predict_party_victory(s)}")


if __name__ == "__main__":
    demo()
