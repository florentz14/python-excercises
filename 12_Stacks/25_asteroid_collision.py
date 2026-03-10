# -------------------------------------------------
# File Name: 25_asteroid_collision.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Asteroid collision simulation using stack.
# -------------------------------------------------

"""
============================================================
  ASTEROID COLLISION - Python 3.14
  Given asteroids represented by integers:
    - positive value: moving right
    - negative value: moving left
    - absolute value: size

  When two asteroids collide:
    - smaller one explodes
    - equal sizes both explode
    - same direction never collide

  Return final asteroid state after all collisions.

  Technique:
    - Maintain stack of surviving asteroids.
    - Only possible collision: top moving right and new moving left.
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def asteroid_collision(asteroids: list[int]) -> list[int]:
    """Simulate collisions and return survivors."""
    stack: list[int] = []

    for ast in asteroids:
        alive = True

        # Collisions happen only in this direction pair: right vs left.
        while alive and stack and stack[-1] > 0 and ast < 0:
            if abs(stack[-1]) < abs(ast):
                stack.pop()
                continue
            if abs(stack[-1]) == abs(ast):
                stack.pop()
            alive = False

        if alive:
            stack.append(ast)

    return stack


def demo() -> None:
    title("ASTEROID COLLISION - Stack simulation")

    tests = [
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([-2, -1, 1, 2], [-2, -1, 1, 2]),
        ([1, -2, -2, -2], [-2, -2, -2]),
        ([2, -1, 1, -2], []),
    ]

    for asteroids, expected in tests:
        result = asteroid_collision(asteroids)
        print(f"\n  Input   : {asteroids}")
        print(f"  Result  : {result}")
        print(f"  Expected: {expected}")
        print(f"  Match   : {result == expected}")


if __name__ == "__main__":
    demo()
