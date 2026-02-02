# 248. Max Value After Mapping

def max_after_map(lst: list, func) -> int | float:
    return max(func(x) for x in lst)


print(max_after_map([1, 2, 3, 4], lambda x: x * 2))  # 8
