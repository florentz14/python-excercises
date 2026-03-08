# -------------------------------------------------
# File Name: 11_copy.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Shallow copy with copy(). Simple values isolated;
# -------------------------------------------------

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
