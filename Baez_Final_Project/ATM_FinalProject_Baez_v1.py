# ATM_FinalProject_Baez_v1.py - Simple ATM, NO FUNCTIONS (working version)
# Florentino Baez
# Version: 1.0 basic version with no functions
# course: ITSE-1002 Python Programming
# professor: Mauricio Quiroga
# description: Simple ATM, NO FUNCTIONS (working version)

from datetime import datetime
from pathlib import Path

# constants
PIN = "1234"
MAX_ATTEMPTS = 3

# variables
balance = 0.0
deposit_history = []
withdrawal_history = []
balance_history = []

# 1) PIN verification - inline
for attempt in range(MAX_ATTEMPTS):
    if input("Enter PIN: ").strip() == PIN:
        print("Login successful!\n")
        break
    print(f"Wrong. {MAX_ATTEMPTS - attempt} attempts left.")
else:
    print("Too many attempts. Exiting.")
    exit()

# 2) Main loop - menu and options
while True:
    # 1) Create the menu - print print print
    print("\n" + "=" * 50)
    print("ATM MENU")
    print("=" * 50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Deposit History")
    print("5. Withdrawal History")
    print("6. Balance History")
    print("7. Exit")
    print("=" * 50)

    choice = input("Enter your choice (1-7): ").strip()

    # 2) Deposit - NO FUNCTIONS YET
    if choice == "1":
        amount = float(input("Enter amount to deposit: $").strip())
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            balance += amount
            deposit_history.append(amount)
            balance_history.append(balance)
            print(f"Deposit successful. New balance: ${balance:,.2f}")

    # 3) Withdraw - NO FUNCTIONS YET
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: $").strip())
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > balance:
            print(f"Insufficient funds. Balance: ${balance:,.2f}")
        else:
            balance -= amount
            withdrawal_history.append(amount)
            balance_history.append(balance)
            print(f"Withdrawal successful. New balance: ${balance:,.2f}")

    # 4) Check Balance - NO FUNCTIONS YET
    elif choice == "3":
        print(f"\nCurrent balance: ${balance:,.2f}")

    # 5) Deposit History - NO FUNCTIONS YET
    elif choice == "4":
        print("\n" + "-" * 50)
        print("Deposit History")
        print("-" * 50)
        if not deposit_history:
            print("No deposits yet.")
        else:
            for i, d in enumerate(deposit_history, 1):
                print(f"{i}. ${d:,.2f}")

    # 6) Withdrawal History - NO FUNCTIONS YET
    elif choice == "5":
        print("\n" + "-" * 50)
        print("Withdrawal History")
        print("-" * 50)
        if not withdrawal_history:
            print("No withdrawals yet.")
        else:
            for i, w in enumerate(withdrawal_history, 1):
                print(f"{i}. ${w:,.2f}")

    # 7) Balance History - NO FUNCTIONS YET
    elif choice == "6":
        print("\n" + "-" * 50)
        print("Balance History (after each transaction)")
        print("-" * 50)
        if not balance_history:
            print("No balance changes yet.")
        else:
            for i, b in enumerate(balance_history, 1):
                print(f"{i}. ${b:,.2f}")

    # 8) Exit - NO FUNCTIONS YET
    elif choice == "7":
        print("\nThank you for using our ATM. Goodbye!")
        if input("Save histories to file? (y/n): ").strip().lower() == "y":
            filepath = Path(__file__).parent / "atm_history.txt"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"ATM Session History\nSaved: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
                f.write("=" * 50 + "\n\nDeposit History:\n")
                for i, d in enumerate(deposit_history, 1):
                    f.write(f"{i}. ${d:,.2f}\n")
                if not deposit_history:
                    f.write("No deposits.\n")
                f.write("\nWithdrawal History:\n")
                for i, w in enumerate(withdrawal_history, 1):
                    f.write(f"{i}. ${w:,.2f}\n")
                if not withdrawal_history:
                    f.write("No withdrawals.\n")
                f.write("\nBalance History:\n")
                for i, b in enumerate(balance_history, 1):
                    f.write(f"{i}. ${b:,.2f}\n")
                if not balance_history:
                    f.write("No balance changes.\n")
            print(f"Saved to: {filepath.resolve()}")
        break

    else:
        print("Invalid choice. Enter 1-7.")
