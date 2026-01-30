#!/usr/bin/env python3
"""Match-case example: Rectangle Area (tuple pattern)

Demonstrates matching a tuple pattern to compute area of a rectangle.
Requires Python 3.10+ for `match`/`case`.
"""


def rectangle_area(shape: tuple[str, int | float, int | float]) -> None:
    match shape:
        case ("rectangle", w, h):
            print("Area:", w * h)
        case _:
            print("Unknown shape")


if __name__ == "__main__":
    shape = ("rectangle", 3, 4)  # (name, width, height)
    rectangle_area(shape)
