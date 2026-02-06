# ------------------------------------------------------------
# File Name: 02_ATM_Database_Version.py
# Author: Florentino Baez
# Date: February 06, 2026
# Description: ATM Simulation with MySQL Database Integration
# Python Version: 3.14.2
# Requirements: pip install mysql-connector-python bcrypt python-dotenv
# ------------------------------------------------------------

from __future__ import annotations
from datetime import datetime
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import bcrypt
from typing import Optional, Tuple

# Load environment variables from .env file
load_dotenv()


# -------------------------
# Database Configuration
# -------------------------

DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'database': os.getenv('MYSQL_DATABASE', 'ATM_Database_Schema'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'port': int(os.getenv('MYSQL_PORT', 3306))
}


# -------------------------
# Database Connection
# -------------------------

class DatabaseConnection:
    """Manages database connection with context manager support."""
    
    def __init__(self, config: dict = None):
        self.config = config or DB_CONFIG
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        """Establish database connection."""
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor(dictionary=True)
            return self
        except Error as e:
            print(f"Database connection error: {e}")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def execute(self, query: str, params: tuple = None):
        """Execute a query."""
        try:
            self.cursor.execute(query, params or ())
            return self.cursor
        except Error as e:
            print(f"Query execution error: {e}")
            raise
    
    def commit(self):
        """Commit transaction."""
        if self.connection:
            self.connection.commit()
    
    def rollback(self):
        """Rollback transaction."""
        if self.connection:
            self.connection.rollback()


# -------------------------
# User Authentication
# -------------------------

