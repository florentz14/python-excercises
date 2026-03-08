# -------------------------------------------------
# File Name: 04_get_smallest_number.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Obtiene el número más pequeño de una lista.
# -------------------------------------------------

def get_smallest(lst: list[int | float]) -> int | float:
    # min() es una función built-in que devuelve el elemento menor de la lista
    return min(lst)


# --- Ejemplo de uso ---
nums = [3, 7, 2, 9, 1]
print(get_smallest(nums))  # 1
