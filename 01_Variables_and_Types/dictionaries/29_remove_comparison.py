# Compare del, pop, popitem, clear

original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Original:", original)

# del - removes key, raises KeyError if not found
temp = original.copy()
del temp['a']
print("After del 'a':", temp)

# pop - removes and returns value, can provide default
temp = original.copy()
removed = temp.pop('b')
print(f"Popped 'b': {removed}, dict: {temp}")

removed_default = temp.pop('x', 'not found')
print(f"Pop 'x' with default: {removed_default}")

# popitem - removes and returns last item (Python 3.7+ maintains order)
temp = original.copy()
key, value = temp.popitem()
print(f"Popitem: {key}={value}, dict: {temp}")

# clear - removes all items
temp = original.copy()
temp.clear()
print("After clear:", temp)
