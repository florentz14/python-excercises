# -------------------------------------------------
# File Name: 08_inheritance_basic.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Basic inheritance in Python.
# -------------------------------------------------

class Animal:
    """Parent class - Animal."""

    def __init__(self, name: str, species: str) -> None:
        self.name: str = name
        self.species: str = species

    def make_sound(self) -> str:
        """Generic sound method."""
        return "Some generic animal sound"

    def eat(self) -> str:
        """Eating behavior."""
        return f"{self.name} is eating"

    def sleep(self) -> str:
        """Sleeping behavior."""
        return f"{self.name} is sleeping"

    def get_info(self) -> str:
        """Get animal information."""
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    """Child class - Dog inherits from Animal."""

    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        """Override parent method."""
        return "Woof! Woof!"

    def fetch(self) -> str:
        """Dog-specific method."""
        return f"{self.name} is fetching the ball"

    def get_info(self) -> str:
        """Override to include breed."""
        return f"{self.name} is a {self.breed} {self.species}"


class Cat(Animal):
    """Child class - Cat inherits from Animal."""

    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        """Override parent method."""
        return "Meow!"

    def climb(self) -> str:
        """Cat-specific method."""
        return f"{self.name} is climbing the tree"

    def get_info(self) -> str:
        """Override to include color."""
        return f"{self.name} is a {self.color} {self.species}"


class Bird(Animal):
    """Child class - Bird inherits from Animal."""

    def __init__(self, name, can_fly=True):
        super().__init__(name, "Bird")
        self.can_fly = can_fly

    def make_sound(self):
        """Override parent method."""
        return "Tweet! Tweet!"

    def fly(self) -> str:
        """Bird-specific method."""
        if self.can_fly:
            return f"{self.name} is flying"
        else:
            return f"{self.name} cannot fly"


# Demonstration
if __name__ == "__main__":
    print("=== Basic Inheritance Demo ===\n")

    # Create different animals
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Black")
    bird = Bird("Tweety", True)
    ostrich = Bird("Ozzy", False)  # Cannot fly

    animals = [dog, cat, bird, ostrich]

    print("Animal information:")
    for animal in animals:
        print(f"  {animal.get_info()}")

    print("\nAnimal sounds:")
    for animal in animals:
        print(f"  {animal.name}: {animal.make_sound()}")

    print("\nCommon behaviors (inherited):")
    for animal in animals:
        print(f"  {animal.eat()}")
        print(f"  {animal.sleep()}")

    print("\nSpecific behaviors:")
    print(f"  {dog.fetch()}")
    print(f"  {cat.climb()}")
    print(f"  {bird.fly()}")
    print(f"  {ostrich.fly()}")

    print("\n=== Inheritance Concepts ===")
    print("- Child classes inherit all methods and attributes from parent")
    print("- Child classes can override parent methods")
    print("- Child classes can add new methods and attributes")
    print("- Use super() to call parent methods")
    print("- isinstance() works with inheritance hierarchy")

    # isinstance checks
    print(f"\nType checking:")
    print(f"  isinstance(dog, Dog): {isinstance(dog, Dog)}")
    print(f"  isinstance(dog, Animal): {isinstance(dog, Animal)}")
    print(f"  isinstance(dog, Cat): {isinstance(dog, Cat)}")
