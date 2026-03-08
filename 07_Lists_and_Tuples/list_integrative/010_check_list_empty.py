# -------------------------------------------------
# File Name: 010_check_list_empty.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Comprueba si una lista no tiene elementos.
# -------------------------------------------------

def is_empty(lst: list) -> bool:
    # len(lst) da el número de elementos; 0 significa vacía
    return len(lst) == 0


# --- Ejemplo de uso ---
print(is_empty([]))   # True
print(is_empty([1]))  # False
