# -------------------------------------------------
# File Name: 34_remove_duplicate_words.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Remove Duplicate Words from List (preserve order)
# -------------------------------------------------

def remove_duplicate_words(lst: list[str]) -> list[str]:
    seen = set()
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [w for w in lst if not (w in seen or seen.add(w))]


sample = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
print(remove_duplicate_words(sample))
