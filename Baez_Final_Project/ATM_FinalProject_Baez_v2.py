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
import os
from datetime import datetime
from pathlib import Path

# Global constants
DEFAULT_USER = ("elvin", "1234")  # (username, pin)
MAX_ATTEMPTS = 3 # Maximum number of attempts
DATA_FILE = "atm_data.txt"  # Persistent account data


def clear_screen():
    """Clear the terminal screen (Windows: cls, Unix: clear). Not called yet."""
    os.system("cls" if os.name == "nt" else "clear") # Clear the screen


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


def verify_login():
    """Verify username and PIN. Returns (True, username) if correct, (False, None) otherwise."""
    clear_screen()
    print("=" * 50)
    print("Verify Login")
    print("=" * 50)
    username, pin = DEFAULT_USER # Get the username and pin from the DEFAULT_USER
    # Loop over the number of attempts left
    for attempts_left in range(MAX_ATTEMPTS, 0, -1):
        entered_user = input("Enter username: ").strip()
        entered_pin = input("Enter PIN: ").strip()
        # Check if the entered username and pin are correct
        if entered_user == username and entered_pin == pin:
            clear_screen()
            print("=" * 50)
            print("Login successful!")
            print("=" * 50)
            return True, username
        # Print the incorrect username or PIN message
        if attempts_left > 1:
            print(f"Incorrect username or PIN. Attempts left: {attempts_left - 1}")
        # Print the login failed message
        else:
            clear_screen()
            print("=" * 50)
            print("Login failed!")
            print("=" * 50)
            print("Too many incorrect attempts. Exiting.")
    # Return False and None
    return False, None


def show_history(title, items):
    """Display a list of amounts with currency format."""
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)
    if not items:# Check if the items is empty
        print("No transactions yet.") # Print the no transactions message
    else:
        for i, val in enumerate(items, 1):# Loop over the items and print the index and the value
            print(f"{i}. ${val:,.2f}") # Print the index and the value
            # Return the index and the value


def deposit(balance, deposits, balances):
    """Process deposit: get amount, update balance and histories. Returns new balance."""
    amount = get_amount("Enter amount to deposit: $")
    balance += amount # Update the balance
    deposits.append(amount) # Add the amount to the deposits list
    balances.append(balance) # Add the balance to the balances list
    print(f"Deposit successful. New balance: ${balance:,.2f}") # Print the new balance
    return balance # Return the new balance


def withdraw(balance, withdrawals, balances):
    """Process withdrawal: get amount, check funds, update balance and histories. Returns new balance."""
    amount = get_amount("Enter amount to withdraw: $")
    # Check if the amount is greater than the balance
    if amount > balance:
        # Print the insufficient funds message
        print(f"Insufficient funds. Balance: ${balance:,.2f}")
        return balance
    # Subtract the amount from the balance
    balance -= amount
    # Add the amount to the withdrawals list
    withdrawals.append(amount)
    # Add the balance to the balances list
    balances.append(balance)
    # Print the new balance
    print(f"Withdrawal successful. New balance: ${balance:,.2f}")
    # Return the new balance
    return balance


def print_menu(username):
    """Print the menu with user and time."""

    print("=" * 50)
    # Print the user and time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"  User: {username}  |  {now}")
    print("=" * 50)
    print("--- ATM Menu ---".center(50))
    print("=" * 50)
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Check Balance")
    print("4 - Deposit History")
    print("5 - Withdrawal History")
    print("6 - Balance History")
    print("7 - Exit")
    print("=" * 50)


def save_to_file(deposits, withdrawals, balances):
    """Save histories to atm_history.txt."""
    # Get the path to the history file
    filepath = Path(__file__).parent / "atm_history.txt"
    try:
        # Try to open the file and write the history to it
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"ATM Session History\nSaved: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
            f.write("=" * 50 + "\n\n")
            f.write("Deposit History:\n")
            # Loop over the deposits and write the amount to the file
            for i, d in enumerate(deposits, 1):
                f.write(f"{i}. ${d:,.2f}\n")
            if not deposits: # Check if the deposits is empty
                f.write("No deposits.\n")
            f.write("\nWithdrawal History:\n")
            # Loop over the withdrawals and write the amount to the file
            for i, w in enumerate(withdrawals, 1):
                f.write(f"{i}. ${w:,.2f}\n")
            if not withdrawals: # Check if the withdrawals is empty
                f.write("No withdrawals.\n")
            f.write("\nBalance History:\n")
            # Loop over the balances and write the balance to the file
            for i, b in enumerate(balances, 1):
                f.write(f"{i}. ${b:,.2f}\n")
            if not balances: # Check if the balances is empty
                f.write("No balance changes.\n")
        print(f"Saved to: {filepath.resolve()}") # Print the path to the file
    except OSError as e: # Catch the error
        print(f"Error saving file: {e}") # Print the error


def get_data_filepath():
    """Return the path to the persistent data file."""
    return Path(__file__).parent / DATA_FILE # Return the path to the data file


def file_exists():
    """Check if the persistent account file exists."""
    # Check if the data file exists
    return get_data_filepath().exists() # Return the path to the data file


def _parse_amount_line(line):
    """Extract amount from line like '1. $78.90'. Returns float or None."""
    line = line.strip() # Strip the line
    if ". $" in line:
        try:
            return float(line.split("$")[1].strip()) # Return the amount
        except (IndexError, ValueError):
            pass
    return None # Return None


