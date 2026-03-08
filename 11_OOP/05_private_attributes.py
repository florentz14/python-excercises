# -------------------------------------------------
# File Name: 05_private_attributes.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Private attributes in Python.
# -------------------------------------------------

class BankAccount:
    """Bank account with private attributes."""

    def __init__(self, account_number: str, owner: str, initial_balance: float = 0) -> None:
        # Private attributes (by convention, single underscore)
        self._account_number: str = account_number
        self._owner: str = owner

        # Truly private (name mangling, double underscore)
        self.__balance: float = initial_balance
        self.__transaction_history: list[str] = []

    def deposit(self, amount: float) -> None:
        """Deposit money."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.__balance += amount
        self.__transaction_history.append(f"Deposit: ${amount}")
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount: float) -> None:
        """Withdraw money."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount
        self.__transaction_history.append(f"Withdrawal: ${amount}")
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")

    def get_balance(self) -> float:
        """Get current balance (safe access to private attribute)."""
        return self.__balance

    def get_transaction_history(self) -> list[str]:
        """Get transaction history."""
        return self.__transaction_history.copy()  # Return copy to prevent modification

    def get_account_info(self) -> str:
        """Get account information."""
        return f"Account: {self._account_number}, Owner: {self._owner}"


class Employee:
    """Employee class with different attribute visibilities."""

    def __init__(self, name: str, salary: float) -> None:
        self.name: str = name
        self._department: str = "General"  # Protected (convention)
        self.__salary: float = salary      # Private (name mangling)

    def get_salary(self) -> float:
        """Getter for private salary."""
        return self.__salary

    def set_salary(self, new_salary: float) -> None:
        """Setter for private salary with validation."""
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = new_salary

    def display_info(self) -> str:
        """Display employee information."""
        return f"Name: {self.name}, Department: {self._department}, Salary: ${self.__salary}"


# Demonstration
if __name__ == "__main__":
    print("=== Private Attributes Demo ===\n")

    # Bank account example
    account = BankAccount("123456789", "John Doe", 1000)

    print("Account info:", account.get_account_info())
    print("Initial balance:", account.get_balance())

    account.deposit(500)
    account.withdraw(200)

    print("Transaction history:", account.get_transaction_history())

    print("\n=== Attempting to access private attributes directly ===")

    # Convention-based private (can still access)
    print("Convention private _account_number:", account._account_number)

    # Name-mangled private (harder to access)
    try:
        print("Direct access to __balance:", account.__balance)
    except AttributeError as e:
        print(f"Cannot access __balance directly: {e}")

    # But can still access with name mangling
    print("Name-mangled access _BankAccount__balance:",
          account._BankAccount__balance)  # type: ignore

    print("\n=== Employee Example ===")

    emp = Employee("Alice", 50000)
    print("Employee info:", emp.display_info())

    # Can access public attribute
    print("Public name:", emp.name)

    # Convention private (can access but shouldn't)
    print("Convention private _department:", emp._department)

    # Private salary (name mangling)
    print("Salary via getter:", emp.get_salary())

    # Update salary via setter
    emp.set_salary(55000)
    print("Updated salary:", emp.get_salary())

    print("\n=== Key Points ===")
    print("- Single underscore: convention (can still access)")
    print("- Double underscore: name mangling (harder to access)")
    print("- Use getters/setters for controlled access")
    print("- Private attributes protect internal state")
