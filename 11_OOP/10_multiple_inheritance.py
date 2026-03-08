# -------------------------------------------------
# File Name: 10_multiple_inheritance.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Multiple inheritance in Python.
# -------------------------------------------------

class Animal:
    """Base class - Animal."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        print(f"Animal.__init__ called for {name}")

    def eat(self):
        return f"{self.name} is eating"

    def make_sound(self):
        return "Generic animal sound"


class Walker:
    """Mixin class - provides walking ability."""

    def __init__(self, legs: int = 4) -> None:
        self.legs: int = legs
        print(f"Walker.__init__ called with {legs} legs")

    def walk(self):
        return f"Walking on {self.legs} legs"


class Swimmer:
    """Mixin class - provides swimming ability."""

    def __init__(self, can_swim=True):
        self.can_swim = can_swim
        print(f"Swimmer.__init__ called, can_swim={can_swim}")

    def swim(self):
        if self.can_swim:
            return "Swimming gracefully"
        return "Cannot swim"


class Flyer:
    """Mixin class - provides flying ability."""

    def __init__(self, wingspan: float = 0.0):
        self.wingspan = wingspan
        print(f"Flyer.__init__ called with wingspan {wingspan}")

    def fly(self):
        if self.wingspan > 0:
            return f"Flying with {self.wingspan}m wingspan"
        return "Cannot fly"


class Dog(Animal, Walker):
    """Dog inherits from Animal and Walker."""

    def __init__(self, name: str, breed: str) -> None:
        # Multiple inheritance - need to call both parents
        Animal.__init__(self, name)
        Walker.__init__(self, 4)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} the {self.breed} is fetching"


class Duck(Animal, Walker, Swimmer, Flyer):
    """Duck inherits from multiple classes (diamond problem example)."""

    def __init__(self, name):
        # Call all parent constructors
        Animal.__init__(self, name)
        Walker.__init__(self, 2)
        Swimmer.__init__(self, True)
        Flyer.__init__(self, 0.8)

    def make_sound(self):
        return "Quack!"

    def migrate(self):
        return f"{self.name} is migrating south"


class Penguin(Animal, Walker, Swimmer):
    """Penguin - cannot fly but can walk and swim."""

    def __init__(self, name: str) -> None:
        Animal.__init__(self, name)
        Walker.__init__(self, 2)
        Swimmer.__init__(self, True)
        # Penguins can't fly, so no Flyer.__init__ call

    def make_sound(self):
        return "Honk!"

    def slide(self):
        return f"{self.name} is sliding on ice"


# Demonstration
if __name__ == "__main__":
    print("=== Multiple Inheritance Demo ===\n")

    print("Creating a Dog:")
    dog = Dog("Buddy", "Golden Retriever")
    print(f"  Sound: {dog.make_sound()}")
    print(f"  Walk: {dog.walk()}")
    print(f"  Fetch: {dog.fetch()}")

    print(f"\nDog MRO: {Dog.__mro__}")

    print("\nCreating a Duck (diamond problem):")
    duck = Duck("Donald")
    print(f"  Sound: {duck.make_sound()}")
    print(f"  Walk: {duck.walk()}")
    print(f"  Swim: {duck.swim()}")
    print(f"  Fly: {duck.fly()}")
    print(f"  Migrate: {duck.migrate()}")

    print(f"\nDuck MRO: {Duck.__mro__}")

    print("\nCreating a Penguin:")
    penguin = Penguin("Pingu")
    print(f"  Sound: {penguin.make_sound()}")
    print(f"  Walk: {penguin.walk()}")
    print(f"  Swim: {penguin.swim()}")
    print(f"  Slide: {penguin.slide()}")

    print(f"\nPenguin MRO: {Penguin.__mro__}")

    print("\n=== Multiple Inheritance Concepts ===")
    print("- Classes can inherit from multiple parents")
    print("- Method Resolution Order (MRO) determines method lookup")
    print("- Diamond problem: when two parents inherit from same grandparent")
    print("- Python uses C3 linearization for MRO")
    print("- Mixin classes provide specific functionality")

    print("\n=== Mixin Pattern ===")
    print("- Mixins are small classes that provide specific functionality")
    print("- They don't stand alone, meant to be combined with other classes")
    print("- Example: Walker, Swimmer, Flyer are mixins")

    # Check inheritance
    print(f"\nInheritance checks:")
    print(f"  isinstance(dog, Animal): {isinstance(dog, Animal)}")
    print(f"  isinstance(dog, Walker): {isinstance(dog, Walker)}")
    print(f"  isinstance(duck, Flyer): {isinstance(duck, Flyer)}")
