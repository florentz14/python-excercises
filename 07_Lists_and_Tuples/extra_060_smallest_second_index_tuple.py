# 60. Find Tuple with Smallest Second Index from List of Tuples

def smallest_second_index(tuples: list[tuple]) -> tuple | None:
    return min(tuples, key=lambda t: t[1]) if tuples else None


sample = [(1, 5), (2, 3), (3, 8)]
print(smallest_second_index(sample))  # (2, 3)
