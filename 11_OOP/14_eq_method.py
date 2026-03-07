# -------------------------------------------------
# File: 14_eq_method.py
# Description: __eq__ magic method for equality comparison.
#              Making objects comparable with == operator.
# -------------------------------------------------

from typing import Any


class Point:
    """Point class with equality comparison."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        """Check equality based on coordinates."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        """Hash based on coordinates for use as dict key."""
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Person:
    """Person class with equality based on ID."""

    def __init__(self, name: str, age: int, person_id: str) -> None:
        self.name: str = name
        self.age: int = age
        self.person_id: str = person_id

    def __eq__(self, other: object) -> bool:
        """Two persons are equal if they have the same ID."""
        if not isinstance(other, Person):
            return False
        return self.person_id == other.person_id

    def __str__(self) -> str:
        return f"Person({self.name}, {self.age}, ID:{self.person_id})"


class BankAccount:
    """Bank account with equality based on account number."""

    def __init__(self, account_number: str, owner: str) -> None:
        self.account_number = account_number
        self.owner = owner
        self.balance = 0

    def __eq__(self, other: object) -> bool:
        """Accounts are equal if they have the same number."""
        if not isinstance(other, BankAccount):
            return False
        return self.account_number == other.account_number

    def __str__(self):
        return f"Account({self.account_number}, {self.owner})"


class Rectangle:
    """Rectangle with equality based on dimensions."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def __eq__(self, other):
        """Rectangles are equal if dimensions match (regardless of order)."""
        if not isinstance(other, Rectangle):
            return False
        return (self.width == other.width and self.height == other.height) or \
               (self.width == other.height and self.height == other.width)

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


# Demonstration
if __name__ == "__main__":
    print("=== __eq__ Magic Method Demo ===\n")

    # Point equality
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    p3 = Point(4, 3)

    print("Point equality:")
    print(f"{p1} == {p2}: {p1 == p2}")
    print(f"{p1} == {p3}: {p1 == p3}")
    print(f"{p1} == 'not a point': {p1 == 'not a point'}")

    # Person equality
    person1 = Person("John", 25, "12345")
    person2 = Person("Jane", 30, "12345")  # Same ID
    person3 = Person("John", 25, "67890")  # Different ID

    print("\nPerson equality (based on ID):")
    print(f"{person1} == {person2}: {person1 == person2}")
    print(f"{person1} == {person3}: {person1 == person3}")

    # Bank account equality
    acc1 = BankAccount("1001", "Alice")
    acc2 = BankAccount("1001", "Bob")  # Same account number
    acc3 = BankAccount("1002", "Alice")  # Different account

    print("\nBank account equality (based on account number):")
    print(f"{acc1} == {acc2}: {acc1 == acc2}")
    print(f"{acc1} == {acc3}: {acc1 == acc3}")

    # Rectangle equality
    rect1 = Rectangle(5, 3)
    rect2 = Rectangle(3, 5)  # Same dimensions, different order
    rect3 = Rectangle(5, 4)  # Different dimensions

    print("\nRectangle equality (dimensions match regardless of order):")
    print(f"{rect1} == {rect2}: {rect1 == rect2}")
    print(f"{rect1} == {rect3}: {rect1 == rect3}")

    print("\n=== Using == in Collections ===")

    points = [Point(1, 2), Point(3, 4), Point(5, 6)]
    target = Point(3, 4)

    print(f"Point {target} in list: {target in points}")

    # Dictionary with custom objects as keys
    point_dict = {Point(1, 2): "first", Point(3, 4): "second"}
    print(f"Dictionary lookup: {point_dict.get(Point(3, 4), 'not found')}")

    print("\n=== Default Equality Behavior ===")
    print("Without __eq__, objects are equal only if they are the same instance")
    print("With __eq__, you define what 'equality' means for your class")

    print("\n=== Best Practices ===")
    print("- Check isinstance() in __eq__ for type safety")
    print("- Make __eq__ symmetric: if a == b, then b == a")
    print("- Consider implementing __hash__ if using objects as dict keys/sets")
    print("- __eq__ should be based on immutable or essential attributes")
