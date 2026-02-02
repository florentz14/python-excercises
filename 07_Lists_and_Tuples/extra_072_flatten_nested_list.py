# 72. Flatten Nested List Structure (arbitrary depth)

def flatten_deep(lst: list) -> list:
    result = []
    for x in lst:
        if isinstance(x, list):
            result.extend(flatten_deep(x))
        else:
            result.append(x)
    return result


sample = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print(flatten_deep(sample))
