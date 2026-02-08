# ---------------------------------------------------------------------------
# Sets - 05: Loop Sets
# ---------------------------------------------------------------------------
# Description: Loop through set items using for loops. Since sets are
#              unordered, there is no index-based access, but you can
#              use enumerate() to get a counter.
# ---------------------------------------------------------------------------

fruits = {"apple", "banana", "cherry", "pineapple", "grape", "mango"}

# =========================================================================
# Method 1: Simple for loop
# =========================================================================
print("=== Simple for loop ===")
for fruit in fruits:
    print(f"  {fruit}")
# Note: Order is NOT guaranteed

# =========================================================================
# Method 2: for loop with enumerate() (counter + value)
# =========================================================================
print("\n=== With enumerate() ===")
for i, fruit in enumerate(fruits):
    print(f"  [{i}] {fruit}")

# With custom start
print("\n=== enumerate starting at 1 ===")
for num, fruit in enumerate(sorted(fruits), start=1):
    print(f"  {num}. {fruit}")

# =========================================================================
# Method 3: Loop through a sorted set
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

# Uppercase fruits
upper_fruits = {f.upper() for f in fruits}
print(f"Uppercase: {upper_fruits}")

# =========================================================================
# Practical examples
# =========================================================================

# Filter while looping
print("\n=== Fruits with more than 5 letters ===")
for fruit in fruits:
    if len(fruit) > 5:
        print(f"  {fruit} ({len(fruit)} letters)")

# Loop through two sets together
set_a = {"alice", "bob", "charlie"}
set_b = {"bob", "david", "alice"}

print("\n=== In both sets ===")
for item in set_a & set_b:
    print(f"  {item}")

print("\n=== Only in set_a ===")
for item in set_a - set_b:
    print(f"  {item}")

# Convert to check with while loop (less common)
print("\n=== While loop (via list) ===")
fruit_list = list(fruits)
i = 0
while i < len(fruit_list):
    print(f"  {fruit_list[i]}")
    i += 1
