# -------------------------------------------------
# File Name: 36_remove_specific_words.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Remove Specific Words from List
# -------------------------------------------------

def remove_words(lst: list[str], to_remove: list[str]) -> list[str]:
    remove_set = set(to_remove)
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [w for w in lst if w not in remove_set]


sample = ['red', 'green', 'blue', 'white', 'black', 'orange']
print(remove_words(sample, ['white', 'orange']))
