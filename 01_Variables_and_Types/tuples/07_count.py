# -------------------------------------------------
# File Name: 07_count.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Count Occurrences with count().
# -------------------------------------------------

print("Example 7: Count occurrences")
print("-" * 40)

repeated_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
print("Tuple:", repeated_tuple)

print("Count of 2:", repeated_tuple.count(2))   # 2 appears twice
print("Count of 4:", repeated_tuple.count(4))   # 4 appears four times
