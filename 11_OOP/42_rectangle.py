# -------------------------------------------------
# File Name: 42_rectangle.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Simple Rectangle class with width, height and area() method.
# -------------------------------------------------

class Rectangle:
    """Class with attributes and one method."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Short list of rectangles (e.g., room dimensions)
rectangles = [
    Rectangle(5, 3),
    Rectangle(10, 4),
    Rectangle(7, 2),
]

# Usage
for r in rectangles:
    print(f"Rectangle {r.width}x{r.height}: area = {r.area()}")
