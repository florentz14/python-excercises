# Merge dictionaries with | (Python 3.9+)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Using | operator (Python 3.9+)
merged = dict1 | dict2
print("Merged with |:", merged)

# Using |= for in-place update
dict1_copy = dict1.copy()
dict1_copy |= dict2
print("In-place merge with |=", dict1_copy)

# Comparison with update()
dict1_update = dict1.copy()
dict1_update.update(dict2)
print("Merged with update():", dict1_update)

# Note: | creates new dict, update() modifies in place