# ---------------------------------------------------------------------------
# 39. Convert List of Integers to Single Integer. [11, 33, 50] -> 113350
# ---------------------------------------------------------------------------
# Descripción: Convert List of Integers to Single Integer. [11, 33, 50] -> 113350
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def list_to_int(lst: list[int]) -> int:
    return int(''.join(str(x) for x in lst))


print(list_to_int([11, 33, 50]))  # 113350
