# -------------------------------------------------
# File Name: 13_zip_two_lists_of_lists.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Zip Two Lists of Lists (concatenate corresponding inner lists)
# -------------------------------------------------

def zip_lists_of_lists(a: list[list], b: list[list]) -> list[list]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [x + y for x, y in zip(a, b)]


list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]
print(zip_lists_of_lists(list1, list2))
