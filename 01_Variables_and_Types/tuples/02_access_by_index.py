# -------------------------------------------------
# File Name: 02_access_by_index.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Access Tuple Elements by Index.
#              Tuples support zero-based indexing (0, 1, 2…)
#              and negative indexing (-1 = last, -2 = second
#              to last). Access with tuple[index].
# -------------------------------------------------

print("Example 2: Access tuple elements by index")
print("-" * 40)

fruits = ("apple", "banana", "cherry", "date", "elderberry")

print("First element:", fruits[0])       # Index 0 = first item
print("Last element:", fruits[-1])       # Index -1 = last item
print("Third element:", fruits[2])       # Index 2 = third item
