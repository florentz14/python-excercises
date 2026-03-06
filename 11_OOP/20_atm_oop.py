# ------------------------------------------------------------
# File Name: 20_atm_oop.py
# Author: Florentino Baez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Description: ATM Simulation - OOP version. Same features as ATM_FinalProject_Baez_v2
#              but using classes (ATM encapsulates balance, history, and operations).
# ------------------------------------------------------------

from datetime import datetime
from pathlib import Path


class ATM:
    """ATM simulation with deposit, withdraw, balance, and history."""

    def __init__(self, pin="1234", max_attempts=3):
        self.pin = pin
        self.max_attempts = max_attempts
        self.balance = 0.0
        self.deposits = []
        self.withdrawals = []
        self.balances = []

    def _get_amount(self, prompt):
        """Get a valid positive amount from user."""
        while True:
            try:
                amount = float(input(prompt).strip())
                if amount > 0:
                    return amount
                print("Amount must be greater than 0.")
            except ValueError:
                print("Invalid input. Enter a number (e.g. 25 or 25.50).")

    def verify_pin(self):
        """Verify PIN. Returns True if correct."""
        for attempts_left in range(self.max_attempts, 0, -1):
            password = input("Enter your password: ").strip()
            if password == self.pin:
                print("Login successful!\n")
                return True
            if attempts_left > 1:
                print(f"Incorrect password. Attempts left: {attempts_left - 1}")
            else:
                print("Too many incorrect attempts. Exiting.")
        return False

    def deposit(self):
        """Add funds to balance."""
        amount = self._get_amount("Enter amount to deposit: $")
        self.balance += amount
        self.deposits.append(amount)
        self.balances.append(self.balance)
        print(f"Deposit successful. New balance: ${self.balance:,.2f}")

    def withdraw(self):
        """Remove funds if sufficient balance."""
        amount = self._get_amount("Enter amount to withdraw: $")
        if amount > self.balance:
            print(f"Insufficient funds. Balance: ${self.balance:,.2f}")
        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            self.balances.append(self.balance)
            print(f"Withdrawal successful. New balance: ${self.balance:,.2f}")

    def check_balance(self):
        """Display current balance."""
        print(f"\nCurrent balance: ${self.balance:,.2f}")

    def _show_history(self, title, items):
        """Display a list of amounts with currency format."""
        print("\n" + "-" * 50)
        print(title)
        print("-" * 50)
        if not items:
            print("No transactions yet.")
        else:
            for i, val in enumerate(items, 1):
                print(f"{i}. ${val:,.2f}")

    def show_deposit_history(self):
        """Display deposit history."""
        self._show_history("Deposit History", self.deposits)

    def show_withdrawal_history(self):
        """Display withdrawal history."""
        self._show_history("Withdrawal History", self.withdrawals)

    def show_balance_history(self):
        """Display balance after each transaction."""
        self._show_history("Balance History (after each transaction)", self.balances)

    def save_to_file(self):
        """Save histories to atm_history.txt."""
        filepath = Path(__file__).parent / "atm_history.txt"
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"ATM Session History\nSaved: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
                f.write("=" * 50 + "\n\n")
                f.write("Deposit History:\n")
                for i, d in enumerate(self.deposits, 1):
                    f.write(f"{i}. ${d:,.2f}\n")
                if not self.deposits:
                    f.write("No deposits.\n")
                f.write("\nWithdrawal History:\n")
                for i, w in enumerate(self.withdrawals, 1):
                    f.write(f"{i}. ${w:,.2f}\n")
                if not self.withdrawals:
                    f.write("No withdrawals.\n")
                f.write("\nBalance History:\n")
                for i, b in enumerate(self.balances, 1):
                    f.write(f"{i}. ${b:,.2f}\n")
                if not self.balances:
                    f.write("No balance changes.\n")
            print(f"Saved to: {filepath.resolve()}")
        except OSError as e:
            print(f"Error saving file: {e}")

    def run(self):
        """Main loop: verify PIN and process menu."""
        if not self.verify_pin():
            return

        while True:
            print("\n--- ATM Menu ---")
            print("1 - Deposit    2 - Withdraw    3 - Check Balance")
            print("4 - Deposit History    5 - Withdrawal History    6 - Balance History")
            print("7 - Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                self.show_deposit_history()
            elif choice == "5":
                self.show_withdrawal_history()
            elif choice == "6":
                self.show_balance_history()
            elif choice == "7":
                print("\nThank you for using our ATM. Goodbye!")
                if input("Save histories to file? (y/n): ").strip().lower() == "y":
                    self.save_to_file()
                break
            else:
                print("Invalid choice. Enter 1-7.")


if __name__ == "__main__":
    atm = ATM(pin="1234", max_attempts=3)
    atm.run()
