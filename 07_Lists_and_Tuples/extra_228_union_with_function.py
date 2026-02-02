# 228. Union of Two Lists (unique) After Applying Function

def union_by_func(a: list, b: list, func) -> list:
    seen = set()
    result = []
    for x in a + b:
        key = func(x)
        if key not in seen:
            seen.add(key)
            result.append(x)
    return result


print(union_by_func([1.1, 2.2], [2.2, 4.1], round))  # [1.1, 2.2, 4.1]
