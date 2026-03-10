# -------------------------------------------------
# File Name: 21_daily_temperatures.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Daily Temperatures problem using monotonic stack.
# -------------------------------------------------

"""
============================================================
  DAILY TEMPERATURES - Python 3.14
  For each day, compute how many days you must wait until
  a warmer temperature appears. If no warmer day exists, 0.

  Example:
    temps  = [73, 74, 75, 71, 69, 72, 76, 73]
    output = [ 1,  1,  4,  2,  1,  1,  0,  0]

  Technique:
    - Monotonic decreasing stack of indexes.
    - O(n) time, O(n) space.
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def daily_temperatures(temps: list[int]) -> list[int]:
    """Return wait days for a warmer temperature."""
    result = [0] * len(temps)
    stack: list[int] = []  # indexes with unresolved warmer day

    for i, current in enumerate(temps):
        # Resolve all previous days cooler than current day.
        while stack and temps[stack[-1]] < current:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)

    return result


def daily_temperatures_bruteforce(temps: list[int]) -> list[int]:
    """Reference O(n^2) approach for validation."""
    out = [0] * len(temps)
    for i in range(len(temps)):
        for j in range(i + 1, len(temps)):
            if temps[j] > temps[i]:
                out[i] = j - i
                break
    return out


def demo() -> None:
    title("DAILY TEMPERATURES - Monotonic stack demo")

    tests = [
        [73, 74, 75, 71, 69, 72, 76, 73],
        [30, 40, 50, 60],
        [30, 60, 90],
        [90, 80, 70, 60],
        [70, 70, 70, 71],
    ]

    for temps in tests:
        fast = daily_temperatures(temps)
        slow = daily_temperatures_bruteforce(temps)
        print(f"\n  Temperatures: {temps}")
        print(f"  Fast O(n):   {fast}")
        print(f"  Check O(n^2):{slow}")
        print(f"  Match: {fast == slow}")


if __name__ == "__main__":
    demo()
