# 17_simple_cuenta.py - Simple class: Account (bank account)
# Florentino Baez - ITSE-1002

class Account:
    """Class with mutable state (bank balance)."""
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return f"{self.holder}: ${self.balance}"

# Short list of bank accounts
accounts = [
    Account("John", 1000),
    Account("Jane", 500),
    Account("Mike", 2500),
]

# Usage: deposit and show balance
accounts[1].deposit(200)
for a in accounts:
    print(a.get_balance())
