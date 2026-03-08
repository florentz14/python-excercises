# -------------------------------------------------
# File Name: 035_concatenate_elements.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Concatenate Elements of a List
# -------------------------------------------------

def concat_elements(lst: list, sep: str = '') -> str:
    return sep.join(str(x) for x in lst)


print(concat_elements(['a', 'b', 'c']))       # abc
print(concat_elements([1, 2, 3], '-'))        # 1-2-3
