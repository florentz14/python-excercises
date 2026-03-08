# -------------------------------------------------
# File Name: 03_get.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Use get() for safe access without KeyError.
# -------------------------------------------------

print("Example 3: Use get() method")
print("-" * 40)

# --- Single user with password key ---
user = {
    "username": "johndoe",
    "email": "john@example.com",
    "password": "s3cur3P@ss",
    "active": True
}
print("Single user:", user)
print("Username:", user.get("username"))          # Key exists -> returns value
print("Password:", user.get("password"))          # Key exists -> returns value
print("Phone (not exists):", user.get("phone", "Not provided"))  # Key missing -> returns default

print()

# --- Multiple records using a list of dictionaries ---
print("Multiple users:")
print("-" * 40)

# A list of dicts allows storing multiple records with the same structure
users = [
    {"username": "johndoe",  "email": "john@example.com",  "password": "s3cur3P@ss",  "active": True},
    {"username": "janedoe",  "email": "jane@example.com",  "password": "J@ne1234",    "active": True},
    {"username": "bobsmith", "email": "bob@example.com",   "password": "b0bRocks!",   "active": False},
]

# Iterate over each user record using enumerate for numbering
for i, u in enumerate(users, start=1):
    print(f"  User {i}: {u.get('username')} | Email: {u.get('email')} | Active: {u.get('active')}")

# --- Safe access with get() on each record ---
print()
print("Check 'phone' key on every user (does not exist):")
for u in users:
    # get() with default avoids KeyError when key is missing
    print(f"  {u.get('username')}: phone = {u.get('phone', 'Not provided')}")
