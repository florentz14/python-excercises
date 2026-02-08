# ---------------------------------------------------------------------------
# Sets - 02: Access Set Items
# ---------------------------------------------------------------------------
# Description: You CANNOT access set items by index or key because sets
#              are unordered. However, you can check if an item exists
#              using 'in', loop through the set, or convert it to a list.
# ---------------------------------------------------------------------------

fruits = {"apple", "banana", "cherry", "pineapple", "grape", "mango"}

# =========================================================================
# You CANNOT access by index (sets have no index)
# =========================================================================
try:
    print(fruits[0])  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")
# Output: Error: 'set' object is not subscriptable

# =========================================================================
# Check if an item EXISTS using 'in'
# =========================================================================
print("\n'banana' in fruits:", "banana" in fruits)     # True
print("'pear' in fruits:", "pear" in fruits)           # False
print("'pear' not in fruits:", "pear" not in fruits)   # True

# Use in conditional statements
search = "cherry"
if search in fruits:
    print(f"\n'{search}' is available!")
else:
    print(f"\n'{search}' is NOT available")

# =========================================================================
# Loop through the set to access items
# =========================================================================
print("\nAll fruits:")
for fruit in fruits:
    print(f"  - {fruit}")
# Note: Order is not guaranteed

# =========================================================================
# Convert to list to access by index
# =========================================================================
fruits_list = list(fruits)
print(f"\nAs list: {fruits_list}")
print(f"First item (from list): {fruits_list[0]}")
# Note: The "first" item may vary since sets are unordered

# Convert to sorted list for predictable order
sorted_fruits = sorted(fruits)
print(f"Sorted: {sorted_fruits}")
print(f"First alphabetically: {sorted_fruits[0]}")

# =========================================================================
# Other ways to get information from a set
# =========================================================================
numbers = {34, 12, 89, 5, 67, 23}

print(f"\nSet: {numbers}")
print(f"Length: {len(numbers)}")    # 6
print(f"Min: {min(numbers)}")      # 5
print(f"Max: {max(numbers)}")      # 89
print(f"Sum: {sum(numbers)}")      # 230

# Check if set is empty
empty = set()
if not empty:
    print("\nThe set is empty")
