# -------------------------------------------------
# File Name: 116_fill_list_with_value.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Fill List with Specified Value
# -------------------------------------------------

def fill_list(value, length: int) -> list:
    # Se repite el valor length veces en una lista.
    return [value] * length


print(fill_list(0, 7))    # [0,0,0,0,0,0,0]
print(fill_list(3, 8))    # [3,3,...]
print(fill_list(3.2, 5))  # [3.2, ...]
