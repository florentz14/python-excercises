# -------------------------------------------------
# File Name: 062_reverse_strings_in_list.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Reverse Each String in List
# -------------------------------------------------

def reverse_strings(lst: list[str]) -> list[str]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [s[::-1] for s in lst]


sample = ['Red', 'Green', 'Blue', 'White', 'Black']
print(reverse_strings(sample))  # ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
