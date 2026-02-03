# ---------------------------------------------------------------------------
# 11. Check Common Member Between Two Lists
# ---------------------------------------------------------------------------
# Descripción: Check Common Member Between Two Lists
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def have_common_member(a: list, b: list) -> bool:
    return bool(set(a) & set(b))


print(have_common_member([1, 2, 3], [3, 4, 5]))   # True
print(have_common_member([1, 2], [3, 4]))         # False
