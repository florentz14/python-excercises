# 18_simple_punto.py - Simple class: Point (2D coordinates)
# Florentino Baez - ITSE-1002

class Point:
    """Minimal class with __str__ for print."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

# Short list of points
points = [
    Point(3, 4),
    Point(0, 0),
    Point(-2, 5),
]

# Usage
for p in points:
    print(p)
