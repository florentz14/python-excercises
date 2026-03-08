# -------------------------------------------------
# File Name: 01_basic_class.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Creating a basic class in Python.
# -------------------------------------------------

class Car:
    """A basic class representing a car."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Constructor - called when creating a new object."""
        self.make: str = make
        self.model: str = model
        self.year: int = year

    def start_engine(self) -> str:
        """Method to start the car's engine."""
        return f"The {self.make} {self.model}'s engine is now running!"

    def get_info(self) -> str:
        """Method to get car information."""
        return f"{self.year} {self.make} {self.model}"


# Creating objects (instances) of the class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

# Using the objects
print("Car 1 info:", car1.get_info())
print("Car 2 info:", car2.get_info())
print("Starting car 1:", car1.start_engine())

# Accessing attributes directly
print(f"Car 1 make: {car1.make}")
print(f"Car 2 year: {car2.year}")

# Checking object types
print(f"car1 is instance of Car: {isinstance(car1, Car)}")
print(f"Type of car1: {type(car1)}")
