# 117. Remove All Elements Present in Another List

def remove_if_in(list1: list, list2: list) -> list:
    set2 = set(list2)
    return [x for x in list1 if x not in set2]


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
print(remove_if_in(list1, list2))  # [1, 3, 5, 7, 9, 10]
