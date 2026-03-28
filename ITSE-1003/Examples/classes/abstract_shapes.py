# -------------------------------------------------
# File Name: ITSE-1003/Examples/abstract_shapes.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Abstraction with ABC.
# -------------------------------------------------

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


def main() -> None:
    rect = Rectangle(5, 3)
    print("Rectangle area:", rect.area())


if __name__ == "__main__":
    main()
