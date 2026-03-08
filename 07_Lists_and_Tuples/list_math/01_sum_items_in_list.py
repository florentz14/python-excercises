# -------------------------------------------------
# File Name: 01_sum_items_in_list.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Suma todos los elementos numéricos de una lista.
# -------------------------------------------------

def sum_list_items(lst: list[int | float]) -> int | float:
    # sum() recorre la lista y suma todos sus elementos
    return sum(lst)


# --- Ejemplo de uso ---
# Lista de números a sumar
nums = [1, 2, 3, 4, 5]
# Mostrar el resultado (15)
print(sum_list_items(nums))
