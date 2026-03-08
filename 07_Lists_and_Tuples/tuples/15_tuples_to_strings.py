# -------------------------------------------------
# File Name: 15_tuples_to_strings.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Convert List of Tuples to List of Strings (join with space)
# -------------------------------------------------

def tuples_to_strings(tuples: list[tuple]) -> list[str]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [' '.join(str(x) for x in t) for t in tuples]


sample = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
print(tuples_to_strings(sample))  # ['red green', 'black white', 'orange pink']
