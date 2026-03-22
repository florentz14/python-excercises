# -------------------------------------------------
# File Name: ITSE-1003/Examples/car_composition.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Composition example (HAS-A).
# -------------------------------------------------


class Engine:
    def start(self) -> str:
        return "Engine started."


class Car:
    def __init__(self, model: str) -> None:
        self.model = model
        self.engine = Engine()  # Composition: Car has an Engine.

    def start(self) -> str:
        return f"{self.model}: {self.engine.start()}"


def main() -> None:
    car = Car("Sedan X")
    print(car.start())


if __name__ == "__main__":
    main()
