# -------------------------------------------------
# File Name: 54_dog.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Simple inheritance: Animal base and Dog child with speak override.
# -------------------------------------------------

class Animal:
    """Base class."""
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    """Child class that overrides speak."""
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

# Usage
dog = Dog("Max", "Labrador")
print(f"{dog.name} ({dog.breed}): {dog.speak()}")
