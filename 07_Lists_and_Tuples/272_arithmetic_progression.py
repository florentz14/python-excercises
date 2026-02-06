# ---------------------------------------------------------------------------
# 272. Generate Arithmetic Progression (start, step, limit)
# ---------------------------------------------------------------------------
# Descripción: Generate Arithmetic Progression (start, step, limit)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def arithmetic_progression(start: int, step: int, limit: int) -> list[int]:
    result = []
    x = start
    while x <= limit:
        result.append(x)
        x += step
    return result


print(arithmetic_progression(1, 1, 15))   # [1,2,...,15]
print(arithmetic_progression(3, 3, 36))  # [3,6,9,...,36]
print(arithmetic_progression(5, 5, 25))  # [5,10,15,20,25]
