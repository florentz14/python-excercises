# ---------------------------------------------------------------------------
# 120. Create List with Alternate Elements (even indices: 0, 2, 4, ...)
# ---------------------------------------------------------------------------
# Descripción: Create List with Alternate Elements (even indices: 0, 2, 4, ...)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def alternate_elements(lst: list) -> list:
    return lst[::2]


print(alternate_elements(['red', 'black', 'white', 'green', 'orange']))  # ['red', 'white', 'orange']
print(alternate_elements([2, 0, 3, 4, 0, 2, 8, 3, 4, 2]))  # [2, 3, 0, 8, 4]
