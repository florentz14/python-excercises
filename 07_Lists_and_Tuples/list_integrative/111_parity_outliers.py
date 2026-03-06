# ---------------------------------------------------------------------------
# 236. Find Parity Outliers (majority even -> return odd; majority odd -> return even)
# ---------------------------------------------------------------------------
# Descripción: Find Parity Outliers (majority even -> return odd; majority odd -> ...
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def parity_outliers(lst: list[int]) -> list[int]:
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    # Se devuelve un valor u otro según la condición.
    return odd if len(even) > len(odd) else even


print(parity_outliers([1, 2, 3, 4, 6, 8]))  # [1, 3]
print(parity_outliers([1, 2, 3, 5, 7]))     # [2]
