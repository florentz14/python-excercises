# 99. Max and Min in Heterogeneous List (numbers only)

def max_min_heterogeneous(lst: list) -> tuple:
    nums = [x for x in lst if isinstance(x, (int, float))]
    return (max(nums), min(nums)) if nums else (None, None)


sample = ['Python', 3, 2, 4, 5, 'version']
print(max_min_heterogeneous(sample))  # (5, 2)
