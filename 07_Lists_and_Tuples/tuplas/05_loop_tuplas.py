# ---------------------------------------------------------------------------
# Tuplas - 05: Loop Tuples (Recorrer Tuplas)
# ---------------------------------------------------------------------------
# Description: You can loop through tuple items using for loops,
#              while loops, or index-based iteration with range().
# ---------------------------------------------------------------------------

fruits = ("apple", "banana", "cherry", "pineapple", "grape", "mango")

# =========================================================================
# Method 1: for loop (direct iteration)
# =========================================================================
print("=== for loop (direct) ===")
for fruit in fruits:
    print(f"  {fruit}")
# Output: apple, banana, cherry, pineapple, grape, mango

# =========================================================================
# Method 2: for loop with index using range(len())
# =========================================================================
print("\n=== for loop with range(len()) ===")
for i in range(len(fruits)):
    print(f"  [{i}] {fruits[i]}")

# =========================================================================
# Method 3: for loop with enumerate() (index + value)
# =========================================================================
print("\n=== for loop with enumerate() ===")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# enumerate with custom start number
print("\n=== enumerate starting at 1 ===")
for num, fruit in enumerate(fruits, start=1):
    print(f"  {num}. {fruit}")

# =========================================================================
# Method 4: while loop
# =========================================================================
print("\n=== while loop ===")
i = 0
while i < len(fruits):
    print(f"  {fruits[i]}")
    i += 1

# =========================================================================
# Practical examples
# =========================================================================

# Filter while looping
print("\n=== Fruits with more than 5 letters ===")
for fruit in fruits:
    if len(fruit) > 5:
        print(f"  {fruit} ({len(fruit)} letters)")
# Output: banana (6), cherry (6), pineapple (9)

# Loop through a tuple of tuples
students = (("Alice", 90), ("Bob", 85), ("Charlie", 92))
print("\n=== Student grades ===")
for name, grade in students:
    status = "PASS" if grade >= 70 else "FAIL"
    print(f"  {name}: {grade} -> {status}")

# Sum elements in a tuple
numbers = (10, 20, 30, 40, 50)
total = 0
for num in numbers:
    total += num
print(f"\nSum of {numbers} = {total}")

# Or simply use sum()
print(f"Using sum(): {sum(numbers)}")
