# -------------------------------------------------
# File Name: 056_scramble_letters.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Scramble Letters of Strings in List
# -------------------------------------------------

import random

def scramble_string(s: str) -> str:
    chars = list(s)
    random.shuffle(chars)
    return ''.join(chars)


def scramble_list_strings(lst: list[str]) -> list[str]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [scramble_string(s) for s in lst]


sample = ['Python', 'list', 'exercises']
print(scramble_list_strings(sample))
