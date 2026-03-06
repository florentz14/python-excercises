# ---------------------------------------------------------------------------
# 79. Remove K-th Element from List (1-based index in sample: remove 3rd -> index 2)
# ---------------------------------------------------------------------------
# Descripción: Remove K-th Element from List (1-based index in sample: remove 3rd ...
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_kth(lst: list, k: int) -> list:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for i, x in enumerate(lst) if i != k]


sample = [1, 1, 2, 3, 4, 4, 5, 1]
print(remove_kth(sample, 2))  # remove index 2 -> [1, 1, 3, 4, 4, 5, 1]
