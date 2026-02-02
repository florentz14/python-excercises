# 154. Join Two Lists of Lists Element-Wise (concatenate corresponding sublists)

def join_lists_element_wise(a: list[list], b: list[list]) -> list[list]:
    return [x + y for x, y in zip(a, b)]


list1 = [[10, 20], [30, 40], [50, 60]]
list2 = [[61], [12, 14, 15], [12, 13, 19, 20]]
print(join_lists_element_wise(list1, list2))
