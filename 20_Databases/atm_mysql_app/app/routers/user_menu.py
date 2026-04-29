from __future__ import annotations

from atm_mysql_app.app.schemas.user_admin import UserCreateRequest
from atm_mysql_app.app.services.user_admin_service import (
    check_database_connection,
    create_user,
    delete_user_by_username,
    list_users,
    parse_decimal_input,
)


def _get_input(prompt: str, required: bool = True, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    while True:
        value = input(f"{prompt}{suffix}: ").strip()
        if value:
            return value
        if not required:
            return default
        print("This field is required. Please try again.")


def _create_user_wizard():
    print("\n" + "=" * 60)
    print("ATM USER CREATION WIZARD")
    print("=" * 60)
    print("\nPlease provide the following information:")
    print("-" * 60)
    username = _get_input("Username (unique)", required=True)
    password = _get_input("Password", required=True)
    full_name = _get_input("Full Name", required=True)
    email = _get_input("Email", required=False, default="")
    phone = _get_input("Phone", required=False, default="")

    while True:
        raw = input("Initial Balance [$0.00]: ").strip()
        initial_balance = parse_decimal_input(raw, default=0.0)
        if initial_balance is not None:
            break
        print("Invalid amount. Please enter a non-negative numeric value.")

    print("\n" + "=" * 60)
    print("CONFIRM USER DETAILS")
    print("=" * 60)
    print(f"Username:        {username}")
    print(f"Full Name:       {full_name}")
    print(f"Email:           {email or '(not provided)'}")
    print(f"Phone:           {phone or '(not provided)'}")
    print(f"Initial Balance: ${initial_balance:.2f}")
    print("=" * 60)

    confirm = input("\nCreate this user? (yes/no): ").strip().lower()
    if confirm not in ["yes", "y"]:
        print("User creation cancelled.")
        return

    request = UserCreateRequest(
        username=username,
        password=password,
        full_name=full_name,
        email=email or None,
        phone=phone or None,
        initial_balance=initial_balance,
    )
    create_user(request)


def run_user_admin_menu():
    print("\n" + "=" * 60)
    print("ATM USER MANAGEMENT TOOL")
    print("Make sure your database is configured and running")
    print("=" * 60)
    if not check_database_connection():
        print("\n[ERROR] Database connection failed.")
        print("\nPlease check your .env file configuration")
        return
    print("[OK] Database connection successful!")

    while True:
        print("\n" + "=" * 60)
        print("ATM USER MANAGEMENT")
        print("=" * 60)
        print("1. Create New User")
        print("2. List All Users")
        print("3. Delete User")
        print("4. Exit")
        print("=" * 60)

        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            _create_user_wizard()
        elif choice == "2":
            list_users()
        elif choice == "3":
            username = _get_input("Username to delete", required=True)
            delete_user_by_username(username)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")
