# ------------------------------------------------------------
# File Name: ATM_FinalProject_Baez.py
# Author: Florentino Baez
# Date: August 16, 2025
# Description: Simple ATM Simulation Program (Final Project)
# Python Version: 3.14.2
# ------------------------------------------------------------

# Enable postponed evaluation of type annotations (e.g. list[float] instead of List[float])
from __future__ import annotations

# For timestamp when saving session history to file
from datetime import datetime


# -------------------------
# Utility / Validation
# -------------------------

def get_positive_amount(prompt: str) -> float:
    """
    # Function: Keeps asking until the user enters a valid positive number (> 0).
    Prevents crashes due to invalid input.
    """
    while True:
        raw = input(prompt).strip()
        try:
            amount = float(raw)
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value (example: 25 or 25.50).")


def print_history(title: str, items: list[float]) -> None:
    """
    # Function: Prints a list of amounts in a friendly format.
    Used for both deposit and withdrawal history display.
    """
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)

    if not items:
        print("No transactions yet.")
        return

    # Number each item starting from 1; format amount with comma and 2 decimals
    for i, value in enumerate(items, start=1):
        print(f"{i}. ${value:,.2f}")


# -------------------------
# Password Verification
# -------------------------

def verify_password(correct_password: str = "1234", max_attempts: int = 3) -> bool:
    """
    # Function: Asks for a password and allows up to max_attempts.
    Returns True if correct, False otherwise.
    """
    attempts_left = max_attempts

    while attempts_left > 0:
        entered = input("Enter your password: ").strip()

        if entered == correct_password:
            print("Login successful!\n")
            return True

        attempts_left -= 1
        if attempts_left > 0:
            print(f"Incorrect password. Attempts left: {attempts_left}")
        else:
            print("Too many incorrect attempts. Program will exit.")

    return False  # All attempts used; caller should exit


# -------------------------
# ATM Operations (Functions)
# -------------------------

def deposit(balance: float, deposit_history: list[float], balance_history: list[float]) -> float:
    # Function: Process a deposit: validate amount, update balance and histories.
    amount = get_positive_amount("Enter amount to deposit: $")
    balance += amount

    deposit_history.append(amount)
    balance_history.append(balance)

    print(f"Deposit successful. New balance: ${balance:,.2f}")
    return balance


def withdraw(balance: float, withdrawal_history: list[float], balance_history: list[float]) -> float:
    # Function: Process a withdrawal: validate amount, check sufficient funds, update balance and histories.
    amount = get_positive_amount("Enter amount to withdraw: $")

    # Reject withdrawal if requested amount exceeds current balance
    if amount > balance:
        print(f"Withdrawal denied. You only have ${balance:,.2f}.")
        return balance

    balance -= amount
    withdrawal_history.append(amount)
    balance_history.append(balance)

    print(f"Withdrawal successful. New balance: ${balance:,.2f}")
    return balance


def check_balance(balance: float) -> None:
    # Function: Print the current balance
    print(f"\nCurrent balance: ${balance:,.2f}")


def show_deposit_history(deposit_history: list[float]) -> None:
    # Function: Print the deposit history
    print_history("Deposit History", deposit_history)


def show_withdrawal_history(withdrawal_history: list[float]) -> None:
    # Function: Print the withdrawal history
    print_history("Withdrawal History", withdrawal_history)


def show_balance_history(balance_history: list[float]) -> None:
    """Display balance after each transaction (snapshot history)."""
    print("\n" + "-" * 50)
    print("Balance History (after each transaction)")
    print("-" * 50)

    if not balance_history:
        # If there are no balance changes, print a message and return
        print("No balance changes yet.")
        return

    # Loop: Iterate through each balance in the history and print it
    for i, balance in enumerate(balance_history, start=1):
        print(f"{i}. ${balance:,.2f}")


def save_histories_to_file(
    deposit_history: list[float],
    withdrawal_history: list[float],
    balance_history: list[float],
    filename: str = "atm_history.txt"
) -> None:
    """
    # Function: Saves all three histories to a text file before exit.
    Overwrites the file if it already exists. It uses UTF-8 encoding for compatibility.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # "w" = write mode (overwrites); encoding="utf-8" for special chars
    with open(filename, "w", encoding="utf-8") as f:
        f.write("ATM SESSION HISTORY\n")
        f.write(f"Saved at: {timestamp}\n")
        f.write("=" * 50 + "\n\n")

        f.write("Deposit History:\n")
        if deposit_history:
            # Loop: Iterate through each deposit in the history and write it to the file
            for i, d in enumerate(deposit_history, start=1):
                f.write(f"{i}. ${d:,.2f}\n")
        else:
            f.write("No deposits.\n")

        f.write("\nWithdrawal History:\n")
        if withdrawal_history:
            # Loop: Iterate through each withdrawal in the history and write it to the file
            for i, w in enumerate(withdrawal_history, start=1):
                f.write(f"{i}. ${w:,.2f}\n")
        else:
            f.write("No withdrawals.\n")

        f.write("\nBalance History:\n")
        if balance_history:
            # Loop: Iterate through each balance in the history and write it to the file
            for i, b in enumerate(balance_history, start=1):
                f.write(f"{i}. ${b:,.2f}\n")
        else:
            f.write("No balance changes.\n")

    print(f"Histories saved to: {filename}")


# -------------------------
# Menu / Main Loop
# -------------------------

def print_menu() -> None:
    """# Function: Display the ATM main menu with all available options (1-7)."""
    print("\nWelcome, please pick an option")
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Check Balance")
    print("4 - History of Deposit")
    print("5 - History of Withdrawals")
    print("6 - History of Balance")
    print("7 - Exit")


def main() -> None:
    """# Function: Entry point: password check, then main menu loop until user chooses Exit."""
    # 1) Password gate: exit immediately if user fails after max attempts
    if not verify_password(correct_password="1234", max_attempts=3):
        return

    # 2) Initial state: zero balance and empty lists to track all transactions
    balance = 0.0
    deposit_history: list[float] = []      # every deposit amount in order
    withdrawal_history: list[float] = []   # every withdrawal amount in order
    balance_history: list[float] = []     # balance snapshot AFTER each deposit/withdraw

    # 3) Menu loop: keep showing menu and handling choice until user selects 7 (Exit)
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            balance = deposit(balance, deposit_history, balance_history)

        elif choice == "2":
            balance = withdraw(balance, withdrawal_history, balance_history)

        elif choice == "3":
            check_balance(balance)

        elif choice == "4":
            show_deposit_history(deposit_history)

        elif choice == "5":
            show_withdrawal_history(withdrawal_history)

        elif choice == "6":
            show_balance_history(balance_history)

        elif choice == "7":
            print("\nThank you for using our ATM. Goodbye!")

            # Optional: offer to save session histories to a text file before exiting
            save_option = input("Do you want to save histories to a file? (y/n): ").strip().lower()
            if save_option == "y":
                save_histories_to_file(deposit_history, withdrawal_history, balance_history)

            break  # exit the loop and end the program

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


# Run program only when this file is executed directly (not when imported as a module)
if __name__ == "__main__":
    main()
