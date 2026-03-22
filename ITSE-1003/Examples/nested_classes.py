# -------------------------------------------------
# File Name: ITSE-1003/Examples/nested_classes.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Inner classes.
# -------------------------------------------------

class Computer:
    """Represents a computer with a brand and CPU."""
    
    class CPU:
        """Represents a CPU with a model."""
        
        def __init__(self, model: str) -> None:
            self.model = model

        def details(self) -> str:
            return f"CPU model: {self.model}"

    def __init__(self, brand: str, cpu_model: str) -> None:
        self.brand = brand
        self.cpu = Computer.CPU(cpu_model)

    def info(self) -> str:
        """Returns a string with the computer's brand and CPU details."""
        return f"Computer: {self.brand}, {self.cpu.details()}"


def main() -> None:
    """Main function to demonstrate the Computer and CPU classes."""
    pc = Computer("Lenovo", "i7")
    print(pc.info())


if __name__ == "__main__":
    main()
