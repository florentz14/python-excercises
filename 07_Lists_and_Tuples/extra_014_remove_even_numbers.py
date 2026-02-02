# 14. Remove Even Numbers from List

def remove_even(lst: list[int]) -> list[int]:
    return [x for x in lst if x % 2 != 0]


sample = [1, 2, 3, 4, 5, 6]
print(remove_even(sample))  # [1, 3, 5]
