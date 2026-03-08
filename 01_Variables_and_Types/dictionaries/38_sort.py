# -------------------------------------------------
# File Name: 38_sort.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Sort dict by keys or values using sorted() with key=lambda.
# -------------------------------------------------

original = {'c': 3, 'a': 1, 'b': 2, 'd': 4}
print("Original:", original)

# Sort by keys
sorted_by_keys = dict(sorted(original.items()))
print("Sorted by keys:", sorted_by_keys)

# Sort by values
sorted_by_values = dict(sorted(original.items(), key=lambda x: x[1]))
print("Sorted by values:", sorted_by_values)

# Sort by values descending
sorted_by_values_desc = dict(
    sorted(original.items(), key=lambda x: x[1], reverse=True))
print("Sorted by values desc:", sorted_by_values_desc)

# Sort by key length
data = {'short': 1, 'very_long_key': 2, 'medium': 3}
sorted_by_key_len = dict(sorted(data.items(), key=lambda x: len(x[0])))
print("Sorted by key length:", sorted_by_key_len)

# Note: sorted() returns list of tuples, dict() converts back
# Original dict is unchanged
