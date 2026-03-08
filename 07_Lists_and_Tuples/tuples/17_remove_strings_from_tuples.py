# -------------------------------------------------
# File Name: 17_remove_strings_from_tuples.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Remove All Strings from List of Tuples
# -------------------------------------------------

def remove_strings_from_tuples(tuples: list[tuple]) -> list[tuple]:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [tuple(x for x in t if not isinstance(x, str)) for t in tuples]


sample = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
print(remove_strings_from_tuples(sample))
