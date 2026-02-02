# 197. Average of n-th Element Across Nested Lists (Different Lengths)

def average_nth_element(lists: list[list[float]], n: int) -> float:
    """n is 0-based index. Only include lists that have that index."""
    values = [L[n] for L in lists if len(L) > n]
    return sum(values) / len(values) if values else 0


sample = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average at index 0,1,2,3,4
avgs = [average_nth_element(sample, j) for j in range(5)]
print(avgs)
