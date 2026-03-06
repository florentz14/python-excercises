# ---------------------------------------------------------------------------
# 244. Generate Range with Ratio (geometric: start, start*step, start*step^2, ...)
# ---------------------------------------------------------------------------
# Descripción: Generate Range with Ratio (geometric: start, start*step, start*step...
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def range_ratio(start: int | float, step: int | float, n: int) -> list:
    if step == 1:
        raise ValueError("step must not be 1")
    result = []
    x = start
    for _ in range(n):
        result.append(x)
        x *= step
    return result


print(range_ratio(1, 2, 9))   # [1, 2, 4, 8, 16, 32, 64, 128, 256]
print(range_ratio(3, 2, 7))   # [3, 6, 12, 24, 48, 96, 192]
