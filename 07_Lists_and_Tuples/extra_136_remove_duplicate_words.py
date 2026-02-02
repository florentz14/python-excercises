# 136. Remove Duplicate Words from List (preserve order)

def remove_duplicate_words(lst: list[str]) -> list[str]:
    seen = set()
    return [w for w in lst if not (w in seen or seen.add(w))]


sample = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
print(remove_duplicate_words(sample))
