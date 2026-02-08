# ---------------------------------------------------------------------------
# 3. Get Largest Number in List
# ---------------------------------------------------------------------------
# Descripción: Obtiene el número más grande de una lista.
# Entrada: Lista de números.
# Salida: El valor máximo (un solo número).
# ---------------------------------------------------------------------------

def get_largest(lst: list[int | float]) -> int | float:
    # max() es una función built-in que devuelve el elemento mayor de la lista
    return max(lst)


# --- Ejemplo de uso ---
nums = [3, 7, 2, 9, 1]
print(get_largest(nums))  # 9
