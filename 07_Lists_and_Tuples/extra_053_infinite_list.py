# 53. Create List with Infinite Elements (using generator)

def infinite_list(start=0, step=1):
    """Generator yielding infinite elements."""
    n = start
    while True:
        yield n
        n += step


# Usage: take first 10
gen = infinite_list(0)
first_10 = [next(gen) for _ in range(10)]
print(first_10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
