# ---------------------------------------------------------------------------
# 238. Average of List After Mapping Each Element
# ---------------------------------------------------------------------------
# Descripción: Average of List After Mapping Each Element
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def average_after_map(lst: list, func) -> float:
    mapped = [func(x) for x in lst]
    # Se devuelve un valor u otro según la condición.
    return sum(mapped) / len(mapped) if mapped else 0


print(average_after_map([1, 2, 3, 4, 5], lambda x: x))   # 3.0
print(average_after_map([1, 2, 3, 4, 5], lambda x: x * 2))  # 6.0
