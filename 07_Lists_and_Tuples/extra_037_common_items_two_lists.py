# 37. Find Common Items in Two Lists

def common_items(a: list, b: list) -> list:
    return list(set(a) & set(b))


print(common_items([1, 2, 3], [2, 3, 4]))  # [2, 3]
