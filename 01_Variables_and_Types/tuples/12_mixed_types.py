# -------------------------------------------------
# File Name: 12_mixed_types.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Tuple with Mixed Data Types.
#              A single tuple can hold int, str, float,
#              bool, and None. Use enumerate() to loop
#              with both index and value.
# -------------------------------------------------

print("Example 12: Tuple with mixed data types")
print("-" * 40)

# Tuples can store elements of different types
mixed = (10, "hello", 3.14, True, None)
print("Mixed tuple:", mixed)

# enumerate() gives both the index and the value
for index, item in enumerate(mixed):
    print(f"Index {index}: {item} (type: {type(item).__name__})")
