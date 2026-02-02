# 132. All Index Positions of Max and Min in List

def index_max_min(lst: list) -> tuple[list[int], list[int]]:
    if not lst:
        return [], []
    mx, mn = max(lst), min(lst)
    max_indices = [i for i, x in enumerate(lst) if x == mx]
    min_indices = [i for i, x in enumerate(lst) if x == mn]
    return max_indices, min_indices


sample = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
max_i, min_i = index_max_min(sample)
print("Max indices:", max_i, "Min indices:", min_i)
