# -------------------------------------------------
# File Name: ITSE-1003/Examples/oop_10.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Inner classes.
# -------------------------------------------------


class Computer:
    class CPU:
        def __init__(self, model: str) -> None:
            self.model = model

        def details(self) -> str:
            return f"CPU model: {self.model}"

    def __init__(self, brand: str, cpu_model: str) -> None:
        self.brand = brand
        self.cpu = Computer.CPU(cpu_model)

    def info(self) -> str:
        return f"Computer: {self.brand}, {self.cpu.details()}"


def main() -> None:
    pc = Computer("Lenovo", "i7")
    print(pc.info())


if __name__ == "__main__":
    main()
