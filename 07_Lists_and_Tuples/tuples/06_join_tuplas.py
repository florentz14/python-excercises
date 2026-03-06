# ---------------------------------------------------------------------------
# Tuplas - 06: Join Tuples (Unir Tuplas)
# ---------------------------------------------------------------------------
# Description: Tuples are immutable, but you can join (concatenate) two or
#              more tuples to create a NEW tuple using the + operator.
#              You can also multiply a tuple using the * operator.
# Syntax:      tuple3 = tuple1 + tuple2
#              repeated = tuple1 * n
# ---------------------------------------------------------------------------

# =========================================================================
# Concatenate tuples with +
# =========================================================================

tuple1 = ("apple", "banana", "cherry")
tuple2 = ("mango", "grape", "kiwi")

# Join two tuples
tuple3 = tuple1 + tuple2
print("tuple1 + tuple2:", tuple3)
# Output: ('apple', 'banana', 'cherry', 'mango', 'grape', 'kiwi')

# Originals are unchanged (tuples are immutable)
print("tuple1:", tuple1)  # ('apple', 'banana', 'cherry')
print("tuple2:", tuple2)  # ('mango', 'grape', 'kiwi')

# Join multiple tuples
letters = ("a", "b") + ("c", "d") + ("e", "f")
print("\nMultiple join:", letters)
# Output: ('a', 'b', 'c', 'd', 'e', 'f')

# Add a single item (must use trailing comma)
fruits = ("apple", "banana")
fruits = fruits + ("orange",)
print("Add single item:", fruits)
# Output: ('apple', 'banana', 'orange')

# =========================================================================
# Multiply (repeat) tuples with *
# =========================================================================

# Repeat a tuple
greet = ("Hello!",)
repeated = greet * 3
print("\n('Hello!',) * 3:", repeated)
# Output: ('Hello!', 'Hello!', 'Hello!')

# Repeat a multi-element tuple
pattern = (0, 1)
repeated_pattern = pattern * 4
print("(0, 1) * 4:", repeated_pattern)
# Output: (0, 1, 0, 1, 0, 1, 0, 1)

# Create a tuple of zeros
zeros = (0,) * 10
print("(0,) * 10:", zeros)
# Output: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# =========================================================================
# Practical examples
# =========================================================================

# Build a tuple incrementally
result = ()
for i in range(5):
    result = result + (i ** 2,)
print("\nSquares tuple:", result)
# Output: (0, 1, 4, 9, 16)

# Merge coordinate points
point_x = (1, 2, 3)
point_y = (4, 5, 6)
all_points = point_x + point_y
print("All points:", all_points)

# Note: for better performance with many items, use a list and convert
items = []
for i in range(5):
    items.append(i * 10)
final_tuple = tuple(items)
print("From list:", final_tuple)
# Output: (0, 10, 20, 30, 40)
