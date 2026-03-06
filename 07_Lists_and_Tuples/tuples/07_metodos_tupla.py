# ---------------------------------------------------------------------------
# Tuplas - 07: Tuple Methods (Metodos de Tupla)
# ---------------------------------------------------------------------------
# Description: Tuples have only TWO built-in methods: count() and index().
#              This is because tuples are immutable - methods that modify
#              (like append, remove, sort) are not available.
# Methods:     tuple.count(value)  /  tuple.index(value)
# ---------------------------------------------------------------------------

fruits = ("apple", "banana", "cherry", "banana", "grape", "banana", "kiwi")
print("Tuple:", fruits)

# =========================================================================
# count() - Returns the number of times a value appears
# =========================================================================

# Count occurrences of "banana"
banana_count = fruits.count("banana")
print(f"\n'banana' appears {banana_count} times")
# Output: 'banana' appears 3 times

# Count a value that doesn't exist
pear_count = fruits.count("pear")
print(f"'pear' appears {pear_count} times")
# Output: 'pear' appears 0 times

# Count with numbers
numbers = (1, 3, 7, 3, 8, 3, 2, 3, 9)
print(f"\n3 appears {numbers.count(3)} times in {numbers}")
# Output: 3 appears 4 times

# =========================================================================
# index() - Returns the index of the FIRST occurrence of a value
# =========================================================================

# Find the index of "cherry"
cherry_index = fruits.index("cherry")
print(f"\n'cherry' is at index: {cherry_index}")
# Output: 'cherry' is at index: 2

# Find the first "banana"
banana_index = fruits.index("banana")
print(f"First 'banana' at index: {banana_index}")
# Output: First 'banana' at index: 1

# Search starting from a specific index
banana_second = fruits.index("banana", 2)  # Start searching from index 2
print(f"Second 'banana' at index: {banana_second}")
# Output: Second 'banana' at index: 3

# Search within a range (start, end)
banana_third = fruits.index("banana", 4, 7)  # Search from index 4 to 6
print(f"Third 'banana' at index: {banana_third}")
# Output: Third 'banana' at index: 5

# ---------------------------------------------------------------------------
# Error: ValueError if the value is not found
# ---------------------------------------------------------------------------
try:
    fruits.index("pear")
except ValueError as e:
    print(f"\nError: {e}")
# Output: Error: tuple.index(x): x not in tuple

# Safe search: check before using index()
search = "grape"
if search in fruits:
    print(f"'{search}' found at index {fruits.index(search)}")
else:
    print(f"'{search}' not in tuple")

# =========================================================================
# Other useful operations (not methods, but built-in functions)
# =========================================================================
numbers = (34, 12, 89, 5, 67, 23, 45)
print(f"\nTuple: {numbers}")
print(f"  len():    {len(numbers)}")      # 7
print(f"  min():    {min(numbers)}")      # 5
print(f"  max():    {max(numbers)}")      # 89
print(f"  sum():    {sum(numbers)}")      # 275
print(f"  sorted(): {sorted(numbers)}")   # [5, 12, 23, 34, 45, 67, 89] (returns list!)

# Convert sorted result back to tuple
sorted_tuple = tuple(sorted(numbers))
print(f"  As tuple: {sorted_tuple}")

# ---------------------------------------------------------------------------
# Summary:
# | Method   | Description                              |
# |----------|------------------------------------------|
# | count()  | Returns count of specified value          |
# | index()  | Returns index of first specified value    |
#
# That's it! Only 2 methods because tuples are immutable.
# For more functionality, convert to a list first.
# ---------------------------------------------------------------------------
