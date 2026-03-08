# -------------------------------------------------
# File Name: 011_clone_copy_list.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Crea una copia de la lista para que cambios en la copia
# -------------------------------------------------

def clone_list(lst: list) -> list:
    # .copy() crea una nueva lista con los mismos elementos (copia superficial)
    return lst.copy()


# --- Ejemplo de uso ---
original = [1, 2, 3]
# copied es una lista nueva; modificar copied no cambia original
copied = clone_list(original)
print(copied)
# Comprobación: son listas distintas (no el mismo objeto)
print(copied is not original)  # True
