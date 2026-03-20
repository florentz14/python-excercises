# -------------------------------------------------
# File Name: ITSE-1003/Examples/oop_04.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Inheritance and super().
# -------------------------------------------------


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "Some generic sound"


class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)
        self.breed = breed

    def speak(self) -> str:
        return "Woof!"


def main() -> None:
    dog = Dog("Buddy", "Labrador")
    print(dog.name, "-", dog.breed)
    print(dog.speak())


if __name__ == "__main__":
    main()
