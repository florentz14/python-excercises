# -------------------------------------------------
# File: 24_shape.py
# Description: Shape hierarchy - practical application.
#              Inheritance, polymorphism, abstract classes.
# -------------------------------------------------

from abc import ABC, abstractmethod
from typing import List
import math


class Shape(ABC):
    """Abstract base class for all shapes."""

    def __init__(self, color: str = "blue"):
        self.color = color

    @property
    def color(self) -> str:
        """Get color."""
        return self._color

    @color.setter
    def color(self, value: str):
        """Set color with validation."""
        valid_colors = ["red", "blue", "green", "yellow", "black", "white",
                        "purple", "orange", "pink", "brown"]
        if value.lower() not in valid_colors:
            raise ValueError(
                f"Color must be one of: {', '.join(valid_colors)}")
        self._color = value.lower()

    @abstractmethod
    def area(self) -> float:
        """Calculate area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter of the shape."""
        pass

    @abstractmethod
    def describe(self) -> str:
        """Describe the shape."""
        pass

    def __str__(self) -> str:
        """String representation."""
        return f"{self._color} {self.__class__.__name__.lower()}"

    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"{self.__class__.__name__}(color='{self._color}')"


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius: float, color: str = "blue"):
        super().__init__(color)
        self.radius = radius

    @property
    def radius(self) -> float:
        """Get radius."""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """Set radius with validation."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius = float(value)

    def area(self) -> float:
        """Calculate circle area."""
        return math.pi * self._radius ** 2

    def perimeter(self) -> float:
        """Calculate circle circumference."""
        return 2 * math.pi * self._radius

    def diameter(self) -> float:
        """Calculate diameter."""
        return 2 * self._radius

    def describe(self) -> str:
        """Describe the circle."""
        return f"A {self._color} circle with radius {self._radius:.1f}"


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width: float, height: float, color: str = "blue"):
        super().__init__(color)
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        """Get width."""
        return self._width

    @width.setter
    def width(self, value: float):
        """Set width with validation."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Width must be a positive number")
        self._width = float(value)

    @property
    def height(self) -> float:
        """Get height."""
        return self._height

    @height.setter
    def height(self, value: float):
        """Set height with validation."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Height must be a positive number")
        self._height = float(value)

    def area(self) -> float:
        """Calculate rectangle area."""
        return self._width * self._height

    def perimeter(self) -> float:
        """Calculate rectangle perimeter."""
        return 2 * (self._width + self._height)

    def diagonal(self) -> float:
        """Calculate diagonal length."""
        return math.sqrt(self._width ** 2 + self._height ** 2)

    @property
    def is_square(self) -> bool:
        """Check if rectangle is a square."""
        return abs(self._width - self._height) < 1e-10

    def describe(self) -> str:
        """Describe the rectangle."""
        shape_type = "square" if self.is_square else "rectangle"
        return f"A {self._color} {shape_type} {self._width:.1f}x{self._height:.1f}"


class Triangle(Shape):
    """Triangle shape."""

    def __init__(self, a: float, b: float, c: float, color: str = "blue"):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self) -> float:
        """Get side a."""
        return self._a

    @a.setter
    def a(self, value: float):
        """Set side a with validation."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Side a must be a positive number")
        self._a = float(value)
        self._validate_triangle()

    @property
    def b(self) -> float:
        """Get side b."""
        return self._b

    @b.setter
    def b(self, value: float):
        """Set side b with validation."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Side b must be a positive number")
        self._b = float(value)
        self._validate_triangle()

    @property
    def c(self) -> float:
        """Get side c."""
        return self._c

    @c.setter
    def c(self, value: float):
        """Set side c with validation."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Side c must be a positive number")
        self._c = float(value)
        self._validate_triangle()

    def _validate_triangle(self):
        """Validate triangle inequality."""
        if hasattr(self, '_a') and hasattr(self, '_b') and hasattr(self, '_c'):
            a, b, c = self._a, self._b, self._c
            if not (a + b > c and a + c > b and b + c > a):
                raise ValueError(
                    "Invalid triangle sides - triangle inequality violated")

    def area(self) -> float:
        """Calculate triangle area using Heron's formula."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    def perimeter(self) -> float:
        """Calculate triangle perimeter."""
        return self._a + self._b + self._c

    def is_equilateral(self) -> bool:
        """Check if triangle is equilateral."""
        return abs(self._a - self._b) < 1e-10 and abs(self._b - self._c) < 1e-10

    def is_isosceles(self) -> bool:
        """Check if triangle is isosceles."""
        sides = [self._a, self._b, self._c]
        return len(set(round(s, 10) for s in sides)) <= 2

    def is_scalene(self) -> bool:
        """Check if triangle is scalene."""
        return not self.is_isosceles()

    def describe(self) -> str:
        """Describe the triangle."""
        if self.is_equilateral():
            type_desc = "equilateral"
        elif self.is_isosceles():
            type_desc = "isosceles"
        else:
            type_desc = "scalene"
        return f"A {self._color} {type_desc} triangle with sides {self._a:.1f}, {self._b:.1f}, {self._c:.1f}"


class ShapeCollection:
    """Collection of shapes with operations."""

    def __init__(self):
        self.shapes: List[Shape] = []

    def add_shape(self, shape: Shape):
        """Add a shape to the collection."""
        self.shapes.append(shape)

    def remove_shape(self, shape: Shape):
        """Remove a shape from the collection."""
        self.shapes.remove(shape)

    def get_total_area(self) -> float:
        """Calculate total area of all shapes."""
        return sum(shape.area() for shape in self.shapes)

    def get_total_perimeter(self) -> float:
        """Calculate total perimeter of all shapes."""
        return sum(shape.perimeter() for shape in self.shapes)

    def get_shapes_by_color(self, color: str) -> List[Shape]:
        """Get all shapes of a specific color."""
        return [shape for shape in self.shapes if shape.color == color.lower()]

    def get_largest_shape(self) -> Shape:
        """Get the shape with the largest area."""
        if not self.shapes:
            raise ValueError("No shapes in collection")
        return max(self.shapes, key=lambda s: s.area())

    def sort_by_area(self, reverse: bool = False):
        """Sort shapes by area."""
        self.shapes.sort(key=lambda s: s.area(), reverse=reverse)

    def describe_all(self) -> str:
        """Describe all shapes in the collection."""
        if not self.shapes:
            return "No shapes in collection"

        descriptions = []
        for i, shape in enumerate(self.shapes, 1):
            descriptions.append(f"{i}. {shape.describe()}")
            descriptions.append(
                f"   Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")

        return "\n".join(descriptions)


# Demonstration
if __name__ == "__main__":
    print("=== Shape Hierarchy Demo ===\n")

    # Create shapes
    circle = Circle(5, "red")
    rectangle = Rectangle(4, 6, "blue")
    square = Rectangle(5, 5, "green")  # Square
    triangle = Triangle(3, 4, 5, "yellow")

    shapes = [circle, rectangle, square, triangle]

    print("Individual shapes:")
    for shape in shapes:
        print(f"  {shape}")
        print(f"    {shape.describe()}")
        print(f"    Area: {shape.area():.2f}")
        print(f"    Perimeter: {shape.perimeter():.2f}")

        # Shape-specific properties
        if isinstance(shape, Circle):
            print(f"    Diameter: {shape.diameter():.2f}")
        elif isinstance(shape, Rectangle):
            print(f"    Diagonal: {shape.diagonal():.2f}")
            print(f"    Is square: {shape.is_square}")
        elif isinstance(shape, Triangle):
            print(f"    Is equilateral: {shape.is_equilateral()}")
            print(f"    Is isosceles: {shape.is_isosceles()}")
            print(f"    Is scalene: {shape.is_scalene()}")

        print()

    # Shape collection
    print("Shape collection:")
    collection = ShapeCollection()
    for shape in shapes:
        collection.add_shape(shape)

    print(f"Total shapes: {len(collection.shapes)}")
    print(f"Total area: {collection.get_total_area():.2f}")
    print(f"Total perimeter: {collection.get_total_perimeter():.2f}")

    print(
        f"\nShapes by color 'red': {[str(s) for s in collection.get_shapes_by_color('red')]}")
    print(f"Largest shape: {collection.get_largest_shape()}")

    print(f"\nBefore sorting by area:")
    for shape in collection.shapes:
        print(f"  {shape}: area = {shape.area():.2f}")

    collection.sort_by_area(reverse=True)
    print(f"\nAfter sorting by area (descending):")
    for shape in collection.shapes:
        print(f"  {shape}: area = {shape.area():.2f}")

    print(f"\nDetailed descriptions:")
    print(collection.describe_all())

    print("\n=== OOP Concepts Demonstrated ===")
    print("- Abstract base class: Shape defines interface")
    print("- Inheritance: Circle, Rectangle, Triangle extend Shape")
    print("- Polymorphism: All shapes implement area(), perimeter(), describe()")
    print("- Encapsulation: Private attributes with validation")
    print("- Composition: ShapeCollection contains Shape objects")
    print("- Method overriding: Each shape implements abstract methods")
    print("- isinstance() checks: Type-specific behavior")

    print("\n=== Polymorphism in Action ===")
    print("All shapes can be treated uniformly:")
    for shape in shapes:
        print(f"  {shape.__class__.__name__}: {shape.area():.2f} area units")

    print("\n=== Error Handling Demo ===")
    try:
        invalid_circle = Circle(-5)
    except ValueError as e:
        print(f"Circle validation: {e}")

    try:
        invalid_triangle = Triangle(1, 1, 10)
    except ValueError as e:
        print(f"Triangle validation: {e}")

    # try:
    #     shape = Shape()  # Cannot instantiate abstract class
    # except TypeError as e:
    #     print(f"Abstract class error: {e}")

    try:
        collection.get_largest_shape()  # Empty collection
    except ValueError as e:
        print(f"Empty collection error: {e}")
