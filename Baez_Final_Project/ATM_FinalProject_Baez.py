# ------------------------------------------------------------
# File Name: ATM_FinalProject_Baez.py
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

# PEP 563: postponed type annotations
from __future__ import annotations

from datetime import datetime  # Timestamp for session history
from pathlib import Path       # Save file in script folder


# -------------------------
# Get Positive Amount Function
# -------------------------

def get_positive_amount(prompt: str) -> float:
    """Prompt until valid positive number. Catches ValueError for non-numeric input."""
    while True:
        raw = input(prompt).strip() # Get input and strip whitespace
        try:
            amount = float(raw) # Convert to float
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value (example: 25 or 25.50).")


# -------------------------
# Print History Function
# -------------------------

def print_history(title: str, items: list[float]) -> None:
    """Display amounts as numbered list with currency format."""
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)

    if not items:
        print("No transactions yet.")
        return

    for i, value in enumerate(items, start=1): # Display the amount as a numbered list
        print(f"{i}. ${value:,.2f}")


# -------------------------
# Password Verification Function
# -------------------------

def verify_password(correct_password: str = "1234", max_attempts: int = 3) -> bool:
    """Validate password. Returns True if correct, False if max attempts exceeded."""
    attempts_left = max_attempts

    while attempts_left > 0:
        entered = input("Enter your password: ").strip() # Get input and strip whitespace

        if entered == correct_password: # Check if the password is correct
            print("Login successful!\n")
            return True # Return True if the password is correct

        attempts_left -= 1 # Decrement the number of attempts   
        if attempts_left > 0: # Check if there are attempts left
            print(f"Incorrect password. Attempts left: {attempts_left}")
        else: # If there are no attempts left, print a message and return False
            print("Too many incorrect attempts. Program will exit.")

    return False # Return False if the password is incorrect


# -------------------------
# Deposit Function
# -------------------------

def deposit(balance: float, deposit_history: list[float], balance_history: list[float]) -> float:
    """Validate amount, update balance and histories. Returns new balance."""
    amount = get_positive_amount("Enter amount to deposit: $") # Get the amount to deposit
    balance += amount # Add the amount to the balance

    deposit_history.append(amount) # Add the amount to the deposit history
    balance_history.append(balance) # Add the balance to the balance history

    print(f"Deposit successful. New balance: ${balance:,.2f}") # Print a message and return the balance
    return balance # Return the new balance


# -------------------------
# Withdraw Function
# -------------------------

def withdraw(balance: float, withdrawal_history: list[float], balance_history: list[float]) -> float:
    """Validate amount, check funds, update histories. Returns new balance or unchanged if denied."""
    amount = get_positive_amount("Enter amount to withdraw: $") # Get the amount to withdraw

    if amount > balance:  # Insufficient funds
        print(f"Withdrawal denied. You only have ${balance:,.2f}.") # Print a message and return the balance
        return balance # Return the unchanged balance

    balance -= amount # Subtract the amount from the balance
    withdrawal_history.append(amount) # Add the amount to the withdrawal history
    balance_history.append(balance) # Add the balance to the balance history

    print(f"Withdrawal successful. New balance: ${balance:,.2f}") # Print a message and return the balance
    return balance # Return the new balance


# -------------------------
# Check Balance Function
# -------------------------

def check_balance(balance: float) -> None:
    """Display current balance."""
    print(f"\nCurrent balance: ${balance:,.2f}") # Print the current balance


# -------------------------
# Show Deposit History Function
# -------------------------

def show_deposit_history(deposit_history: list[float]) -> None:
    """Display deposit history."""
    print_history("Deposit History", deposit_history) # Print the deposit history


# -------------------------
# Show Withdrawal History Function
# -------------------------

def show_withdrawal_history(withdrawal_history: list[float]) -> None:
    """Display withdrawal history."""
    print_history("Withdrawal History", withdrawal_history) # Print the withdrawal history


# -------------------------
# Show Balance History Function
# -------------------------

def show_balance_history(balance_history: list[float]) -> None:
    """Display balance snapshot after each transaction."""
    print("\n" + "-" * 50) # Print the separator
    print("Balance History (after each transaction)") # Print the header
    print("-" * 50) # Print the separator

    if not balance_history:
        print("No balance changes yet.") # Print a message if there are no balance changes
        return

    for i, balance in enumerate(balance_history, start=1): # Print the balance as a numbered list
        print(f"{i}. ${balance:,.2f}") # Print the balance as a numbered list


