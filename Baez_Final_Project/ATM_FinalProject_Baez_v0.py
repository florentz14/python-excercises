# ------------------------------------------------------------
# File Name: ATM_FinalProject_Baez_v0.py
# Version: 0.1 basic version with simple functions
# Author: Florentino Baez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: February 26, 2026
# Description: Menu for the ATM.
# Python Version: 3.14.2
# ------------------------------------------------------------

# Global constants
PIN = "1234"
MAX_ATTEMPTS = 3

def verify_pin():
    """Verify PIN. Returns True if correct, False otherwise."""
    for i in range(MAX_ATTEMPTS):
        if input("Enter PIN: ").strip() == PIN:
            return True
        print(f"Wrong. {MAX_ATTEMPTS - i - 1} attempts left.")
    return False 

def print_menu():
    """Print the menu."""
    print("=" * 50)
    print("Welcome to the ATM")
    print("=" * 50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Deposit History")
    print("5. Withdrawal History")
    print("6. Balance History")
    print("7. Exit")
    print("=" * 50)

def deposit():
    """Deposit option."""
    print("I am the deposit function.")

def withdraw():
    """Withdraw option."""
    print("I am the withdraw function.")

def check_balance():
    """Check balance option."""
    print("I am the check balance function.")

def deposit_history():
    """Deposit history option."""
    print("I am the deposit history function.")

def withdrawal_history():
    """Withdrawal history option."""
    print("I am the withdrawal history function.")

def balance_history():
    """Balance history option."""
    print("I am the balance history function.")

def exit_menu():
    """Exit option."""
    print("I am the exit function.")

# Function: Get the user's choice
# int: User's choice
def get_choice():
    """Get the user's choice."""
    choice = int(input("Enter your choice: "))
    # Return the choice
    return choice
# Function: Main function
# None: None
def main():
    """Main function."""
    if not verify_pin():
        return
    while True:
        print_menu()
        choice = get_choice()
        if choice == 1:
            deposit()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            check_balance()
        elif choice == 4:
            deposit_history()
        elif choice == 5:
            withdrawal_history()
        elif choice == 6:
            balance_history()
        elif choice == 7:
            exit_menu()
            break
        else:
            print("Invalid choice.")
# Call the main function
if __name__ == "__main__":
    main()