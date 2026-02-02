# 91. Find List with Max and Min Lengths

def max_min_length_lists(lists: list[list]) -> tuple[tuple[int, list], tuple[int, list]]:
    with_len = [(len(L), L) for L in lists]
    return max(with_len, key=lambda x: x[0]), min(with_len, key=lambda x: x[0])


sample = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
max_l, min_l = max_min_length_lists(sample)
print("Max length:", max_l)
print("Min length:", min_l)
