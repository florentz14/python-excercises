# 226. Common Elements After Applying Function to Both Lists

def common_by_func(a: list, b: list, func) -> list:
    set_b = {func(x) for x in b}
    return [x for x in a if func(x) in set_b]


# e.g. round: [1.1, 2.1], [2.2, 3.2] -> common rounded: [2.1]
print(common_by_func([1.1, 2.1, 3.1], [2.2, 3.4], round))  # [2.1, 3.1] -> after func [2, 3] vs {2,3}
