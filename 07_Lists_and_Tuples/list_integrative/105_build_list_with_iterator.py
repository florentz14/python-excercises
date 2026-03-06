# ---------------------------------------------------------------------------
# 219. Build List Using Iterator and Seed (e.g. -10, -20, -30, -40)
# ---------------------------------------------------------------------------
# Descripción: Build List Using Iterator and Seed (e.g. -10, -20, -30, -40)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def build_list(seed, func, n: int) -> list:
    result = []
    x = seed
    for _ in range(n):
        result.append(x)
        x = func(x)
    return result


print(build_list(-10, lambda x: x - 10, 4))  # [-10, -20, -30, -40]
