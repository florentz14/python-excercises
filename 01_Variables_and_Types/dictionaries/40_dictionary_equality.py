# Dictionary equality and comparison

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}
dict3 = {'c': 3, 'b': 2, 'a': 1}  # same content, different order
dict4 = {'a': 1, 'b': 2, 'd': 4}

print("Dict1:", dict1)
print("Dict2:", dict2)
print("Dict3:", dict3)
print("Dict4:", dict4)

# Equality (==)
print(f"\ndict1 == dict2: {dict1 == dict2}")  # True - same content
# True - order doesn't matter (Python 3.7+)
print(f"dict1 == dict3: {dict1 == dict3}")
print(f"dict1 == dict4: {dict1 == dict4}")  # False - different content

# Inequality (!=)
print(f"\ndict1 != dict4: {dict1 != dict4}")  # True

# Identity (is)
dict5 = dict1  # reference to same object
dict6 = dict1.copy()  # new object with same content

print(f"\ndict1 is dict5: {dict1 is dict5}")  # True - same object
print(f"dict1 is dict6: {dict1 is dict6}")  # False - different objects

# Comparison with subsets
dict_small = {'a': 1, 'b': 2}
print(
    f"\nIs dict_small subset of dict1? {all(k in dict1 and dict1[k] == v for k, v in dict_small.items())}")

# Dictionary views comparison
keys1 = dict1.keys()
keys2 = dict2.keys()
print(f"\nKeys equal: {keys1 == keys2}")

values1 = dict1.values()
values2 = dict2.values()
print(f"Values equal: {values1 == values2}")

# Note: dict views are equal if their dicts are equal
# But they don't support <, > comparisons directly

# Custom comparison function


def dict_compare(d1, d2):
    """Compare dictionaries and return detailed result."""
    if d1 == d2:
        return "Equal"
    elif set(d1.keys()) == set(d2.keys()):
        return "Same keys, different values"
    elif set(d1.keys()).issubset(set(d2.keys())):
        return "d1 is subset of d2"
    elif set(d2.keys()).issubset(set(d1.keys())):
        return "d2 is subset of d1"
    else:
        return "Different keys"


print(f"\nComparison dict1 vs dict4: {dict_compare(dict1, dict4)}")
print(f"Comparison dict_small vs dict1: {dict_compare(dict_small, dict1)}")
