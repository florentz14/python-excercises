# -------------------------------------------------
# File Name: 09_check_key_exists.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Check if a Key Exists in a Dictionary.
#              Use 'key in dict' to test membership.
#              Returns True if the key is present, False
#              otherwise. Use 'not in' for the inverse check.
# -------------------------------------------------

# Example 9: Check if key exists
print("Example 9: Check if key exists")
print("-" * 40)

settings = {"theme": "dark", "language": "English", "notifications": True}
print("Dictionary:", settings)

# 'in' checks if the key exists in the dictionary (O(1) lookup)
if "theme" in settings:
    print("'theme' is in the dictionary")

# 'not in' checks for absence of a key
if "password" not in settings:
    print("'password' is not in the dictionary")
