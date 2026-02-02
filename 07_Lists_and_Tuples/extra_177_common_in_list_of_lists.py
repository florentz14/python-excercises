# 177. Common Elements in List of Lists (intersection of all)

def common_in_all(lists: list[list]) -> list:
    if not lists:
        return []
    result = set(lists[0])
    for L in lists[1:]:
        result &= set(L)
    return list(result)


sample = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
print(common_in_all(sample))  # [2, 3]
