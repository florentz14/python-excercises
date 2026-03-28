# -------------------------------------------------
# File Name: user_class.py
# Author: Florentino
# Date: 3/20/26
# Description: User class with email getter and setter methods.
# -------------------------------------------------

import sys
from pathlib import Path

_EXAMPLES_ROOT = Path(__file__).resolve().parent.parent
if str(_EXAMPLES_ROOT) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES_ROOT))

from datetime import datetime
from utils import is_valid_email

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    
    def get_email(self):
        print(f"Accessed at: {datetime.now()}")
        return self._email
    
    def set_email(self, new_email):
        if is_valid_email(new_email):
            self._email = new_email
            print(f"Email updated successfully to: {new_email}")
        else:
            print("Invalid email format")

# Example usage
user1 = User("dantheman", "dan@gmail.com", "123")
print(user1.get_email())

# Test email validation
print("\n=== Testing Email Validation ===")
user1.set_email("newemail@domain.com")  # Valid email
print(user1.get_email())

user1.set_email("invalid-email")  # Invalid email
print(user1.get_email())

user1.set_email("another.valid@email.org")  # Valid email
print(user1.get_email())
