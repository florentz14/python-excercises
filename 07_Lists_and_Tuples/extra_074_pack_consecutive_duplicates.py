# 74. Pack Consecutive Duplicates into Sublists

def pack_consecutive(lst: list) -> list[list]:
    if not lst:
        return []
    result = [[lst[0]]]
    for x in lst[1:]:
        if x == result[-1][0]:
            result[-1].append(x)
        else:
            result.append([x])
    return result


sample = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print(pack_consecutive(sample))
