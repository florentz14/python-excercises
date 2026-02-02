# ---------------------------------------------------------------------------
# 9. Clone or Copy a List
# ---------------------------------------------------------------------------
# Descripción: Crea una copia de la lista para que cambios en la copia
#              no afecten a la original (y al revés).
# Entrada: Lista original.
# Salida: Nueva lista con los mismos elementos (objeto distinto en memoria).
# ---------------------------------------------------------------------------

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
