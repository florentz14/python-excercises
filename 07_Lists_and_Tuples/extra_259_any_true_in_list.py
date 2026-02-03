# ---------------------------------------------------------------------------
# 259. Check If Any Element Satisfies Function
# ---------------------------------------------------------------------------
# Descripción: Check If Any Element Satisfies Function
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def any_satisfy(lst: list, predicate) -> bool:
    return any(predicate(x) for x in lst)


print(any_satisfy([1, 2, 3], lambda x: x > 2))   # True
print(any_satisfy([1, 2, 3], lambda x: x > 5))   # False
