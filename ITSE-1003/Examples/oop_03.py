# -------------------------------------------------
# File Name: ITSE-1003/Examples/oop_03.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Encapsulation with property validation.
# -------------------------------------------------


class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount


def main() -> None:
    account = BankAccount("Sofia", 100.0)
    account.deposit(50)
    print("Owner:", account.owner)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
