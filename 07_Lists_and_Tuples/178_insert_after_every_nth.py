# ---------------------------------------------------------------------------
# 178. Insert Specified Element After Every nth Element
# ---------------------------------------------------------------------------
# Descripción: Insert Specified Element After Every nth Element
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def insert_after_every_nth(lst: list, n: int, elem) -> list:
    result = []
    for i, x in enumerate(lst):
        result.append(x)
        if (i + 1) % n == 0:
            result.append(elem)
    return result


sample = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10]
print(insert_after_every_nth(sample, 4, 20))
