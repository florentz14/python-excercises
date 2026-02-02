# 121. Find Nested List Elements Present in Another List

def nested_intersection(flat: list, nested: list[list]) -> list[list]:
    """For each sublist, keep only elements that are in flat."""
    flat_set = set(flat)
    return [[x for x in sub if x in flat_set] for sub in nested]


flat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nested = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
print(nested_intersection(flat, nested))  # [[12], [7, 11], [1, 5, 8]]
