# -------------------------------------------------
# File Name: 07_sort_string_numbers_numerically.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Sort List of String Numbers Numerically
# -------------------------------------------------

def sort_numeric_strings(lst: list[str]) -> list[str]:
    # Se ordena la lista usando key para comparar (p. ej. por longitud o valor).
    return sorted(lst, key=lambda s: int(s))


sample = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
print(sort_numeric_strings(sample))
