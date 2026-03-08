# -------------------------------------------------
# File Name: 78_match_rectangle.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Rectangle area (tuple pattern).
# -------------------------------------------------

def rectangle_area(shape: tuple[str, int | float, int | float]) -> None:
    match shape:
        case ("rectangle", w, h):
            print("Area:", w * h)
        case _:
            print("Unknown shape")


if __name__ == "__main__":
    shape = ("rectangle", 3, 4)  # (name, width, height)
    rectangle_area(shape)
