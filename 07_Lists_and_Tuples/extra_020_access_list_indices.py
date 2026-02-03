# ---------------------------------------------------------------------------
# 20. Access the Index of a List
# ---------------------------------------------------------------------------
# Descripción: Access the Index of a List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def with_index(lst: list) -> list[tuple[int, any]]:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(enumerate(lst))


sample = ['a', 'b', 'c']
for i, v in with_index(sample):
    print(i, v)
