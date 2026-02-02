# 257. Check If Two Lists Have Same Elements (Regardless of Order)

def same_elements(a: list, b: list) -> bool:
    return len(a) == len(b) and set(a) == set(b)


print(same_elements([1, 2, 4], [2, 4, 1]))  # True
print(same_elements([1, 2, 3], [1, 2, 4]))  # False
