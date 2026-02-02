# 250. Sum After Mapping

def sum_after_map(lst: list, func) -> int | float:
    return sum(func(x) for x in lst)


print(sum_after_map([1, 2, 3, 4], lambda x: x * 2))  # 20
