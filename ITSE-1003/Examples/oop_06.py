# -------------------------------------------------
# File Name: ITSE-1003/Examples/oop_06.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Polymorphism and duck typing.
# -------------------------------------------------

from typing import Protocol


class Dog:
    def speak(self) -> str:
        return "Woof!"


class Cat:
    def speak(self) -> str:
        return "Meow!"


class Robot:
    def speak(self) -> str:
        return "Beep!"


class Speakable(Protocol):
    def speak(self) -> str: ...


def make_it_speak(entity: Speakable) -> None:
    # Duck typing: if it has speak(), we call it.
    print(entity.speak())


def main() -> None:
    for item in [Dog(), Cat(), Robot()]:
        make_it_speak(item)


if __name__ == "__main__":
    main()
