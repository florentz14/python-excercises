# ---------------------------------------------------------------------------
# 47. Insert Element Before Each List Item
# ---------------------------------------------------------------------------
# Descripción: Insert Element Before Each List Item
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def insert_before(lst: list, elem) -> list:
    result = []
    for x in lst:
        result.append(elem)
        result.append(x)
    return result


print(insert_before([1, 2, 3], 0))  # [0, 1, 0, 2, 0, 3]
