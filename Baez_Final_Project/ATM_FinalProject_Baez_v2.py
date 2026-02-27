# ------------------------------------------------------------
# File Name: ATM_FinalProject_Baez_v2.py
# Version: 2.0 version (Final Project) to be evaluated
# Author: Florentino Baez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: February 17, 2026
# Description: ATM Simulation Program (Final Project). Simulates a basic
#              automated teller machine with password protection (3 attempts,
#              default PIN: 1234). Menu-driven interface offers: (1) Deposit
#              - add funds with validation; (2) Withdraw - remove funds if
#              sufficient balance; (3) Check Balance - display current amount;
#              (4) Deposit History - list all deposits; (5) Withdrawal History -
#              list all withdrawals; (6) Balance History - balance snapshot after
#              each transaction; (7) Exit - optionally save all session histories
#              (deposits, withdrawals, balance snapshots) to atm_history.txt
#              before quitting. Input validation prevents invalid amounts and
#              non-numeric entries.
# Python Version: 3.14.2
# ------------------------------------------------------------

# Import necessary modules
from datetime import datetime
from pathlib import Path

# Global constants
PIN = "1234"
MAX_ATTEMPTS = 3


def get_amount(prompt):
    """Get a valid positive amount from user."""
    while True:
        try:
            amount = float(input(prompt).strip())
            if amount > 0:
                # Return the amount if it is greater than 0
                return amount
            # Print a message if the amount is not greater than 0
            print("Amount must be greater than 0.")
        except ValueError:
            print("Invalid input. Enter a number (e.g. 25 or 25.50).")


def verify_pin():
    """Verify PIN. Returns True if correct."""
    # Loop over the number of attempts left
    for attempts_left in range(MAX_ATTEMPTS, 0, -1):
        # Get the password from the user
        password = input("Enter your password: ").strip()
        # Check if the password is correct
        if password == PIN:
            # Print a success message
            print("Login successful!\n")
            return True
        # Print a message if the password is incorrect
        if attempts_left > 1:
            # Print a message if the password is incorrect
            print(f"Incorrect password. Attempts left: {attempts_left - 1}")
        else:
            print("Too many incorrect attempts. Exiting.")
    return False


def show_history(title, items):
    """Display a list of amounts with currency format."""
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)
    if not items:
        print("No transactions yet.")
    else:
        for i, val in enumerate(items, 1):# Loop over the items and print the index and the value
            print(f"{i}. ${val:,.2f}")


def save_to_file(deposits, withdrawals, balances):
    """Save histories to atm_history.txt."""
    filepath = Path(__file__).parent / "atm_history.txt"
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"ATM Session History\nSaved: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
            f.write("=" * 50 + "\n\n")
            f.write("Deposit History:\n")
            for i, d in enumerate(deposits, 1):
                f.write(f"{i}. ${d:,.2f}\n")
            if not deposits:
                f.write("No deposits.\n")
            f.write("\nWithdrawal History:\n")
            for i, w in enumerate(withdrawals, 1):
                f.write(f"{i}. ${w:,.2f}\n")
            if not withdrawals:
                f.write("No withdrawals.\n")
            f.write("\nBalance History:\n")
            for i, b in enumerate(balances, 1):
                f.write(f"{i}. ${b:,.2f}\n")
            if not balances:
                f.write("No balance changes.\n")
        print(f"Saved to: {filepath.resolve()}")
    except OSError as e:
        print(f"Error saving file: {e}")


def main():
    """Main function to run the ATM."""
    # Verify the PIN
    if not verify_pin():
        # Return if the PIN is not correct
        return

    # Initialize the balance, deposits, withdrawals, and balances
    balance = 0.0
    deposits = []
    withdrawals = []
    balances = []

    # Loop over the menu
    while True:
        # Print the menu
        print("\n--- ATM Menu ---")
        print("1 - Deposit    2 - Withdraw    3 - Check Balance")
        print("4 - Deposit History    5 - Withdrawal History    6 - Balance History")
        print("7 - Exit")

        # Get the choice from the user
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            amount = get_amount("Enter amount to deposit: $")
            balance += amount
            deposits.append(amount)
            balances.append(balance)
            print(f"Deposit successful. New balance: ${balance:,.2f}")

        elif choice == "2":
            amount = get_amount("Enter amount to withdraw: $")
            if amount > balance:
                print(f"Insufficient funds. Balance: ${balance:,.2f}")
            else:
                balance -= amount
                withdrawals.append(amount)
                balances.append(balance)
                print(f"Withdrawal successful. New balance: ${balance:,.2f}")

        elif choice == "3":
            print(f"\nCurrent balance: ${balance:,.2f}")

        elif choice == "4":
            show_history("Deposit History", deposits)

        elif choice == "5":
            show_history("Withdrawal History", withdrawals)

        elif choice == "6":
            show_history("Balance History (after each transaction)", balances)

        elif choice == "7":
            print("\nThank you for using our ATM. Goodbye!")
            if input("Save histories to file? (y/n): ").strip().lower() == "y":
                save_to_file(deposits, withdrawals, balances)
            break

        else:
            print("Invalid choice. Enter 1-7.")


if __name__ == "__main__":
    main()
