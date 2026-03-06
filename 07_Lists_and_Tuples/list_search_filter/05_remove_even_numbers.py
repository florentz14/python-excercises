# ---------------------------------------------------------------------------
# 14. Remove Even Numbers from List
# ---------------------------------------------------------------------------
# Descripción: Remove Even Numbers from List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_even(lst: list[int]) -> list[int]:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in lst if x % 2 != 0]


sample = [1, 2, 3, 4, 5, 6]
print(remove_even(sample))  # [1, 3, 5]
