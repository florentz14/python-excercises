# -------------------------------------------------
# File Name: 09_all_true_for_function.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Check If Function Returns True for Every Element
# -------------------------------------------------

def all_match(lst: list, predicate) -> bool:
    return all(predicate(x) for x in lst)


print(all_match([1, 2, 3, 4], lambda x: x > 0))   # True
print(all_match([1, 2, 3, 4], lambda x: x > 2))   # False
