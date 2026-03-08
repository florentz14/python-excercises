# -------------------------------------------------
# File Name: 19_abstract_classes.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Abstract base classes (ABC).
# -------------------------------------------------

from abc import ABC, abstractmethod
from typing import List
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape."""
        pass

    def description(self):
        """Concrete method - can be inherited."""
        return f"This is a {self.__class__.__name__}"


class Circle(Shape):
    """Circle implementation."""

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        """Calculate circle area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate circle circumference."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle implementation."""

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        """Calculate rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)


class Triangle(Shape):
    """Triangle implementation."""

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a, self.b, self.c = a, b, c

    def area(self):
        """Calculate triangle area using Heron's formula."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        """Calculate triangle perimeter."""
        return self.a + self.b + self.c


class Animal(ABC):
    """Abstract animal class."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        """Animal sound."""
        pass

    @abstractmethod
    def move(self):
        """How the animal moves."""
        pass

    def eat(self):
        """Concrete method - all animals eat."""
        return f"{self.name} is eating"


class Dog(Animal):
    """Dog implementation."""

    def make_sound(self):
        return "Woof!"

    def move(self):
        return f"{self.name} runs on four legs"


class Bird(Animal):
    """Bird implementation."""

    def make_sound(self):
        return "Chirp!"

    def move(self):
        return f"{self.name} flies in the sky"


class Fish(Animal):
    """Fish implementation."""

    def make_sound(self):
        return "Blub blub"

    def move(self):
        return f"{self.name} swims in water"


class Vehicle(ABC):
    """Abstract vehicle class."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self):
        """Start the vehicle."""
        pass

    @abstractmethod
    def stop_engine(self):
        """Stop the vehicle."""
        pass

    @property
    @abstractmethod
    def max_speed(self):
        """Maximum speed of the vehicle."""
        pass

    def get_info(self):
        """Concrete method."""
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    """Car implementation."""

    def start_engine(self):
        return "Vroom! Car engine started."

    def stop_engine(self):
        return "Car engine stopped."

    @property
    def max_speed(self):
        return 120  # km/h


class Motorcycle(Vehicle):
    """Motorcycle implementation."""

    def start_engine(self):
        return "Vroom vroom! Motorcycle engine started."

    def stop_engine(self):
        return "Motorcycle engine stopped."

    @property
    def max_speed(self):
        return 180  # km/h


class PaymentProcessor(ABC):
    """Abstract payment processor."""

    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process a payment."""
        pass

    @abstractmethod
    def refund_payment(self, amount: float) -> bool:
        """Process a refund."""
        pass

    def validate_amount(self, amount: float) -> bool:
        """Concrete validation method."""
        return amount > 0


class CreditCardProcessor(PaymentProcessor):
    """Credit card payment processor."""

    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount}")
        return True  # Simulate success

    def refund_payment(self, amount: float) -> bool:
        print(f"Processing credit card refund of ${amount}")
        return True  # Simulate success


class PayPalProcessor(PaymentProcessor):
    """PayPal payment processor."""

    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount}")
        return True  # Simulate success

    def refund_payment(self, amount: float) -> bool:
        print(f"Processing PayPal refund of ${amount}")
        return True  # Simulate success


class ShapeCalculator:
    """Calculator that works with any shape."""

    @staticmethod
    def calculate_total_area(shapes: List[Shape]) -> float:
        """Calculate total area of all shapes."""
        return sum(shape.area() for shape in shapes)

    @staticmethod
    def calculate_total_perimeter(shapes: List[Shape]) -> float:
        """Calculate total perimeter of all shapes."""
        return sum(shape.perimeter() for shape in shapes)


# Demonstration
if __name__ == "__main__":
    print("=== Abstract Classes Demo ===\n")

    # Shape examples
    print("Shape calculations:")
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5)
    ]

    for shape in shapes:
        print(f"{shape.description()}")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")

    total_area = ShapeCalculator.calculate_total_area(shapes)
    total_perimeter = ShapeCalculator.calculate_total_perimeter(shapes)
    print(f"\nTotal area: {total_area:.2f}")
    print(f"Total perimeter: {total_perimeter:.2f}")

    # Animal examples
    print("\nAnimal behaviors:")
    animals = [Dog("Buddy"), Bird("Tweety"), Fish("Nemo")]

    for animal in animals:
        print(f"{animal.name}:")
        print(f"  Sound: {animal.make_sound()}")
        print(f"  Movement: {animal.move()}")
        print(f"  Eating: {animal.eat()}")

    # Vehicle examples
    print("\nVehicle operations:")
    vehicles = [Car("Toyota", "Camry", 2020), Motorcycle("Honda", "CBR", 2021)]

    for vehicle in vehicles:
        print(f"{vehicle.get_info()}:")
        print(f"  Start: {vehicle.start_engine()}")
        print(f"  Max speed: {vehicle.max_speed} km/h")
        print(f"  Stop: {vehicle.stop_engine()}")

    # Payment processing
    print("\nPayment processing:")
    processors = [CreditCardProcessor(), PayPalProcessor()]

    for processor in processors:
        print(f"\n{processor.__class__.__name__}:")
        processor.process_payment(100.50)
        processor.refund_payment(25.00)
        print(f"Valid amount $50: {processor.validate_amount(50)}")
        print(f"Valid amount -$10: {processor.validate_amount(-10)}")

    print("\n=== Abstract Class Characteristics ===")
    print("- Cannot be instantiated directly")
    print("- Define interface with @abstractmethod")
    print("- Subclasses must implement all abstract methods")
    print("- Can have concrete methods and properties")
    print("- Support inheritance and polymorphism")

    print("\n=== When to Use Abstract Classes ===")
    print("- Define common interface for related classes")
    print("- Enforce implementation of certain methods")
    print("- Share common functionality")
    print("- Create frameworks or libraries")
    print("- Model real-world hierarchies")

    print("\n=== Abstract vs Regular Classes ===")
    print("Abstract: Template for subclasses, cannot instantiate")
    print("Regular: Can instantiate, full implementation")
    print("Abstract methods: Must be implemented by subclasses")
    print("Concrete methods: Inherited as-is")

    # Try to instantiate abstract class (will fail)
    print("\n=== Attempting to Instantiate Abstract Class ===")
    try:
        shape = Shape()  # This will raise TypeError
    except TypeError as e:
        print(f"Error: {e}")
