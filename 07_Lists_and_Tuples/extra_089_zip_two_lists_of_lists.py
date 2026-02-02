# 89. Zip Two Lists of Lists (concatenate corresponding inner lists)

def zip_lists_of_lists(a: list[list], b: list[list]) -> list[list]:
    return [x + y for x, y in zip(a, b)]


list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]
print(zip_lists_of_lists(list1, list2))
