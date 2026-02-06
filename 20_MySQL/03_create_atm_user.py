# ------------------------------------------------------------
# File Name: 03_create_atm_user.py
# Author: Florentino Baez
# Date: February 06, 2026
# Description: Helper script to create ATM users easily
# Usage: python 03_create_atm_user.py
# ------------------------------------------------------------

import os
from dotenv import load_dotenv
import bcrypt
import mysql.connector
from mysql.connector import Error
from decimal import Decimal

# Load environment variables from .env file
load_dotenv()


# Database configuration from .env
DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'database': os.getenv('MYSQL_DATABASE', 'ATM_Database_Schema'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'port': int(os.getenv('MYSQL_PORT', 3306))
}


def hash_password(password: str) -> str:
    """Generate bcrypt hash for password."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def get_input(prompt: str, required: bool = True, default: str = "") -> str:
    """Get input from user with optional default value."""
    if default:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "
    
    while True:
        value = input(prompt).strip()
        
        if value:
            return value
        elif not required:
            return default
        else:
            print("This field is required. Please try again.")


def get_decimal_input(prompt: str, default: float = 0.0) -> Decimal:
    """Get decimal input for balance."""
    while True:
        value = input(f"{prompt} [${default:.2f}]: ").strip()
        
        if not value:
            return Decimal(str(default))
        
        try:
            decimal_value = Decimal(value)
            if decimal_value < 0:
                print("Balance cannot be negative. Try again.")
                continue
            return decimal_value
        except:
            print("Invalid amount. Please enter a numeric value.")


def create_user():
    """Interactive user creation."""
    print("\n" + "="*60)
    print("ATM USER CREATION WIZARD")
    print("="*60)
    
    # Collect user information
    print("\nPlease provide the following information:")
    print("-"*60)
    
    username = get_input("Username (unique)", required=True)
    password = get_input("Password", required=True)
    full_name = get_input("Full Name", required=True)
    email = get_input("Email", required=False)
    phone = get_input("Phone", required=False)
    initial_balance = get_decimal_input("Initial Balance", default=0.0)
    
    # Hash the password
    password_hash = hash_password(password)
    
    # Confirm details
    print("\n" + "="*60)
    print("CONFIRM USER DETAILS")
    print("="*60)
    print(f"Username:        {username}")
    print(f"Full Name:       {full_name}")
    print(f"Email:           {email or '(not provided)'}")
    print(f"Phone:           {phone or '(not provided)'}")
    print(f"Initial Balance: ${initial_balance:.2f}")
    print("="*60)
    
    confirm = input("\nCreate this user? (yes/no): ").strip().lower()
    
    if confirm not in ['yes', 'y']:
        print("User creation cancelled.")
        return False
    
    # Insert into database
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        query = """
            INSERT INTO atm_users 
            (username, password_hash, full_name, email, phone, initial_balance, current_balance)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        
        values = (
            username,
            password_hash,
            full_name,
            email if email else None,
            phone if phone else None,
            initial_balance,
            initial_balance  # current_balance starts same as initial
        )
        
        cursor.execute(query, values)
        connection.commit()
        
        user_id = cursor.lastrowid
        
        print("\n" + "="*60)
        print("[OK] USER CREATED SUCCESSFULLY!")
        print("="*60)
        print(f"User ID:   {user_id}")
        print(f"Username:  {username}")
        print(f"Password:  {password}")
        print("\nThe user can now log in with these credentials.")
        print("="*60)
        
        cursor.close()
        connection.close()
        
        return True
        
    except Error as e:
        print(f"\n[ERROR] Error creating user: {e}")
        
        if "Duplicate entry" in str(e):
            print("This username already exists. Please choose a different one.")
        
        return False


def list_users():
    """List all existing users."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        
        query = """
            SELECT 
                id,
                username,
                full_name,
                email,
                current_balance,
                is_active,
                last_login_at,
                created_at
            FROM atm_users
            ORDER BY created_at DESC
        """
        
        cursor.execute(query)
        users = cursor.fetchall()
        
        print("\n" + "="*100)
        print("EXISTING ATM USERS")
        print("="*100)
        
        if not users:
            print("No users found.")
        else:
            print(f"{'ID':<5} {'Username':<15} {'Full Name':<25} {'Balance':<15} {'Active':<8} {'Last Login':<20}")
            print("-"*100)
            
            for user in users:
                user_id = user['id']
                username = user['username'][:14]
                full_name = user['full_name'][:24]
                balance = f"${user['current_balance']:,.2f}"
                is_active = "Yes" if user['is_active'] else "No"
                last_login = user['last_login_at'].strftime('%Y-%m-%d %H:%M') if user['last_login_at'] else "Never"
                
                print(f"{user_id:<5} {username:<15} {full_name:<25} {balance:<15} {is_active:<8} {last_login:<20}")
        
        print("="*100)
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"Error listing users: {e}")


def delete_user():
    """Delete a user (with confirmation)."""
    username = get_input("Username to delete", required=True)
    
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        
        # Check if user exists
        query = "SELECT id, username, full_name, current_balance FROM atm_users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        
        if not user:
            print(f"User '{username}' not found.")
            cursor.close()
            connection.close()
            return False
        
        # Show user details
        print("\n" + "="*60)
        print("USER TO DELETE")
        print("="*60)
        print(f"ID:            {user['id']}")
        print(f"Username:      {user['username']}")
        print(f"Full Name:     {user['full_name']}")
        print(f"Balance:       ${user['current_balance']:,.2f}")
        print("="*60)
        
        # Confirm deletion
        confirm = input("\nAre you sure you want to delete this user? (yes/no): ").strip().lower()
        
        if confirm not in ['yes', 'y']:
            print("Deletion cancelled.")
            cursor.close()
            connection.close()
            return False
        
        # Delete user
        delete_query = "DELETE FROM atm_users WHERE id = %s"
        cursor.execute(delete_query, (user['id'],))
        connection.commit()
        
        print(f"\n[OK] User '{username}' deleted successfully!")
        
        cursor.close()
        connection.close()
        
        return True
        
    except Error as e:
        print(f"Error deleting user: {e}")
        return False


def main_menu():
    """Main menu for user management."""
    while True:
        print("\n" + "="*60)
        print("ATM USER MANAGEMENT")
        print("="*60)
        print("1. Create New User")
        print("2. List All Users")
        print("3. Delete User")
        print("4. Exit")
        print("="*60)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            create_user()
        
        elif choice == "2":
            list_users()
        
        elif choice == "3":
            delete_user()
        
        elif choice == "4":
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    try:
        print("\n" + "="*60)
        print("ATM USER MANAGEMENT TOOL")
        print("Make sure your database is configured and running")
        print("="*60)
        
        # Test database connection
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            if connection.is_connected():
                print("[OK] Database connection successful!")
                connection.close()
                main_menu()
        except Error as e:
            print(f"\n[ERROR] Database connection failed: {e}")
            print("\nPlease check your .env file configuration")
            
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
