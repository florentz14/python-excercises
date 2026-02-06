# ---------------------------------------------------------------------------
# 125. Product of Unique Numbers in List
# ---------------------------------------------------------------------------
# Descripción: Product of Unique Numbers in List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def product_unique(lst: list[int | float]) -> int | float:
    result = 1
    for x in set(lst):
        result *= x
    return result


sample = [10, 20, 30, 40, 20, 50, 60, 40]
print(product_unique(sample))  # 720000000
