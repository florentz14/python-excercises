# -------------------------------------------------
# File Name: 04_custom_exceptions.py
# Author: Florentino Báez
# Date: 22_Exceptions
# Description: Custom Exceptions. InsufficientFundsError implementation.
# -------------------------------------------------

from typing import Optional


# -----------------------------------------------------------------------------
# Custom Exception Classes
# -----------------------------------------------------------------------------

class InsufficientFundsError(Exception):
    """Raised when account balance is too low for a withdrawal."""
    def __init__(self, balance: float, amount: float, message: str = ""):
        self.balance = balance
        self.amount = amount
        msg = message or f"Insufficient funds: balance={balance:.2f}, requested={amount:.2f}"
        super().__init__(msg)


class InvalidAgeError(Exception):
    """Raised when age is outside valid range."""
    def __init__(self, age: int, min_age: int = 0, max_age: int = 150):
        self.age = age
        self.min_age = min_age
        self.max_age = max_age
        super().__init__(f"Age {age} must be between {min_age} and {max_age}")


class EmptyListError(Exception):
    """Raised when an operation requires a non-empty list."""
    pass


# -----------------------------------------------------------------------------
# Example 1: Bank withdrawal with InsufficientFundsError
# -----------------------------------------------------------------------------

def withdraw(balance: float, amount: float) -> float:
    """Withdraw amount from balance. Raises InsufficientFundsError if not enough."""
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


# -----------------------------------------------------------------------------
# Example 2: Age validation with InvalidAgeError
# -----------------------------------------------------------------------------

def set_age(age: int, min_age: int = 0, max_age: int = 150) -> int:
    """Validate age. Raises InvalidAgeError if out of range."""
    if not min_age <= age <= max_age:
        raise InvalidAgeError(age, min_age, max_age)
    return age


# -----------------------------------------------------------------------------
# Example 3: Safe max of list with EmptyListError
# -----------------------------------------------------------------------------

def safe_max(values: list[float]) -> float:
    """Return max of list. Raises EmptyListError if empty."""
    if not values:
        raise EmptyListError("Cannot compute max of empty list")
    return max(values)


# -----------------------------------------------------------------------------
# Main - Run all examples
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 55)
    print("1. InsufficientFundsError - Bank withdrawal")
    print("=" * 55)
    try:
        new_balance = withdraw(100.0, 50.0)
        print(f"Withdrew 50 from 100. New balance: {new_balance}")
    except InsufficientFundsError as e:
        print(f"Error: {e}")

    try:
        withdraw(30.0, 50.0)
    except InsufficientFundsError as e:
        print(f"Caught: {e}")
        print(f"  Balance: {e.balance}, Requested: {e.amount}")

    print("\n" + "=" * 55)
    print("2. InvalidAgeError - Age validation")
    print("=" * 55)
    for age in (25, -5, 200):
        try:
            set_age(age)
            print(f"Age {age}: OK")
        except InvalidAgeError as e:
            print(f"Age {age}: {e}")

    print("\n" + "=" * 55)
    print("3. EmptyListError - Safe max")
    print("=" * 55)
    try:
        print(f"max([1, 5, 3]) = {safe_max([1, 5, 3])}")
    except EmptyListError as e:
        print(f"Error: {e}")

    try:
        safe_max([])
    except EmptyListError as e:
        print(f"max([]): {e}")
