# 27_simple_dog.py - Simple inheritance: Animal -> Dog
# Florentino Baez - ITSE-1002

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
