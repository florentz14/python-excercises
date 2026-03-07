# Dictionary unpacking with **

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merge dictionaries
merged = {**dict1, **dict2}
print("Merged with **:", merged)

# Override values
dict3 = {'a': 10, 'e': 5}
overridden = {**dict1, **dict3}
print("Overridden:", overridden)

# Function arguments


def func(a, b, c=0):
    return a + b + c


args = {'a': 1, 'b': 2, 'c': 3}
result = func(**args)
print("Function call with **:", result)

# Partial override
defaults = {'c': 100}
custom = {'a': 5, 'b': 10}
call_args = {**defaults, **custom}
result2 = func(**call_args)
print("With defaults:", result2)

# Creating new dict with modifications
original = {'x': 1, 'y': 2, 'z': 3}
modified = {**original, 'y': 20, 'w': 4}
print("Modified copy:", modified)
print("Original unchanged:", original)
