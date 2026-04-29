from __future__ import annotations

from atm_mysql_app.app.models.user import ATMUser
from atm_mysql_app.app.services.atm_service import ATMOperations


def print_menu():
    print("\n" + "=" * 50)
    print("ATM MAIN MENU")
    print("=" * 50)
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Check Balance")
    print("4 - Deposit History")
    print("5 - Withdrawal History")
    print("6 - Balance History")
    print("7 - Export History to File")
    print("8 - Exit")
    print("=" * 50)


def run_menu_loop(user: ATMUser):
    atm = ATMOperations(user)
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()
        if choice == "1":
            atm.deposit()
        elif choice == "2":
            atm.withdraw()
        elif choice == "3":
            atm.check_balance()
        elif choice == "4":
            atm.show_deposit_history()
        elif choice == "5":
            atm.show_withdrawal_history()
        elif choice == "6":
            atm.show_balance_history()
        elif choice == "7":
            save_option = input("Export history to file? (y/n): ").strip().lower()
            if save_option == "y":
                atm.export_history_to_file()
        elif choice == "8":
            print("\n" + "=" * 50)
            print("Thank you for using our ATM!")
            print("=" * 50)
            save_option = input("Do you want to export your history before exiting? (y/n): ").strip().lower()
            if save_option == "y":
                atm.export_history_to_file()
            user.close_session()
            print(f"Goodbye, {user.full_name}!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
