# 176. Create New List by Dividing Two Lists Element-Wise

def divide_lists(a: list[float], b: list[float]) -> list[float]:
    return [a[i] / b[i] if b[i] != 0 else 0 for i in range(min(len(a), len(b)))]


list1 = [7, 2, 3, 4, 9, 2, 3]
list2 = [7, 2, 3, 4, 9, 2, 3]
print(divide_lists(list1, list2))  # [1.0, 1.0, ...]
