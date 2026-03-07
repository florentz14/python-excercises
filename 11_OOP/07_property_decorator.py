# -------------------------------------------------
# File: 07_property_decorator.py
# Description: @property decorator for Pythonic getters/setters.
#              Computed properties and property validation.
# -------------------------------------------------


class Rectangle:
    """Rectangle class using @property decorator."""

    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter for width."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self) -> float:
        """Getter for height."""
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """Setter for height with validation."""
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        """Computed property - area of rectangle."""
        return self._width * self._height

    @property
    def perimeter(self):
        """Computed property - perimeter of rectangle."""
        return 2 * (self._width + self._height)


class Temperature:
    """Temperature class with property for different scales."""

    def __init__(self, celsius: float = 0) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Get temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Get temperature in Fahrenheit (computed property)."""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Set temperature in Fahrenheit."""
        self.celsius = (value - 32) * 5/9  # Convert and use celsius setter

    @property
    def kelvin(self):
        """Get temperature in Kelvin (computed property)."""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        """Set temperature in Kelvin."""
        self.celsius = value - 273.15


class Person:
    """Person class with property validation."""

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self) -> str:
        """Computed property for full name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        """Getter for age."""
        return self._age

    @age.setter
    def age(self, value):
        """Setter for age with validation."""
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError("Age must be an integer between 0 and 150")
        self._age = value

    @property
    def is_adult(self) -> bool:
        """Computed property - check if person is adult."""
        return self._age >= 18


# Demonstration
if __name__ == "__main__":
    print("=== @property Decorator Demo ===\n")

    # Rectangle example
    rect = Rectangle(5, 3)
    print("Rectangle properties:")
    print(f"Width: {rect.width}")
    print(f"Height: {rect.height}")
    print(f"Area: {rect.area}")        # Computed property
    print(f"Perimeter: {rect.perimeter}")  # Computed property

    rect.width = 10
    print(f"After setting width to 10: Area = {rect.area}")

    print("\n=== Temperature Example ===")
    temp = Temperature(20)
    print(f"Celsius: {temp.celsius}°C")
    print(f"Fahrenheit: {temp.fahrenheit}°F")  # Computed
    print(f"Kelvin: {temp.kelvin}K")          # Computed

    temp.fahrenheit = 68
    print(f"After setting to 68°F: {temp.celsius}°C")

    print("\n=== Person Example ===")
    person = Person("John", "Doe", 25)
    print(f"Full name: {person.full_name}")  # Computed
    print(f"Age: {person.age}")
    print(f"Is adult: {person.is_adult}")    # Computed

    person.age = 17
    print(f"After setting age to 17: Is adult = {person.is_adult}")

    print("\n=== Property vs Regular Methods ===")
    print("Properties are accessed like attributes:")
    print("  obj.property (not obj.property())")
    print("But can have setters for validation")
    print("Computed properties update automatically")

    print("\n=== Benefits ===")
    print("- Clean syntax: obj.property instead of obj.get_property()")
    print("- Backward compatibility when adding validation")
    print("- Computed properties for derived values")
    print("- Encapsulation with Pythonic interface")
