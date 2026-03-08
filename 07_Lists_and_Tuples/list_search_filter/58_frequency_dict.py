# -------------------------------------------------
# File Name: 58_frequency_dict.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Frequency Dict from List (unique values as keys, count as value)
# -------------------------------------------------

from collections import Counter

def frequency_dict(lst: list) -> dict:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return dict(Counter(lst))


print(frequency_dict(['a', 'b', 'a', 'c', 'a', 'b', 'f', 'e', 'e']))
