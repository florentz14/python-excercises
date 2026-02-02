# 128. Sum of Numbers in List Between Two Indices (inclusive)

def sum_between_indices(lst: list[int], start: int, end: int) -> int:
    return sum(lst[start:end + 1])


sample = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
print(sum_between_indices(sample, 8, 10))  # indices 8,9,10 -> 29
