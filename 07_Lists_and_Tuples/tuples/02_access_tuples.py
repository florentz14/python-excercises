# ---------------------------------------------------------------------------
# Tuplas - 02: Access Tuples (Acceder a Elementos)
# ---------------------------------------------------------------------------
# Description: Access tuple elements using index numbers. Positive indices
#              start at 0 from the left. Negative indices start at -1 from
#              the right. Use slicing to get a range of elements.
# Syntax:      tuple[index]  /  tuple[start:end]  /  tuple[start:end:step]
# ---------------------------------------------------------------------------

fruits = ("apple", "banana", "cherry", "pineapple", "grape", "mango", "kiwi")
#  index:   0        1         2          3           4        5        6
#  neg:    -7       -6        -5         -4          -3       -2       -1

# --- Access by positive index ---
print("First item:", fruits[0])     # apple
print("Third item:", fruits[2])     # cherry

# --- Access by negative index (from the end) ---
print("Last item:", fruits[-1])     # kiwi
print("Second to last:", fruits[-2])  # mango

# ---------------------------------------------------------------------------
# Slicing - get a range of elements (returns a new tuple)
# ---------------------------------------------------------------------------

# Slice from index 2 to 5 (5 excluded)
print("\nfruits[2:5]:", fruits[2:5])
# Output: ('cherry', 'pineapple', 'grape')

# Slice from the beginning to index 4 (4 excluded)
print("fruits[:4]:", fruits[:4])
# Output: ('apple', 'banana', 'cherry', 'pineapple')

# Slice from index 3 to the end
print("fruits[3:]:", fruits[3:])
# Output: ('pineapple', 'grape', 'mango', 'kiwi')

# Slice with negative indices (last 3 items)
print("fruits[-3:]:", fruits[-3:])
# Output: ('grape', 'mango', 'kiwi')

# Slice with step (every 2nd element)
print("fruits[::2]:", fruits[::2])
# Output: ('apple', 'cherry', 'grape', 'kiwi')

# Reverse the tuple
print("fruits[::-1]:", fruits[::-1])
# Output: ('kiwi', 'mango', 'grape', 'pineapple', 'cherry', 'banana', 'apple')

# ---------------------------------------------------------------------------
# Check if an item exists using 'in'
# ---------------------------------------------------------------------------
print("\n'cherry' in fruits:", "cherry" in fruits)   # True
print("'pear' in fruits:", "pear" in fruits)         # False
print("'pear' not in fruits:", "pear" not in fruits) # True

# ---------------------------------------------------------------------------
# Error: IndexError if index is out of range
# ---------------------------------------------------------------------------
try:
    print(fruits[10])
except IndexError as e:
    print(f"\nError: {e}")
# Output: Error: tuple index out of range
