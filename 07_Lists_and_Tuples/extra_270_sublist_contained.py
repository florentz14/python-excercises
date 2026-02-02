# 270. Check If First List Is Contained in Second (Regardless of Order)

def sublist_contained(sub: list, lst: list) -> bool:
    return set(sub) <= set(lst)


print(sublist_contained([1, 2], [1, 2, 3, 4]))   # True
print(sublist_contained([1, 5], [1, 2, 3, 4]))   # False
