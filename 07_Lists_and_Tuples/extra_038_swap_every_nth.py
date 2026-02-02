# 38. Swap Every n-th and (n+1)th - [0,1,2,3,4,5] -> [1,0,3,2,5,4]

def swap_pairs(lst: list) -> list:
    result = lst.copy()
    for i in range(0, len(result) - 1, 2):
        result[i], result[i + 1] = result[i + 1], result[i]
    return result


print(swap_pairs([0, 1, 2, 3, 4, 5]))  # [1, 0, 3, 2, 5, 4]
