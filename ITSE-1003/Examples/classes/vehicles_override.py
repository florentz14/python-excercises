# -------------------------------------------------
# File Name: ITSE-1003/Examples/vehicles_override.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Method overriding.
# -------------------------------------------------


class Vehicle:
    def move(self) -> str:
        return "The vehicle moves."


class Car(Vehicle):
    def move(self) -> str:
        return "The car drives on the road."


class Boat(Vehicle):
    def move(self) -> str:
        return "The boat sails on water."


def main() -> None:
    vehicles = [Vehicle(), Car(), Boat()]
    for item in vehicles:
        print(item.move())


if __name__ == "__main__":
    main()
