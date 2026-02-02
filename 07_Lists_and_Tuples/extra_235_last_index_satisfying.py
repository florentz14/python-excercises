# 235. Last Index Where Element Satisfies Function

def last_index_where(lst: list, predicate) -> int:
    for i in range(len(lst) - 1, -1, -1):
        if predicate(lst[i]):
            return i
    return -1


print(last_index_where([1, 2, 3, 2, 4], lambda x: x == 2))  # 3
