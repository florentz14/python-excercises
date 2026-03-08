# -------------------------------------------------
# File Name: 04_str_repr.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: __str__ vs __repr__ magic methods.
# -------------------------------------------------

class Point:
    """Point class with __str__ and __repr__."""

    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"Point at ({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Unambiguous string representation (for developers)."""
        return f"Point({self.x}, {self.y})"


class Book:
    """Book class demonstrating __str__ and __repr__."""

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = year

    def __str__(self) -> str:
        """User-friendly string."""
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"


class ComplexNumber:
    """Complex number with string representations."""

    def __init__(self, real: float, imag: float) -> None:
        self.real: float = real
        self.imag: float = imag

    def __str__(self) -> str:
        """Display as mathematical notation."""
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __repr__(self) -> str:
        """Show constructor call."""
        return f"ComplexNumber({self.real}, {self.imag})"


# Demonstration
if __name__ == "__main__":
    print("=== __str__ vs __repr__ Demo ===\n")

    # Point examples
    p1 = Point(3, 4)
    p2 = Point(0, 0)

    print("Point objects:")
    print(f"str(p1): {str(p1)}")
    print(f"repr(p1): {repr(p1)}")
    print(f"p1: {p1}")        # Calls __str__
    print(f"print(p1):", p1)  # Calls __str__

    points = [p1, p2]
    print(f"List of points: {points}")  # Uses repr for list elements

    print("\n=== Book Example ===")
    book = Book("1984", "George Orwell", 1949)
    print(f"str(book): {str(book)}")
    print(f"repr(book): {repr(book)}")

    print("\n=== Complex Number Example ===")
    c1 = ComplexNumber(3, 4)
    c2 = ComplexNumber(1, -2)

    print(f"c1: {c1}")
    print(f"repr(c1): {repr(c1)}")
    print(f"c2: {c2}")
    print(f"repr(c2): {repr(c2)}")

    print("\n=== When each is called ===")
    print("print(obj) calls __str__")
    print("str(obj) calls __str__")
    print("repr(obj) calls __repr__")
    print("In containers like lists, repr() is used")
    print("Interactive prompt shows repr()")

    # Demonstrating the difference
    print(f"\nDirect call: str(book) = {str(book)}")
    print(f"Direct call: repr(book) = {repr(book)}")
