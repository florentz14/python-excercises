# 135. Iterate Over All Pairs of Consecutive Items

def consecutive_pairs(lst: list) -> list[tuple]:
    return list(zip(lst[:-1], lst[1:]))


sample = [1, 1, 2, 3, 3, 4, 4, 5]
print(consecutive_pairs(sample))
