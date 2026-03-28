# -------------------------------------------------
# File Name: ITSE-1003/Examples/product_dunder.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Magic / dunder methods.
# -------------------------------------------------


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"

    def __repr__(self) -> str:
        return f"Product(name={self.name!r}, price={self.price!r})"

    def __add__(self, other: "Product") -> float:
        return self.price + other.price


def main() -> None:
    p1 = Product("Mouse", 25.50)
    p2 = Product("Keyboard", 45.00)
    print(str(p1))
    print(repr(p2))
    print("Total:", p1 + p2)


if __name__ == "__main__":
    main()
