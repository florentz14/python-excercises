# -------------------------------------------------
# File Name: 27_list_flatten.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Flattens nested lists recursively and using
# -------------------------------------------------

def flatten(lst):
    """Flatten a nested list."""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested = [1, [2, [3, 4], 5], 6]
print("Nested:", nested)
print("Flattened:", flatten(nested))

# Using itertools.chain
import itertools
print("Flattened (itertools):", list(itertools.chain.from_iterable(nested)))