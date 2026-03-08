# -------------------------------------------------
# File Name: 39_deep_flatten.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Deep Flatten List (any nesting level)
# -------------------------------------------------

def deep_flatten(lst: list) -> list:
    result = []
    for x in lst:
        if isinstance(x, list):
            # Si es lista se aplana recursivamente; si no, se añade el elemento.
            result.extend(deep_flatten(x))
        else:
            result.append(x)
    return result


print(deep_flatten([1, [2], [[3], [4], 5], 6]))
print(deep_flatten([[[1, 2, 3], [4, 5]], 6]))
