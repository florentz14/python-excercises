# 73. Remove Consecutive Duplicates

def remove_consecutive_duplicates(lst: list) -> list:
    result = []
    for x in lst:
        if not result or result[-1] != x:
            result.append(x)
    return result


sample = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print(remove_consecutive_duplicates(sample))
