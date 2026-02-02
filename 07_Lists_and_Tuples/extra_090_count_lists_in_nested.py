# 90. Count Number of Lists in Nested List (top-level only, or recursive)

def count_lists_top(lst: list) -> int:
    return sum(1 for x in lst if isinstance(x, list))


def count_lists_recursive(lst: list) -> int:
    count = 0
    for x in lst:
        if isinstance(x, list):
            count += 1 + count_lists_recursive(x)
    return count


sample = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
print(count_lists_top(sample))  # 4
