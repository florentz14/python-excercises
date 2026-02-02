# 35. Create List by Concatenating List with Range 1 to n
# Sample: ['p', 'q'], n=5 -> ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

def concat_with_range(lst: list, n: int) -> list[str]:
    return [f"{item}{i}" for i in range(1, n + 1) for item in lst]


print(concat_with_range(['p', 'q'], 5))
