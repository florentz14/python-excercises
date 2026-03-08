# -------------------------------------------------
# File Name: 11_polymorphism.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Polymorphism in Python.
# -------------------------------------------------

from typing import Any, List


class Shape:
    """Abstract shape class."""

    def area(self) -> float:
        """Calculate area - to be overridden."""
        return 0.0

    def perimeter(self) -> float:
        """Calculate perimeter - to be overridden."""
        return 0.0

    def describe(self) -> str:
        """Describe the shape."""
        return f"This is a {self.__class__.__name__}"


class Rectangle(Shape):
    """Rectangle implementation."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle implementation."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius


class Triangle(Shape):
    """Triangle implementation."""

    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.sides = [side1, side2, side3]

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return sum(self.sides)


def print_shape_info(shape: Shape) -> None:
    """Function that works with any shape (polymorphism)."""
    print(f"{shape.describe()}")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")


class Animal:
    """Animal base class."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self):
        """To be overridden by subclasses."""
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Duck(Animal):
    def speak(self):
        return "Quack!"


def animal_chorus(animals):
    """Function demonstrating polymorphism with animals."""
    print("Animal chorus:")
    for animal in animals:
        print(f"  {animal.name}: {animal.speak()}")


# Demonstration
if __name__ == "__main__":
    print("=== Polymorphism Demo ===\n")

    # Shape polymorphism
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(6, 4, 3, 4, 5)
    ]

    print("Shape calculations (same interface, different behavior):")
    for shape in shapes:
        print_shape_info(shape)
        print()

    # Animal polymorphism
    animals = [
        Dog("Buddy"),
        Cat("Whiskers"),
        Duck("Donald")
    ]

    animal_chorus(animals)

    print("\n=== Polymorphism Benefits ===")
    print("- Same interface for different types")
    print("- Code reusability and flexibility")
    print("- Easier to extend with new types")
    print("- Functions work with any object that implements the interface")

    print("\n=== Duck Typing Example ===")
    print("Python uses duck typing - if it walks like a duck...")

    # Objects with same method work interchangeably
    class Robot:
        def speak(self):
            return "Beep boop!"

    # Add robot to animals list
    animals.append(Robot())
    animal_chorus(animals)

    print("\n=== Key Concepts ===")
    print("- Polymorphism: many forms, same interface")
    print("- Method overriding enables polymorphism")
    print("- Functions can work with different types uniformly")
    print("- Duck typing: behavior matters more than inheritance")
