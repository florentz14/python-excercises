# -------------------------------------------------
# File Name: 12_clear.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Clear a Dictionary.
#              clear() removes all key-value pairs, leaving
#              an empty dictionary {}. The dict object itself
#              still exists in memory.
# -------------------------------------------------

# Example 12: Clear dictionary
print("Example 12: Clear dictionary")
print("-" * 40)

temp_dict = {"x": 10, "y": 20, "z": 30}
print("Before clear:", temp_dict)

temp_dict.clear()                        # Remove all items from the dictionary
print("After clear:", temp_dict)         # Now an empty dict {}
