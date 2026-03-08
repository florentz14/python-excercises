# -------------------------------------------------
# File Name: 52_triangle.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Triangle class with base, height and area() method.
# -------------------------------------------------

class Triangle:
    """Class with attributes and area method."""
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Short list of triangles
triangles = [
    Triangle(4, 3),
    Triangle(10, 5),
    Triangle(6, 8),
]

# Usage
for t in triangles:
    print(f"Triangle base={t.base} height={t.height}: area = {t.area()}")
