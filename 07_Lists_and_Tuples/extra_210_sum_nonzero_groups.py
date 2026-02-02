# 210. Sum of Each Non-Zero Group (separated by zeros)

def sum_nonzero_groups(lst: list[int]) -> list[int]:
    result = []
    current = 0
    for x in lst:
        if x != 0:
            current += x
        else:
            if current != 0:
                result.append(current)
                current = 0
    if current != 0:
        result.append(current)
    return result


sample = [3, 4, 6, 2, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 7, 4, 4, 0, 5, 3, 2, 9, 7, 1]
print(sum_nonzero_groups(sample))
