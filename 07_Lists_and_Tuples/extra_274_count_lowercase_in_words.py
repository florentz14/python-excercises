# 274. Count Lowercase Letters in List of Words

def count_lowercase(words: list[str]) -> int:
    return sum(sum(1 for c in w if c.islower()) for w in words)


print(count_lowercase(["Red", "Green", "Blue", "White"]))  # 13
print(count_lowercase(["SQL", "C++", "C"]))  # 0
