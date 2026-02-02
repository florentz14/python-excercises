# 105. Average of Two Lists (average of all elements from both)

def average_two_lists(a: list[float], b: list[float]) -> float:
    combined = a + b
    return sum(combined) / len(combined) if combined else 0


print(average_two_lists([1, 1, 3, 4, 4, 5, 6, 7], [0, 1, 2, 3, 4, 4, 5, 7, 8]))
