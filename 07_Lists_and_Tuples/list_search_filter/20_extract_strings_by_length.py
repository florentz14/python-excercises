# -------------------------------------------------
# File Name: 20_extract_strings_by_length.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Extract Strings of Specified Length from List
# -------------------------------------------------

def strings_of_length(lst: list[str], n: int) -> list[str]:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [s for s in lst if len(s) == n]


sample = ['Python', 'list', 'exercises', 'practice', 'solution']
print(strings_of_length(sample, 8))  # ['practice', 'solution']
