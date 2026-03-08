# -------------------------------------------------
# File Name: 10_custom_hashable_objects.py
# Author: Florentino Báez
# Date: 19_Hash_Tables
# Description: Custom hashable objects with __hash__ and __eq__.
# -------------------------------------------------

class Point:
    """Immutable point. Hashable if __hash__ and __eq__ are consistent."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Person:
    """Hashable by id/name."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name

    def __repr__(self):
        return f"Person({self.name}, {self.age})"


if __name__ == "__main__":
    print("=" * 50)
    print("CUSTOM HASHABLE OBJECTS (__hash__, __eq__)")
    print("=" * 50)

    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)

    print(f"p1 == p2: {p1 == p2}")
    print(f"hash(p1) == hash(p2): {hash(p1) == hash(p2)}")
    print(f"hash(p3): {hash(p3)}")

    # Use as dict key / set element
    d = {p1: "first", p3: "third"}
    print(f"\ndict: {d}")
    print(f"d[p2] = {d[p2]}")  # p2 equals p1

    s = {p1, p2, p3}
    print(f"set: {s}")  # p1 and p2 collapse to one
