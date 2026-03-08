# -------------------------------------------------
# File Name: 09_check_key.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Check key existence with 'in' and 'not in' operators.
# -------------------------------------------------

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
