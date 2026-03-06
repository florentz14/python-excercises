# ---------------------------------------------------------------------------
# 26. Check if Two Lists Are Circularly Identical
# ---------------------------------------------------------------------------
# Descripción: Check if Two Lists Are Circularly Identical
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def circularly_identical(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    doubled = a + a
    return any(doubled[i:i + len(a)] == b for i in range(len(a)))


# Sample
list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]
print(circularly_identical(list1, list2))  # True
