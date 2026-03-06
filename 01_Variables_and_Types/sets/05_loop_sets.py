# -------------------------------------------------
# File Name: 05_loop_sets.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Loop Through Sets.
#              Iterate using for loops, enumerate(), sorted(),
#              and set comprehensions. Also shows filtering,
#              set intersection/difference in loops, and
#              while loop via list conversion.
# -------------------------------------------------

fruits = {"apple", "banana", "cherry", "pineapple", "grape", "mango"}

# =========================================================================
# Method 1: Simple for loop (order is NOT guaranteed)
# =========================================================================
print("=== Simple for loop ===")
for fruit in fruits:
    print(f"  {fruit}")

# =========================================================================
# Method 2: for loop with enumerate() for a counter
# =========================================================================
print("\n=== With enumerate() ===")
for i, fruit in enumerate(fruits):
    print(f"  [{i}] {fruit}")

# With custom start index
print("\n=== enumerate starting at 1 ===")
for num, fruit in enumerate(sorted(fruits), start=1):
    print(f"  {num}. {fruit}")

# =========================================================================
# Method 3: Loop through a sorted set for predictable order
# =========================================================================
print("\n=== Sorted loop ===")
for fruit in sorted(fruits):
    print(f"  {fruit}")
# Output: alphabetical order (predictable)

# =========================================================================
# Method 4: Set comprehension (create new set while looping)
# =========================================================================
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Create a new set with squares of even numbers
even_squares = {x**2 for x in numbers if x % 2 == 0}
print(f"\nEven squares: {even_squares}")
# Output: {4, 16, 36, 64, 100}

# Uppercase all fruit names using comprehension
upper_fruits = {f.upper() for f in fruits}
print(f"Uppercase: {upper_fruits}")

# =========================================================================
# Practical examples
# =========================================================================

# Filter while looping: only fruits with more than 5 letters
print("\n=== Fruits with more than 5 letters ===")
for fruit in fruits:
    if len(fruit) > 5:
        print(f"  {fruit} ({len(fruit)} letters)")

# Loop through set operations (intersection & difference)
set_a = {"alice", "bob", "charlie"}
set_b = {"bob", "david", "alice"}

print("\n=== In both sets (intersection) ===")
for item in set_a & set_b:           # & = intersection
    print(f"  {item}")

print("\n=== Only in set_a (difference) ===")
for item in set_a - set_b:           # - = difference
    print(f"  {item}")

# While loop via list conversion (less common with sets)
print("\n=== While loop (via list) ===")
fruit_list = list(fruits)
i = 0
while i < len(fruit_list):
    print(f"  {fruit_list[i]}")
    i += 1
