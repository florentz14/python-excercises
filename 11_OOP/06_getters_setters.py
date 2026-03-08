# -------------------------------------------------
# File Name: 06_getters_setters.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Traditional getters and setters.
# -------------------------------------------------

class Temperature:
    """Temperature class with manual getters and setters."""

    def __init__(self, celsius: float = 0) -> None:
        self._celsius: float = celsius

    def get_celsius(self) -> float:
        """Getter for celsius."""
        return self._celsius

    def set_celsius(self, value: float) -> None:
        """Setter for celsius with validation."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value

    def get_fahrenheit(self):
        """Getter for fahrenheit."""
        return (self._celsius * 9/5) + 32

    def set_fahrenheit(self, value: float) -> None:
        """Setter for fahrenheit."""
        celsius = (value - 32) * 5/9
        self.set_celsius(celsius)  # Reuse celsius setter for validation

    def get_kelvin(self):
        """Getter for kelvin."""
        return self._celsius + 273.15

    def set_kelvin(self, value: float) -> None:
        """Setter for kelvin."""
        self.set_celsius(value - 273.15)  # Reuse celsius setter


class Circle:
    """Circle class with radius validation."""

    def __init__(self, radius: float = 1) -> None:
        self.set_radius(radius)

    def get_radius(self) -> float:
        """Getter for radius."""
        return self._radius

    def set_radius(self, value: float) -> None:
        """Setter for radius with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def get_area(self):
        """Calculate area."""
        import math
        return math.pi * self._radius ** 2

    def get_circumference(self) -> float:
        """Calculate circumference."""
        import math
        return 2 * math.pi * self._radius


class Person:
    """Person class with name and age validation."""

    def __init__(self, name: str, age: int) -> None:
        self.set_name(name)
        self.set_age(age)

    def get_name(self) -> str:
        """Getter for name."""
        return self._name

    def set_name(self, value):
        """Setter for name with validation."""
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()

    def get_age(self) -> int:
        """Getter for age."""
        return self._age

    def set_age(self, value):
        """Setter for age with validation."""
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError("Age must be an integer between 0 and 150")
        self._age = value

    def get_info(self) -> str:
        """Get person information."""
        return f"{self._name}, age {self._age}"


# Demonstration
if __name__ == "__main__":
    print("=== Getters and Setters Demo ===\n")

    # Temperature example
    temp = Temperature(20)
    print("Temperature examples:")
    print(f"Celsius: {temp.get_celsius()}°C")
    print(f"Fahrenheit: {temp.get_fahrenheit()}°F")
    print(f"Kelvin: {temp.get_kelvin()}K")

    temp.set_fahrenheit(68)
    print(f"After setting to 68°F: {temp.get_celsius()}°C")

    try:
        temp.set_celsius(-300)
    except ValueError as e:
        print(f"Error: {e}")

    print("\n=== Circle Example ===")
    circle = Circle(5)
    print(f"Radius: {circle.get_radius()}")
    print(f"Area: {circle.get_area():.2f}")
    print(f"Circumference: {circle.get_circumference():.2f}")

    circle.set_radius(10)
    print(f"After setting radius to 10: Area = {circle.get_area():.2f}")

    print("\n=== Person Example ===")
    person = Person("Alice", 25)
    print("Person info:", person.get_info())

    person.set_name("Alice Johnson")
    person.set_age(26)
    print("Updated info:", person.get_info())

    try:
        person.set_age(-5)
    except ValueError as e:
        print(f"Age validation error: {e}")

    try:
        person.set_name("")
    except ValueError as e:
        print(f"Name validation error: {e}")

    print("\n=== Benefits of Getters/Setters ===")
    print("- Encapsulation: hide internal representation")
    print("- Validation: ensure data integrity")
    print("- Flexibility: change implementation without breaking interface")
    print("- Debugging: add logging or breakpoints")
