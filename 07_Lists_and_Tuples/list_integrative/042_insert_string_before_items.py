# ---------------------------------------------------------------------------
# 63. Insert String at Beginning of All Items. [1,2,3,4], 'emp' -> ['emp1','emp2','emp3','emp4']
# ---------------------------------------------------------------------------
# Descripción: Insert String at Beginning of All Items. [1,2,3,4], 'emp' -> ['emp1...
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def prefix_items(lst: list, prefix: str) -> list[str]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [f"{prefix}{x}" for x in lst]


print(prefix_items([1, 2, 3, 4], 'emp'))
