# -------------------------------------------------
# File Name: 20_nested_mixed.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Mixed structures: dicts with lists, lists of dicts.
# -------------------------------------------------

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
    },
    "users": [
        {"id": 1, "name": "Admin", "role": "admin"},
        {"id": 2, "name": "User1", "role": "user"},
    ],
    "features": ["auth", "logging", "cache"],
}

print("Mixed Nested Structures")
print("-" * 40)

# Dict with nested dict
print("Database host:", config["database"]["host"])

# Dict with list of dicts
print("\nUsers (list of dicts):")
for user in config["users"]:
    print(f"  {user['name']} ({user['role']})")

# Dict with list of strings
print("\nFeatures:", config["features"])
