# ---------------------------------------------------------------------------
# 239. First Value That Satisfies Function
# ---------------------------------------------------------------------------
# Descripción: First Value That Satisfies Function
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def first_value_where(lst: list, predicate):
    for x in lst:
        if predicate(x):
            return x
    return None


print(first_value_where([1, 2, 3, 4], lambda x: x > 2))  # 3
print(first_value_where([1, 2, 3, 4], lambda x: x > 1))  # 2