def load_account():
    """Load account data from file if it exists. Returns (balance, deposits, withdrawals, balances)."""
    filepath = get_data_filepath() # Get the path to the data file
    if not filepath.exists(): # Check if the data file exists
        return 0.0, [], [], [] # Return 0.0, [], [], []

    try:
        # Open the file and read the content
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read() # Read the content of the file

        # Check if the content is in the file
        if "Deposit History:" in content:
            deposits = [] # Initialize the deposits list
            withdrawals = [] # Initialize the withdrawals list
            balances_list = [] # Initialize the balances list
            section = None # Initialize the section
            # Loop over the content and split the lines
            for line in content.splitlines():
                line_stripped = line.strip() # Strip the line
                if line_stripped == "Deposit History:":
                    section = "deposits" # Set the section to deposits
                    continue
                if line_stripped == "Withdrawal History:":
                    section = "withdrawals" # Set the section to withdrawals
                    continue
                if line_stripped == "Balance History:":
                    section = "balances"
                    continue
                # Parse the amount from the line
                amount = _parse_amount_line(line)
                # Check if the amount is not None and the section is not None
                if amount is not None and section:
                    if section == "deposits":
                        deposits.append(amount) # Add the amount to the deposits list
                    elif section == "withdrawals":
                        withdrawals.append(amount) # Add the amount to the withdrawals list
                    elif section == "balances":
                        balances_list.append(amount) # Add the amount to the balances list
            balance = balances_list[-1] if balances_list else 0.0 # Get the last balance
            return balance, deposits, withdrawals, balances_list # Return the balance, deposits, withdrawals, and balances list

        return 0.0, [], [], [] # Return 0.0, [], [], []
    except (OSError, ValueError) as e:
        print(f"Error loading account: {e}. Starting with empty account.") # Print the error
        return 0.0, [], [], []


def save_account(balance, deposits, withdrawals, balances_list):
    """Save account data to file (same format as atm_history.txt)."""
    filepath = get_data_filepath() # Get the path to the data file
    try:
        # Try to open the file and write the content
        # Open the file and write the content
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("ATM Session History\n") # Write the session history to the file
            f.write(f"Saved: {datetime.now():%Y-%m-%d %H:%M:%S}\n") # Write the saved time to the file
            f.write("=" * 50 + "\n\n")
            f.write("Deposit History:\n") # Write the deposit history to the file
            # Loop over the deposits and write the amount to the file
            for i, d in enumerate(deposits, 1):
                f.write(f"{i}. ${d:,.2f}\n")
            if not deposits: # Check if the deposits is empty
                f.write("No deposits.\n")
            f.write("\nWithdrawal History:\n") # Write the withdrawal history to the file
            # Loop over the withdrawals and write the amount to the file
            for i, w in enumerate(withdrawals, 1):
                f.write(f"{i}. ${w:,.2f}\n")
            if not withdrawals: # Check if the withdrawals is empty
                f.write("No withdrawals.\n")
            f.write("\nBalance History:\n") # Write the balance history to the file
            # Loop over the balances and write the balance to the file
            for i, b in enumerate(balances_list, 1):
                f.write(f"{i}. ${b:,.2f}\n")
            if not balances_list: # Check if the balances list is empty
                f.write("No balance changes.\n")
    except OSError as e: # Catch the error
        print(f"Error saving account: {e}") # Print the error


def main():
    """Main function to run the ATM."""
    success, username = verify_login() # Verify the login
    if not success:
        return

    # Load account from file if it exists, otherwise start with empty account
    balance, deposits, withdrawals, balances = load_account() # Load the account
    if file_exists():
        clear_screen() # Clear the screen
        print("=" * 50) # Print the header
        print(f"Account loaded. Current balance: ${balance:,.2f}") # Print the account loaded message

    # Loop over the menu
    while True:
        # Print the menu with user and time
        print_menu(username)
        # Get the choice from the user
        choice = input("Enter your choice: ").strip() # Get the choice from the user

        if choice == "1":
            clear_screen()
            balance = deposit(balance, deposits, balances) # Deposit the amount

        elif choice == "2":
            clear_screen()
            balance = withdraw(balance, withdrawals, balances) # Withdraw the amount

        elif choice == "3":
            clear_screen()
            print(f"\nCurrent balance: ${balance:,.2f}")

        elif choice == "4":
            clear_screen()
            show_history("Deposit History", deposits) # Show the deposit history

        elif choice == "5":
            clear_screen()
            show_history("Withdrawal History", withdrawals) # Show the withdrawal history

        elif choice == "6":
            clear_screen()
            show_history("Balance History (after each transaction)", balances) # Show the balance history

        elif choice == "7":
            clear_screen()
            print("\nThank you for using our ATM. Goodbye!")
            # Always save account data (persistent)
            save_account(balance, deposits, withdrawals, balances) # Save the account data
            print("Account data saved.")
            if input("Save session report to atm_history.txt? (y/n): ").strip().lower() == "y":
                save_to_file(deposits, withdrawals, balances) # Save the session report to the file
            break

        else:
            clear_screen() # Clear the screen
            print("Invalid choice. Enter 1-7.") # Print the invalid choice message


if __name__ == "__main__":
    main() # Run the main function
