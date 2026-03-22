# -------------------------------------------------
# File Name: ITSE-1003/Examples/bank_property.py
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

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    def __str__(self) -> str:
        """String representation of the account."""
        return f"BankAccount(owner='{self.owner}', balance=${self._balance:.2f})"


def main() -> None:
    account = BankAccount("Sofia", 100.0)
    account.deposit(50)
    print("Owner:", account.owner)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
