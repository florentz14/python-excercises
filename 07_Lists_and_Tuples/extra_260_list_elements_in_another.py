# 260. Check If All Elements of List Are in Another List

def all_in(list1: list, list2: list) -> bool:
    return all(x in list2 for x in list1)


print(all_in([1, 2, 3], [1, 2, 3, 4, 5]))  # True
print(all_in([1, 2, 6], [1, 2, 3, 4, 5]))  # False