class ATMUser:
    """Represents an ATM user with authentication methods."""
    
    def __init__(self, user_id: int, username: str, full_name: str, current_balance: float):
        self.user_id = user_id
        self.username = username
        self.full_name = full_name
        self.current_balance = current_balance
        self.session_id: Optional[int] = None
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify password against hash."""
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    @classmethod
    def authenticate(cls, username: str, password: str, max_attempts: int = 3) -> Optional['ATMUser']:
        """
        Authenticate user with username and password.
        Returns ATMUser object if successful, None otherwise.
        """
        attempts_left = max_attempts
        
        while attempts_left > 0:
            entered_password = password if attempts_left == max_attempts else input("Enter your password: ").strip()
            
            with DatabaseConnection() as db:
                # Get user information
                query = "SELECT id, username, password_hash, full_name, current_balance, is_active FROM atm_users WHERE username = %s"
                db.execute(query, (username,))
                user_data = db.cursor.fetchone()
                
                if not user_data:
                    cls._log_login_attempt(username, None, 'failed', 'User not found')
                    print("User not found.")
                    return None
                
                if not user_data['is_active']:
                    cls._log_login_attempt(username, user_data['id'], 'blocked', 'Account inactive')
                    print("Account is inactive. Contact support.")
                    return None
                
                # Verify password
                if cls.verify_password(entered_password, user_data['password_hash']):
                    # Successful login
                    user = cls(
                        user_id=user_data['id'],
                        username=user_data['username'],
                        full_name=user_data['full_name'],
                        current_balance=float(user_data['current_balance'])
                    )
                    
                    # Reset failed attempts and update last login
                    update_query = """
                        UPDATE atm_users 
                        SET failed_login_attempts = 0, last_login_at = NOW()
                        WHERE id = %s
                    """
                    db.execute(update_query, (user.user_id,))
                    db.commit()
                    
                    # Log successful login
                    cls._log_login_attempt(username, user.user_id, 'success', None)
                    
                    print(f"Login successful! Welcome, {user.full_name}\n")
                    return user
                else:
                    # Failed password
                    attempts_left -= 1
                    
                    # Update failed attempts
                    update_query = """
                        UPDATE atm_users 
                        SET failed_login_attempts = failed_login_attempts + 1
                        WHERE id = %s
                    """
                    db.execute(update_query, (user_data['id'],))
                    db.commit()
                    
                    # Log failed attempt
                    cls._log_login_attempt(username, user_data['id'], 'failed', 'Incorrect password')
                    
                    if attempts_left > 0:
                        print(f"Incorrect password. Attempts left: {attempts_left}")
                    else:
                        print("Too many incorrect attempts. Program will exit.")
        
        return None
    
    @staticmethod
    def _log_login_attempt(username: str, user_id: Optional[int], status: str, reason: Optional[str]):
        """Log login attempt to database."""
        try:
            with DatabaseConnection() as db:
                query = """
                    INSERT INTO atm_login_attempts (username, id_user, attempt_status, failure_reason)
                    VALUES (%s, %s, %s, %s)
                """
                db.execute(query, (username, user_id, status, reason))
                db.commit()
        except Exception as e:
            print(f"Warning: Could not log login attempt: {e}")
    
    def create_session(self) -> int:
        """Create a new session for the user."""
        with DatabaseConnection() as db:
            query = "INSERT INTO atm_sessions (id_user) VALUES (%s)"
            db.execute(query, (self.user_id,))
            db.commit()
            self.session_id = db.cursor.lastrowid
            return self.session_id
    
    def close_session(self):
        """Close current session."""
        if self.session_id:
            with DatabaseConnection() as db:
                query = """
                    UPDATE atm_sessions 
                    SET logout_at = NOW(),
                        session_duration = TIMESTAMPDIFF(SECOND, login_at, NOW())
                    WHERE id = %s
                """
                db.execute(query, (self.session_id,))
                db.commit()


# -------------------------
# ATM Operations (Database)
# -------------------------

class ATMOperations:
    """Handles all ATM operations with database integration."""
    
    def __init__(self, user: ATMUser):
        self.user = user
    
    def deposit(self) -> bool:
        """Process a deposit transaction."""
        amount = self._get_positive_amount("Enter amount to deposit: $")
        
        try:
            with DatabaseConnection() as db:
                # Call stored procedure
                args = (self.user.user_id, self.user.session_id, amount, 0, 0)
                result = db.cursor.callproc('sp_make_deposit', args)
                db.commit()
                
                new_balance = result[3]
                transaction_id = result[4]
                
                # Update user's current balance
                self.user.current_balance = float(new_balance)
                
                print(f"\n[OK] Deposit successful!")
                print(f"  Amount: ${amount:,.2f}")
                print(f"  New balance: ${new_balance:,.2f}")
                print(f"  Transaction ID: {transaction_id}")
                
                return True
        except Exception as e:
            print(f"Deposit failed: {e}")
            return False
    
    def withdraw(self) -> bool:
        """Process a withdrawal transaction."""
        amount = self._get_positive_amount("Enter amount to withdraw: $")
        
        try:
            with DatabaseConnection() as db:
                # Call stored procedure
                args = (self.user.user_id, self.user.session_id, amount, 0, 0, False, '')
                result = db.cursor.callproc('sp_make_withdrawal', args)
                db.commit()
                
                new_balance = result[3]
                transaction_id = result[4]
                success = result[5]
                message = result[6]
                
                if success:
                    # Update user's current balance
                    self.user.current_balance = float(new_balance)
                    
                    print(f"\n[OK] Withdrawal successful!")
                    print(f"  Amount: ${amount:,.2f}")
                    print(f"  New balance: ${new_balance:,.2f}")
                    print(f"  Transaction ID: {transaction_id}")
                    return True
                else:
                    print(f"\n[ERROR] Withdrawal denied: {message}")
                    return False
        except Exception as e:
            print(f"Withdrawal failed: {e}")
            return False
    
    def check_balance(self):
        """Display current balance."""
        print(f"\n{'='*50}")
        print(f"Current Balance: ${self.user.current_balance:,.2f}")
        print(f"{'='*50}")
    
    def show_deposit_history(self):
        """Display deposit history from database."""
        try:
            with DatabaseConnection() as db:
                db.cursor.callproc('sp_get_deposit_history', (self.user.user_id,))
                
                # Get results from stored procedure
                for result in db.cursor.stored_results():
                    deposits = result.fetchall()
                
                self._print_transaction_history("Deposit History", deposits)
        except Exception as e:
            print(f"Error retrieving deposit history: {e}")
    
    def show_withdrawal_history(self):
        """Display withdrawal history from database."""
        try:
            with DatabaseConnection() as db:
                db.cursor.callproc('sp_get_withdrawal_history', (self.user.user_id,))
                
                # Get results from stored procedure
                for result in db.cursor.stored_results():
                    withdrawals = result.fetchall()
                
                self._print_transaction_history("Withdrawal History", withdrawals)
        except Exception as e:
            print(f"Error retrieving withdrawal history: {e}")
    
    def show_balance_history(self):
        """Display balance history from database."""
        try:
            with DatabaseConnection() as db:
                db.cursor.callproc('sp_get_balance_history', (self.user.user_id,))
                
                # Get results from stored procedure
                for result in db.cursor.stored_results():
                    snapshots = result.fetchall()
                
                print("\n" + "="*70)
                print("Balance History (after each transaction)")
                print("="*70)
                
                if not snapshots:
                    print("No balance changes yet.")
                    return
                
                print(f"{'#':<5} {'Date/Time':<20} {'Type':<12} {'Amount':<15} {'Balance':<15}")
                print("-"*70)
                
                for i, snap in enumerate(snapshots, start=1):
                    date_str = snap['created_at'].strftime('%Y-%m-%d %H:%M:%S')
                    trans_type = snap['transaction_type'].capitalize()
                    amount = f"${snap['amount']:,.2f}"
                    balance = f"${snap['balance']:,.2f}"
                    
                    print(f"{i:<5} {date_str:<20} {trans_type:<12} {amount:<15} {balance:<15}")
        except Exception as e:
            print(f"Error retrieving balance history: {e}")
    
    def export_history_to_file(self) -> bool:
        """Export all histories to a text file."""
        try:
            filename = f"atm_history_{self.user.username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            
            with DatabaseConnection() as db:
                # Get all transaction data
                query = """
                    SELECT transaction_type, amount, balance_after, created_at, transaction_status
                    FROM atm_transactions
                    WHERE id_user = %s
                    ORDER BY created_at ASC
                """
                db.execute(query, (self.user.user_id,))
                transactions = db.cursor.fetchall()
                
                # Write to file
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("="*70 + "\n")
                    f.write(f"ATM SESSION HISTORY - {self.user.full_name}\n")
                    f.write(f"Username: {self.user.username}\n")
                    f.write(f"Exported at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("="*70 + "\n\n")
                    
                    # Separate by transaction type
                    deposits = [t for t in transactions if t['transaction_type'] == 'deposit']
                    withdrawals = [t for t in transactions if t['transaction_type'] == 'withdrawal']
                    
                    # Deposit History
                    f.write("DEPOSIT HISTORY:\n")
                    f.write("-"*70 + "\n")
                    if deposits:
                        for i, dep in enumerate(deposits, start=1):
                            f.write(f"{i}. ${dep['amount']:,.2f} - {dep['created_at']}\n")
                    else:
                        f.write("No deposits.\n")
                    f.write("\n")
                    
                    # Withdrawal History
                    f.write("WITHDRAWAL HISTORY:\n")
                    f.write("-"*70 + "\n")
                    if withdrawals:
                        for i, wit in enumerate(withdrawals, start=1):
                            status = f" [{wit['transaction_status']}]" if wit['transaction_status'] != 'completed' else ""
                            f.write(f"{i}. ${wit['amount']:,.2f}{status} - {wit['created_at']}\n")
                    else:
                        f.write("No withdrawals.\n")
                    f.write("\n")
                    
                    # Balance History
                    f.write("BALANCE HISTORY:\n")
                    f.write("-"*70 + "\n")
                    if transactions:
                        for i, trans in enumerate(transactions, start=1):
                            f.write(f"{i}. ${trans['balance_after']:,.2f} - {trans['created_at']}\n")
                    else:
                        f.write("No balance changes.\n")
                    f.write("\n")
                    
                    # Summary
                    total_deposited = sum(t['amount'] for t in deposits)
                    total_withdrawn = sum(t['amount'] for t in withdrawals if t['transaction_status'] == 'completed')
                    
                    f.write("="*70 + "\n")
                    f.write("SUMMARY:\n")
                    f.write(f"Total Deposits: ${total_deposited:,.2f}\n")
                    f.write(f"Total Withdrawals: ${total_withdrawn:,.2f}\n")
                    f.write(f"Current Balance: ${self.user.current_balance:,.2f}\n")
                    f.write("="*70 + "\n")
                
                # Log the export
                export_query = """
                    INSERT INTO atm_history_exports 
                    (id_user, id_session, filename, export_type, total_deposits, total_withdrawals)
                    VALUES (%s, %s, %s, 'full_history', %s, %s)
                """
                db.execute(export_query, (
                    self.user.user_id,
                    self.user.session_id,
                    filename,
                    len(deposits),
                    len(withdrawals)
                ))
                db.commit()
                
                print(f"\n[OK] History exported successfully to: {filename}")
                return True
                
        except Exception as e:
            print(f"Error exporting history: {e}")
            return False
    
    @staticmethod
    def _get_positive_amount(prompt: str) -> float:
        """Get a valid positive amount from user input."""
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
    
    @staticmethod
    def _print_transaction_history(title: str, transactions: list):
        """Print transaction history in formatted table."""
        print("\n" + "="*70)
        print(title)
        print("="*70)
        
        if not transactions:
            print("No transactions yet.")
            return
        
        print(f"{'#':<5} {'Date/Time':<20} {'Amount':<15} {'Balance After':<15} {'Status':<10}")
        print("-"*70)
        
        for i, trans in enumerate(transactions, start=1):
            date_str = trans['created_at'].strftime('%Y-%m-%d %H:%M:%S')
            amount = f"${trans['amount']:,.2f}"
            balance_after = f"${trans['balance_after']:,.2f}"
            status = trans['transaction_status'].capitalize()
            
            print(f"{i:<5} {date_str:<20} {amount:<15} {balance_after:<15} {status:<10}")


# -------------------------
# Menu / Main Loop
# -------------------------

def print_menu():
    """Display the ATM main menu."""
    print("\n" + "="*50)
    print("ATM MAIN MENU")
    print("="*50)
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Check Balance")
    print("4 - Deposit History")
    print("5 - Withdrawal History")
    print("6 - Balance History")
    print("7 - Export History to File")
    print("8 - Exit")
    print("="*50)


def main():
    """Main program entry point."""
    print("="*50)
    print("Welcome to ATM Database System")
    print("="*50)
    
    # Step 1: User authentication
    username = input("Enter your username: ").strip()
    
    user = ATMUser.authenticate(username, "", max_attempts=3)
    
    if not user:
        print("Authentication failed. Exiting...")
        return
    
    # Step 2: Create session
    user.create_session()
    
    # Step 3: Initialize ATM operations
    atm = ATMOperations(user)
    
    # Step 4: Main menu loop
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
            if save_option == 'y':
                atm.export_history_to_file()
        
        elif choice == "8":
            print("\n" + "="*50)
            print("Thank you for using our ATM!")
            print("="*50)
            
            # Optional: export history before exit
            save_option = input("Do you want to export your history before exiting? (y/n): ").strip().lower()
            if save_option == 'y':
                atm.export_history_to_file()
            
            # Close session
            user.close_session()
            
            print(f"Goodbye, {user.full_name}!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


# -------------------------
# Run Program
# -------------------------

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
