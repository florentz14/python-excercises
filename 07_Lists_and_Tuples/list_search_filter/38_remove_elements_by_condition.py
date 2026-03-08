# -------------------------------------------------
# File Name: 38_remove_elements_by_condition.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Remove First n Elements Satisfying Condition (e.g. first 4 even num...
# -------------------------------------------------

def remove_first_n_matching(lst: list, n: int, condition) -> list:
    result = []
    count = 0
    for x in lst:
        if count < n and condition(x):
            count += 1
        else:
            result.append(x)
    return result


sample = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
print(remove_first_n_matching(sample, 4, lambda x: x % 2 == 0))
