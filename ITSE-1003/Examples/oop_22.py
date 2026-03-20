# -------------------------------------------------
# File Name: ITSE-1003/Examples/oop_22.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Strategy pattern with Protocol.
# -------------------------------------------------

from typing import Protocol


class PaymentStrategy(Protocol):
    def pay(self, amount: float) -> str:
        ...


class CardPayment:
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using card."


class CashPayment:
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} in cash."


class Checkout:
    def __init__(self, strategy: PaymentStrategy) -> None:
        self.strategy = strategy

    def process(self, amount: float) -> None:
        print(self.strategy.pay(amount))


def main() -> None:
    checkout = Checkout(CardPayment())
    checkout.process(29.99)

    checkout.strategy = CashPayment()
    checkout.process(12.50)


if __name__ == "__main__":
    main()
