# ---------------------------------------------------------------------------
# 1. Sum Items in List
# ---------------------------------------------------------------------------
# Descripción: Suma todos los elementos numéricos de una lista.
# Entrada: Lista de números (int o float).
# Salida: Un solo número (suma total).
# ---------------------------------------------------------------------------

def sum_list_items(lst: list[int | float]) -> int | float:
    # sum() recorre la lista y suma todos sus elementos
    return sum(lst)


# --- Ejemplo de uso ---
# Lista de números a sumar
nums = [1, 2, 3, 4, 5]
# Mostrar el resultado (15)
print(sum_list_items(nums))
