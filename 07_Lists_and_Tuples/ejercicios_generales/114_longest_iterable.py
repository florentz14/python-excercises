# ---------------------------------------------------------------------------
# 245. Longest Iterable Among Arguments
# ---------------------------------------------------------------------------
# Descripción: Longest Iterable Among Arguments
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def longest(*args) -> list | str:
    return max(args, key=len)


print(longest('Red', 'Green', 'Blue'))  # Green
print(longest([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]))  # [1,2,3,4,5]
