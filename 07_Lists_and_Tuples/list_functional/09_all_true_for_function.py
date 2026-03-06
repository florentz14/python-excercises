# ---------------------------------------------------------------------------
# 243. Check If Function Returns True for Every Element
# ---------------------------------------------------------------------------
# Descripción: Check If Function Returns True for Every Element
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def all_match(lst: list, predicate) -> bool:
    return all(predicate(x) for x in lst)


print(all_match([1, 2, 3, 4], lambda x: x > 0))   # True
print(all_match([1, 2, 3, 4], lambda x: x > 2))   # False
