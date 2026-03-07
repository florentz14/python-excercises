# -------------------------------------------------
# File: 23_account.py
# Description: Bank account class - practical application.
#              Encapsulation, validation, transactions.
# -------------------------------------------------

from datetime import datetime
from typing import List, Optional, Dict
from decimal import Decimal, ROUND_DOWN


class Account:
    """Bank account class with transaction management."""

    # Class variables
    _next_account_number = 1000
    _interest_rate = Decimal('0.02')  # 2% annual interest

    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        """Initialize account with validation."""
        self._account_number = Account._next_account_number
        Account._next_account_number += 1

        self._owner_name = ""
        self._balance = Decimal('0.00')
        self._transactions = []
        self._is_active = True

        # Use setters for validation
        self.owner_name = owner_name
        self.deposit(initial_balance)  # Use deposit method for initial balance

    @property
    def account_number(self) -> int:
        """Get account number (read-only)."""
        return self._account_number

    @property
    def owner_name(self) -> str:
        """Get owner name."""
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value: str):
        """Set owner name with validation."""
        if not value or not value.strip():
            raise ValueError("Owner name cannot be empty")
        if len(value.strip()) < 2:
            raise ValueError("Owner name must be at least 2 characters")
        self._owner_name = value.strip().title()

    @property
    def balance(self) -> float:
        """Get current balance."""
        return float(self._balance)

    @property
    def is_active(self) -> bool:
        """Check if account is active."""
        return self._is_active

    def deposit(self, amount: float) -> str:
        """Deposit money into account."""
        if not self._is_active:
            raise ValueError("Cannot deposit into inactive account")

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be positive")

        decimal_amount = Decimal(str(amount)).quantize(
            Decimal('0.01'), rounding=ROUND_DOWN)
        self._balance += decimal_amount

        transaction = {
            'type': 'deposit',
            'amount': float(decimal_amount),
            'balance_after': float(self._balance),
            'timestamp': datetime.now(),
            'description': f"Deposit of ${decimal_amount}"
        }
        self._transactions.append(transaction)

        return f"Deposited ${decimal_amount}. New balance: ${self._balance}"

    def withdraw(self, amount: float) -> str:
        """Withdraw money from account."""
        if not self._is_active:
            raise ValueError("Cannot withdraw from inactive account")

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        decimal_amount = Decimal(str(amount)).quantize(
            Decimal('0.01'), rounding=ROUND_DOWN)

        if decimal_amount > self._balance:
            raise ValueError(
                f"Insufficient funds. Available: ${self._balance}")

        self._balance -= decimal_amount

        transaction = {
            'type': 'withdrawal',
            'amount': float(decimal_amount),
            'balance_after': float(self._balance),
            'timestamp': datetime.now(),
            'description': f"Withdrawal of ${decimal_amount}"
        }
        self._transactions.append(transaction)

        return f"Withdrew ${decimal_amount}. New balance: ${self._balance}"

    def transfer(self, other_account: 'Account', amount: float) -> str:
        """Transfer money to another account."""
        if not isinstance(other_account, Account):
            raise ValueError("Invalid target account")

        if other_account == self:
            raise ValueError("Cannot transfer to the same account")

        # Withdraw from this account
        self.withdraw(amount)

        # Deposit to other account
        try:
            other_account.deposit(amount)
            return f"Transferred ${amount} to account {other_account.account_number}"
        except Exception as e:
            # If deposit fails, refund this account
            self.deposit(amount)
            raise ValueError(f"Transfer failed: {e}")

    def apply_interest(self) -> str:
        """Apply annual interest to account."""
        if not self._is_active:
            raise ValueError("Cannot apply interest to inactive account")

        if self._balance <= 0:
            return "No interest applied (zero or negative balance)"

        interest = (
            self._balance * Account._interest_rate).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        self._balance += interest

        transaction = {
            'type': 'interest',
            'amount': float(interest),
            'balance_after': float(self._balance),
            'timestamp': datetime.now(),
            'description': f"Interest applied at {Account._interest_rate * 100}%"
        }
        self._transactions.append(transaction)

        return f"Interest of ${interest} applied. New balance: ${self._balance}"

    def close_account(self) -> str:
        """Close the account."""
        if not self._is_active:
            raise ValueError("Account is already closed")

        if self._balance > 0:
            raise ValueError(
                "Cannot close account with positive balance. Withdraw funds first.")

        self._is_active = False
        return f"Account {self._account_number} closed successfully"

    def get_transaction_history(self, limit: Optional[int] = None) -> List[Dict]:
        """Get transaction history."""
        transactions = self._transactions.copy()
        if limit:
            transactions = transactions[-limit:]
        return transactions

    def get_account_summary(self) -> str:
        """Get account summary."""
        status = "Active" if self._is_active else "Closed"
        summary = f"Account Summary\n"
        summary += f"Account Number: {self._account_number}\n"
        summary += f"Owner: {self._owner_name}\n"
        summary += f"Balance: ${self._balance}\n"
        summary += f"Status: {status}\n"
        summary += f"Total Transactions: {len(self._transactions)}"

        if self._transactions:
            recent = self._transactions[-1]
            summary += f"\nLast Transaction: {recent['description']} ({recent['timestamp'].strftime('%Y-%m-%d %H:%M')})"

        return summary

    def __str__(self) -> str:
        """String representation."""
        status = "Active" if self._is_active else "Closed"
        return f"Account {self._account_number} - {self._owner_name} (${self._balance}) [{status}]"

    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"Account(owner_name='{self._owner_name}', balance={self._balance}, active={self._is_active})"

    @classmethod
    def get_next_account_number(cls) -> int:
        """Get the next account number that will be assigned."""
        return cls._next_account_number

    @classmethod
    def set_interest_rate(cls, rate: float):
        """Set the annual interest rate for all accounts."""
        if not isinstance(rate, (int, float)) or rate < 0 or rate > 1:
            raise ValueError(
                "Interest rate must be between 0 and 1 (0% to 100%)")
        cls._interest_rate = Decimal(str(rate))

    @classmethod
    def get_interest_rate(cls) -> float:
        """Get the current interest rate."""
        return float(cls._interest_rate)

    @staticmethod
    def validate_amount(amount: float) -> bool:
        """Validate if amount is positive."""
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def format_currency(amount: float) -> str:
        """Format amount as currency."""
        return f"${amount:.2f}"


