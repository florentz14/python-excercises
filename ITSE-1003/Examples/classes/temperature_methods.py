# -------------------------------------------------
# File Name: ITSE-1003/Examples/temperature_methods.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Instance, class, and static methods (Celsius, Fahrenheit, Kelvin).
# -------------------------------------------------


class Temperature:
    """Internal value is always stored in degrees Celsius."""

    unit = "C"

    def __init__(self, value_celsius: float) -> None:
        self.value = value_celsius

    def to_celsius(self) -> float:
        return self.value

    def to_fahrenheit(self) -> float:
        return (self.value * 9 / 5) + 32

    def to_kelvin(self) -> float:
        return self.value + 273.15

    @classmethod
    def from_celsius(cls, value_c: float) -> "Temperature":
        return cls(value_c)

    @classmethod
    def from_fahrenheit(cls, value_f: float) -> "Temperature":
        return cls((value_f - 32) * 5 / 9)

    @classmethod
    def from_kelvin(cls, value_k: float) -> "Temperature":
        return cls(value_k - 273.15)

    @staticmethod
    def is_valid_celsius(value_c: float) -> bool:
        return value_c >= -273.15

    @staticmethod
    def is_valid_fahrenheit(value_f: float) -> bool:
        return Temperature.is_valid_celsius((value_f - 32) * 5 / 9)

    @staticmethod
    def is_valid_kelvin(value_k: float) -> bool:
        return value_k >= 0


def main() -> None:
    t1 = Temperature.from_celsius(25)
    t2 = Temperature.from_fahrenheit(77)
    t3 = Temperature.from_kelvin(310.15)

    print("t1 (25 °C):", round(t1.to_celsius(), 2), "°C |", round(t1.to_fahrenheit(), 2), "°F |", round(t1.to_kelvin(), 2), "K")
    print("t2 (77 °F):", round(t2.to_celsius(), 2), "°C |", round(t2.to_fahrenheit(), 2), "°F |", round(t2.to_kelvin(), 2), "K")
    print("t3 (310.15 K):", round(t3.to_celsius(), 2), "°C |", round(t3.to_fahrenheit(), 2), "°F |", round(t3.to_kelvin(), 2), "K")
    print("Is -300 °C valid?", Temperature.is_valid_celsius(-300))
    print("Is -500 °F valid?", Temperature.is_valid_fahrenheit(-500))
    print("Is -1 K valid?", Temperature.is_valid_kelvin(-1))


if __name__ == "__main__":
    main()
