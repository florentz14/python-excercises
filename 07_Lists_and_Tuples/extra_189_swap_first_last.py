# 189. Swap First and Last Element of List

def swap_first_last(lst: list) -> list:
    if len(lst) < 2:
        return lst[:]
    result = lst.copy()
    result[0], result[-1] = result[-1], result[0]
    return result


print(swap_first_last([1, 2, 3, 4, 5, 6, 7]))  # [7, 2, 3, 4, 5, 6, 1]
