# -------------------------------------------------
# File Name: 11_copy.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Copy a Dictionary.
#              copy() creates a shallow copy, so changes to
#              the copy do not affect the original (for simple
#              values). Nested mutable objects are still shared.
# -------------------------------------------------

# Example 11: Copy dictionary
print("Example 11: Copy dictionary")
print("-" * 40)

original = {"a": 1, "b": 2, "c": 3}
copy_dict = original.copy()             # Shallow copy of the dictionary
print("Original:", original)
print("Copy:", copy_dict)

copy_dict["a"] = 100                    # Modify the copy only
print("After modifying copy:")
print("Original:", original)            # Original remains unchanged
print("Copy:", copy_dict)               # Only the copy is modified
