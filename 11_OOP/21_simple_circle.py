# ------------------------------------------------------------
# File: 21_simple_circle.py
# OOP: Class Circle with private attributes and encapsulation
#
# Purpose:
#   Demonstrates:
#   - Private attributes (name mangling: __attr -> _ClassName__attr)
#   - Getter and setter methods
#   - Validation in setter (type and positive value)
#   - Area and perimeter calculations
#
# Note:
#   __radius is name-mangled to _Circle__radius. In general: _ClassName__attr.
#   This is not true privacy; it avoids accidental overrides in subclasses.
#
# Author: Florentino Baez (adapted)
# ------------------------------------------------------------

import math


class Circle:
    """
    Circle with encapsulated radius. Uses name mangling for "private" attrs.
    """

    def __init__(self, radius: float) -> None:
        """Initialize circle with given radius."""
        self.__radius = radius
        # Use math.pi for accuracy instead of a constant
        self.__pi = math.pi

    def calculate_perimeter(self) -> float:
        """Return perimeter: 2 * pi * radius."""
        return 2 * self.__pi * self.__radius

    def calculate_area(self) -> float:
        """Return area: pi * radius^2."""
        return self.__pi * self.__radius**2

    def get_pi(self) -> float:
        """Getter for the pi constant."""
        return self.__pi

    def set_radius(self, new_value: float) -> None:
        """
        Setter for radius. Validates type (int or float) and positive value.
        """
        if isinstance(new_value, (int, float)):
            if new_value > 0:
                self.__radius = float(new_value)
                print(f"Radius updated successfully: {self.__radius}")
            else:
                print("Error: radius must be positive")
        else:
            print("Error: radius must be a positive number")


# ------------------------------------------------------------
# Main - demonstration
# ------------------------------------------------------------

if __name__ == "__main__":
    c1 = Circle(2.5)

    print(c1.calculate_area())
    print(c1.calculate_perimeter())
    print(f"PI constant: {c1.get_pi()}")

    # Valid update
    c1.set_radius(34)

    # Invalid: negative
    c1.set_radius(-23)

    # Invalid: wrong type
    c1.set_radius("helloworld")
