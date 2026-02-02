# 229. First Index Where Element Satisfies Function

def first_index_where(lst: list, predicate) -> int:
    for i, x in enumerate(lst):
        if predicate(x):
            return i
    return -1


print(first_index_where([1, 2, 3, 4], lambda x: x > 2))  # 2
