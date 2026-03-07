# -------------------------------------------------
# File: 12_duck_typing.py
# Description: Duck typing in Python.
#              "If it walks like a duck and quacks like a duck..."
# -------------------------------------------------

from typing import Any


class Dog:
    """Dog class."""

    def __init__(self, name: str) -> None:
        self.name: str = name

    def speak(self) -> str:
        return "Woof!"

    def move(self) -> str:
        return f"{self.name} runs on four legs"


class Duck:
    """Duck class."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self):
        return "Quack!"

    def move(self):
        return f"{self.name} waddles"


class Robot:
    """Robot class - no inheritance, but same interface."""

    def __init__(self, name: str) -> None:
        self.name: str = name

    def speak(self) -> str:
        return "Beep boop!"

    def move(self) -> str:
        return f"{self.name} rolls on wheels"


def animal_sounds(animals: list[Any]) -> None:
    """Function that works with any object that has speak() method."""
    print("Animal sounds:")
    for animal in animals:
        print(f"  {animal.name}: {animal.speak()}")


def make_them_move(things: list[Any]) -> None:
    """Function that works with any object that has move() method."""
    print("Movement:")
    for thing in things:
        print(f"  {thing.move()}")


class FileLikeObject:
    """Custom object that behaves like a file."""

    def __init__(self, content: str) -> None:
        self.content: str = content
        self.position: int = 0

    def read(self, size: int = -1) -> str:
        """Read method like file objects."""
        if size == -1:
            result = self.content[self.position:]
            self.position = len(self.content)
        else:
            result = self.content[self.position:self.position + size]
            self.position += len(result)
        return result

    def seek(self, position: int) -> None:
        """Seek method like file objects."""
        self.position = position

    def tell(self) -> int:
        """Tell method like file objects."""
        return self.position


def process_file_like(obj: Any) -> None:
    """Function that works with any file-like object."""
    print(f"Processing {obj.__class__.__name__}:")
    print(f"  Content: {obj.read()}")
    obj.seek(0)  # Reset to beginning
    print(f"  First 5 chars: {obj.read(5)}")
    print(f"  Position: {obj.tell()}")


class Calculator:
    """Calculator with add method."""

    def add(self, a, b):
        return a + b


class Vector:
    """Vector with add method."""

    def __init__(self, x, y):
        self.x, self.y = x, y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


def perform_addition(objects, a, b):
    """Function that works with any object that has add method."""
    print("Addition results:")
    for obj in objects:
        result = obj.add(a, b)
        print(f"  {obj.__class__.__name__}.add({a}, {b}) = {result}")


# Demonstration
if __name__ == "__main__":
    print("=== Duck Typing Demo ===\n")

    # Animals example
    animals = [Dog("Buddy"), Duck("Donald"), Robot("R2D2")]

    animal_sounds(animals)
    print()
    make_them_move(animals)

    print("\n=== File-like Objects ===")

    # File-like objects
    file_like = FileLikeObject("Hello, World!")
    real_file = open(__file__, 'r')  # This script file

    # Both work with the same function
    process_file_like(file_like)
    print()
    real_file_content = real_file.read(50) + "..."
    print(f"Real file content: {real_file_content}")
    real_file.close()

    print("\n=== Objects with add Method ===")

    # Objects with add method
    adders = [Calculator(), Vector(1, 2)]
    perform_addition(adders, 3, 4)

    print("\n=== Duck Typing Principles ===")
    print("- No need for inheritance or interfaces")
    print("- Behavior matters, not the class hierarchy")
    print("- 'If it walks like a duck and quacks like a duck...'")
    print("- Flexible and dynamic typing")

    print("\n=== Benefits ===")
    print("- Loose coupling between components")
    print("- Easy to add new types without changing existing code")
    print("- Promotes composition over inheritance")
    print("- Pythonic way of programming")

    print("\n=== When to Use ===")
    print("- When you need flexibility")
    print("- When inheritance would be too rigid")
    print("- When working with different libraries/frameworks")
    print("- For protocols (like file objects, iterators, etc.)")