# -------------------------
# Save Histories to File Function
# -------------------------

def save_histories_to_file(
    deposit_history: list[float],
    withdrawal_history: list[float],
    balance_history: list[float],
    filename: str | Path | None = None
) -> None:
    """Save histories to atm_history.txt in script folder. Overwrites if exists."""
    if filename is None: # If the filename is not passed in, set the filename to atm_history.txt in the script folder
        filename = Path(__file__).parent / "atm_history.txt" # Set the filename to atm_history.txt in the script folder
    else: # If the filename is passed in, set the filename to the filename passed in
        filename = Path(filename) # Set the filename to the filename passed in

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Get the current timestamp

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("ATM SESSION HISTORY\n") # Write the header to the file
            f.write(f"Saved at: {timestamp}\n")
            f.write("=" * 50 + "\n\n") # Write the separator to the file

            f.write("Deposit History:\n")
            if deposit_history:
                for i, d in enumerate(deposit_history, start=1):
                    f.write(f"{i}. ${d:,.2f}\n") # Write the deposit history to the file
            else:
                f.write("No deposits.\n")

            f.write("\nWithdrawal History:\n")
            if withdrawal_history:
                for i, w in enumerate(withdrawal_history, start=1):
                    f.write(f"{i}. ${w:,.2f}\n") # Write the withdrawal history to the file
            else:
                f.write("No withdrawals.\n")

            f.write("\nBalance History:\n")
            if balance_history:
                for i, b in enumerate(balance_history, start=1):
                    f.write(f"{i}. ${b:,.2f}\n") # Write the balance history to the file
            else:
                f.write("No balance changes.\n")

        print(f"Histories saved to: {filename.resolve()}") # Print a message and return the filename
    except OSError as e:
        print(f"Error: Could not save file. {e}") # Print a message and return the error


# -------------------------
# Print Menu Function
# -------------------------

def print_menu() -> None:
    """Display ATM menu (1-7).""" 
    print("\nWelcome, please pick an option") # Print the welcome message
    print("1 - Deposit") # Print the deposit option
    print("2 - Withdraw") # Print the withdraw option
    print("3 - Check Balance") # Print the check balance option
    print("4 - History of Deposit") # Print the history of deposit option
    print("5 - History of Withdrawals") # Print the history of withdrawals option
    print("6 - History of Balance") # Print the history of balance option
    print("7 - Exit") # Print the exit option


# -------------------------
# Main Function
# -------------------------

def main() -> None:
    """Entry point: authenticate, then menu loop until Exit."""
    if not verify_password(correct_password="1234", max_attempts=3): # Check if the password is correct
        return # Return if the password is incorrect

    # Initialize the balance, deposit history, withdrawal history, and balance history
    balance = 0.0
    deposit_history: list[float] = []
    withdrawal_history: list[float] = []
    balance_history: list[float] = []

    try: # Try to run the program
        while True:
            print_menu()
            choice = input("Enter your choice: ").strip() # Get the choice from the user

            if choice == "1":
                balance = deposit(balance, deposit_history, balance_history) # Deposit the money

            elif choice == "2":
                balance = withdraw(balance, withdrawal_history, balance_history) # Withdraw the money

            elif choice == "3":
                check_balance(balance) # Check the balance

            elif choice == "4":
                show_deposit_history(deposit_history) # Show the deposit history

            elif choice == "5":
                show_withdrawal_history(withdrawal_history) # Show the withdrawal history

            elif choice == "6":
                show_balance_history(balance_history) # Show the balance history

            elif choice == "7":
                print("\nThank you for using our ATM. Goodbye!")
                save_option = input("Do you want to save histories to a file? (y/n): ").strip().lower() # Get the save option from the user
                if save_option == "y":
                    save_histories_to_file(deposit_history, withdrawal_history, balance_history) # Save the histories to a file if the user wants to save it
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 7.") # Print a message if the choice is invalid
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.") # Print a message if the program is interrupted by the user
    except Exception as e:
        print(f"\nError: {e}") # Print a message if an error occurs


if __name__ == "__main__":
    main() # Run the main function
