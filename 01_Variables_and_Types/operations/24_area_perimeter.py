# -------------------------------------------------
# File Name: 24_area_perimeter.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Area and perimeter for rectangle, circle, and triangle.
# -------------------------------------------------

import math


def rectangle_area(length, width):
    return length * width


def rectangle_perimeter(length, width):
    return 2 * (length + width)


# Circle


def circle_area(radius):
    return math.pi * radius ** 2


def circle_circumference(radius):
    return 2 * math.pi * radius

# Triangle


def triangle_area(base, height):
    return 0.5 * base * height


def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3


# Example usage
if __name__ == "__main__":
    print("Rectangle area (5x3):", rectangle_area(5, 3))
    print("Rectangle perimeter (5x3):", rectangle_perimeter(5, 3))
    print("Circle area (r=4):", circle_area(4))
    print("Circle circumference (r=4):", circle_circumference(4))
    print("Triangle area (b=6, h=4):", triangle_area(6, 4))
    print("Triangle perimeter (3,4,5):", triangle_perimeter(3, 4, 5))
