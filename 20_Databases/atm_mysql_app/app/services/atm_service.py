from __future__ import annotations

from datetime import datetime

from atm_mysql_app.app.database import DatabaseConnection
from atm_mysql_app.app.models.user import ATMUser


class ATMOperations:
    """Handles all ATM operations with database integration."""

    def __init__(self, user: ATMUser):
        self.user = user

    def deposit(self) -> bool:
        amount = self._get_positive_amount("Enter amount to deposit: $")
        try:
            with DatabaseConnection() as db:
                args = (self.user.user_id, self.user.session_id, amount, 0, 0)
                result = db.cursor.callproc("sp_make_deposit", args)
                db.commit()
                new_balance = result[3]
                transaction_id = result[4]
                self.user.current_balance = float(new_balance)
                print("\n[OK] Deposit successful!")
                print(f"  Amount: ${amount:,.2f}")
                print(f"  New balance: ${new_balance:,.2f}")
                print(f"  Transaction ID: {transaction_id}")
                return True
        except Exception as exc:
            print(f"Deposit failed: {exc}")
            return False

    def withdraw(self) -> bool:
        amount = self._get_positive_amount("Enter amount to withdraw: $")
        try:
            with DatabaseConnection() as db:
                args = (self.user.user_id, self.user.session_id, amount, 0, 0, False, "")
                result = db.cursor.callproc("sp_make_withdrawal", args)
                db.commit()
                new_balance = result[3]
                transaction_id = result[4]
                success = result[5]
                message = result[6]
                if success:
                    self.user.current_balance = float(new_balance)
                    print("\n[OK] Withdrawal successful!")
                    print(f"  Amount: ${amount:,.2f}")
                    print(f"  New balance: ${new_balance:,.2f}")
                    print(f"  Transaction ID: {transaction_id}")
                    return True
                print(f"\n[ERROR] Withdrawal denied: {message}")
                return False
        except Exception as exc:
            print(f"Withdrawal failed: {exc}")
            return False

    def check_balance(self):
        print(f"\n{'=' * 50}")
        print(f"Current Balance: ${self.user.current_balance:,.2f}")
        print(f"{'=' * 50}")

    def show_deposit_history(self):
        try:
            with DatabaseConnection() as db:
                db.cursor.callproc("sp_get_deposit_history", (self.user.user_id,))
                deposits = []
                for result in db.cursor.stored_results():
                    deposits = result.fetchall()
                self._print_transaction_history("Deposit History", deposits)
        except Exception as exc:
            print(f"Error retrieving deposit history: {exc}")

    def show_withdrawal_history(self):
        try:
            with DatabaseConnection() as db:
                db.cursor.callproc("sp_get_withdrawal_history", (self.user.user_id,))
                withdrawals = []
                for result in db.cursor.stored_results():
                    withdrawals = result.fetchall()
                self._print_transaction_history("Withdrawal History", withdrawals)
        except Exception as exc:
            print(f"Error retrieving withdrawal history: {exc}")

    def show_balance_history(self):
        try:
            with DatabaseConnection() as db:
                db.cursor.callproc("sp_get_balance_history", (self.user.user_id,))
                snapshots = []
                for result in db.cursor.stored_results():
                    snapshots = result.fetchall()
                print("\n" + "=" * 70)
                print("Balance History (after each transaction)")
                print("=" * 70)
                if not snapshots:
                    print("No balance changes yet.")
                    return
                print(f"{'#':<5} {'Date/Time':<20} {'Type':<12} {'Amount':<15} {'Balance':<15}")
                print("-" * 70)
                for i, snap in enumerate(snapshots, start=1):
                    date_str = snap["created_at"].strftime("%Y-%m-%d %H:%M:%S")
                    trans_type = snap["transaction_type"].capitalize()
                    amount = f"${snap['amount']:,.2f}"
                    balance = f"${snap['balance']:,.2f}"
                    print(f"{i:<5} {date_str:<20} {trans_type:<12} {amount:<15} {balance:<15}")
        except Exception as exc:
            print(f"Error retrieving balance history: {exc}")

    def export_history_to_file(self) -> bool:
        try:
            filename = f"atm_history_{self.user.username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with DatabaseConnection() as db:
                query = """
                    SELECT transaction_type, amount, balance_after, created_at, transaction_status
                    FROM atm_transactions
                    WHERE id_user = %s
                    ORDER BY created_at ASC
                """
                db.execute(query, (self.user.user_id,))
                transactions = db.cursor.fetchall()
                with open(filename, "w", encoding="utf-8") as file:
                    file.write("=" * 70 + "\n")
                    file.write(f"ATM SESSION HISTORY - {self.user.full_name}\n")
                    file.write(f"Username: {self.user.username}\n")
                    file.write(f"Exported at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.write("=" * 70 + "\n\n")
                    deposits = [t for t in transactions if t["transaction_type"] == "deposit"]
                    withdrawals = [t for t in transactions if t["transaction_type"] == "withdrawal"]
                    file.write("DEPOSIT HISTORY:\n")
                    file.write("-" * 70 + "\n")
                    if deposits:
                        for i, dep in enumerate(deposits, start=1):
                            file.write(f"{i}. ${dep['amount']:,.2f} - {dep['created_at']}\n")
                    else:
                        file.write("No deposits.\n")
                    file.write("\n")
                    file.write("WITHDRAWAL HISTORY:\n")
                    file.write("-" * 70 + "\n")
                    if withdrawals:
                        for i, wit in enumerate(withdrawals, start=1):
                            status = f" [{wit['transaction_status']}]" if wit["transaction_status"] != "completed" else ""
                            file.write(f"{i}. ${wit['amount']:,.2f}{status} - {wit['created_at']}\n")
                    else:
                        file.write("No withdrawals.\n")
                    file.write("\n")
                    file.write("BALANCE HISTORY:\n")
                    file.write("-" * 70 + "\n")
                    if transactions:
                        for i, trans in enumerate(transactions, start=1):
                            file.write(f"{i}. ${trans['balance_after']:,.2f} - {trans['created_at']}\n")
                    else:
                        file.write("No balance changes.\n")
                    file.write("\n")
                    total_deposited = sum(t["amount"] for t in deposits)
                    total_withdrawn = sum(t["amount"] for t in withdrawals if t["transaction_status"] == "completed")
                    file.write("=" * 70 + "\n")
                    file.write("SUMMARY:\n")
                    file.write(f"Total Deposits: ${total_deposited:,.2f}\n")
                    file.write(f"Total Withdrawals: ${total_withdrawn:,.2f}\n")
                    file.write(f"Current Balance: ${self.user.current_balance:,.2f}\n")
                    file.write("=" * 70 + "\n")
                export_query = """
                    INSERT INTO atm_history_exports
                    (id_user, id_session, filename, export_type, total_deposits, total_withdrawals)
                    VALUES (%s, %s, %s, 'full_history', %s, %s)
                """
                db.execute(
                    export_query,
                    (self.user.user_id, self.user.session_id, filename, len(deposits), len(withdrawals)),
                )
                db.commit()
                print(f"\n[OK] History exported successfully to: {filename}")
                return True
        except Exception as exc:
            print(f"Error exporting history: {exc}")
            return False

    @staticmethod
    def _get_positive_amount(prompt: str) -> float:
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
        print("\n" + "=" * 70)
        print(title)
        print("=" * 70)
        if not transactions:
            print("No transactions yet.")
            return
        print(f"{'#':<5} {'Date/Time':<20} {'Amount':<15} {'Balance After':<15} {'Status':<10}")
        print("-" * 70)
        for i, trans in enumerate(transactions, start=1):
            date_str = trans["created_at"].strftime("%Y-%m-%d %H:%M:%S")
            amount = f"${trans['amount']:,.2f}"
            balance_after = f"${trans['balance_after']:,.2f}"
            status = trans["transaction_status"].capitalize()
            print(f"{i:<5} {date_str:<20} {amount:<15} {balance_after:<15} {status:<10}")