class SavingsAccount(Account):
    """Savings account with withdrawal limits."""

    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        super().__init__(owner_name, initial_balance)
        self._monthly_withdrawals = 0
        self._withdrawal_limit = 6  # Max 6 withdrawals per month

    def withdraw(self, amount: float) -> str:
        """Withdraw with monthly limit."""
        if self._monthly_withdrawals >= self._withdrawal_limit:
            raise ValueError(
                f"Monthly withdrawal limit ({self._withdrawal_limit}) exceeded")

        result = super().withdraw(amount)
        self._monthly_withdrawals += 1
        return result

    def reset_monthly_withdrawals(self):
        """Reset monthly withdrawal counter (call at start of month)."""
        self._monthly_withdrawals = 0

    def get_withdrawal_info(self) -> str:
        """Get withdrawal limit information."""
        remaining = self._withdrawal_limit - self._monthly_withdrawals
        return f"Withdrawals this month: {self._monthly_withdrawals}/{self._withdrawal_limit} (remaining: {remaining})"


# Demonstration
if __name__ == "__main__":
    print("=== Account Class Demo ===\n")

    # Create accounts
    account1 = Account("John Doe", 1000.00)
    account2 = Account("Jane Smith", 500.00)
    savings = SavingsAccount("Bob Wilson", 2000.00)

    print("Initial accounts:")
    print(account1)
    print(account2)
    print(savings)
    print()

    # Transactions
    print("Transactions:")
    print(account1.deposit(250.50))
    print(account1.withdraw(100.00))
    print(account2.deposit(750.25))
    print()

    # Transfer
    print("Transfer:")
    print(account1.transfer(account2, 200.00))
    print(f"After transfer: {account1}")
    print(f"After transfer: {account2}")
    print()

    # Interest
    print("Interest application:")
    Account.set_interest_rate(0.03)  # 3%
    print(f"Interest rate set to {Account.get_interest_rate() * 100}%")
    print(account1.apply_interest())
    print(account2.apply_interest())
    print()

    # Savings account
    print("Savings account operations:")
    print(savings.withdraw(500.00))
    print(savings.get_withdrawal_info())
    print(savings.withdraw(300.00))
    print(savings.get_withdrawal_info())
    print()

    # Account summary
    print("Account summaries:")
    print(account1.get_account_summary())
    print()
    print(savings.get_account_summary())
    print()

    # Transaction history
    print("Recent transactions for account1:")
    for transaction in account1.get_transaction_history(3):
        print(
            f"  {transaction['timestamp'].strftime('%Y-%m-%d %H:%M')}: {transaction['description']}")
    print()

    # Static methods
    print("Static method validation:")
    print(f"Valid amount $100: {Account.validate_amount(100)}")
    print(f"Valid amount -$50: {Account.validate_amount(-50)}")
    print(f"Formatted currency: {Account.format_currency(1234.56)}")

    print("\n=== OOP Concepts Demonstrated ===")
    print("- Encapsulation: Private balance and transaction management")
    print("- Inheritance: SavingsAccount extends Account")
    print("- Polymorphism: SavingsAccount overrides withdraw()")
    print("- Class methods: Interest rate management")
    print("- Static methods: Utility functions")
    print("- Properties: Read-only account number")
    print("- Validation: Input validation throughout")
    print("- Exception handling: Proper error management")

    print("\n=== Error Handling Demo ===")
    try:
        account1.withdraw(5000)  # Insufficient funds
    except ValueError as e:
        print(f"Withdrawal error: {e}")

    try:
        invalid_account = Account("", -100)  # Invalid name and balance
    except ValueError as e:
        print(f"Account creation error: {e}")

    try:
        account1.transfer(account1, 100)  # Transfer to self
    except ValueError as e:
        print(f"Transfer error: {e}")

    try:
        closed_account = Account("Test User", 100)
        closed_account.close_account()
        closed_account.deposit(50)  # Try to use closed account
    except ValueError as e:
        print(f"Closed account error: {e}")
