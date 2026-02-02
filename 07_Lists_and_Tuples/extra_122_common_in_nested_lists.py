# 122. Find Common Elements in Nested List (in all sublists)

def common_in_nested(lists: list[list]) -> list:
    if not lists:
        return []
    result = set(lists[0])
    for L in lists[1:]:
        result &= set(L)
    return list(result)


sample = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
print(common_in_nested(sample))  # [18, 12]
