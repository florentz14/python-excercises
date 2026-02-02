# 276. Find Largest Odd Number in List

def largest_odd(lst: list[int]) -> int | None:
    odds = [x for x in lst if x % 2 != 0]
    return max(odds) if odds else None


print(largest_odd([0, 9, 2, 4, 5, 6]))   # 9
print(largest_odd([-4, 0, 6, 1, 0, 2]))  # 1
print(largest_odd([1, 2, 3]))            # 3
