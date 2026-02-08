# -------------------------------------------------
# File Name: 02_access_set_items.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Access Set Items.
#              Sets do NOT support indexing (no set[0]).
#              Use 'in' for membership testing, loop to
#              iterate, or convert to list for index access.
#              Also shows min(), max(), sum(), len().
# -------------------------------------------------

fruits = {"apple", "banana", "cherry", "pineapple", "grape", "mango"}

# =========================================================================
# You CANNOT access by index (sets have no index)
# =========================================================================
try:
    print(fruits[0])  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")
# Output: Error: 'set' object is not subscriptable

# =========================================================================
# Check if an item EXISTS using 'in' (O(1) average time)
# =========================================================================
print("\n'banana' in fruits:", "banana" in fruits)     # True
print("'pear' in fruits:", "pear" in fruits)           # False
print("'pear' not in fruits:", "pear" not in fruits)   # True

# Use 'in' within conditional statements
search = "cherry"
if search in fruits:
    print(f"\n'{search}' is available!")
else:
    print(f"\n'{search}' is NOT available")

# =========================================================================
# Loop through the set to access items one by one
# =========================================================================
print("\nAll fruits:")
for fruit in fruits:
    print(f"  - {fruit}")
# Note: Order is not guaranteed

# =========================================================================
# Convert to list to enable index-based access
# =========================================================================
fruits_list = list(fruits)
print(f"\nAs list: {fruits_list}")
print(f"First item (from list): {fruits_list[0]}")
# Note: The "first" item may vary since sets are unordered

# Convert to sorted list for predictable, alphabetical order
sorted_fruits = sorted(fruits)
print(f"Sorted: {sorted_fruits}")
print(f"First alphabetically: {sorted_fruits[0]}")

# =========================================================================
# Aggregate functions work on sets of numbers
# =========================================================================
numbers = {34, 12, 89, 5, 67, 23}

print(f"\nSet: {numbers}")
print(f"Length: {len(numbers)}")    # 6
print(f"Min: {min(numbers)}")       # 5
print(f"Max: {max(numbers)}")       # 89
print(f"Sum: {sum(numbers)}")       # 230

# Check if set is empty using truthiness (empty set is falsy)
empty = set()
if not empty:
    print("\nThe set is empty")
