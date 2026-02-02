# 100. Extract Common Index Elements (same value at same index across lists)

def common_index_elements(*lists: list) -> list:
    return [lists[0][i] for i in range(min(len(L) for L in lists))
            if all(L[i] == lists[0][i] for L in lists)]


a, b, c = [1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]
print(common_index_elements(a, b, c))  # [1, 7]
