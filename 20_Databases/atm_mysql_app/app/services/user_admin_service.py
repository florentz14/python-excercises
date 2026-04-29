from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Any, cast

import mysql.connector
from mysql.connector import Error

from atm_mysql_app.app.database import DB_CONFIG, DatabaseConnection
from atm_mysql_app.app.models.user import ATMUser
from atm_mysql_app.app.schemas.user_admin import UserCreateRequest


def format_last_login(value: Any) -> str:
    if value is None:
        return "Never"
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M")
    if isinstance(value, date):
        return value.strftime("%Y-%m-%d")
    return str(value)


def create_user(request: UserCreateRequest) -> bool:
    try:
        with DatabaseConnection() as db:
            query = """
                INSERT INTO atm_users
                (username, password_hash, full_name, email, phone, initial_balance, current_balance)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                request.username,
                ATMUser.hash_password(request.password),
                request.full_name,
                request.email,
                request.phone,
                request.initial_balance,
                request.initial_balance,
            )
            db.execute(query, values)
            db.commit()
            user_id = db.cursor.lastrowid
            print("\n" + "=" * 60)
            print("[OK] USER CREATED SUCCESSFULLY!")
            print("=" * 60)
            print(f"User ID:   {user_id}")
            print(f"Username:  {request.username}")
            print(f"Password:  {request.password}")
            print("\nThe user can now log in with these credentials.")
            print("=" * 60)
            return True
    except Error as exc:
        print(f"\n[ERROR] Error creating user: {exc}")
        if "Duplicate entry" in str(exc):
            print("This username already exists. Please choose a different one.")
        return False


def list_users():
    try:
        with DatabaseConnection() as db:
            query = """
                SELECT id, username, full_name, email, current_balance, is_active, last_login_at, created_at
                FROM atm_users
                ORDER BY created_at DESC
            """
            db.execute(query)
            users_raw = db.cursor.fetchall()
            users = cast(list[dict[str, Any]], users_raw)
            print("\n" + "=" * 100)
            print("EXISTING ATM USERS")
            print("=" * 100)
            if not users:
                print("No users found.")
            else:
                print(f"{'ID':<5} {'Username':<15} {'Full Name':<25} {'Balance':<15} {'Active':<8} {'Last Login':<20}")
                print("-" * 100)
                for user in users:
                    user_id = int(user.get("id", 0))
                    username = str(user.get("username", ""))[:14]
                    full_name = str(user.get("full_name", ""))[:24]
                    current_balance = user.get("current_balance", 0)
                    balance = f"${float(current_balance):,.2f}"
                    is_active = "Yes" if bool(user.get("is_active", False)) else "No"
                    last_login = format_last_login(user.get("last_login_at"))
                    print(f"{user_id:<5} {username:<15} {full_name:<25} {balance:<15} {is_active:<8} {last_login:<20}")
            print("=" * 100)
    except Error as exc:
        print(f"Error listing users: {exc}")


def delete_user_by_username(username: str) -> bool:
    try:
        with DatabaseConnection() as db:
            query = "SELECT id, username, full_name, current_balance FROM atm_users WHERE username = %s"
            db.execute(query, (username,))
            user_raw = db.cursor.fetchone()
            user = cast(dict[str, Any] | None, user_raw)
            if not user:
                print(f"User '{username}' not found.")
                return False
            print("\n" + "=" * 60)
            print("USER TO DELETE")
            print("=" * 60)
            user_id = int(user.get("id", 0))
            print(f"ID:            {user_id}")
            print(f"Username:      {str(user.get('username', ''))}")
            print(f"Full Name:     {str(user.get('full_name', ''))}")
            print(f"Balance:       ${float(user.get('current_balance', 0)):,.2f}")
            print("=" * 60)
            confirm = input("\nAre you sure you want to delete this user? (yes/no): ").strip().lower()
            if confirm not in ["yes", "y"]:
                print("Deletion cancelled.")
                return False
            delete_query = "DELETE FROM atm_users WHERE id = %s"
            db.execute(delete_query, (user_id,))
            db.commit()
            print(f"\n[OK] User '{username}' deleted successfully!")
            return True
    except Error as exc:
        print(f"Error deleting user: {exc}")
        return False


def check_database_connection() -> bool:
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            connection.close()
            return True
        return False
    except Error:
        return False


def parse_decimal_input(raw: str, default: float = 0.0) -> Decimal | None:
    if not raw:
        return Decimal(str(default))
    try:
        value = Decimal(raw)
        if value < 0:
            return None
        return value
    except Exception:
        return None
