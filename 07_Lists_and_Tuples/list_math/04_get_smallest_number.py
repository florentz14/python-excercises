# ---------------------------------------------------------------------------
# 4. Get Smallest Number in List
# ---------------------------------------------------------------------------
# Descripción: Obtiene el número más pequeño de una lista.
# Entrada: Lista de números.
# Salida: El valor mínimo (un solo número).
# ---------------------------------------------------------------------------

def get_smallest(lst: list[int | float]) -> int | float:
    # min() es una función built-in que devuelve el elemento menor de la lista
    return min(lst)


# --- Ejemplo de uso ---
nums = [3, 7, 2, 9, 1]
print(get_smallest(nums))  # 1
