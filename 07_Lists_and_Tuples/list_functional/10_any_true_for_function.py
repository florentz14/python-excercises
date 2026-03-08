# -------------------------------------------------
# File Name: 10_any_true_for_function.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Check If Function Returns True for At Least One Element
# -------------------------------------------------

def any_match(lst: list, predicate) -> bool:
    return any(predicate(x) for x in lst)


print(any_match([1, 2, 3, 4], lambda x: x > 3))   # True
print(any_match([1, 2, 3], lambda x: x > 5))      # False
