# ---------------------------------------------------------------------------
# 8. Check if List is Empty
# ---------------------------------------------------------------------------
# Descripción: Comprueba si una lista no tiene elementos.
# Entrada: Una lista.
# Salida: True si está vacía, False en caso contrario.
# ---------------------------------------------------------------------------

def is_empty(lst: list) -> bool:
    # len(lst) da el número de elementos; 0 significa vacía
    return len(lst) == 0


# --- Ejemplo de uso ---
print(is_empty([]))   # True
print(is_empty([1]))  # False
