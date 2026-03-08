# -------------------------------------------------
# File Name: 22_rectangle.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Rectangle class - practical application.
# -------------------------------------------------

from typing import Optional, Tuple


class Rectangle:
    """Rectangle class with comprehensive functionality."""

    # Class variable to track all instances
    _all_rectangles = []

    def __init__(self, width: float, height: float, color: str = "blue"):
        """Initialize rectangle with validation."""
        self._width = 0
        self._height = 0
        self._color = "blue"

        # Use setters for validation
        self.width = width
        self.height = height
        self.color = color

        # Track this instance
        Rectangle._all_rectangles.append(self)

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
            raise ValueError(f"Color must be one of: {', '.join(valid_colors)}")
        self._color = value.lower()

    @property
    def area(self) -> float:
        """Calculate area."""
        return self._width * self._height

    @property
    def perimeter(self) -> float:
        """Calculate perimeter."""
        return 2 * (self._width + self._height)

    @property
    def diagonal(self) -> float:
        """Calculate diagonal length."""
        return (self._width ** 2 + self._height ** 2) ** 0.5

    @property
    def is_square(self) -> bool:
        """Check if rectangle is a square."""
        return abs(self._width - self._height) < 1e-10  # Account for floating point precision

    def scale(self, factor: float) -> 'Rectangle':
        """Return a new rectangle scaled by factor."""
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        return Rectangle(self._width * factor, self._height * factor, self._color)

    def scale_in_place(self, factor: float):
        """Scale this rectangle in place."""
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self._width *= factor
        self._height *= factor

    def rotate(self) -> 'Rectangle':
        """Return a new rectangle rotated 90 degrees."""
        return Rectangle(self._height, self._width, self._color)

    def rotate_in_place(self):
        """Rotate this rectangle 90 degrees in place."""
        self._width, self._height = self._height, self._width

    def can_fit_inside(self, other: 'Rectangle') -> bool:
        """Check if this rectangle can fit inside another."""
        return (self._width <= other._width and self._height <= other._height) or \
               (self._width <= other._height and self._height <= other._width)

    def get_larger_dimension(self) -> str:
        """Get which dimension is larger."""
        if self._width > self._height:
            return "width"
        elif self._height > self._width:
            return "height"
        else:
            return "equal"

    def to_tuple(self) -> Tuple[float, float, str]:
        """Return rectangle as (width, height, color) tuple."""
        return (self._width, self._height, self._color)

    def __str__(self) -> str:
        """String representation."""
        return f"{self._color.capitalize()} rectangle {self._width:.1f}x{self._height:.1f}"

    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"Rectangle(width={self._width}, height={self._height}, color='{self._color}')"

    def __eq__(self, other) -> bool:
        """Check equality based on dimensions and color."""
        if not isinstance(other, Rectangle):
            return False
        return (abs(self._width - other._width) < 1e-10 and
                abs(self._height - other._height) < 1e-10 and
                self._color == other._color)

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        """Add two rectangles (combine areas)."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_width = (self._width + other._width) / 2  # Average width
        new_height = (self._height + other._height) / 2  # Average height
        return Rectangle(new_width, new_height, self._color)

    def __mul__(self, factor: float) -> 'Rectangle':
        """Multiply rectangle by scalar."""
        return self.scale(factor)

    def __rmul__(self, factor: float) -> 'Rectangle':
        """Right multiplication."""
        return self.__mul__(factor)

    def __lt__(self, other: 'Rectangle') -> bool:
        """Compare by area."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area < other.area

    def __le__(self, other: 'Rectangle') -> bool:
        """Compare by area."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area <= other.area

    @classmethod
    def create_square(cls, side: float, color: str = "blue") -> 'Rectangle':
        """Create a square rectangle."""
        return cls(side, side, color)

    @classmethod
    def from_tuple(cls, dimensions: Tuple[float, float], color: str = "blue") -> 'Rectangle':
        """Create rectangle from (width, height) tuple."""
        width, height = dimensions
        return cls(width, height, color)

    @classmethod
    def get_all_rectangles(cls) -> list:
        """Get all rectangle instances."""
        return cls._all_rectangles.copy()

    @classmethod
    def get_total_area(cls) -> float:
        """Get total area of all rectangles."""
        return sum(rect.area for rect in cls._all_rectangles)

    @classmethod
    def find_largest(cls) -> Optional['Rectangle']:
        """Find the rectangle with largest area."""
        if not cls._all_rectangles:
            return None
        return max(cls._all_rectangles, key=lambda r: r.area)

    @staticmethod
    def calculate_aspect_ratio(width: float, height: float) -> float:
        """Calculate aspect ratio (width/height)."""
        if height == 0:
            raise ValueError("Height cannot be zero")
        return width / height

    @staticmethod
    def is_valid_dimensions(width: float, height: float) -> bool:
        """Check if dimensions are valid."""
        return width > 0 and height > 0


# Demonstration
if __name__ == "__main__":
    print("=== Rectangle Class Demo ===\n")

    # Create rectangles
    rect1 = Rectangle(5, 3, "red")
    rect2 = Rectangle(4, 4, "blue")  # Square
    rect3 = Rectangle(2, 6, "green")

    print("Rectangle Information:")
    for i, rect in enumerate([rect1, rect2, rect3], 1):
        print(f"Rectangle {i}: {rect}")
        print(f"  Area: {rect.area}")
        print(f"  Perimeter: {rect.perimeter}")
        print(f"  Diagonal: {rect.diagonal:.2f}")
        print(f"  Is square: {rect.is_square}")
        print(f"  Larger dimension: {rect.get_larger_dimension()}")
        print()

    # Scaling
    print("Scaling operations:")
    scaled = rect1.scale(2)
    print(f"Original: {rect1}")
    print(f"Scaled by 2: {scaled}")

    rect1.scale_in_place(1.5)
    print(f"Scaled in place: {rect1}")

    # Rotation
    print(f"\nRotation: {rect1} -> {rect1.rotate()}")

    # Class methods
    print(f"\nClass methods:")
    square = Rectangle.create_square(5, "yellow")
    print(f"Created square: {square}")

    tuple_rect = Rectangle.from_tuple((7, 2), "purple")
    print(f"From tuple: {tuple_rect}")

    # Static methods
    print(f"\nStatic methods:")
    print(f"Aspect ratio 16:9 = {Rectangle.calculate_aspect_ratio(16, 9):.2f}")
    print(f"Valid dimensions 5x3: {Rectangle.is_valid_dimensions(5, 3)}")
    print(f"Valid dimensions -1x3: {Rectangle.is_valid_dimensions(-1, 3)}")

    # Comparisons and operations
    print(f"\nComparisons:")
    print(f"{rect1} < {rect2}: {rect1 < rect2}")
    print(f"{rect1} == {rect1.scale(1)}: {rect1 == rect1.scale(1)}")

    combined = rect1 + rect2
    print(f"Combined {rect1} + {rect2} = {combined}")

    multiplied = rect3 * 3
    print(f"{rect3} * 3 = {multiplied}")

    # Class-level tracking
    print(f"\nClass tracking:")
    print(f"Total rectangles created: {len(Rectangle.get_all_rectangles())}")
    print(f"Total area of all rectangles: {Rectangle.get_total_area():.1f}")
    largest = Rectangle.find_largest()
    if largest:
        print(f"Largest rectangle: {largest} (area: {largest.area})")

    # Fitting
    print(f"\nFitting check:")
    print(f"Can {rect3} fit inside {rect1}? {rect3.can_fit_inside(rect1)}")
    print(f"Can {rect1} fit inside {rect3}? {rect1.can_fit_inside(rect3)}")

    print("\n=== OOP Concepts Demonstrated ===")
    print("- Encapsulation: Private attributes with validation")
    print("- Properties: Computed attributes (area, perimeter, diagonal)")
    print("- Class methods: Factory methods and class-level operations")
    print("- Static methods: Utility functions")
    print("- Magic methods: __str__, __repr__, __eq__, __add__, __mul__, __lt__")
    print("- Class variables: Tracking all instances")
    print("- Validation: Input validation in setters")

    print("\n=== Error Handling Demo ===")
    try:
        invalid_rect = Rectangle(-5, 3)
    except ValueError as e:
        print(f"Dimension validation: {e}")

    try:
        rect1.color = "rainbow"
    except ValueError as e:
        print(f"Color validation: {e}")

    try:
        rect1.scale(-1)
    except ValueError as e:
        print(f"Scale validation: {e}")