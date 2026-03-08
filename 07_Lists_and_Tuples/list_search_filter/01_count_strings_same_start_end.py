# -------------------------------------------------
# File Name: 01_count_strings_same_start_end.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Demonstrates count strings same start end.
# -------------------------------------------------

def count_same_start_end(lst: list[str]) -> int:
    # sum() suma 1 por cada elemento que cumple la condición
    # len(s) >= 2: la cadena tiene al menos 2 caracteres
    # s[0] == s[-1]: el primer carácter es igual al último
    return sum(1 for s in lst if len(s) >= 2 and s[0] == s[-1])


# --- Ejemplo: ['abc', 'xyz', 'aba', '1221'] -> 2 (aba y 1221)
sample = ['abc', 'xyz', 'aba', '1221']
print(count_same_start_end(sample))  # 2
