# -------------------------------------------------
# File Name: 12_clear.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Remove all items with clear(), leaving empty dict {}.
# -------------------------------------------------

print("Example 12: Clear dictionary")
print("-" * 40)

temp_dict = {"x": 10, "y": 20, "z": 30}
print("Before clear:", temp_dict)

temp_dict.clear()                        # Remove all items from the dictionary
print("After clear:", temp_dict)         # Now an empty dict {}
