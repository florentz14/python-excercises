# ---------------------------------------------------------------------------
# 61. Create List of Empty Dictionaries
# ---------------------------------------------------------------------------
# Descripción: Create List of Empty Dictionaries
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def list_of_empty_dicts(n: int) -> list[dict]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [{} for _ in range(n)]


print(list_of_empty_dicts(5))  # [{}, {}, {}, {}, {}]
